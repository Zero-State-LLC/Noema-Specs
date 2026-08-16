# RFC-0073 — GC2-S14 multi-cycle generator CONSTRUCT

## Status

**Accepted**

Specification-only until hosted. No `STRUCTURE_*`. No `event-catalog/0.3`. No project minigame. Help still omits BUILD. Other classes stay as they are: `relay` follows [RFC-0061](RFC-0061-multicycle-construct.md); `workshop` follows [RFC-0072](RFC-0072-workshop-cycle.md); storage_bay, production_node, route_link, defensive_work, and archive_annex stay instant.

## Problem

[CONSTRUCTION.md](../docs/CONSTRUCTION.md) allows multi-cycle projects. S9 and S13 closed that pin for `relay` and `workshop`. A public `generator` still goes live on CONSTRUCT. An implementer would either keep every remaining class instant forever or invent a build minigame.

## Proposed change

Accept GC2-S14. `BUILD.CONSTRUCT class=generator` in a **public** room creates a first-class `IN_PROGRESS` entity:

- Same `entity_id` for the whole life
- Occupies the room’s generator slot immediately. Not a live generator until promotion
- After **1** committed cycle, the same entity becomes live (`IN_PROGRESS` cleared)
- Hidden rooms still reject CONSTRUCT
- `DISMANTLE` of `IN_PROGRESS` salvages the catalog salvage and leaves **no** live generator and **no** scar
- Events: `ENTITY_CREATE` at start, `ENTITY_UPDATE` on promotion, `ENTITY_DESTROY` + `BUDGET_CONSUMED` on salvage. No `STRUCTURE_*`
- PLAY MAY say a generator is under construction. WATCH silent
- Chamber help still omits BUILD

Catalog: [`construction-catalog.gc2-s14.json`](../specs/construction-catalog.gc2-s14.json).  
Slice: [GC2-S14-GENERATOR-CYCLE.md](../docs/GC2-S14-GENERATOR-CYCLE.md).

## Alternatives rejected

| Alternative | Why |
|-------------|-----|
| All remaining classes multi-cycle | Out of slice |
| Duration other than 1 | Extra machinery |
| New room / project site | Hidden topology |
| `STRUCTURE_*` | Extra catalog |
| Help BUILD | S0 pin |
| Scar on in-progress salvage | Never live |

## Compatibility

Additive for `generator` only. Existing live generators stay live. Worlds ignoring S14 keep instant generator CONSTRUCT. S9 relay and S13 workshop pins are unchanged.

## Data / security

`in_progress` on the entity. Hidden rooms store none. WATCH silent.

## Validation

`check_gc2_s14`: public generator CONSTRUCT is `IN_PROGRESS`; after 1 committed cycle same `entity_id` is live; hidden reject; DISMANTLE of in-progress salvages with no live leftover; no new verbs.

## Rollback

Ignore `in_progress` on generators (treat every generator as live immediately).

## Unresolved

Remaining-class multi-cycle (`storage_bay`, `production_node`, `route_link`, `defensive_work`, `archive_annex`). Third-and-later co-owners.
