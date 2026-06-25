import os
import pandas as pd
import numpy as np

# Columns to load from the test scores CSV to minimize memory footprint
COLS_SCORES = [
    'sedalea', 'sedaleaname', 'subject', 'grade', 'year', 'fips', 'stateabb',
    'gcs_mn_all', 'gcs_mn_se_all', 'tot_asmt_all',
    'gcs_mn_wht', 'gcs_mn_se_wht', 'tot_asmt_wht',
    'gcs_mn_blk', 'gcs_mn_se_blk', 'tot_asmt_blk',
    'gcs_mn_ecd', 'gcs_mn_se_ecd', 'tot_asmt_ecd'
]

# Columns to load from the covariates CSV to minimize memory footprint
COLS_COVS = [
    'sedalea', 'year', 'grade', 'fips', 'stateabb',
    'sesall', 'povertyall', 'unempall', 'snapall', 'single_momall',
    'lninc50all', 'baplusall', 'perwht', 'perblk', 'perhsp', 'totenrl', 'urbanicity'
]

def clean_district_id(lea_id):
    """
    Standardize district (LEA) ID to a 7-character zero-padded string.
    Handles:
      - Integers (e.g. 100005 -> "0100005")
      - Floats (e.g. 100005.0 -> "0100005")
      - String representations (e.g. "100005" -> "0100005")
    """
    if pd.isna(lea_id) or lea_id is None:
        return None
        
    try:
        # Convert to string and strip whitespace
        s = str(lea_id).strip()
        # Handle float strings like "100005.0"
        if '.' in s:
            s = s.split('.')[0]
        # Pad with leading zeros to length 7
        return s.zfill(7)
    except Exception:
        return None

def load_and_filter_seda_scores(file_path, pilot_states=None):
    """
    Loads and cleans SEDA scores. Filters by state, grades (3-8), and subjects.
    Standardizes LEA IDs and filters out rows without valid outcomes.
    """
    print(f"Loading SEDA scores from {file_path}...")
    
    # Read only required columns to save RAM
    df = pd.read_csv(file_path, usecols=COLS_SCORES)
    
    # Filter by state if requested
    if pilot_states is not None:
        df = df[df['stateabb'].isin(pilot_states)]
        
    # Standardize LEA ID
    df['sedalea'] = df['sedalea'].apply(clean_district_id)
    # Drop rows where LEA ID cleaning failed
    df = df.dropna(subset=['sedalea'])
    
    # Filter valid outcome scores
    df = df.dropna(subset=['gcs_mn_all'])
    
    return df

def load_and_filter_seda_covariates(file_path, pilot_states=None):
    """
    Loads and cleans SEDA covariates. Filters by state and standardizes LEA IDs.
    """
    print(f"Loading SEDA covariates from {file_path}...")
    
    # Read only required columns to save RAM
    df = pd.read_csv(file_path, usecols=COLS_COVS)
    
    # Filter by state if requested
    if pilot_states is not None:
        df = df[df['stateabb'].isin(pilot_states)]
        
    # Standardize LEA ID
    df['sedalea'] = df['sedalea'].apply(clean_district_id)
    df = df.dropna(subset=['sedalea'])
    
    return df

def merge_seda_data(df_scores, df_covs):
    """
    Inner-merges SEDA scores and covariates on ['sedalea', 'year', 'grade'].
    """
    print("Merging scores and covariates...")
    # Drop redundant stateabb/fips columns from covariates prior to merge
    df_covs_subset = df_covs.drop(columns=['stateabb', 'fips'], errors='ignore')
    
    df_merged = pd.merge(
        df_scores,
        df_covs_subset,
        on=['sedalea', 'year', 'grade'],
        how='inner'
    )
    return df_merged

def run_pipeline(scores_path, covs_path, output_path, pilot_states=None):
    """
    Coordinates SEDA data loading, filtering, merging, and saves the output to a CSV.
    """
    df_scores = load_and_filter_seda_scores(scores_path, pilot_states)
    df_covs = load_and_filter_seda_covariates(covs_path, pilot_states)
    
    df_merged = merge_seda_data(df_scores, df_covs)
    
    # Ensure processed directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    print(f"Saving merged panel to {output_path}...")
    df_merged.to_csv(output_path, index=False)
    print("Pipeline execution completed successfully.")
    
    return df_merged
