# RFC-0050 — GC2-S2 workshop

## Status

**Accepted**

Specification-only until hosted. No new verbs. No `event-catalog/0.3`. No crafting tree. No mastery discount.

## Problem

[CONSTRUCTION.md](../docs/CONSTRUCTION.md) allows a `workshop` that couples construction and repair without becoming a recipe minigame. GC2-S0/S1 can build relays and route links, but every CONSTRUCT/REPAIR pays full storage even beside a bench.

## Proposed change

Accept GC2-S2. Add constructible class `workshop` on existing `BUILD.CONSTRUCT` / `DISMANTLE`:

- Costs: energy 6, compute 3, storage 5, influence 0; salvage 2
- One live `workshop` per public room. Hidden rooms stay unbuildable
- Effect: while a live `workshop` is in the room, **CONSTRUCT** and **REPAIR** pay **−1 storage** (floor 0). Energy and compute unchanged
- Building the first workshop in an empty room pays full catalog cost
- No recipes. No yield bonus. No mastery cheaper-build
- PLAY MAY say a workshop is open. WATCH silent
- Chamber help still omits BUILD

Catalog: [`construction-catalog.gc2-s2.json`](../specs/construction-catalog.gc2-s2.json).  
Slice: [GC2-S2-WORKSHOP.md](../docs/GC2-S2-WORKSHOP.md).

## Alternatives rejected

| Alternative | Why |
|-------------|-----|
| Crafting recipes | Minigame |
| Mastery construct discount | GC1 class discounts rejected |
| Require workshop to CONSTRUCT | Soft-locks S0 |
| WATCH workshop ticker | Spectator leak |
| Help BUILD | S0 pin |

## Compatibility

Additive class. Worlds ignoring S2 keep S1 classes and full storage costs.

## Data / security

Existing `ENTITY_CREATE` / `ENTITY_DESTROY` / `BUDGET_CONSUMED`. Hidden rooms unbuildable.

## Validation

`check_gc2_s2`: class present; CONSTRUCT/REPAIR storage −1 with workshop; hidden reject; no recipes; no new verbs.

## Rollback

Ignore `workshop` (`CLASS_FORBIDDEN`). Costs stay S1.

## Unresolved

`defensive_work`, `archive_annex`, UPGRADE/CONNECT, scars.
