# RFC-0075 — GC2-S16 multi-cycle production_node CONSTRUCT

## Status

**Accepted**

No `STRUCTURE_*`. No `event-catalog/0.3`. No project minigame. Help still omits BUILD. Other classes stay as they are: `relay` follows [RFC-0061](RFC-0061-multicycle-construct.md); `workshop` follows [RFC-0072](RFC-0072-workshop-cycle.md); `generator` follows [RFC-0073](RFC-0073-generator-cycle.md); `storage_bay` follows [RFC-0074](RFC-0074-storage-bay-cycle.md); route_link, defensive_work, and archive_annex stay instant.

## Problem

[CONSTRUCTION.md](../docs/CONSTRUCTION.md) allows multi-cycle projects. S9–S15 closed that pin for `relay`, `workshop`, `generator`, and `storage_bay`. A public `production_node` still goes live on CONSTRUCT. An implementer would either keep every remaining class instant forever or invent a build minigame.

## Proposed change

Accept GC2-S16. `BUILD.CONSTRUCT class=production_node` in a **public** room creates a first-class `IN_PROGRESS` entity:

- Same `entity_id` for the whole life
- Occupies the room’s production_node slot immediately. Not a live node until promotion
- After **1** committed cycle, the same entity becomes live (`IN_PROGRESS` cleared)
- Hidden rooms still reject CONSTRUCT
- `DISMANTLE` of `IN_PROGRESS` salvages the catalog salvage and leaves **no** live node and **no** scar
- Events: `ENTITY_CREATE` at start, `ENTITY_UPDATE` on promotion, `ENTITY_DESTROY` + `BUDGET_CONSUMED` on salvage. No `STRUCTURE_*`
- PLAY MAY say a production node is under construction. WATCH silent
- Chamber help still omits BUILD

Catalog: [`construction-catalog.gc2-s16.json`](../specs/construction-catalog.gc2-s16.json).  
Slice: [GC2-S16-PRODUCTION-NODE-CYCLE.md](../docs/GC2-S16-PRODUCTION-NODE-CYCLE.md).

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

Additive for `production_node` only. Existing live nodes stay live. Worlds ignoring S16 keep instant production_node CONSTRUCT. S9–S15 pins are unchanged.

## Data / security

`in_progress` on the entity. Hidden rooms store none. WATCH silent.

## Validation

`check_gc2_s16`: public production_node CONSTRUCT is `IN_PROGRESS`; after 1 committed cycle same `entity_id` is live; hidden reject; DISMANTLE of in-progress salvages with no live leftover; no new verbs.

## Rollback

Ignore `in_progress` on production nodes (treat every node as live immediately).

## Unresolved

Defensive-work multi-cycle is [RFC-0076](RFC-0076-defensive-work-cycle.md). Remaining-class multi-cycle (`route_link`, `archive_annex`). Third-and-later co-owners.
