import pytest
import pandas as pd
import numpy as np
from src.district_data_pipeline import clean_district_id, merge_seda_data

def test_clean_district_id_numeric():
    # Verify numbers are converted to padded strings of length 7
    assert clean_district_id(100005) == "0100005"
    assert clean_district_id(5) == "0000005"
    # Verify floats are parsed correctly as integers before padding
    assert clean_district_id(100005.0) == "0100005"

def test_clean_district_id_string():
    # Verify strings are standardized and padded
    assert clean_district_id("100005") == "0100005"
    assert clean_district_id("  100005  ") == "0100005"
    assert clean_district_id("100005.0") == "0100005"
    assert clean_district_id("0100005") == "0100005"

def test_clean_district_id_invalid():
    assert clean_district_id(None) is None
    assert clean_district_id(np.nan) is None

def test_merge_seda_data():
    # Mock scores DataFrame
    df_scores = pd.DataFrame({
        "sedalea": ["0100005", "0100005", "0200001"],
        "year": [2012, 2013, 2012],
        "grade": [3, 3, 4],
        "subject": ["mth", "mth", "rla"],
        "gcs_mn_all": [0.5, 0.6, -0.1]
    })
    
    # Mock covariates DataFrame
    df_covs = pd.DataFrame({
        "sedalea": ["0100005", "0100005", "0200001", "0300002"],
        "year": [2012, 2013, 2012, 2012],
        "grade": [3, 3, 4, 3],
        "sesall": [-0.2, -0.1, 0.5, 0.0]
    })
    
    # Merge datasets
    df_merged = merge_seda_data(df_scores, df_covs)
    
    assert len(df_merged) == 3
    assert "gcs_mn_all" in df_merged.columns
    assert "sesall" in df_merged.columns
    # Check specific values
    row_1 = df_merged[df_merged["year"] == 2012].iloc[0]
    assert row_1["sesall"] == -0.2
    assert row_1["gcs_mn_all"] == 0.5
