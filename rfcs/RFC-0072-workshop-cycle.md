# RFC-0072 — GC2-S13 multi-cycle workshop CONSTRUCT

## Status

**Accepted**

Specification-only until hosted. No `STRUCTURE_*`. No `event-catalog/0.3`. No project minigame. Help still omits BUILD. Other classes stay as they are: `relay` already follows [RFC-0061](RFC-0061-multicycle-construct.md); generator, storage_bay, production_node, route_link, defensive_work, and archive_annex stay instant.

## Problem

[CONSTRUCTION.md](../docs/CONSTRUCTION.md) allows multi-cycle projects. GC2-S9 closed that pin for `relay` only. A public `workshop` still goes live on CONSTRUCT. An implementer would either keep every other class instant forever or invent a build minigame.

## Proposed change

Accept GC2-S13. `BUILD.CONSTRUCT class=workshop` in a **public** room creates a first-class `IN_PROGRESS` entity:

- Same `entity_id` for the whole life
- Occupies the room’s workshop slot immediately. Not a live bench (no storage discount) until promotion
- After **1** committed cycle, the same entity becomes live (`IN_PROGRESS` cleared)
- Hidden rooms still reject CONSTRUCT
- `DISMANTLE` of `IN_PROGRESS` salvages the catalog salvage and leaves **no** live workshop and **no** scar
- `UPGRADE` and `REPURPOSE` of `IN_PROGRESS` fail `FORBIDDEN`
- Events: `ENTITY_CREATE` at start, `ENTITY_UPDATE` on promotion, `ENTITY_DESTROY` + `BUDGET_CONSUMED` on salvage. No `STRUCTURE_*`
- PLAY MAY say a workshop is under construction. WATCH silent
- Chamber help still omits BUILD

Catalog: [`construction-catalog.gc2-s13.json`](../specs/construction-catalog.gc2-s13.json).  
Slice: [GC2-S13-WORKSHOP-CYCLE.md](../docs/GC2-S13-WORKSHOP-CYCLE.md).

## Alternatives rejected

| Alternative | Why |
|-------------|-----|
| All remaining classes multi-cycle | Out of slice |
| Duration other than 1 | Extra machinery |
| New room / project site | Hidden topology |
| `STRUCTURE_*` | Extra catalog |
| Help BUILD | S0 pin |
| Scar on in-progress salvage | Never live |
| UPGRADE / REPURPOSE while in progress | Never live |

## Compatibility

Additive for `workshop` only. Existing live workshops stay live. Worlds ignoring S13 keep instant workshop CONSTRUCT. S9 relay pin is unchanged.

## Data / security

`in_progress` on the entity. Hidden rooms store none. WATCH silent.

## Validation

`check_gc2_s13`: public workshop CONSTRUCT is `IN_PROGRESS`; after 1 committed cycle same `entity_id` is live; hidden reject; DISMANTLE of in-progress salvages with no live leftover; UPGRADE/REPURPOSE of in-progress reject; no new verbs.

## Rollback

Ignore `in_progress` on workshops (treat every workshop as live immediately).

## Unresolved

Generator multi-cycle is [RFC-0073](RFC-0073-generator-cycle.md). Remaining-class multi-cycle. Third-and-later co-owners.
