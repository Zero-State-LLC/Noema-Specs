# RFC-0102 — ACCESS_POLICY S1 ROOM deny / clear

## Status

**Accepted**

No new events. No `event-catalog/0.3`. ACCESS_POLICY help stays omitted. ALLOW_ONLY stays later. WED / ATTEST stay omitted.

## Problem

[ACCESS-POLICY-S0.md](../docs/ACCESS-POLICY-S0.md) hosts EXIT DENY/CLEAR. The existing `ACCESS_RESTRICTED` payload and hosted MOVE already understand ROOM DENY (contest / schedule). An implementer would invent inbound locks, ALLOW_ONLY, or skip ROOM.

## Proposed change

Accept ACCESS_POLICY S1. Add **ROOM** scope to the same verb:

- `access here deny for <org>` / `access here clear for <org>` (`room` is an alias)
- Same occupied `GRANT_ACCESS` + treasury cost as S0
- ROOM DENY writes `access_restrictions` on the current public room
- MOVE from that room is rejected while live (existing `isAccessDenied`)
- CLEAR removes a matching ROOM restriction
- EXIT DENY/CLEAR unchanged
- Help still omits ACCESS_POLICY / WED / ATTEST

Catalog: [`access-policy-catalog.s1.json`](../specs/access-policy-catalog.s1.json).  
Slice: [ACCESS-POLICY-S1.md](../docs/ACCESS-POLICY-S1.md).

## Alternatives rejected

| Alternative | Why |
|-------------|-----|
| ALLOW_ONLY | Separate pin; MOVE only checks DENY |
| Inbound lock | Contest ROOM DENY is outbound only |
| Help ACCESS_POLICY | Separate pin |
| New events | Catalog closed |

## Compatibility

Additive ROOM host. Worlds ignoring S1 keep EXIT-only ACCESS_POLICY.

## Data / security

Public rooms only. No hidden-room locks. WATCH uses existing restriction projections.

## Validation

`check_access_policy_s1`: ROOM DENY/CLEAR accepted with grant; EXIT still accepted; ALLOW_ONLY rejected; help still omits ACCESS_POLICY.

## Rollback

Reject `access here` again. Keep S0 EXIT.

## Unresolved

ALLOW_ONLY. ACCESS_POLICY help. WED / ATTEST help. YOUR POSITION.
