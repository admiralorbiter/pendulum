import pytest
from src.state_crosswalk import clean_state_code

def test_clean_state_code_standard():
    assert clean_state_code("CA") == "CA"
    assert clean_state_code("ny") == "NY"
    assert clean_state_code("  Tx  ") == "TX"

def test_clean_state_code_trends():
    assert clean_state_code("US-AL") == "AL"
    assert clean_state_code("US-CA") == "CA"
    assert clean_state_code("US-WY") == "WY"

def test_clean_state_code_gdelt():
    assert clean_state_code("USAL") == "AL"
    assert clean_state_code("USCA") == "CA"
    assert clean_state_code("USNY") == "NY"

def test_clean_state_code_names():
    assert clean_state_code("California") == "CA"
    assert clean_state_code("new york") == "NY"
    assert clean_state_code("District of Columbia") == "DC"
    assert clean_state_code("Washington DC") == "DC"

def test_clean_state_code_invalid():
    assert clean_state_code("invalid") is None
    assert clean_state_code("US123") is None
    assert clean_state_code(123) is None
    assert clean_state_code(None) is None
