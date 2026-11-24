# Hosted STUDY Pipeline Evidence-Readiness Gate

Status: Operator-locked gate definition for `#362` (2026-11-24). `hosted_study_pipeline` remains `BLOCKED` until all criteria below are satisfied and signed off.

## Promotion Criteria

`capabilities.hosted_study_pipeline` remains `BLOCKED` until all three requirements are met:

1. **PSR-1 pass**: PSR-1 (`#383` / `#363`) passes on a live pin with recorded receipts.
2. **Verified natural-play evidence pack**: One clean natural-play evidence pack is archived with:
   - Verified deterministic reconstruction.
   - **Blocking automated privacy redaction check**: zero raw email addresses, session tokens, private inbox contents, or internal entity IDs.
3. **Steward sign-off**: Explicit spot-check sign-off recorded in the promotion receipt by the named steward (Zero-State operator).
