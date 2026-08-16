# RFC-0077 — GC2-S18 multi-cycle archive_annex CONSTRUCT

## Status

**Accepted**

Specification-only until hosted. No `STRUCTURE_*`. No `event-catalog/0.3`. No project minigame. Help still omits BUILD and ATTEST. Other classes stay as they are: `relay` follows [RFC-0061](RFC-0061-multicycle-construct.md); `workshop` follows [RFC-0072](RFC-0072-workshop-cycle.md); `generator` follows [RFC-0073](RFC-0073-generator-cycle.md); `storage_bay` follows [RFC-0074](RFC-0074-storage-bay-cycle.md); `production_node` follows [RFC-0075](RFC-0075-production-node-cycle.md); `defensive_work` follows [RFC-0076](RFC-0076-defensive-work-cycle.md); route_link stays instant. [RFC-0053](RFC-0053-archive-annex.md) attention discount amount stays closed.

## Problem

[CONSTRUCTION.md](../docs/CONSTRUCTION.md) allows multi-cycle projects. S9–S17 closed that pin for every constructible class except `archive_annex` and `route_link`. A public `archive_annex` still goes live on CONSTRUCT, so a shell would save attention on INSPECT/ATTEST. An implementer would either keep remaining classes instant forever or invent a build minigame.

## Proposed change

Accept GC2-S18. `BUILD.CONSTRUCT class=archive_annex` in a **public** room creates a first-class `IN_PROGRESS` entity:

- Same `entity_id` for the whole life
- Occupies the room’s archive_annex slot immediately. Not a live annex until promotion
- After **1** committed cycle, the same entity becomes live (`IN_PROGRESS` cleared)
- Hidden rooms still reject CONSTRUCT
- `DISMANTLE` of `IN_PROGRESS` salvages the catalog salvage and leaves **no** live annex and **no** scar
- In-room INSPECT and ATTEST apply the S4 attention −1 **only** when a live (not `IN_PROGRESS`) `archive_annex` is in the room. Slot occupancy still counts the shell
- Events: `ENTITY_CREATE` at start, `ENTITY_UPDATE` on promotion, `ENTITY_DESTROY` + `BUDGET_CONSUMED` on salvage. No `STRUCTURE_*`
- PLAY MAY say an archive annex is under construction. WATCH silent
- Chamber help still omits BUILD and ATTEST

Catalog: [`construction-catalog.gc2-s18.json`](../specs/construction-catalog.gc2-s18.json).  
Slice: [GC2-S18-ARCHIVE-ANNEX-CYCLE.md](../docs/GC2-S18-ARCHIVE-ANNEX-CYCLE.md).

## Alternatives rejected

| Alternative | Why |
|-------------|-----|
| All remaining classes multi-cycle | Out of slice |
| Duration other than 1 | Extra machinery |
| New room / project site | Hidden topology |
| `STRUCTURE_*` | Extra catalog |
| Help BUILD / ATTEST | S0 / S4 pin |
| Scar on in-progress salvage | Never live |
| Filter `in_progress` from slot occupancy | Would allow a second annex |
| Change S4 discount amount | Closed arithmetic |

## Compatibility

Additive for `archive_annex` only. Existing live annexes stay live and keep the S4 discount. Worlds ignoring S18 keep instant archive_annex CONSTRUCT. S4 millipoints and S9–S17 pins are unchanged.

## Data / security

`in_progress` on the entity. Hidden rooms store none. WATCH silent.

## Validation

`check_gc2_s18`: public archive_annex CONSTRUCT is `IN_PROGRESS`; after 1 committed cycle same `entity_id` is live; hidden reject; DISMANTLE of in-progress salvages with no live leftover; attention discount only when live; no new verbs.

## Rollback

Ignore `in_progress` on archive annexes (treat every annex as live immediately, including the attention discount).

## Unresolved

Remaining-class multi-cycle (`route_link`). Third-and-later co-owners.
