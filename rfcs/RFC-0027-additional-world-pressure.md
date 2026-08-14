# RFC-0027 — GC10-S1 Additional World Pressure Classes

## Status

**Accepted**

Closes the GC10-S1 SPEC GAP. Additional pressure classes perturb existing causal systems through existing events. GC10-S0 `infrastructure_failure` remains valid. No quest director. No rubber-band. No `event-catalog/0.3`.

## Problem

[GC10-FIRST-SLICE.md](../docs/GC10-FIRST-SLICE.md) left later product classes as SPEC GAP. An implementer would add `WED_*` / `PRESSURE_*` events, a weather or famine engine, or target Players by score.

## Proposed change

Accept GC10-S1:

```text
WORLD PRESSURE ≠ QUEST ≠ TARGETED PLAYER PUNISHMENT ≠ DIFFICULTY SCALING ≠ BALANCE RUBBER-BAND ≠ OPERATOR RAW EDIT
```

- Keep S0 `infrastructure_failure` (cycle 4, `ENTITY_UPDATE` condition −15, floor 25).
- Add `resource_scarcity` (cycle 8, `ENTITY_UPDATE` `stock_amount` −4, floor 0).
- Add `access_restriction` (cycle 12, existing `ACCESS_RESTRICTED` on a public exit, 4-cycle expiry).
- Reject standalone communication, route, and environmental engines.
- Authorizers remain `schedule` and `operator`. Player / LLM / STUDY cannot inject.
- Preview of the same inputs equals activation. At most one fire per accepted class in cycles 1–20.
- PLAY / WATCH show world-native consequences. Research class names stay off those surfaces.

Catalog: [`pressure-catalog.gc10-s1.json`](../specs/pressure-catalog.gc10-s1.json).  
Slice: [GC10-S1-PRESSURE.md](../docs/GC10-S1-PRESSURE.md).

## Alternatives rejected

| Alternative | Why |
|-------------|-----|
| `PRESSURE_STARTED` / `PRESSURE_ENDED` | Lifecycle is schedule + existing events |
| Communication outage engine | S0 relay condition already drives GC5 bands |
| Route engine distinct from access | `ACCESS_RESTRICTED` is the route primitive |
| Weather / famine / plague / war engines | Genre labels, not causes; fail the subsystem test |
| Player-score or research targeting | Hidden evaluation of Player quality |
| Rubber-band difficulty | GC10 is not a balance cheat layer |
| Admin spawn / raw `UPDATE entity` | Control plane is not world-edit |

## Compatibility

Additive. GC10-S0 catalog, fixtures, and cycle-4 relay drop stay authoritative for that class. Frozen `event-types.0.2.json` unchanged (`ACCESS_RESTRICTED` already exists).

## Data / security

No new table. No new service. Clients cannot inject WED. Cross-world subject refs are rejected. Duplicate class fire in the 1–20 window is a no-op. Stale-head settlement fails safely. Research overlays cannot mutate pressure.

## Validation

`check_gc10_s1`: accepted classes reuse existing events; targeting / rubber-band / unsupported class / below-floor / duplicate / leak fixtures rejected.

## Rollback

Omit S1 class schedules. S0 cycle-4 relay drop remains.

## Unresolved

Operator confirm UI (still no spawn). Irreversible scar class. First-20 band 13–16 as a further class. Communication remains composed, not a second model.
