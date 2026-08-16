# RFC-0076 — GC2-S17 multi-cycle defensive_work CONSTRUCT

## Status

**Accepted**

Specification-only until hosted. No `STRUCTURE_*`. No `event-catalog/0.3`. No project minigame. Help still omits BUILD. Other classes stay as they are: `relay` follows [RFC-0061](RFC-0061-multicycle-construct.md); `workshop` follows [RFC-0072](RFC-0072-workshop-cycle.md); `generator` follows [RFC-0073](RFC-0073-generator-cycle.md); `storage_bay` follows [RFC-0074](RFC-0074-storage-bay-cycle.md); `production_node` follows [RFC-0075](RFC-0075-production-node-cycle.md); route_link and archive_annex stay instant. [RFC-0052](RFC-0052-defensive-work.md) millipoint amount and contest arithmetic stay closed.

## Problem

[CONSTRUCTION.md](../docs/CONSTRUCTION.md) allows multi-cycle projects. S9–S16 closed that pin for `relay`, `workshop`, `generator`, `storage_bay`, and `production_node`. A public `defensive_work` still goes live on CONSTRUCT, so a shell would add the S3 +50 contest-defense millipoints. An implementer would either keep remaining classes instant forever or invent a build minigame.

## Proposed change

Accept GC2-S17. `BUILD.CONSTRUCT class=defensive_work` in a **public** room creates a first-class `IN_PROGRESS` entity:

- Same `entity_id` for the whole life
- Occupies the room’s defensive_work slot immediately. Not a live work until promotion
- After **1** committed cycle, the same entity becomes live (`IN_PROGRESS` cleared)
- Hidden rooms still reject CONSTRUCT
- `DISMANTLE` of `IN_PROGRESS` salvages the catalog salvage and leaves **no** live work and **no** scar
- Contest scoring applies the S3 +50 defense millipoints **only** when a live (not `IN_PROGRESS`) `defensive_work` is in the room. Slot occupancy still counts the shell
- Events: `ENTITY_CREATE` at start, `ENTITY_UPDATE` on promotion, `ENTITY_DESTROY` + `BUDGET_CONSUMED` on salvage. No `STRUCTURE_*`
- PLAY MAY say a defensive work is under construction. WATCH silent
- Chamber help still omits BUILD

Catalog: [`construction-catalog.gc2-s17.json`](../specs/construction-catalog.gc2-s17.json).  
Slice: [GC2-S17-DEFENSIVE-WORK-CYCLE.md](../docs/GC2-S17-DEFENSIVE-WORK-CYCLE.md).

## Alternatives rejected

| Alternative | Why |
|-------------|-----|
| All remaining classes multi-cycle | Out of slice |
| Duration other than 1 | Extra machinery |
| New room / project site | Hidden topology |
| `STRUCTURE_*` | Extra catalog |
| Help BUILD | S0 pin |
| Scar on in-progress salvage | Never live |
| Filter `in_progress` from slot occupancy | Would allow a second work in the same room |
| Change S3 millipoint amount | Closed arithmetic |

## Compatibility

Additive for `defensive_work` only. Existing live works stay live and keep the S3 bonus. Worlds ignoring S17 keep instant defensive_work CONSTRUCT. S3 millipoints and S9–S16 pins are unchanged.

## Data / security

`in_progress` on the entity. Hidden rooms store none. WATCH silent.

## Validation

`check_gc2_s17`: public defensive_work CONSTRUCT is `IN_PROGRESS`; after 1 committed cycle same `entity_id` is live; hidden reject; DISMANTLE of in-progress salvages with no live leftover; contest bonus only when live; no new verbs.

## Rollback

Ignore `in_progress` on defensive works (treat every work as live immediately, including contest bonus).

## Unresolved

Archive-annex multi-cycle is [RFC-0077](RFC-0077-archive-annex-cycle.md). Remaining-class multi-cycle (`route_link`). Third-and-later co-owners.
