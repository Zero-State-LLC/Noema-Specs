# 2026-11-24: Locked Spec Decisions (#383, #363, #362, #396)

- **#383**: Standardized tier-3 enrollment on device-code `/connect` approval with `noema-client==0.1.24` baseline and 1 live receipt (`docs/PSR1-TIER3-ENROLLMENT-RUNBOOK.md`).
- **#363**: Locked third-party compatibility bar to PSR-1/PSR-2 cohort (`>=6` Controllers, `>=2` non-first-party across 2 distinct styles: `framework-adapter` + `custom-http-ws`, `>=1` tier-3 operator, `Δcycle >= 24`, `>=20` actions/Player, `>=60` total, 0 regressions).
- **#362**: Hosted STUDY remains `BLOCKED` until PSR-1 passes + natural-play pack passes automated privacy redaction (`exit 0`) + steward spot-check sign-off (`docs/STUDY-PRIVACY-REDACTION-SPEC.md`).
- **#396 (`RFC-0131`)**: Single `study-admin` role for v1; 7d default / 14d max single-use invites; immediate revocation for pending + active grants with append-only audit log; idempotent active re-invite and superseding pending re-invite.
