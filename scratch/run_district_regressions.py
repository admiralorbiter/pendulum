import os
import pandas as pd
import numpy as np
from linearmodels.panel import PanelOLS

def run_regressions():
    # 1. Load data
    print("Loading datasets...")
    df_district = pd.read_csv("data/processed/seda_district_panel_pilot.csv")
    df_state = pd.read_csv("data/processed/state_year_panel.csv")
    
    # 2. Standardize district ID format
    df_district['sedalea'] = df_district['sedalea'].astype(str).str.zfill(7)
    
    # 3. Merge state-level indicators (backlash_mass, has_waiver, trifecta, gov_party_rep)
    print("Merging state-level indicators...")
    # Keep only required columns from state panel to avoid duplicates
    df_state_subset = df_state[[
        'state', 'year', 'backlash_mass', 'has_waiver', 
        'gov_party_rep', 'trifecta', 'election_year'
    ]].rename(columns={'state': 'stateabb'})
    
    df = pd.merge(df_district, df_state_subset, on=['stateabb', 'year'], how='inner')
    
    # 4. Construct Lagged and Interaction Variables
    print("Constructing variables...")
    # Since SEDA is a panel, we sort by district, grade, subject, year to compute lags
    df = df.sort_values(by=['sedalea', 'grade', 'subject', 'year'])
    
    # Lagged state-level variables (since they vary by state-year, they are identical within state-year)
    df['backlash_mass_lag1'] = df.groupby(['sedalea', 'grade', 'subject'])['backlash_mass'].shift(1)
    df['has_waiver_lag1'] = df.groupby(['sedalea', 'grade', 'subject'])['has_waiver'].shift(1)
    
    # Interaction: backlash_mass_lag1 * has_waiver_lag1
    df['backlash_x_waiver_lag1'] = df['backlash_mass_lag1'] * df['has_waiver_lag1']
    
    # Newly Constrained Proxy: 1 if district SES is below median (0.0), 0 otherwise
    # Since sesall is standardized, 0 is the national median/mean
    df['newly_constrained'] = (df['sesall'] <= 0.0).astype(int)
    df['backlash_x_waiver_x_constrained_lag1'] = df['backlash_x_waiver_lag1'] * df['newly_constrained']
    
    # Drop rows where lag calculation yielded NaN (the first year 2009 is dropped)
    df = df.dropna(subset=['backlash_mass_lag1', 'has_waiver_lag1', 'sesall', 'povertyall'])
    
    # 5. Create Grade-by-Year Fixed Effects Dummies
    print("Creating Grade-by-Year dummies...")
    df['grade_year'] = df['year'].astype(str) + "_" + df['grade'].astype(str)
    gy_dummies = pd.get_dummies(df['grade_year'], drop_first=True, dtype=float)
    
    # Join dummies to main DataFrame
    df = pd.concat([df, gy_dummies], axis=1)
    dummy_cols = list(gy_dummies.columns)
    
    # 6. Run Regressions Separately by Subject
    for sub, sub_name in [('mth', 'MATH'), ('rla', 'READING')]:
        print(f"\n=======================================================")
        print(f" ESTIMATING MODEL FOR {sub_name} ACHIEVEMENT")
        print(f"=======================================================")
        
        df_sub = df[df['subject'] == sub].copy()
        
        # Set MultiIndex for PanelOLS: [entity, time]
        # We use a combined time index to handle multiple grades per district-year
        df_sub['time_id'] = df_sub['year'] * 10 + df_sub['grade']
        df_sub = df_sub.set_index(['sedalea', 'time_id'])
        
        # Define covariates
        covariates = [
            'backlash_mass_lag1', 'has_waiver_lag1', 'backlash_x_waiver_lag1',
            'sesall', 'povertyall', 'unempall', 'totenrl'
        ] + dummy_cols
        
        # We add a constant to the regression (though with entity_effects it is deflated, PanelOLS handles it)
        # We estimate with District (Entity) Fixed Effects
        mod = PanelOLS(
            dependent=df_sub['gcs_mn_all'],
            exog=df_sub[covariates],
            entity_effects=True
        )
        
        # Fit model: cluster by district (sedalea) for pilot (with small-cluster note)
        res = mod.fit(cov_type='clustered', cluster_entity=True)
        print(f"Entity-Clustered SE (District Level) - R-squared: {res.rsquared:.4f}, N: {res.nobs}")
        print(res.summary.tables[1])
        
        # Fit model: cluster by state (stateabb) to show contrast
        res_state = mod.fit(cov_type='clustered', clusters=df_sub['stateabb'])
        print(f"\nStandard Errors Clustered at the STATE level (N=6):")
        print(res_state.summary.tables[1])

if __name__ == "__main__":
    run_regressions()
