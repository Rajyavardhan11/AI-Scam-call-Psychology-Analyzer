"""
SurakshaCall AI — Safe Advice Detector
Owner: Lakshay
Task: L-05
Prevents "Never share your OTP" from being flagged as SECRET_REQUEST.
"""
import re
from typing import List

SAFE_NEGATION_PATTERNS = [
    re.compile(r"(never|don.?t|do not|never ever|kabhi.?mat|mat).{0,30}(share|give|tell|bata)", re.I),
    re.compile(r"(bank|staff|officer|employee).{0,40}(never|never asks?|kabhi nahi).{0,20}(otp|pin|code|password)", re.I),
    re.compile(r"(protect|keep|save).{0,20}(your\s*)?(otp|pin|password|code)", re.I),
    re.compile(r"(be\s*careful|beware|alert|savdhaan|dhyan\s*raho)", re.I),
    re.compile(r"(legitimate|real|official).{0,30}(never|won.?t|will not).{0,20}(ask|request)", re.I),
]

def is_safe_advice(text: str) -> bool:
    """
    Returns True if the utterance is protective/advisory in nature.
    Used to downgrade a SECRET_REQUEST classification to SAFE_ADVICE.
    """
    for pattern in SAFE_NEGATION_PATTERNS:
        if pattern.search(text):
            return True
    return False

def filter_safe_advice(text: str, detected_labels: List[str]) -> List[str]:
    """
    If text is safe advice, remove conflicting critical labels.
    """
    if is_safe_advice(text):
        return [
            label for label in detected_labels
            if label not in {"SECRET_REQUEST"}
        ] + (["SAFE_ADVICE"] if "SAFE_ADVICE" not in detected_labels else [])
    return detected_labels
