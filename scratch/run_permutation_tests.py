import os
import pandas as pd
import numpy as np
import time
import matplotlib.pyplot as plt
import seaborn as sns

def run_permutation_test(n_permutations=1000):
    print("Loading datasets...")
    df_district = pd.read_csv("data/processed/seda_district_panel_pilot.csv")
    df_state = pd.read_csv("data/processed/state_year_panel.csv")
    
    df_district['sedalea'] = df_district['sedalea'].astype(str).str.zfill(7)
    
    pilot_states = ['FL', 'NY', 'OK', 'TN', 'TX', 'WA']
    df_state_subset = df_state[df_state['state'].isin(pilot_states)][['state', 'year', 'backlash_mass', 'has_waiver']].rename(columns={'state': 'stateabb'})
    
    df_district_pilot = df_district[df_district['stateabb'].isin(pilot_states)].copy()
    
    # We will run the main model for Math and Reading
    for sub, sub_name in [('mth', 'MATH'), ('rla', 'READING')]:
        print(f"\n=======================================================")
        print(f" PERMUTATION TEST FOR {sub_name} ACHIEVEMENT (N={n_permutations} shuffles)")
        print(f"=======================================================")
        
        df_sub = df_district_pilot[df_district_pilot['subject'] == sub].copy()
        
        # Merge and sort
        df_true_full = pd.merge(df_sub, df_state_subset, on=['stateabb', 'year'], how='inner')
        df_true_full = df_true_full.sort_values(by=['sedalea', 'grade', 'year']).reset_index(drop=True)
        
        # Compute lag indices
        districts_full = df_true_full['sedalea'].values
        grades_full = df_true_full['grade'].values
        has_lag = (districts_full[1:] == districts_full[:-1]) & (grades_full[1:] == grades_full[:-1])
        lag_idx = np.zeros(len(df_true_full), dtype=int) - 1
        lag_idx[1:][has_lag] = np.arange(len(df_true_full) - 1)[has_lag]
        
        def get_lags(arr, idx):
            arr_nan = np.append(arr, np.nan)
            return arr_nan[idx]
            
        df_true_full['backlash_mass_lag1'] = get_lags(df_true_full['backlash_mass'].values, lag_idx)
        df_true_full['has_waiver_lag1'] = get_lags(df_true_full['has_waiver'].values, lag_idx)
        df_true_full['backlash_x_waiver_lag1'] = df_true_full['backlash_mass_lag1'] * df_true_full['has_waiver_lag1']
        
        valid_mask = df_true_full[['backlash_mass_lag1', 'has_waiver_lag1', 'sesall', 'povertyall']].notna().all(axis=1).values
        valid_indices = np.where(valid_mask)[0]
        
        df_true = df_true_full[valid_mask].copy().reset_index(drop=True)
        
        # Create Grade-by-Year dummies
        df_true['grade_year'] = df_true['year'].astype(str) + "_" + df_true['grade'].astype(str)
        gy_dummies = pd.get_dummies(df_true['grade_year'], drop_first=True, dtype=float)
        df_true = pd.concat([df_true, gy_dummies], axis=1)
        dummy_cols = list(gy_dummies.columns)
        
        covariates = [
            'backlash_mass_lag1', 'has_waiver_lag1', 'backlash_x_waiver_lag1',
            'sesall', 'povertyall', 'unempall', 'totenrl'
        ] + dummy_cols
        
        # Group variables for demeaning
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
        true_vars = df_true[['backlash_mass_lag1', 'has_waiver_lag1', 'backlash_x_waiver_lag1']].values
        true_vars_demeaned = demean_numpy(true_vars, district_inverse, district_counts)
        
        X_all_demeaned = np.hstack([true_vars_demeaned, static_X_demeaned])
        coefs_true = np.linalg.lstsq(X_all_demeaned, y_demeaned, rcond=None)[0]
        true_coef = coefs_true[2]
        print(f"True {sub_name} Coefficient: {true_coef:.4f}")
        
        # Setup lookup grids for fast permutations
        state_to_idx = {state: idx for idx, state in enumerate(pilot_states)}
        unique_years = np.sort(df_true_full['year'].unique())
        year_to_idx = {year: idx for idx, year in enumerate(unique_years)}
        
        state_idx_full = df_true_full['stateabb'].map(state_to_idx).values
        year_idx_full = df_true_full['year'].map(year_to_idx).values
        
        num_years = len(unique_years)
        backlash_grid = np.zeros((6, num_years))
        waiver_grid = np.zeros((6, num_years))
        for _, row in df_state_subset.iterrows():
            if row['year'] in year_to_idx:
                s_idx = state_to_idx[row['stateabb']]
                y_idx = year_to_idx[row['year']]
                backlash_grid[s_idx, y_idx] = row['backlash_mass']
                waiver_grid[s_idx, y_idx] = row['has_waiver']
        
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
            waiver_full = waiver_grid[shuffled_s_idx, year_idx_full]
            
            # Lagging
            backlash_lag1_full = get_lags(backlash_full, lag_idx)
            waiver_lag1_full = get_lags(waiver_full, lag_idx)
            
            # Slice to valid rows
            backlash_lag1 = backlash_lag1_full[valid_indices]
            waiver_lag1 = waiver_lag1_full[valid_indices]
            interaction = backlash_lag1 * waiver_lag1
            
            # Demean dynamic variables
            dynamic_vars = np.column_stack([backlash_lag1, waiver_lag1, interaction])
            dynamic_demeaned = demean_numpy(dynamic_vars, district_inverse, district_counts)
            
            # Fit
            X_perm_demeaned[:, :3] = dynamic_demeaned
            coefs = np.linalg.lstsq(X_perm_demeaned, y_demeaned, rcond=None)[0]
            perm_coefs.append(coefs[2])
            
        perm_coefs = np.array(perm_coefs)
        # Standard finite-sample permutation p-value formula
        p_val_two_sided = (1 + np.sum(np.abs(perm_coefs) >= np.abs(true_coef))) / (1 + n_permutations)
        print(f"Permutation P-value (2-sided, N={n_permutations}): {p_val_two_sided:.4f}")
        print(f"Permuted coefficients range: [{perm_coefs.min():.4f}, {perm_coefs.max():.4f}]")
        print(f"Permutation test completed in {time.time() - start_time:.1f}s")
        
        # Plot permutation distribution
        plt.figure(figsize=(8, 5))
        sns.histplot(perm_coefs, kde=False, label="Permuted Coefficients", color="skyblue")
        plt.axvline(true_coef, color='crimson', linestyle='--', linewidth=2, label=f"True Coef: {true_coef:.4f} (p={p_val_two_sided:.3f})")
        plt.title(f"Permutation Distribution for {sub_name} (N={n_permutations} shuffles)")
        plt.xlabel("Interaction Coefficient Estimate")
        plt.ylabel("Frequency")
        plt.legend()
        plt.tight_layout()
        os.makedirs("reports", exist_ok=True)
        plt.savefig(f"reports/permutation_{sub}.png", dpi=300)
        plt.close()

if __name__ == "__main__":
    run_permutation_test(1000)
