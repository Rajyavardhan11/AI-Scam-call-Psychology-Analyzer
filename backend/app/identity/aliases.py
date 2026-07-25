"""
SurakshaCall AI — Organization Aliases
Owner: Lakshay
Task: L-08 (support file)
Maps spoken organization names to canonical entries in the trusted directory.
"""

ALIASES: dict[str, str] = {
    # Banks
    "sbi": "State Bank of India",
    "state bank": "State Bank of India",
    "hdfc": "HDFC Bank",
    "hdfc bank": "HDFC Bank",
    "icici": "ICICI Bank",
    "axis bank": "Axis Bank",
    "pnb": "Punjab National Bank",
    "canara": "Canara Bank",
    "kotak": "Kotak Mahindra Bank",
    # Government
    "cbi": "Central Bureau of Investigation",
    "central bureau": "Central Bureau of Investigation",
    "ed": "Enforcement Directorate",
    "enforcement directorate": "Enforcement Directorate",
    "rbi": "Reserve Bank of India",
    "reserve bank": "Reserve Bank of India",
    "trai": "Telecom Regulatory Authority of India",
    "income tax": "Income Tax Department",
    "it department": "Income Tax Department",
    "customs": "Central Board of Indirect Taxes and Customs",
    "cybercrime": "Cyber Crime Department",
    "cyber crime": "Cyber Crime Department",
    # Courier
    "fedex": "FedEx",
    "dhl": "DHL",
    "bluedart": "Blue Dart",
    "india post": "India Post",
}

def resolve_alias(name: str) -> str:
    """Returns canonical org name, or the original if not found."""
    return ALIASES.get(name.lower().strip(), name)
