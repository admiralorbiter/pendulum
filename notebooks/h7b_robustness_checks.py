import pandas as pd
import numpy as np
from linearmodels.panel import PanelOLS
import statsmodels.api as sm
import statsmodels.formula.api as smf

# Load state year panel data
df = pd.read_csv('data/processed/state_year_panel.csv')

# Construction of variables
df = df.sort_values(['state', 'year']).copy()
df['backlash_mass_lag1'] = df.groupby('state')['backlash_mass'].shift(1)
df['delta_policy'] = df.groupby('state')['policy_intensity'].diff()
df['backlash_mass_x_waiver'] = df['backlash_mass_lag1'] * df['has_waiver']

# Base sample
required = ['state', 'year', 'delta_policy', 'backlash_mass_lag1',
            'has_waiver', 'backlash_mass_x_waiver', 'gov_party_rep', 'trifecta', 'policy_intensity']
df_clean = df[required].dropna().copy()
df_panel = df_clean.set_index(['state', 'year'])

print("=================================================================")
print("ROBUSTNESS CHECKS FOR H7B (MASS OPT-OUT x WAIVER ACTIVE)")
print("=================================================================\n")

# 1. Baseline Model
print("--- 1. Baseline H7b Model ---")
fit_base = PanelOLS.from_formula(
    'delta_policy ~ backlash_mass_lag1 + has_waiver + backlash_mass_x_waiver '
    '+ gov_party_rep + trifecta + EntityEffects + TimeEffects',
    data=df_panel
).fit(cov_type='clustered', cluster_entity=True)
print(fit_base.summary.tables[1])

# 2. Add state-specific linear trends to the H7b preferred model
print("\n--- 2. H7b Model with State-Specific Linear Trends ---")
# Create state-specific linear trends: state dummies multiplied by year
df_trends = df_clean.copy()
df_trends['year_trend'] = df_trends['year'] - df_trends['year'].mean()
state_dummies = pd.get_dummies(df_trends['state'], prefix='trend')
for col in state_dummies.columns:
    df_trends[col] = state_dummies[col] * df_trends['year_trend']

# Exclude one trend dummy to avoid collinearity with state effects
trend_cols = list(state_dummies.columns)[1:]
trend_formula = ' + '.join(trend_cols)

formula_trends = (
    'delta_policy ~ backlash_mass_lag1 + has_waiver + backlash_mass_x_waiver '
    f'+ gov_party_rep + trifecta + EntityEffects + TimeEffects + {trend_formula}'
)

df_trends_panel = df_trends.set_index(['state', 'year'])
fit_trends = PanelOLS.from_formula(
    formula_trends,
    data=df_trends_panel
).fit(cov_type='clustered', cluster_entity=True)
# print relevant parameters from the pandas Series
coefs = fit_trends.params
pvals = fit_trends.pvalues
tstats = fit_trends.tstats
std_errs = fit_trends.std_errors
for idx in ['backlash_mass_lag1', 'has_waiver', 'backlash_mass_x_waiver']:
    print(f"{idx:<25}: coef={coefs[idx]:.4f}, se={std_errs[idx]:.4f}, t={tstats[idx]:.4f}, p={pvals[idx]:.4f}")

# 3. Subperiod Analysis
print("\n--- 3. Subperiod Analysis ---")
print("A. Pre-ESSA & Waiver-Active Years Only (year <= 2017)")
df_p1 = df_clean[df_clean['year'] <= 2017].set_index(['state', 'year'])
fit_p1 = PanelOLS.from_formula(
    'delta_policy ~ backlash_mass_lag1 + has_waiver + backlash_mass_x_waiver '
    '+ gov_party_rep + trifecta + EntityEffects + TimeEffects',
    data=df_p1
).fit(cov_type='clustered', cluster_entity=True)
print(fit_p1.summary.tables[1])

print("\nB. Active Waiver Years Only (2012 <= year <= 2016)")
df_p2 = df_clean[(df_clean['year'] >= 2012) & (df_clean['year'] <= 2016)].set_index(['state', 'year'])
fit_p2 = PanelOLS.from_formula(
    'delta_policy ~ backlash_mass_lag1 + has_waiver + backlash_mass_x_waiver '
    '+ gov_party_rep + trifecta + EntityEffects + TimeEffects',
    data=df_p2
).fit(cov_type='clustered', cluster_entity=True)
print(fit_p2.summary.tables[1])

# 4. Compare pre-waiver backlash trends between eventual waiver and non-waiver states
print("\n--- 4. Pre-waiver Backlash Trends (2010-2011) ---")
# Define eventual waiver states
waiver_states_df = pd.read_csv('data/raw/nclb_waivers.csv')
eventual_waiver_states = waiver_states_df[waiver_states_df['waiver_approval_year'] <= 2013]['state'].unique()

df_pre = df[df['year'].isin([2010, 2011])].copy()
df_pre['eventual_waiver'] = df_pre['state'].isin(eventual_waiver_states).astype(int)

# Check change in backlash_mass from 2010 to 2011
# We can do a simple Diff-in-Diff style OLS on backlash_mass
df_pre_clean = df_pre[['state', 'year', 'backlash_mass', 'eventual_waiver']].dropna()
fit_pre = smf.ols('backlash_mass ~ eventual_waiver * C(year)', data=df_pre_clean).fit()
print(fit_pre.summary().tables[1])

# Also show mean backlash_mass by group
means = df_pre_clean.groupby(['eventual_waiver', 'year'])['backlash_mass'].mean().unstack()
print("\nMean backlash_mass:")
print(means)

# 5. Split Sample: Effect of backlash_mass in waiver vs. non-waiver state-years
print("\n--- 5. Effect of backlash_mass by Waiver Status ---")
print("A. When waiver is active (has_waiver == 1)")
df_w1 = df_clean[df_clean['has_waiver'] == 1].set_index(['state', 'year'])
fit_w1 = PanelOLS.from_formula(
    'delta_policy ~ backlash_mass_lag1 + gov_party_rep + trifecta + EntityEffects + TimeEffects',
    data=df_w1
).fit(cov_type='clustered', cluster_entity=True)
print(fit_w1.summary.tables[1])

print("\nB. When waiver is inactive (has_waiver == 0)")
df_w0 = df_clean[df_clean['has_waiver'] == 0].set_index(['state', 'year'])
fit_w0 = PanelOLS.from_formula(
    'delta_policy ~ backlash_mass_lag1 + gov_party_rep + trifecta + EntityEffects + TimeEffects',
    data=df_w0
).fit(cov_type='clustered', cluster_entity=True)
print(fit_w0.summary.tables[1])

# 6. Revocation/Termination within-state analysis
print("\n--- 6. Revocation/Termination Within-State Analysis ---")
# WA and OK had waivers revoked in 2014. Let's see what happens to their policy changes in 2014-2015.
df_rev = df[df['state'].isin(['WA', 'OK'])][['state', 'year', 'has_waiver', 'policy_intensity', 'delta_policy', 'backlash_mass']]
print(df_rev.to_string(index=False))
