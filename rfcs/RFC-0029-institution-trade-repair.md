# RFC-0029 — Institutional TRADE and REPAIR Authority

## Status

**Accepted**

Closes the GC4 follow-through SPEC GAP for institution-side TRADE and REPAIR. Institutions act only through a Player holding an occupied office whose profile grants the capability. No new top-level verbs. No finance or employment engine. No `event-catalog/0.3`.

## Problem

[GC4-S1-OFFICES.md](../docs/GC4-S1-OFFICES.md) recorded `OPERATE_RESOURCE_ACCOUNT` and `OPERATE_NAMED_ASSET` but hosted only `PUBLISH_NOTICE`. An implementer would add `INSTITUTION_TRADE` / `TREASURER_POWER` or spend officer personal lots as if they were the treasury.

## Proposed change

Accept institutional TRADE/REPAIR:

```text
INSTITUTION ≠ PLAYER ≠ CONTROLLER ≠ AUTONOMOUS NPC
```

```text
Player + occupied office + matching profile + explicit acting_for
→ ordinary TRADE or REPAIR
→ institution treasury / institution-scoped asset
```

- No `INSTITUTION_TRADE` / `INSTITUTION_REPAIR` verbs.
- Treasury is institution-owned `Budgets`. Vacating the office ends authority; balances stay.
- Compute fee stays on the acting Player. Offered lots and repair costs come from the selected institution treasury when `acting_for` is set.
- Profiles stay generic: `OPERATE_RESOURCE_ACCOUNT` (TRADE), `OPERATE_NAMED_ASSET` (REPAIR). Display names are not power.

Catalog: [`authority-catalog.gc4-s2.json`](../specs/authority-catalog.gc4-s2.json).  
Slice: [GC4-S2-INSTITUTION-ACTIONS.md](../docs/GC4-S2-INSTITUTION-ACTIONS.md).

## Alternatives rejected

| Alternative | Why |
|-------------|-----|
| New verbs / event family | Verb inflation; frozen catalogs |
| Founder role implies treasury | Office is the grant |
| Silent pick among several offices | Ambiguous provenance |
| Auto-fund vacant office | No institution autopilot |
| Repair cost from whichever account has funds | Must name the source |

## Compatibility

Additive. Personal TRADE/REPAIR unchanged when `acting_for` is omitted. GC4-S0/S1 membership and offices unchanged. Frozen catalogs unchanged.

## Data / security

Treasury lives on the organization record (world head). Not a new table. Cross-world org ids are `NOT_FOUND`. Forged `acting_for` does not spend another institution’s lots.

## Validation

`check_gc4_s2`: authorized trade/repair; vacancy/revocation; member/advisor forbidden; conservation; no new verbs.

## Rollback

Ignore `acting_for`. Personal TRADE/REPAIR and `PUBLISH_NOTICE` remain.

## Unresolved

Emergency scopes. Designated succession. Institution-to-institution conflict-of-interest when one Player holds both sides. Delegation.
