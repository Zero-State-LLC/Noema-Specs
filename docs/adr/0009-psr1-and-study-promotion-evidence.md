# ADR-0009: PSR-1 & Hosted STUDY Promotion Evidence Custody and Governance

- **Status**: Accepted
- **Date**: 2026-11-24
- **Relates to**: `#421`, `#422`, `#423`, `#383`, `#363`, `#362`

## Context
Promoting `third_party_agent_compatibility_at_scale` (PSR-1) and `hosted_study_pipeline` (STUDY) out of `BLOCKED` requires human-gated evidence across three sequential milestones: first Tier-3 operator enrollment (`#421`), multi-Controller two-style endurance (`#422`), and natural-play privacy redaction with Steward sign-off (`#423`). Without explicit governance boundaries, internal testers could substitute for external operators, redaction failures could be hand-patched, or receipts could drift outside version control.

## Decision
1. **Tier-3 Operator Independence (`#421`)**: A `Tier-3 Operator` must be external to Zero-State-LLC with no org membership and no `ADMIN_ALLOWLIST_EMAILS` access, enrolling via standard `/connect` + human approval without admin bypass.
2. **Contiguous Live Cohort Window (`#422`)**: The `>=6` Controller, `Δcycle >= 24`, two-style (`framework-adapter` + `custom-http-ws`) endurance cohort runs on live `world.perihelion-reach-3` in one contiguous `24+` cycle window. Clean individual Controller reconnects are permitted provided `>=6` Controllers meet `>=20` actions each (`>=60` total) with `0` protocol regressions.
3. **Fail-Closed Redaction & Cohort Harvesting (`#423`)**: The `#423` natural-play evidence pack is harvested directly from the `#422` cohort window. Any `validate_study_privacy_redaction.py` failure blocks promotion until the exporter is fixed and the pack is re-exported; hand-editing archives is prohibited.
4. **Steward Separation & Git Receipt Custody**: The `Steward` signing off `#423` must be strictly distinct from the `#421` `Tier-3 Operator` and from any `StudyAdmin`. All three redacted, PII-free receipts (`psr1_tier3_enrollment`, `psr1_cohort_summary`, `hosted_study_promotion`) are committed under `evidence/psr1-study/` so CI validates them continuously.

## Consequences
- External enrollment and Steward independence are auditable in git history.
- Exporter privacy bugs are fixed at the source rather than masked in one-off archives.
- Promotion gates cannot be closed until real human/operator and Steward artifacts are committed and pass `tools/check_psr1_readiness.py`.
