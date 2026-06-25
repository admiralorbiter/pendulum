"""
Randomization Inference: Mass Opt-Out x Waiver Active Interaction (H7b Clean Specification)
==========================================================================
Purpose:
    Re-run the randomization inference permutation test specifically on the
    MASS OPT-OUT x WAIVER interaction (backlash_mass x waiver_active).
    
    The prior p=0.001 in the notebook was computed on the COMPOSITE backlash x waiver
    interaction (H7b composite), which is contaminated by VAM circularity (pre-2018
    ESEA waivers algebraically required VAM, conflating the policy measure with the
    institutional constraint). This script targets only the clean mass-opt-out signal.

Model:
    delta_policy ~ backlash_mass_lag1 + has_waiver + backlash_mass_x_waiver
                   + gov_party_rep + trifecta + state_FE + year_FE
    Clustered SEs on state.

Permutation Strategy:
    Shuffle the waiver_active (has_waiver) TIME-SERIES assignment ACROSS STATES
    within partisan strata (Dem / Rep / Swing), preserving within-state temporal
    structure of the waiver indicator. 1,000 permutations.

Expected Observed Coefficient: approximately -0.128 (p=0.014 from notebook cell 9)
"""

import sys
import io
import pandas as pd
import numpy as np
from linearmodels.panel import PanelOLS

# Force UTF-8 output to avoid Windows cp1252 encoding errors
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# -- 1. Load Data -------------------------------------------------------
print("Loading state_year_panel.csv ...")
df = pd.read_csv('data/processed/state_year_panel.csv')
print(f"  Loaded: {df.shape[0]} rows x {df.shape[1]} columns")
print(f"  States: {df['state'].nunique()}, Years: {df['year'].min()}-{df['year'].max()}")

# -- 2. Construct Required Variables ------------------------------------
df = df.sort_values(['state', 'year']).copy()

# Lagged backlash_mass and delta_policy (if not already present)
df['backlash_mass_lag1'] = df.groupby('state')['backlash_mass'].shift(1)
df['delta_policy']       = df.groupby('state')['policy_intensity'].diff()

# Interaction: mass opt-out x waiver
df['backlash_mass_x_waiver'] = df['backlash_mass_lag1'] * df['has_waiver']

required = ['state', 'year', 'delta_policy', 'backlash_mass_lag1',
            'has_waiver', 'backlash_mass_x_waiver', 'gov_party_rep', 'trifecta']
df_clean = df[required].dropna().copy()
print(f"  Analysis sample after dropna: {len(df_clean)} rows")

# -- 3. Baseline Model: Mass Opt-Out x Waiver ---------------------------
print("\n--- Baseline Model: delta_policy ~ backlash_mass_lag1 * has_waiver ---")
df_panel = df_clean.set_index(['state', 'year'])

fit_observed = PanelOLS.from_formula(
    'delta_policy ~ backlash_mass_lag1 + has_waiver + backlash_mass_x_waiver '
    '+ gov_party_rep + trifecta + EntityEffects + TimeEffects',
    data=df_panel
).fit(cov_type='clustered', cluster_entity=True)

observed_coef = fit_observed.params['backlash_mass_x_waiver']
observed_pval = fit_observed.pvalues['backlash_mass_x_waiver']

print(fit_observed.summary.tables[1])
print(f"\n  Observed beta(backlash_mass_x_waiver) = {observed_coef:.4f}")
print(f"  Analytic p-value (clustered SE)       = {observed_pval:.4f}")

# -- 4. Randomization Inference: Permute waiver_active Across States ----
print("\n--- Randomization Inference (1,000 permutations) ---")
print("    Strategy: shuffle waiver time-series across states")
print("    within partisan strata (Dem / Rep / Swing), preserving temporal order")
print()

# Build partisan strata (same as notebook)
state_party = df.groupby('state')['gov_party_rep'].mean().to_dict()
state_strata = {}
for s, p in state_party.items():
    if p <= 0.2:
        state_strata[s] = 'Dem'
    elif p >= 0.8:
        state_strata[s] = 'Rep'
    else:
        state_strata[s] = 'Swing'

# Store each state's full waiver time-series (indexed from 2010 onward)
state_waivers = df.sort_values('year').groupby('state')['has_waiver'].apply(list).to_dict()

N_PERM = 1000
np.random.seed(42)
placebo_coefs = []

for i in range(N_PERM):
    if (i + 1) % 100 == 0:
        print(f"    Permutation {i+1}/{N_PERM} ...")

    # Build state -> permuted waiver mapping within strata
    shuffled_mapping = {}
    for strata_val in ['Dem', 'Rep', 'Swing']:
        strata_states = [s for s, v in state_strata.items() if v == strata_val]
        shuffled_strata = np.random.permutation(strata_states)
        for s_orig, s_shuf in zip(strata_states, shuffled_strata):
            shuffled_mapping[s_orig] = state_waivers[s_shuf]

    # Apply permuted waiver to temporary copy
    df_temp = df.copy()
    df_temp['has_waiver_perm'] = df_temp.apply(
        lambda r: shuffled_mapping[r['state']][r['year'] - 2010]
        if (r['year'] - 2010) < len(shuffled_mapping[r['state']]) else 0,
        axis=1
    )
    # Reconstruct lagged mass x permuted waiver
    df_temp['backlash_mass_x_waiver_perm'] = (
        df_temp['backlash_mass_lag1'] * df_temp['has_waiver_perm']
    )

    df_h7_perm = df_temp[
        ['state', 'year', 'delta_policy', 'backlash_mass_lag1',
         'has_waiver_perm', 'backlash_mass_x_waiver_perm',
         'gov_party_rep', 'trifecta']
    ].dropna().set_index(['state', 'year'])

    try:
        fit_perm = PanelOLS.from_formula(
            'delta_policy ~ backlash_mass_lag1 + has_waiver_perm '
            '+ backlash_mass_x_waiver_perm + gov_party_rep + trifecta '
            '+ EntityEffects + TimeEffects',
            data=df_h7_perm
        ).fit(cov_type='clustered', cluster_entity=True)
        placebo_coefs.append(fit_perm.params['backlash_mass_x_waiver_perm'])
    except Exception as e:
        # Skip degenerate permutations
        placebo_coefs.append(np.nan)

# -- 5. Compute Randomization P-Value -----------------------------------
placebo_arr = np.array(placebo_coefs)
n_valid     = np.sum(~np.isnan(placebo_arr))
placebo_arr = placebo_arr[~np.isnan(placebo_arr)]

# One-sided p-value: proportion of placebo coefs <= observed coef
# (because observed is negative -- we test that negatives this extreme are rare)
p_one_sided = np.mean(placebo_arr <= observed_coef)

# Two-sided p-value (conventional for randomization inference)
p_two_sided = np.mean(np.abs(placebo_arr) >= np.abs(observed_coef))

print("\n=================================================================")
print("  RANDOMIZATION INFERENCE RESULTS -- Mass Opt-Out x Waiver (H7b)")
print("=================================================================")
print(f"  Observed beta(backlash_mass_x_waiver)  = {observed_coef:.4f}")
print(f"  Analytic p-value (clustered SE)        = {observed_pval:.4f}")
print(f"  Valid permutations completed           = {n_valid} / {N_PERM}")
print(f"  Mean placebo coefficient               = {np.mean(placebo_arr):.4f}")
print(f"  Std  placebo coefficient               = {np.std(placebo_arr):.4f}")
print(f"  Min / Max placebo                      = {np.min(placebo_arr):.4f} / {np.max(placebo_arr):.4f}")
print()
print(f"  Randomization p-value (one-sided <=)   = {p_one_sided:.4f}")
print(f"  Randomization p-value (two-sided)      = {p_two_sided:.4f}")
print()
print("  Interpretation:")
if p_two_sided < 0.05:
    print(f"  SIGNIFICANT: The observed mass opt-out x waiver interaction")
    print(f"  (beta = {observed_coef:.4f}) is more extreme than {(1-p_two_sided)*100:.1f}% of")
    print(f"  permuted placebo distributions. The result is not attributable")
    print(f"  to random assignment of waiver histories.")
else:
    print(f"  NOT SIGNIFICANT at alpha=0.05: The permutation distribution does not")
    print(f"  exclude the observed coefficient at conventional thresholds.")
print("=================================================================")
