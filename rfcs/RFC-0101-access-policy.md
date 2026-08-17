# RFC-0101 — ACCESS_POLICY S0 GRANT_ACCESS exit deny / clear

## Status

**Accepted**

Specification-only until hosted. No new events. No `event-catalog/0.3`. ACCESS_POLICY help stays omitted. WED / ATTEST stay omitted. ALLOW_ONLY and ROOM stay later.

## Problem

[ACTION-CONTRACTS.md](../docs/ACTION-CONTRACTS.md) and [PLAYER-ACTION-MAP.md](../docs/PLAYER-ACTION-MAP.md) already name `COMMIT.ACCESS_POLICY` → `ACCESS_RESTRICTED`. Hosted Chamber returns `NOT_IMPLEMENTED` for `access`. `GRANT_ACCESS` is catalogued as “later access-list mutate” ([GC4-S1-OFFICES.md](../docs/GC4-S1-OFFICES.md)). An implementer would invent a lock anyone can set, add a new event, or advertise help.

## Proposed change

Accept ACCESS_POLICY S0. Host **EXIT DENY and CLEAR** only:

- `access <dir> deny for <org>` / `access <dir> clear for <org>` / structured `COMMIT.ACCESS_POLICY`
- Actor entered, public room, exit exists here
- Occupied `GRANT_ACCESS` office on `acting_for`
- DENY writes the existing `access_restrictions` row (`applies_to` `*` or a named player; default `expires_cycle = cycle+4`)
- CLEAR removes a matching live restriction
- Both emit existing `ACCESS_RESTRICTED`
- Cost: compute 1, influence 2 from the institution treasury
- Hidden rooms `NOT_OBSERVABLE`
- No office / no `acting_for` → `FORBIDDEN`
- Help unchanged (still no ACCESS_POLICY / WED / ATTEST)

Catalog: [`access-policy-catalog.s0.json`](../specs/access-policy-catalog.s0.json).  
Slice: [ACCESS-POLICY-S0.md](../docs/ACCESS-POLICY-S0.md).

## Alternatives rejected

| Alternative | Why |
|-------------|-----|
| Anyone may lock | Control is emergent; office is the grant |
| New events | Catalog closed |
| ALLOW_ONLY | MOVE only checks DENY |
| ROOM scope | Later |
| Help ACCESS_POLICY | Separate pin (WR-S3) |
| Personal acting | GC4-S2 pattern: `acting_for` required |

## Compatibility

Additive verb host. Worlds ignoring S0 keep `access` unimplemented. Scheduled and contest restrictions stay.

## Data / security

Public-room EXIT only. No hidden-room locks. WATCH uses existing restriction projections. No ticker.

## Validation

`check_access_policy_s0`: DENY/CLEAR accepted with grant; no grant rejected; ALLOW_ONLY rejected; help still omits ACCESS_POLICY.

## Rollback

Return `NOT_IMPLEMENTED` for `access` again.

## Unresolved

ALLOW_ONLY. ROOM scope. ACCESS_POLICY help. WED / ATTEST help. YOUR POSITION.
