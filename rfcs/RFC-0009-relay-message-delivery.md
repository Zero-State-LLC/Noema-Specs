# RFC-0009 — GC5-S0 Relay Bands on Existing MESSAGE

## Status

**Accepted**

Specification-only. No new verbs. No `event-catalog` expansion. No rumor schema. No runtime implementation in this RFC.

## Problem

[COMMUNICATION-ECOLOGY.md](../docs/COMMUNICATION-ECOLOGY.md) requires relay condition to change long-range delivery, but left the band table and local/long-range cut as SPEC GAP. An implementation agent would add `SHOUT`/`RUMOR` verbs, a `MESSAGE_FAILED` type, or a random delay.

## Proposed change

Accept GC5-S0:

- `MESSAGE` remains the only verb
- Same room = local; always same-cycle when otherwise addressable
- Different room = long-range; requires a live `relay` whose best condition is ≥ 25
- 25 is the existing stressed-relay number from `MESSAGE` cost, not a new threshold
- Path metric = maximum condition among live relays; none live → `UNREACHABLE`
- Fail closed with typed `UNREACHABLE`; no events; no topology leak
- `DELAYED` and rumor surfaces stay out

Catalog: [`communication-catalog.gc5-s0.json`](../specs/communication-catalog.gc5-s0.json).  
Slice: [GC5-FIRST-SLICE.md](../docs/GC5-FIRST-SLICE.md).

## Alternatives rejected

| Alternative | Why |
|-------------|-----|
| New communication verbs | Parent + doctrine: verb inflation |
| `MESSAGE_FAILED` | Silent catalog expansion |
| Multi-cycle delay in S0 | Delay function is still SPEC GAP |
| Must be co-located with the relay | Post-office industry |
| Invented region map | Rooms already express distance for this cut |

## Compatibility

Overlay on existing `MESSAGE`. v0.1 same-cycle delivery remains the local path and the healthy long-range path. Frozen `action-contracts.v01.json` is not rewritten in this RFC.

## Data / security

No new entity class. Failure reasons must not include relay ids, hidden rooms, or DM text. WATCH stays textless.

## Validation

`check_gc5_s0`: local succeeds on a dead relay; long-range succeeds at 25; long-range `UNREACHABLE` at 24 and when no relay is live; reasons contain no leak tokens.

## Rollback

Omit the catalog. Hosted same-cycle `MESSAGE` remains.

## Unresolved

GC5-S1: deterministic delay for degraded (not failed) paths; rumor provenance; other `MESSAGE` surfaces.
