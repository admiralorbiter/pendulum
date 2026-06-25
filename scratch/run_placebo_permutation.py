import os
import pandas as pd
import numpy as np
import time
import matplotlib.pyplot as plt
import seaborn as sns

def run_placebo_permutation(n_permutations=1000):
    print("Loading datasets for placebo permutation...")
    df_district = pd.read_csv("data/processed/seda_district_panel_pilot.csv")
    df_state = pd.read_csv("data/processed/state_year_panel.csv")
    
    df_district['sedalea'] = df_district['sedalea'].astype(str).str.zfill(7)
    
    # Keep only pre-treatment years (2010, 2011)
    df_district_pre = df_district[df_district['year'].isin([2010, 2011])].copy()
    
    pilot_states = ['FL', 'NY', 'OK', 'TN', 'TX', 'WA']
    df_district_pre = df_district_pre[df_district_pre['stateabb'].isin(pilot_states)].copy()
    
    df_state_subset = df_state[[
        'state', 'year', 'backlash_mass', 'gov_party_rep', 'trifecta'
    ]].rename(columns={'state': 'stateabb'})
    df_state_subset = df_state_subset[df_state_subset['stateabb'].isin(pilot_states)].copy()
    
    # We will run the placebo model for Math and Reading
    for sub, sub_name in [('mth', 'MATH'), ('rla', 'READING')]:
        print(f"\n=======================================================")
        print(f" PLACEBO PERMUTATION TEST FOR {sub_name} ACHIEVEMENT (N={n_permutations} shuffles)")
        print(f"=======================================================")
        
        df_sub = df_district_pre[df_district_pre['subject'] == sub].copy()
        
        # Merge and sort
        df_true_full = pd.merge(df_sub, df_state_subset, on=['stateabb', 'year'], how='inner')
        df_true_full = df_true_full.sort_values(by=['sedalea', 'grade', 'year']).reset_index(drop=True)
        
        # Eventual waiver states
        eventual_waiver_states = ['WA', 'OK', 'FL', 'NY', 'TN']
        df_true_full['has_waiver_placebo'] = np.where(
            (df_true_full['stateabb'].isin(eventual_waiver_states)) & (df_true_full['year'] == 2011),
            1, 0
        )
        df_true_full['backlash_x_waiver_placebo'] = df_true_full['backlash_mass'] * df_true_full['has_waiver_placebo']
        
        valid_mask = df_true_full[['backlash_mass', 'has_waiver_placebo', 'sesall', 'povertyall']].notna().all(axis=1).values
        valid_indices = np.where(valid_mask)[0]
        
        df_true = df_true_full[valid_mask].copy().reset_index(drop=True)
        
        # Create Grade-by-Year dummies
        df_true['grade_year'] = df_true['year'].astype(str) + "_" + df_true['grade'].astype(str)
        gy_dummies = pd.get_dummies(df_true['grade_year'], drop_first=True, dtype=float)
        df_true = pd.concat([df_true, gy_dummies], axis=1)
        dummy_cols = list(gy_dummies.columns)
        
        covariates = [
            'backlash_mass', 'has_waiver_placebo', 'backlash_x_waiver_placebo',
            'sesall', 'povertyall', 'unempall', 'totenrl'
        ] + dummy_cols
        
        # Demean index
        districts = df_true['sedalea'].values
        unique_districts, district_inverse, district_counts = np.unique(districts, return_inverse=True, return_counts=True)
        
        def demean_numpy(v, inverse_idx, counts):
            if len(v.shape) == 1:
                group_sum = np.bincount(inverse_idx, weights=v)
                group_mean = group_sum / counts
                return v - group_mean[inverse_idx]
            else:
                v_demeaned = np.zeros_like(v)
                for col in range(v.shape[1]):
                    group_sum = np.bincount(inverse_idx, weights=v[:, col])
                    group_mean = group_sum / counts
                    v_demeaned[:, col] = v[:, col] - group_mean[inverse_idx]
                return v_demeaned
        
        # Demean dependent variable
        y_val = df_true['gcs_mn_all'].values
        y_demeaned = demean_numpy(y_val, district_inverse, district_counts)
        
        # Demean static controls
        static_covs = ['sesall', 'povertyall', 'unempall', 'totenrl'] + dummy_cols
        static_X = df_true[static_covs].values
        static_X_demeaned = demean_numpy(static_X, district_inverse, district_counts)
        
        # Demean true dynamic variables
        true_vars = df_true[['backlash_mass', 'has_waiver_placebo', 'backlash_x_waiver_placebo']].values
        true_vars_demeaned = demean_numpy(true_vars, district_inverse, district_counts)
        
        X_all_demeaned = np.hstack([true_vars_demeaned, static_X_demeaned])
        coefs_true = np.linalg.lstsq(X_all_demeaned, y_demeaned, rcond=None)[0]
        true_coef = coefs_true[2]
        print(f"True Placebo Coefficient: {true_coef:.4f}")
        
        # Setup lookup grids for fast permutations
        state_to_idx = {state: idx for idx, state in enumerate(pilot_states)}
        unique_years = np.sort(df_true_full['year'].unique())
        year_to_idx = {year: idx for idx, year in enumerate(unique_years)}
        
        state_idx_full = df_true_full['stateabb'].map(state_to_idx).values
        year_idx_full = df_true_full['year'].map(year_to_idx).values
        
        num_years = len(unique_years)
        backlash_grid = np.zeros((6, num_years))
        for _, row in df_state_subset.iterrows():
            if row['year'] in year_to_idx:
                s_idx = state_to_idx[row['stateabb']]
                y_idx = year_to_idx[row['year']]
                backlash_grid[s_idx, y_idx] = row['backlash_mass']
                
        # Eventual waiver states indicator mask
        is_eventual_waiver = np.array([state in eventual_waiver_states for state in pilot_states], dtype=float)
        
        # Run permutations
        perm_coefs = []
        start_time = time.time()
        
        N = len(df_true)
        X_perm_demeaned = np.zeros((N, len(covariates)))
        X_perm_demeaned[:, 3:] = static_X_demeaned
        
        np.random.seed(42)
        for i in range(n_permutations):
            # Shuffle state labels (permutation of 0..5)
            P = np.random.permutation(6)
            
            # Fast lookup of state variables
            shuffled_s_idx = P[state_idx_full]
            backlash_full = backlash_grid[shuffled_s_idx, year_idx_full]
            
            # Waiver placebo status
            # 1 if the permuted stateabb is in eventual_waiver_states AND year is 2011
            # We map shuffled_s_idx to waiver indicators, then multiply by year indicator (year == 2011)
            waiver_placebo_full = is_eventual_waiver[shuffled_s_idx] * (df_true_full['year'].values == 2011).astype(float)
            
            # Slice to valid rows
            backlash = backlash_full[valid_indices]
            waiver_placebo = waiver_placebo_full[valid_indices]
            interaction = backlash * waiver_placebo
            
            # Demean dynamic variables
            dynamic_vars = np.column_stack([backlash, waiver_placebo, interaction])
            dynamic_demeaned = demean_numpy(dynamic_vars, district_inverse, district_counts)
            
            # Fit
            X_perm_demeaned[:, :3] = dynamic_demeaned
            coefs = np.linalg.lstsq(X_perm_demeaned, y_demeaned, rcond=None)[0]
            perm_coefs.append(coefs[2])
            
        perm_coefs = np.array(perm_coefs)
        p_val_two_sided = (1 + np.sum(np.abs(perm_coefs) >= np.abs(true_coef))) / (1 + n_permutations)
        print(f"Permutation P-value (2-sided, N={n_permutations}): {p_val_two_sided:.4f}")
        print(f"Permuted coefficients range: [{perm_coefs.min():.4f}, {perm_coefs.max():.4f}]")
        print(f"Permutation test completed in {time.time() - start_time:.1f}s")
        
        # Plot permutation distribution
        plt.figure(figsize=(8, 5))
        sns.histplot(perm_coefs, kde=False, label="Permuted Coefficients", color="lightgreen")
        plt.axvline(true_coef, color='crimson', linestyle='--', linewidth=2, label=f"True Coef: {true_coef:.4f} (p={p_val_two_sided:.3f})")
        plt.title(f"Placebo Permutation Distribution for {sub_name} (N={n_permutations} shuffles)")
        plt.xlabel("Interaction Coefficient Estimate")
        plt.ylabel("Frequency")
        plt.legend()
        plt.tight_layout()
        os.makedirs("reports", exist_ok=True)
        plt.savefig(f"reports/placebo_permutation_{sub}.png", dpi=300)
        plt.close()

if __name__ == "__main__":
    run_placebo_permutation(1000)
