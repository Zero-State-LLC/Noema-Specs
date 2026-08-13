# RFC-0006 — GC2-S0 Construction via Existing Events

## Status

**Accepted**

Specification-only. Does **not** expand `event-catalog`. Does **not** thaw first-world `BUILD` help. Runtime implementation remains a separate authorized pass.

## Problem

[CONSTRUCTION.md](../docs/CONSTRUCTION.md) closed the generalized `BUILD` deferral in prose but left costs, crowding, and events as SPEC GAP. An implementation agent would invent an event catalog or a crafting tree.

## Context

- [GC2-FIRST-SLICE.md](../docs/GC2-FIRST-SLICE.md)
- [COMPLEXITY-DOCTRINE.md](../docs/COMPLEXITY-DOCTRINE.md)
- Existing `ENTITY_CREATE` / `ENTITY_DESTROY` / `ENTITY_UPDATE` / `BUDGET_CONSUMED` in `event-catalog/0.1`
- Frozen `COMMIT.REPAIR`

## Proposed change

Accept GC2-S0:

- One later verb `BUILD` with `CONSTRUCT` and `DISMANTLE` only
- Closed classes: the four v0.1 infrastructure types
- Success events are existing catalog types only
- Pinned costs and one-per-class-per-room crowding
- Owner = steward = constructing Player

Exact tables live in the slice doc and [`construction-catalog.gc2-s0.json`](../specs/construction-catalog.gc2-s0.json).

## Alternatives

| Alternative | Why rejected |
|-------------|--------------|
| `STRUCTURE_*` event-catalog/0.3 | Violates doctrine primitive reuse; silent catalog expansion |
| New classes in S0 | Extra nouns without proving the four existing types first |
| Crafting / workshop minigame | Isolated progression tree |
| Mastery build discount | Abstract buff |

## Compatibility

Additive. v0.1 worlds ignore `BUILD`. Repair unchanged.

## Data impact

New infrastructure entities via existing create/destroy. No wallet, token, or external title fields.

## Research / security

No research scores. Hidden rooms stay unadvertised.

## Migration

Worlds with genesis infrastructure keep those assets. S0 CONSTRUCT refuses a class already live in the room.

## Validation

`check_gc2_s0` validates the catalog and attempt fixtures (accept construct, reject occupied slot, reject non-owner dismantle, reject hidden room).

## Rollback

Leave unused. `BUILD` stays UNSUPPORTED.

## Unresolved

1. When to add `route_link` (distance primitive) as a class
2. Institution ownership
3. Whether `ENTITY_DESTROY` vs ruined `ENTITY_UPDATE` is better for Deep Time scars
