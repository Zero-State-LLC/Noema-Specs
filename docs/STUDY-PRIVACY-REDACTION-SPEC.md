# Hosted STUDY Privacy Redaction Spec & Promotion Receipt (`#362`)

Status: Operator-locked specification for `#362` (2026-11-24). `capabilities.hosted_study_pipeline` remains `BLOCKED` until all promotion criteria pass.

## Automated Privacy Redaction Validator Contract

Every natural-play evidence pack MUST pass an automated, deterministic redaction check (exit code `0` = pass, non-zero = blocking failure) before steward review.

### Forbidden Patterns (Blocking)

1. **Raw email addresses**: Any RFC-5322-like email string (`[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}`), excluding documented placeholder domains (`example.com`, `users.noreply.github.com`).
2. **Session / bearer / callback tokens**: Any `token_hash=`, `connect_code=`, `Authorization: Bearer `, `noema.play.token`, or signed JWT-shaped three-segment base64url string.
3. **Private inbox contents**: Any `private_inbox`, `inbox_messages`, or direct-message body fields not explicitly redacted.
4. **Internal entity IDs on public surfaces**: Any raw internal UUID/entity ID exposed in public WATCH or spectator transcript fields.

## Steward Promotion Receipt Template (JSON)

```json
{
  "receipt_type": "hosted_study_promotion",
  "recorded_at": "YYYY-MM-DDTHH:MM:SSZ",
  "worker_version_id": "<from GET /version>",
  "world_id": "<from GET /version>",
  "psr1_receipt_ref": "<path or commit SHA>",
  "evidence_pack_ref": "<path or archive SHA256>",
  "reconstruction_verified": true,
  "automated_redaction_exit_code": 0,
  "steward": "Zero-State operator",
  "steward_spot_check_passed": true,
  "verdict": "PROMOTE_HOSTED_STUDY | HOLD"
}
```
