# Lakshay — Detection & Identity Module

**Owner:** Lakshay  
**Role:** Fast first-stage detection + Identity Verification  

## Files Owned

| File | Task | Status |
|:---|:---|:---|
| `backend/app/detection/labels.py` | L-01 Label Taxonomy | ✅ Done |
| `backend/app/detection/rules.py` | L-04 Deterministic Rules | ✅ Done |
| `backend/app/detection/normalizer.py` | L-03 Normalization | ✅ Done |
| `backend/app/detection/safe_advice.py` | L-05 Safe Advice | ✅ Done |
| `backend/app/detection/service.py` | L-07 Detection API | ✅ Done |
| `backend/app/detection/classifier.py` | L-06 Classifier | 🔲 Day 4 |
| `backend/app/identity/phone_numbers.py` | L-09 Phone Normalization | ✅ Done |
| `backend/app/identity/aliases.py` | L-08 Org Aliases | ✅ Done |
| `backend/app/identity/policy_checks.py` | L-08 Policy Contradiction | ✅ Done |
| `backend/app/identity/verifier.py` | L-08 Full Verifier | 🔲 Day 7 |
| `data/dialogues/` | L-02 Dataset | 🔲 Ongoing |
| `data/trusted_directory/seed.json` | L-08 Trusted DB | ✅ Seeded |
| `tests/test_rules.py` | L-10 Tests | ✅ Done |

## Run Tests

```bash
pytest tests/test_rules.py -v
```

## Team API Contract (DetectionResult)

```python
DetectionResult(
    utterance_normalized: str,
    utterance_redacted: str,
    language: str,
    events: List[DetectionEvent],
    detected_labels: List[str],
    is_critical: bool,
    max_severity: int,     # 0–5
    trigger_llm: bool,
    safe_advice_detected: bool,
)
```

## Contact

Ping Lakshay before changing any field in `DetectionResult` or `DetectionEvent` — Ron and Namit depend on this schema.
