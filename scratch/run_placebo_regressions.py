import os
import pandas as pd
import numpy as np
from linearmodels.panel import PanelOLS

def run_placebo_regressions():
    print("Loading datasets for placebo check...")
    df_district = pd.read_csv("data/processed/seda_district_panel_pilot.csv")
    df_state = pd.read_csv("data/processed/state_year_panel.csv")
    
    df_district['sedalea'] = df_district['sedalea'].astype(str).str.zfill(7)
    
    # Keep only pre-treatment years (2010, 2011)
    df_district_pre = df_district[df_district['year'].isin([2010, 2011])].copy()
    
    df_state_subset = df_state[[
        'state', 'year', 'backlash_mass', 'gov_party_rep', 'trifecta'
    ]].rename(columns={'state': 'stateabb'})
    
    df = pd.merge(df_district_pre, df_state_subset, on=['stateabb', 'year'], how='inner')
    
    print("Constructing placebo variables...")
    # Define eventual waiver states (WA, OK, FL, NY, TN)
    eventual_waiver_states = ['WA', 'OK', 'FL', 'NY', 'TN']
    
    # Placebo waiver: active only in year 2011 for eventual waiver states
    df['has_waiver_placebo'] = np.where(
        (df['stateabb'].isin(eventual_waiver_states)) & (df['year'] == 2011),
        1, 0
    )
    
    df = df.sort_values(by=['sedalea', 'grade', 'subject', 'year'])
    
    # Contemporaneous variables for placebo (2009-2010)
    df['backlash_x_waiver_placebo'] = df['backlash_mass'] * df['has_waiver_placebo']
    
    df = df.dropna(subset=['backlash_mass', 'has_waiver_placebo', 'sesall', 'povertyall'])
    
    # Create Grade-by-Year Fixed Effects Dummies
    df['grade_year'] = df['year'].astype(str) + "_" + df['grade'].astype(str)
    gy_dummies = pd.get_dummies(df['grade_year'], drop_first=True, dtype=float)
    df = pd.concat([df, gy_dummies], axis=1)
    dummy_cols = list(gy_dummies.columns)
    
    # Run Placebo Regressions for Math and Reading
    for sub, sub_name in [('mth', 'MATH'), ('rla', 'READING')]:
        print(f"\n=======================================================")
        print(f" PLACEBO MODEL FOR {sub_name} ACHIEVEMENT (2010-2011)")
        print(f"=======================================================")
        
        df_sub = df[df['subject'] == sub].copy()
        
        # Set MultiIndex: time_id is numeric
        df_sub['time_id'] = df_sub['year'] * 10 + df_sub['grade']
        df_sub = df_sub.set_index(['sedalea', 'time_id'])
        
        covariates = [
            'backlash_mass', 'has_waiver_placebo', 'backlash_x_waiver_placebo',
            'sesall', 'povertyall', 'unempall', 'totenrl'
        ] + dummy_cols
        
        mod = PanelOLS(
            dependent=df_sub['gcs_mn_all'],
            exog=df_sub[covariates],
            entity_effects=True,
            drop_absorbed=True
        )
        
        res = mod.fit(cov_type='clustered', cluster_entity=True)
        print(f"Placebo DiD - R-squared: {res.rsquared:.4f}, N: {res.nobs}")
        print(res.summary.tables[1])
        
        res_state = mod.fit(cov_type='clustered', clusters=df_sub['stateabb'])
        print(f"\nStandard Errors Clustered at the STATE level (N=6):")
        print(res_state.summary.tables[1])

if __name__ == "__main__":
    run_placebo_regressions()
