"""
State code crosswalk module.
Provides mapping dictionaries and helper functions to align state identifiers
across GDELT, Google Trends, ESSA plans, and control datasets.
"""

# Map full state names to two-letter abbreviations
NAME_TO_POSTAL = {
    'alabama': 'AL', 'alaska': 'AK', 'arizona': 'AZ', 'arkansas': 'AR', 'california': 'CA',
    'colorado': 'CO', 'connecticut': 'CT', 'delaware': 'DE', 'florida': 'FL', 'georgia': 'GA',
    'hawaii': 'HI', 'idaho': 'ID', 'illinois': 'IL', 'indiana': 'IN', 'iowa': 'IA',
    'kansas': 'KS', 'kentucky': 'KY', 'louisiana': 'LA', 'maine': 'ME', 'maryland': 'MD',
    'massachusetts': 'MA', 'michigan': 'MI', 'minnesota': 'MN', 'mississippi': 'MS', 'missouri': 'MO',
    'montana': 'MT', 'nebraska': 'NE', 'nevada': 'NV', 'new hampshire': 'NH', 'new jersey': 'NJ',
    'new mexico': 'NM', 'new york': 'NY', 'north carolina': 'NC', 'north dakota': 'ND', 'ohio': 'OH',
    'oklahoma': 'OK', 'oregon': 'OR', 'pennsylvania': 'PA', 'rhode island': 'RI', 'south carolina': 'SC',
    'south dakota': 'SD', 'tennessee': 'TN', 'texas': 'TX', 'utah': 'UT', 'vermont': 'VT',
    'virginia': 'VA', 'washington': 'WA', 'west virginia': 'WV', 'wisconsin': 'WI', 'wyoming': 'WY',
    'district of columbia': 'DC', 'washington dc': 'DC'
}

# Map two-letter abbreviations back to full names
POSTAL_TO_NAME = {v: k.title() for k, v in NAME_TO_POSTAL.items()}

def clean_state_code(state_str):
    """
    Standardize any state string to a two-letter postal abbreviation.
    Handles:
      - GDELT codes (e.g. 'USAL', 'USCA')
      - Google Trends codes (e.g. 'US-AL', 'US-CA')
      - Full state names (e.g. 'California', 'new york')
      - Standard abbreviations (e.g. 'CA', 'ca')
    """
    if not isinstance(state_str, str):
        return None
    
    # Strip whitespace and make uppercase for standard checks
    s = state_str.strip().upper()
    
    # Handle Google Trends format: 'US-AL'
    if s.startswith('US-') and len(s) == 5:
        return s[3:]
        
    # Handle GDELT format: 'USCA' or standard ADM1 'US06' etc
    # Standard GDELT US state ADM1 codes are typically 'USAL', 'USAK', etc.
    # Check if it starts with 'US' and has length 4
    if s.startswith('US') and len(s) == 4:
        sub = s[2:]
        if sub.isalpha():
            return sub
            
    # Check if it is already a valid 2-letter code
    if len(s) == 2 and s in POSTAL_TO_NAME:
        return s
        
    # Try mapping full state name
    s_lower = state_str.strip().lower()
    if s_lower in NAME_TO_POSTAL:
        return NAME_TO_POSTAL[s_lower]
        
    return None
