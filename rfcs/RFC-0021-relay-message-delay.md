# RFC-0021 — GC5-S1 Deterministic MESSAGE Delay

## Status

**Accepted**

Closes the GC5-S0 delay SPEC GAP. No new verbs. No `event-catalog/0.3`. No rumor schema. No Genesis reseed.

## Problem

[GC5-FIRST-SLICE.md](../docs/GC5-FIRST-SLICE.md) left multi-cycle delay as SPEC GAP. Scenario E needs a degraded path that delivers later, then a repair that restores a faster class. An implementer would add `RUMOR`, RNG delay, or `MESSAGE_FAILED`.

## Proposed change

Accept GC5-S1:

- Keep S0 fail floor: long-range `< 25` or no live relay → `UNREACHABLE`
- Split the reachable band: `≥ 50` same-cycle; `25`–`49` delay **1** cycle
- Delay is world-time (RFC-0019), not wall clock
- Send still emits `MESSAGE`; `MESSAGE_DELIVERED` waits until `deliver_at_cycle`
- Local same-room delivery unchanged
- Rumor surfaces stay out (GC5-S2)

Catalog: [`communication-catalog.gc5-s1.json`](../specs/communication-catalog.gc5-s1.json).  
Slice: [GC5-S1-DELAY.md](../docs/GC5-S1-DELAY.md).

## Alternatives rejected

| Alternative | Why |
|-------------|-----|
| Delay below 25 | Would replace `UNREACHABLE` and erase the S0 fail class |
| Random hops | Doctrine: no RNG theater |
| `RUMOR` verb / rumor records | Separate surface; later slice |
| `MESSAGE_FAILED` | Catalog expansion; delayed send is not a failure |
| Cron delivers mail | Tick is not world time |

## Compatibility

Additive overlay on S0. Frozen `action-contracts.v01.json` unchanged. Existing S0 fixtures for `< 25` and no-relay remain `UNREACHABLE`. S0 “same-cycle at 25” is **superseded** for long-range: 25 is now delayed.

## Data / security

No new entity class. Pending inbox is not WATCH. Reasons/consequences must not leak relay ids or hidden rooms.

## Validation

`check_gc5_s1`: same-cycle at 50; delay at 25; `UNREACHABLE` at 24; rumor/new verbs rejected; delay cycles = 1.

## Rollback

Omit the S1 catalog. Hosted S0 band (same-cycle at ≥ 25) remains.

## Unresolved

GC5-S2 rumor provenance. Multi-hop delay. Org/board surfaces.
