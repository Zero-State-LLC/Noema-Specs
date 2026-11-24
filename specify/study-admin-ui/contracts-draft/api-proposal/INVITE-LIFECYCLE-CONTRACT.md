# Study Admin UI: Invite Lifecycle & Revocation Contract (Draft)

Status: Draft (operator-selected policy for `#396` / `RFC-0131`; confers no runtime-ready or deployment authority).

## Role Scope (v1)

- **Single role**: `study-admin` only for v1. Additional role granularity (e.g. read-only vs. study-steward) is deferred.
- **Issuer & target**: Follows `ISSUER-TARGET-CONTRACT.md` (fresh Admin-authentication event derivative, no extra global Admin grant, existing stable `HumanPrincipal` targets only, contact-only targets deferred).

## Invite Lifecycle

- **TTL**: 7 days default, configurable up to a 14-day maximum.
- **Consumption**: Single-use upon acceptance by the target `HumanPrincipal`. Expired or revoked invites MUST be rejected.

## Revocation

- **Scope**: An Admin can immediately revoke both pending invites and active `study-admin` grants.
- **Audit**: Every invite issuance, acceptance, and revocation (pending or active) MUST emit an immutable audit event recording actor, target `HumanPrincipal`, `study_id`, and timestamp.

## Re-Invite Semantics

- **Already-active `study-admin`**: Idempotent; returns the existing active grant without creating a duplicate grant or invite.
- **Pending invite exists**: Supersedes any prior pending invite for the same `(study_id, human_principal_id)` and invalidates the superseded invite token.
