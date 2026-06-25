import os
import pandas as pd
import numpy as np
from linearmodels.panel import PanelOLS
import statsmodels.api as sm

def generate_manifest():
    print("Loading datasets...")
    df_state = pd.read_csv("data/processed/state_year_panel.csv")
    df_district = pd.read_csv("data/processed/seda_district_panel_full.csv")
    
    df_district['sedalea'] = df_district['sedalea'].astype(str).str.zfill(7)
    
    df_state_seda = df_state[['state', 'year', 'backlash_mass', 'has_waiver', 'gov_party_rep', 'trifecta', 'election_year']].rename(columns={'state': 'stateabb'})
    
    manifest_rows = []
    
    # ----------------------------------------------------
    # 1. STATE-LEVEL REGRESSIONS
    # ----------------------------------------------------
    print("Running state-level regressions...")
    
    # Prep state variables
    df_state['policy_lag1'] = df_state.groupby('state')['policy_intensity'].shift(1)
    df_state['policy_comm_lag1'] = df_state.groupby('state')['policy_community'].shift(1)
    df_state['policy_labor_lag1'] = df_state.groupby('state')['policy_labor'].shift(1)
    df_state['backlash_lag1'] = df_state.groupby('state')['backlash'].shift(1)
    df_state['delta_policy'] = df_state.groupby('state')['policy_intensity'].diff()
    df_state['backlash_x_waiver'] = df_state['backlash_lag1'] * df_state['has_waiver']
    
    df_state['backlash_mass_lag1'] = df_state.groupby('state')['backlash_mass'].shift(1)
    df_state['backlash_mass_x_waiver'] = df_state['backlash_mass_lag1'] * df_state['has_waiver']
    
    df_state['backlash_media_lag1'] = df_state.groupby('state')['backlash_media'].shift(1)
    df_state['backlash_media_x_waiver'] = df_state['backlash_media_lag1'] * df_state['has_waiver']
    
    df_state['gov_party_change'] = df_state.groupby('state')['gov_party_rep'].diff().abs().fillna(0.0)
    df_state['backlash_x_rep'] = df_state['backlash_lag1'] * df_state['gov_party_rep']
    
    # Model 1.1: H1 Baseline (Policy on Backlash)
    cols1 = ['state', 'year', 'backlash', 'policy_lag1', 'gov_party_rep', 'trifecta', 'election_year']
    df_s1 = df_state[cols1].dropna().set_index(['state', 'year'])
    fit1 = PanelOLS.from_formula(
        'backlash ~ policy_lag1 + gov_party_rep + trifecta + election_year + EntityEffects + TimeEffects',
        data=df_s1
    ).fit(cov_type='clustered', cluster_entity=True)
    manifest_rows.append({
        'model_id': 'state_h1_baseline_policy_on_backlash',
        'level': 'state',
        'subject': 'n/a',
        'subgroup': 'n/a',
        'dependent_var': 'backlash',
        'independent_var': 'policy_lag1',
        'coefficient': fit1.params['policy_lag1'],
        'std_error': fit1.std_errors['policy_lag1'],
        't_stat': fit1.tstats['policy_lag1'],
        'p_value': fit1.pvalues['policy_lag1'],
        'n_obs': fit1.nobs,
        'r_squared': fit1.rsquared
    })
    
    # Model 1.2: H1 Baseline (Backlash on Policy Correction)
    cols2 = ['state', 'year', 'delta_policy', 'backlash_lag1', 'gov_party_rep', 'trifecta']
    df_s2 = df_state[cols2].dropna().set_index(['state', 'year'])
    fit2 = PanelOLS.from_formula(
        'delta_policy ~ backlash_lag1 + gov_party_rep + trifecta + EntityEffects + TimeEffects',
        data=df_s2
    ).fit(cov_type='clustered', cluster_entity=True)
    manifest_rows.append({
        'model_id': 'state_h1_baseline_backlash_on_correction',
        'level': 'state',
        'subject': 'n/a',
        'subgroup': 'n/a',
        'dependent_var': 'delta_policy',
        'independent_var': 'backlash_lag1',
        'coefficient': fit2.params['backlash_lag1'],
        'std_error': fit2.std_errors['backlash_lag1'],
        't_stat': fit2.tstats['backlash_lag1'],
        'p_value': fit2.pvalues['backlash_lag1'],
        'n_obs': fit2.nobs,
        'r_squared': fit2.rsquared
    })
    
    # Model 1.3: H7b (ESEA Waiver x Mass Backlash)
    cols3 = ['state', 'year', 'delta_policy', 'backlash_mass_lag1', 'has_waiver', 'backlash_mass_x_waiver', 'gov_party_rep', 'trifecta']
    df_s3 = df_state[cols3].dropna().set_index(['state', 'year'])
    fit3 = PanelOLS.from_formula(
        'delta_policy ~ backlash_mass_lag1 + has_waiver + backlash_mass_x_waiver + gov_party_rep + trifecta + EntityEffects + TimeEffects',
        data=df_s3
    ).fit(cov_type='clustered', cluster_entity=True)
    manifest_rows.append({
        'model_id': 'state_h7b_waiver_x_mass_backlash',
        'level': 'state',
        'subject': 'n/a',
        'subgroup': 'n/a',
        'dependent_var': 'delta_policy',
        'independent_var': 'backlash_mass_x_waiver',
        'coefficient': fit3.params['backlash_mass_x_waiver'],
        'std_error': fit3.std_errors['backlash_mass_x_waiver'],
        't_stat': fit3.tstats['backlash_mass_x_waiver'],
        'p_value': fit3.pvalues['backlash_mass_x_waiver'],
        'n_obs': fit3.nobs,
        'r_squared': fit3.rsquared
    })
    
    # Model 1.4: H7b (ESEA Waiver x Media Backlash)
    cols4 = ['state', 'year', 'delta_policy', 'backlash_media_lag1', 'has_waiver', 'backlash_media_x_waiver', 'gov_party_rep', 'trifecta']
    df_s4 = df_state[cols4].dropna().set_index(['state', 'year'])
    fit4 = PanelOLS.from_formula(
        'delta_policy ~ backlash_media_lag1 + has_waiver + backlash_media_x_waiver + gov_party_rep + trifecta + EntityEffects + TimeEffects',
        data=df_s4
    ).fit(cov_type='clustered', cluster_entity=True)
    manifest_rows.append({
        'model_id': 'state_h7b_waiver_x_media_backlash',
        'level': 'state',
        'subject': 'n/a',
        'subgroup': 'n/a',
        'dependent_var': 'delta_policy',
        'independent_var': 'backlash_media_x_waiver',
        'coefficient': fit4.params['backlash_media_x_waiver'],
        'std_error': fit4.std_errors['backlash_media_x_waiver'],
        't_stat': fit4.tstats['backlash_media_x_waiver'],
        'p_value': fit4.pvalues['backlash_media_x_waiver'],
        'n_obs': fit4.nobs,
        'r_squared': fit4.rsquared
    })

    # Model 1.5: H2 legislative frequency (cross-sectional OLS)
    df_state['biennial_legislature'] = df_state['state'].isin(['TX', 'MT', 'NV', 'ND']).astype(float)
    detrended_series = []
    for state, gp in df_state.groupby('state'):
        gp = gp.sort_values('year').copy()
        y = gp['policy_intensity'].values
        x = gp['year'].values
        if len(gp) > 1:
            slope, intercept = np.polyfit(x, y, 1)
            gp['policy_detrended'] = y - (slope * x + intercept)
        else:
            gp['policy_detrended'] = 0.0
        detrended_series.append(gp)
    df_detrend = pd.concat(detrended_series, ignore_index=True)
    state_amplitude = df_detrend.groupby('state')['policy_detrended'].std().reset_index().rename(columns={'policy_detrended': 'amplitude'})
    state_biennial = df_state.groupby('state')['biennial_legislature'].first().reset_index()
    df_h2 = pd.merge(state_amplitude, state_biennial, on='state')
    X_h2 = sm.add_constant(df_h2['biennial_legislature'])
    fit_h2 = sm.OLS(df_h2['amplitude'], X_h2).fit()
    manifest_rows.append({
        'model_id': 'state_h2_biennial_legislature_on_amplitude',
        'level': 'state',
        'subject': 'n/a',
        'subgroup': 'n/a',
        'dependent_var': 'amplitude',
        'independent_var': 'biennial_legislature',
        'coefficient': fit_h2.params['biennial_legislature'],
        'std_error': fit_h2.bse['biennial_legislature'],
        't_stat': fit_h2.tvalues['biennial_legislature'],
        'p_value': fit_h2.pvalues['biennial_legislature'],
        'n_obs': int(fit_h2.nobs),
        'r_squared': fit_h2.rsquared
    })

    # Model 1.6: H7b Robustness (Leave-One-Component-Out: No VAM)
    df_state['raw_intensity_no_vam'] = df_state['exit_exam'] + df_state['af_grading'] + df_state['third_grade_retention']
    df_state['policy_intensity_no_vam'] = 0.0
    for mask in [df_state['year'] <= 2017, df_state['year'] >= 2018]:
        mean_val = df_state.loc[mask, 'raw_intensity_no_vam'].mean()
        std_val = df_state.loc[mask, 'raw_intensity_no_vam'].std()
        if std_val == 0 or pd.isna(std_val): std_val = 1.0
        df_state.loc[mask, 'policy_intensity_no_vam'] = (df_state.loc[mask, 'raw_intensity_no_vam'] - mean_val) / std_val
    df_state['delta_policy_no_vam'] = df_state.groupby('state')['policy_intensity_no_vam'].diff()
    df_state['policy_no_vam_lag1'] = df_state.groupby('state')['policy_intensity_no_vam'].shift(1)
    df_state['backlash_x_waiver_no_vam'] = df_state['backlash_lag1'] * df_state['has_waiver']
    
    cols_loco = ['state', 'year', 'delta_policy_no_vam', 'backlash_lag1', 'has_waiver', 'backlash_x_waiver_no_vam', 'gov_party_rep', 'trifecta']
    df_s_loco = df_state[cols_loco].dropna().set_index(['state', 'year'])
    fit_loco = PanelOLS.from_formula(
        'delta_policy_no_vam ~ backlash_lag1 + has_waiver + backlash_x_waiver_no_vam + gov_party_rep + trifecta + EntityEffects + TimeEffects',
        data=df_s_loco
    ).fit(cov_type='clustered', cluster_entity=True)
    manifest_rows.append({
        'model_id': 'state_h7b_robustness_no_vam_index',
        'level': 'state',
        'subject': 'n/a',
        'subgroup': 'n/a',
        'dependent_var': 'delta_policy_no_vam',
        'independent_var': 'backlash_x_waiver_no_vam',
        'coefficient': fit_loco.params['backlash_x_waiver_no_vam'],
        'std_error': fit_loco.std_errors['backlash_x_waiver_no_vam'],
        't_stat': fit_loco.tstats['backlash_x_waiver_no_vam'],
        'p_value': fit_loco.pvalues['backlash_x_waiver_no_vam'],
        'n_obs': fit_loco.nobs,
        'r_squared': fit_loco.rsquared
    })
    
    # Model 1.7: H7b Robustness on Individual Components
    for comp in ['exit_exam', 'af_grading', 'third_grade_retention', 'vam_eval']:
        df_state[f'delta_{comp}'] = df_state.groupby('state')[comp].diff()
        cols_comp = ['state', 'year', f'delta_{comp}', 'backlash_lag1', 'has_waiver', 'backlash_x_waiver', 'gov_party_rep', 'trifecta']
        df_s_comp = df_state[cols_comp].dropna().set_index(['state', 'year'])
        fit_comp = PanelOLS.from_formula(
            f'delta_{comp} ~ backlash_lag1 + has_waiver + backlash_x_waiver + gov_party_rep + trifecta + EntityEffects + TimeEffects',
            data=df_s_comp
        ).fit(cov_type='clustered', cluster_entity=True)
        manifest_rows.append({
            'model_id': f'state_h7b_robustness_outcome_change_in_{comp}',
            'level': 'state',
            'subject': 'n/a',
            'subgroup': 'n/a',
            'dependent_var': f'delta_{comp}',
            'independent_var': 'backlash_x_waiver',
            'coefficient': fit_comp.params['backlash_x_waiver'],
            'std_error': fit_comp.std_errors['backlash_x_waiver'],
            't_stat': fit_comp.tstats['backlash_x_waiver'],
            'p_value': fit_comp.pvalues['backlash_x_waiver'],
            'n_obs': fit_comp.nobs,
            'r_squared': fit_comp.rsquared
        })

    # ----------------------------------------------------
    # 2. DISTRICT-LEVEL REGRESSIONS (Full 51-State SEDA Panel)
    # ----------------------------------------------------
    print("Running district-level regressions (on full 1.23M panel, this may take a couple of minutes)...")
    
    subgroups = {
        'all': ('All Students', 'gcs_mn_all'),
        'wht': ('White Students', 'gcs_mn_wht'),
        'blk': ('Black Students', 'gcs_mn_blk'),
        'ecd': ('Econ-Disadvantaged', 'gcs_mn_ecd')
    }
    
    # event_waiver states for placebo
    eventual_waiver_states = df_state[df_state['has_waiver'] == 1]['state'].unique()
    
    for sub, sub_name in [('mth', 'Math'), ('rla', 'Reading')]:
        df_sub = df_district[df_district['subject'] == sub].copy()
        
        # Merge with full state panel
        df_merged = pd.merge(df_sub, df_state_seda, on=['stateabb', 'year'], how='inner')
        df_merged = df_merged.sort_values(by=['sedalea', 'grade', 'year']).reset_index(drop=True)
        
        # Lags
        districts_full = df_merged['sedalea'].values
        grades_full = df_merged['grade'].values
        has_lag = (districts_full[1:] == districts_full[:-1]) & (grades_full[1:] == grades_full[:-1])
        lag_idx = np.zeros(len(df_merged), dtype=int) - 1
        lag_idx[1:][has_lag] = np.arange(len(df_merged) - 1)[has_lag]
        
        def get_lags(arr, idx):
            arr_nan = np.append(arr, np.nan)
            return arr_nan[idx]
            
        df_merged['backlash_mass_lag1'] = get_lags(df_merged['backlash_mass'].values, lag_idx)
        df_merged['has_waiver_lag1'] = get_lags(df_merged['has_waiver'].values, lag_idx)
        df_merged['backlash_x_waiver_lag1'] = df_merged['backlash_mass_lag1'] * df_merged['has_waiver_lag1']
        
        # Loop over subgroups
        for g_key, (g_label, outcome_col) in subgroups.items():
            df_g = df_merged.dropna(subset=[outcome_col, 'backlash_mass_lag1', 'has_waiver_lag1', 'sesall', 'povertyall']).copy().reset_index(drop=True)
            
            if len(df_g) < 5000:
                continue
                
            # Grade-by-year dummies
            df_g['grade_year'] = df_g['year'].astype(str) + "_" + df_g['grade'].astype(str)
            gy_dummies = pd.get_dummies(df_g['grade_year'], drop_first=True, dtype=float)
            df_g = pd.concat([df_g, gy_dummies], axis=1)
            dummy_cols = list(gy_dummies.columns)
            
            df_g['time_id'] = df_g['year'] * 10 + df_g['grade']
            df_g_panel = df_g.set_index(['sedalea', 'time_id'])
            
            covariates = [
                'backlash_mass_lag1', 'has_waiver_lag1', 'backlash_x_waiver_lag1',
                'sesall', 'povertyall', 'unempall', 'totenrl'
            ] + dummy_cols
            
            mod = PanelOLS(df_g_panel[outcome_col], df_g_panel[covariates], entity_effects=True)
            res = mod.fit(cov_type='clustered', clusters=df_g_panel['stateabb'])
            
            manifest_rows.append({
                'model_id': f'district_{sub}_subgroup_{g_key}_model_a',
                'level': 'district',
                'subject': sub_name.lower(),
                'subgroup': g_key,
                'dependent_var': outcome_col,
                'independent_var': 'backlash_x_waiver_lag1',
                'coefficient': res.params['backlash_x_waiver_lag1'],
                'std_error': res.std_errors['backlash_x_waiver_lag1'],
                't_stat': res.tstats['backlash_x_waiver_lag1'],
                'p_value': res.pvalues['backlash_x_waiver_lag1'],
                'n_obs': res.nobs,
                'r_squared': res.rsquared
            })
            
        # 2.2 Model B (Triple Interaction with Newly Constrained proxy)
        df_g_all = df_merged.dropna(subset=['gcs_mn_all', 'backlash_mass_lag1', 'has_waiver_lag1', 'sesall', 'povertyall']).copy().reset_index(drop=True)
        df_g_all['newly_constrained'] = (df_g_all['sesall'] <= 0.0).astype(int)
        df_g_all['backlash_x_waiver_x_constrained_lag1'] = df_g_all['backlash_x_waiver_lag1'] * df_g_all['newly_constrained']
        
        df_g_all['grade_year'] = df_g_all['year'].astype(str) + "_" + df_g_all['grade'].astype(str)
        gy_dummies = pd.get_dummies(df_g_all['grade_year'], drop_first=True, dtype=float)
        df_g_all = pd.concat([df_g_all, gy_dummies], axis=1)
        dummy_cols = list(gy_dummies.columns)
        
        df_g_all['time_id'] = df_g_all['year'] * 10 + df_g_all['grade']
        df_g_all_panel = df_g_all.set_index(['sedalea', 'time_id'])
        
        covariates_b = [
            'backlash_mass_lag1', 'has_waiver_lag1', 'backlash_x_waiver_lag1',
            'newly_constrained', 'backlash_x_waiver_x_constrained_lag1',
            'sesall', 'povertyall', 'unempall', 'totenrl'
        ] + dummy_cols
        
        mod_b = PanelOLS(df_g_all_panel['gcs_mn_all'], df_g_all_panel[covariates_b], entity_effects=True)
        res_b = mod_b.fit(cov_type='clustered', clusters=df_g_all_panel['stateabb'])
        
        manifest_rows.append({
            'model_id': f'district_{sub}_model_b_newly_constrained',
            'level': 'district',
            'subject': sub_name.lower(),
            'subgroup': 'all',
            'dependent_var': 'gcs_mn_all',
            'independent_var': 'backlash_x_waiver_x_constrained_lag1',
            'coefficient': res_b.params['backlash_x_waiver_x_constrained_lag1'],
            'std_error': res_b.std_errors['backlash_x_waiver_x_constrained_lag1'],
            't_stat': res_b.tstats['backlash_x_waiver_x_constrained_lag1'],
            'p_value': res_b.pvalues['backlash_x_waiver_x_constrained_lag1'],
            'n_obs': res_b.nobs,
            'r_squared': res_b.rsquared
        })

        # 2.3 Placebo Regressions (2010-2011)
        df_pre = df_district[(df_district['subject'] == sub) & (df_district['year'].isin([2010, 2011]))].copy()
        
        df_pre_merged = pd.merge(df_pre, df_state_seda, on=['stateabb', 'year'], how='inner')
        df_pre_merged = df_pre_merged.sort_values(by=['sedalea', 'grade', 'year']).reset_index(drop=True)
        
        df_pre_merged['has_waiver_placebo'] = np.where(
            (df_pre_merged['stateabb'].isin(eventual_waiver_states)) & (df_pre_merged['year'] == 2011),
            1, 0
        )
        df_pre_merged['backlash_x_waiver_placebo'] = df_pre_merged['backlash_mass'] * df_pre_merged['has_waiver_placebo']
        
        for g_key, (g_label, outcome_col) in subgroups.items():
            df_g_pre = df_pre_merged.dropna(subset=[outcome_col, 'backlash_mass', 'has_waiver_placebo', 'sesall', 'povertyall']).copy().reset_index(drop=True)
            
            if len(df_g_pre) < 5000:
                continue
                
            df_g_pre['grade_year'] = df_g_pre['year'].astype(str) + "_" + df_g_pre['grade'].astype(str)
            gy_dummies_pre = pd.get_dummies(df_g_pre['grade_year'], drop_first=True, dtype=float)
            df_g_pre = pd.concat([df_g_pre, gy_dummies_pre], axis=1)
            dummy_cols_pre = list(gy_dummies_pre.columns)
            
            df_g_pre['time_id'] = df_g_pre['year'] * 10 + df_g_pre['grade']
            df_g_pre_panel = df_g_pre.set_index(['sedalea', 'time_id'])
            
            covariates_pre = [
                'backlash_mass', 'has_waiver_placebo', 'backlash_x_waiver_placebo',
                'sesall', 'povertyall', 'unempall', 'totenrl'
            ] + dummy_cols_pre
            
            mod_pre = PanelOLS(df_g_pre_panel[outcome_col], df_g_pre_panel[covariates_pre], entity_effects=True, drop_absorbed=True)
            res_pre = mod_pre.fit(cov_type='clustered', clusters=df_g_pre_panel['stateabb'])
            
            manifest_rows.append({
                'model_id': f'district_{sub}_subgroup_{g_key}_placebo',
                'level': 'district',
                'subject': sub_name.lower(),
                'subgroup': g_key,
                'dependent_var': outcome_col,
                'independent_var': 'backlash_x_waiver_placebo',
                'coefficient': res_pre.params['backlash_x_waiver_placebo'],
                'std_error': res_pre.std_errors['backlash_x_waiver_placebo'],
                't_stat': res_pre.tstats['backlash_x_waiver_placebo'],
                'p_value': res_pre.pvalues['backlash_x_waiver_placebo'],
                'n_obs': res_pre.nobs,
                'r_squared': res_pre.rsquared
            })

    # Save to CSV
    os.makedirs("reports", exist_ok=True)
    df_manifest = pd.DataFrame(manifest_rows)
    df_manifest.to_csv("reports/results_manifest.csv", index=False)
    print("Successfully generated reports/results_manifest.csv!")
    print(f"Total models exported: {len(df_manifest)}")

if __name__ == "__main__":
    generate_manifest()
