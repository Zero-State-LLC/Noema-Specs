# Operator Handoff: PSR-1 & Hosted STUDY Promotion (`#421` -> `#422` -> `#423`)

All automated code, validators, and client tooling are merged and green on `main`. The remaining gates require real human/operator and Steward execution:

1. **Pre-flight (`noema-client==0.1.24`)**
   - Run `noema doctor --json` and confirm `reachability == "ok"`, `credential_origin_ok == true`, and `worker_version == "6a94f045-77e8-4957-9393-e56a071040b5"`.
2. **`#421` — First Live Tier-3 `/connect` Enrollment Receipt**
   - Outside Tier-3 operator runs `noema connect` + human approval on live pin, then emits a `psr1_tier3_enrollment` receipt (reference helper: `noema-client/examples/custom_http_ws_reference.py:emit_psr1_enrollment_receipt`).
   - Validate: `python3 tools/check_psr1_readiness.py --enrollment <receipt.json>`.
3. **`#422` — PSR-1 Cohort & Two-Style Adapter Endurance**
   - Run `>=6` Controllers (`>=2` non-first-party spanning `framework-adapter` and `custom-http-ws`, `>=1` Tier-3 operator, `Δcycle >= 24`, `>=20` actions/Player, `>=60` total, `0` regressions) and archive a `psr1_cohort_summary` receipt.
   - Validate: `python3 tools/check_psr1_readiness.py --cohort <cohort.json>`.
4. **`#423` — Natural-Play Privacy Redaction & Steward Sign-Off**
   - Run `python3 scripts/validate_study_privacy_redaction.py <pack-dir>` in `Noema` (must exit `0`), record Steward spot-check sign-off in a `hosted_study_promotion` receipt.
   - Validate: `python3 tools/check_psr1_readiness.py --study <study.json>`.
