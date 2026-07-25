"""
SurakshaCall AI — Published Policy Contradiction Checker
Owner: Lakshay
Task: L-08

Checks if a claimed organization's actions contradict its published policies.
E.g. "CBI" calling to demand money transfer = policy contradiction = scam indicator.
"""
from typing import Optional

# Known policies: what each org NEVER does over a phone call
NEVER_DO = {
    "State Bank of India": ["ask for OTP", "ask for PIN", "ask for CVV", "demand payment"],
    "HDFC Bank": ["ask for OTP", "ask for PIN", "demand payment"],
    "ICICI Bank": ["ask for OTP", "ask for card number"],
    "Reserve Bank of India": ["call individuals", "ask for money", "demand payment"],
    "Central Bureau of Investigation": ["call civilians to demand payment", "ask for money transfer"],
    "Enforcement Directorate": ["ask for money over phone", "demand bank transfer"],
    "Income Tax Department": ["demand immediate payment over call", "ask for OTP"],
    "Telecom Regulatory Authority of India": ["disconnect your SIM unless you pay"],
    "Cyber Crime Department": ["ask for money to clear your name"],
}

def check_policy_contradiction(
    claimed_org: str,
    detected_labels: list[str],
) -> Optional[str]:
    """
    Returns a contradiction description string if the claimed org's
    behaviour contradicts its known policies. Returns None if no contradiction.
    """
    policies = NEVER_DO.get(claimed_org)
    if not policies:
        return None

    violations = []
    if "SECRET_REQUEST" in detected_labels:
        violations.append("requesting confidential credentials (OTP/PIN)")
    if "PAYMENT_REQUEST" in detected_labels:
        violations.append("demanding money transfer")
    if "REMOTE_ACCESS" in detected_labels:
        violations.append("requesting remote access to your device")

    if violations:
        return f"{claimed_org} policy violation: {'; '.join(violations)}"
    return None
