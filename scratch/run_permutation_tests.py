import os
import pandas as pd
import numpy as np
import time
from linearmodels.panel import PanelOLS

def run_permutation_test(n_permutations=20):
    # 1. Load data
    print("Loading datasets...")
    df_district = pd.read_csv("data/processed/seda_district_panel_pilot.csv")
    df_state = pd.read_csv("data/processed/state_year_panel.csv")
    
    df_district['sedalea'] = df_district['sedalea'].astype(str).str.zfill(7)
    
    # 2. Extract state-level panels to shuffle
    pilot_states = ['FL', 'NY', 'OK', 'TN', 'TX', 'WA']
    df_state_pilot = df_state[df_state['state'].isin(pilot_states)].copy()
    
    state_vars = ['backlash_mass', 'has_waiver', 'gov_party_rep', 'trifecta', 'election_year']
    df_state_subset = df_state_pilot[['state', 'year'] + state_vars].rename(columns={'state': 'stateabb'})
    
    # Keep only pilot states in district panel
    df_district = df_district[df_district['stateabb'].isin(pilot_states)].copy()
    
    # We will run the main model for Math and Reading
    def fit_model(df_sub, covariates, dep_var):
        mod = PanelOLS(
            dependent=df_sub[dep_var],
            exog=df_sub[covariates],
            entity_effects=True
        )
        res = mod.fit(cov_type='unadjusted')
        return res.params.get('backlash_x_waiver_lag1', np.nan)

    # Let's run for both subjects
    for sub, sub_name in [('mth', 'MATH'), ('rla', 'READING')]:
        print(f"\n=======================================================")
        print(f" PERMUTATION TEST FOR {sub_name} ACHIEVEMENT")
        print(f"=======================================================")
        
        df_sub = df_district[df_district['subject'] == sub].copy()
        
        # Sort for lag calculation
        df_sub = df_sub.sort_values(by=['sedalea', 'grade', 'year'])
        
        # True merge and fit
        df_true = pd.merge(df_sub, df_state_subset, on=['stateabb', 'year'], how='inner')
        df_true = df_true.sort_values(by=['sedalea', 'grade', 'year'])
        df_true['backlash_mass_lag1'] = df_true.groupby(['sedalea', 'grade'])['backlash_mass'].shift(1)
        df_true['has_waiver_lag1'] = df_true.groupby(['sedalea', 'grade'])['has_waiver'].shift(1)
        df_true['backlash_x_waiver_lag1'] = df_true['backlash_mass_lag1'] * df_true['has_waiver_lag1']
        df_true = df_true.dropna(subset=['backlash_mass_lag1', 'has_waiver_lag1', 'sesall', 'povertyall'])
        
        # Create Grade-by-Year dummies for the filtered sample
        df_true['grade_year'] = df_true['year'].astype(str) + "_" + df_true['grade'].astype(str)
        gy_dummies = pd.get_dummies(df_true['grade_year'], drop_first=True, dtype=float)
        df_true = pd.concat([df_true, gy_dummies], axis=1)
        dummy_cols = list(gy_dummies.columns)
        
        df_true['time_id'] = df_true['year'] * 10 + df_true['grade']
        df_true = df_true.set_index(['sedalea', 'time_id'])
        
        covariates = [
            'backlash_mass_lag1', 'has_waiver_lag1', 'backlash_x_waiver_lag1',
            'sesall', 'povertyall', 'unempall', 'totenrl'
        ] + dummy_cols
        
        true_coef = fit_model(df_true, covariates, 'gcs_mn_all')
        print(f"True {sub_name} Coefficient: {true_coef:.4f}")
        
        # Now run permutations
        perm_coefs = []
        start_time = time.time()
        
        # Generate unique permutation mappings
        np.random.seed(42)
        for i in range(n_permutations):
            # Shuffle state names
            shuffled_states = list(pilot_states)
            np.random.shuffle(shuffled_states)
            state_map = dict(zip(pilot_states, shuffled_states))
            
            # Apply mapping to state panel
            df_state_perm = df_state_subset.copy()
            df_state_perm['stateabb'] = df_state_perm['stateabb'].map(state_map)
            
            # Merge and calculate lags
            df_perm = pd.merge(df_sub, df_state_perm, on=['stateabb', 'year'], how='inner')
            df_perm = df_perm.sort_values(by=['sedalea', 'grade', 'year'])
            df_perm['backlash_mass_lag1'] = df_perm.groupby(['sedalea', 'grade'])['backlash_mass'].shift(1)
            df_perm['has_waiver_lag1'] = df_perm.groupby(['sedalea', 'grade'])['has_waiver'].shift(1)
            df_perm['backlash_x_waiver_lag1'] = df_perm['backlash_mass_lag1'] * df_perm['has_waiver_lag1']
            df_perm = df_perm.dropna(subset=['backlash_mass_lag1', 'has_waiver_lag1', 'sesall', 'povertyall'])
            
            # Create Grade-by-Year dummies for the permuted sample
            df_perm['grade_year'] = df_perm['year'].astype(str) + "_" + df_perm['grade'].astype(str)
            gy_dummies_perm = pd.get_dummies(df_perm['grade_year'], drop_first=True, dtype=float)
            df_perm = pd.concat([df_perm, gy_dummies_perm], axis=1)
            dummy_cols_perm = list(gy_dummies_perm.columns)
            
            df_perm['time_id'] = df_perm['year'] * 10 + df_perm['grade']
            df_perm = df_perm.set_index(['sedalea', 'time_id'])
            
            covariates_perm = [
                'backlash_mass_lag1', 'has_waiver_lag1', 'backlash_x_waiver_lag1',
                'sesall', 'povertyall', 'unempall', 'totenrl'
            ] + dummy_cols_perm
            
            coef = fit_model(df_perm, covariates_perm, 'gcs_mn_all')
            perm_coefs.append(coef)
            
        perm_coefs = np.array(perm_coefs)
        p_val_two_sided = np.mean(np.abs(perm_coefs) >= np.abs(true_coef))
        print(f"Permutation P-value (2-sided, N={n_permutations}): {p_val_two_sided:.4f}")
        print(f"Permuted coefficients range: [{perm_coefs.min():.4f}, {perm_coefs.max():.4f}]")
        print(f"Permutation test completed in {time.time() - start_time:.1f}s")

if __name__ == "__main__":
    run_permutation_test(20)
