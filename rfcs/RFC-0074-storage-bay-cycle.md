# RFC-0074 — GC2-S15 multi-cycle storage_bay CONSTRUCT

## Status

**Accepted**

Specification-only until hosted. No `STRUCTURE_*`. No `event-catalog/0.3`. No project minigame. Help still omits BUILD. Other classes stay as they are: `relay` follows [RFC-0061](RFC-0061-multicycle-construct.md); `workshop` follows [RFC-0072](RFC-0072-workshop-cycle.md); `generator` follows [RFC-0073](RFC-0073-generator-cycle.md); production_node, route_link, defensive_work, and archive_annex stay instant. [RFC-0057](RFC-0057-workshop-repurpose.md) REPURPOSE still yields a live `storage_bay`.

## Problem

[CONSTRUCTION.md](../docs/CONSTRUCTION.md) allows multi-cycle projects. S9–S14 closed that pin for `relay`, `workshop`, and `generator`. A public `storage_bay` still goes live on CONSTRUCT. An implementer would either keep every remaining class instant forever or invent a build minigame.

## Proposed change

Accept GC2-S15. `BUILD.CONSTRUCT class=storage_bay` in a **public** room creates a first-class `IN_PROGRESS` entity:

- Same `entity_id` for the whole life
- Occupies the room’s storage_bay slot immediately. Not a live bay until promotion
- After **1** committed cycle, the same entity becomes live (`IN_PROGRESS` cleared)
- Hidden rooms still reject CONSTRUCT
- `DISMANTLE` of `IN_PROGRESS` salvages the catalog salvage and leaves **no** live bay and **no** scar
- `REPURPOSE` of a live workshop still produces a live `storage_bay` (not a shell)
- Events: `ENTITY_CREATE` at start, `ENTITY_UPDATE` on promotion, `ENTITY_DESTROY` + `BUDGET_CONSUMED` on salvage. No `STRUCTURE_*`
- PLAY MAY say a storage bay is under construction. WATCH silent
- Chamber help still omits BUILD

Catalog: [`construction-catalog.gc2-s15.json`](../specs/construction-catalog.gc2-s15.json).  
Slice: [GC2-S15-STORAGE-BAY-CYCLE.md](../docs/GC2-S15-STORAGE-BAY-CYCLE.md).

## Alternatives rejected

| Alternative | Why |
|-------------|-----|
| All remaining classes multi-cycle | Out of slice |
| Duration other than 1 | Extra machinery |
| New room / project site | Hidden topology |
| `STRUCTURE_*` | Extra catalog |
| Help BUILD | S0 pin |
| Scar on in-progress salvage | Never live |
| REPURPOSE yields IN_PROGRESS | S6 already closed a live conversion |

## Compatibility

Additive for `CONSTRUCT class=storage_bay` only. Existing live bays stay live. Worlds ignoring S15 keep instant storage_bay CONSTRUCT. S6 REPURPOSE, S9 relay, S13 workshop, and S14 generator pins are unchanged.

## Data / security

`in_progress` on the entity. Hidden rooms store none. WATCH silent.

## Validation

`check_gc2_s15`: public storage_bay CONSTRUCT is `IN_PROGRESS`; after 1 committed cycle same `entity_id` is live; hidden reject; DISMANTLE of in-progress salvages with no live leftover; no new verbs.

## Rollback

Ignore `in_progress` on storage bays (treat every CONSTRUCT bay as live immediately).

## Unresolved

Remaining-class multi-cycle (`production_node`, `route_link`, `defensive_work`, `archive_annex`). Third-and-later co-owners.
