import os
import sys

# Ensure src is in python path
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from district_data_pipeline import run_pipeline

if __name__ == "__main__":
    scores_path = "data/raw/seda/seda_geodist_long_gcs_6.0.csv"
    covs_path = "data/raw/seda/seda_cov_geodist_long_6.0.csv"
    output_path = "data/processed/seda_district_panel_full.csv"
    
    print("=======================================================")
    print(" RUNNING PIPELINE FOR ALL 51 JURISDICTIONS (FULL)")
    print("=======================================================")
    
    df_merged = run_pipeline(
        scores_path=scores_path,
        covs_path=covs_path,
        output_path=output_path,
        pilot_states=None  # Keeps all states
    )
    print(f"\nCompleted! Merged panel saved to {output_path}")
    print(f"Total row count: {len(df_merged)}")
    print(f"Unique districts: {df_merged['sedalea'].nunique()}")
    print(f"Unique states: {df_merged['stateabb'].nunique()}")
