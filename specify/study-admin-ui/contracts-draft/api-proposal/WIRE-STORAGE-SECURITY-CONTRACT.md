# Study Admin UI: Wire, Storage, Audit & Security Contract (Draft)

Status: Draft (qualification artifact for `#396` / `RFC-0131`; confers no runtime-ready or deployment authority).

## Wire Endpoints (v1 — Single `study-admin` Role)

All endpoints require a fresh Admin-authentication event derivative (no extra global Admin grant) and same-origin CSRF protection.

- `POST /api/admin/studies/{study_id}/invites`
  - Request: `{ "human_principal_id": string, "ttl_days"?: number (1..14, default 7) }`
  - `201 Created`: New pending invite created (supersedes any prior pending invite for `(study_id, human_principal_id)`).
  - `200 OK` (`ALREADY_ACTIVE`): Target `HumanPrincipal` already holds an active `study-admin` grant (idempotent, no duplicate).
- `POST /api/study-admin/invites/{invite_id}/accept`
  - Authenticated as the target `HumanPrincipal`. Single-use.
  - Errors: `410 INVITE_EXPIRED`, `410 INVITE_REVOKED`, `403 FORBIDDEN` (principal mismatch).
- `POST /api/admin/studies/{study_id}/invites/{invite_id}/revoke`
  - Immediately revokes a pending invite.
- `POST /api/admin/studies/{study_id}/grants/{human_principal_id}/revoke`
  - Immediately revokes an active `study-admin` grant.

## Durable Storage & Immutable Audit Events

- **`study_admin_invites`**: `(invite_id PK, study_id, human_principal_id, status [pending|accepted|revoked|superseded|expired], issued_by_auth_event_id, created_at, expires_at, resolved_at)`
- **`study_admin_grants`**: `(study_id, human_principal_id, role='study-admin', status [active|revoked], granted_at, revoked_at, PRIMARY KEY (study_id, human_principal_id))`
- **`study_admin_audit_log`** (append-only): `(event_id PK, event_type [invite_issued|invite_superseded|invite_accepted|invite_revoked|grant_revoked], actor_id, study_id, target_human_principal_id, auth_event_id, occurred_at)`

## Security & Rollback Disposition

- **Auth**: Requires a fresh Admin-authentication event derivative; contact-only targets remain unavailable.
- **Origin / CSRF**: Rejects cross-origin state-changing requests; tokens never appear in URL query strings or analytics.
- **Rollback**: Disabling the feature flag halts new invites/accepts while preserving `study_admin_audit_log` intact; active grants can be bulk-revoked without touching global Admin privileges.
