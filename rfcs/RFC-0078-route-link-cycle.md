# RFC-0078 — GC2-S19 multi-cycle route_link CONSTRUCT

## Status

**Accepted**

Specification-only until hosted. No `STRUCTURE_*`. No `event-catalog/0.3`. No project minigame. Help still omits BUILD. No new exits. [RFC-0049](RFC-0049-route-link.md) cargo waiver amount stays closed. [RFC-0071](RFC-0071-connect-dest.md) dest pin stays dest-only. Other constructible classes already follow S9–S18.

## Problem

[CONSTRUCTION.md](../docs/CONSTRUCTION.md) allows multi-cycle projects. S9–S18 closed that pin for every constructible class except `route_link`. A public `route_link` still goes live on CONSTRUCT, so a shell would waive cargo MOVE extra. An implementer would invent a new exit or a build minigame.

## Proposed change

Accept GC2-S19. `BUILD.CONSTRUCT class=route_link` in a **public** room creates a first-class `IN_PROGRESS` entity:

- Same `entity_id` for the whole life
- Occupies the room’s route_link slot immediately. Not a live link until promotion
- After **1** committed cycle, the same entity becomes live (`IN_PROGRESS` cleared)
- Hidden rooms still reject CONSTRUCT
- `DISMANTLE` of `IN_PROGRESS` salvages the catalog salvage and leaves **no** live link and **no** scar
- Departing MOVE waives the S1/S4 cargo extra **only** when a live (not `IN_PROGRESS`) `route_link` is in the room. Slot occupancy still counts the shell
- `BUILD.CONNECT` dest pin stays [RFC-0071](RFC-0071-connect-dest.md). An `IN_PROGRESS` link is not a live route link (`FORBIDDEN`). No new exit
- Events: `ENTITY_CREATE` at start, `ENTITY_UPDATE` on promotion, `ENTITY_DESTROY` + `BUDGET_CONSUMED` on salvage. No `STRUCTURE_*`
- PLAY MAY say a route link is under construction. WATCH silent
- Chamber help still omits BUILD

Catalog: [`construction-catalog.gc2-s19.json`](../specs/construction-catalog.gc2-s19.json).  
Slice: [GC2-S19-ROUTE-LINK-CYCLE.md](../docs/GC2-S19-ROUTE-LINK-CYCLE.md).

## Alternatives rejected

| Alternative | Why |
|-------------|-----|
| New exit / new `to_room_id` | Hidden topology |
| Duration other than 1 | Extra machinery |
| `STRUCTURE_*` | Extra catalog |
| Help BUILD | S0 pin |
| Scar on in-progress salvage | Never live |
| Filter `in_progress` from slot occupancy | Would allow a second link |
| Change S1 cargo waiver | Closed arithmetic |
| CONNECT as a new exit | S12 pin |

## Compatibility

Additive for `route_link` CONSTRUCT only. Existing live links stay live and keep the S1 waiver and S12 dest pin. Worlds ignoring S19 keep instant route_link CONSTRUCT. S1–S18 pins are unchanged.

## Data / security

`in_progress` on the entity. Hidden rooms store none. WATCH silent. Failure does not name hidden rooms.

## Validation

`check_gc2_s19`: public route_link CONSTRUCT is `IN_PROGRESS`; after 1 committed cycle same `entity_id` is live; hidden reject; DISMANTLE of in-progress salvages with no live leftover; cargo waiver only when live; no new verbs or exits.

## Rollback

Ignore `in_progress` on route links (treat every link as live immediately, including the cargo waiver).

## Unresolved

Third-and-later co-owners. Comms cycle expiry.
