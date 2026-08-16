# RFC-0061 — GC2-S9 multi-cycle relay CONSTRUCT

## Status

**Accepted**

Specification-only until hosted. No `STRUCTURE_*`. No `event-catalog/0.3`. No project minigame. Help still omits BUILD.

## Problem

[CONSTRUCTION.md](../docs/CONSTRUCTION.md) allows multi-cycle projects as first-class entities. GC2-S0–S8 CONSTRUCT is instant. An implementer would invent a build minigame, new rooms, or `STRUCTURE_CONSTRUCTED`.

## Proposed change

Accept GC2-S9. `BUILD.CONSTRUCT class=relay` in a **public** room creates a first-class `IN_PROGRESS` entity:

- Same `entity_id` for the whole life. Other classes stay instant
- Occupies the room’s relay slot immediately. Not a live relay (no comms) until promotion
- After **1** committed cycle, the same entity becomes live (`IN_PROGRESS` cleared)
- Hidden rooms still reject CONSTRUCT
- `DISMANTLE` of `IN_PROGRESS` salvages the catalog salvage and leaves **no** live relay and **no** scar
- Events: `ENTITY_CREATE` at start, `ENTITY_UPDATE` on promotion, `ENTITY_DESTROY` + `BUDGET_CONSUMED` on salvage. No `STRUCTURE_*`
- PLAY MAY say a relay is under construction. WATCH silent
- Chamber help still omits BUILD

Catalog: [`construction-catalog.gc2-s9.json`](../specs/construction-catalog.gc2-s9.json).  
Slice: [GC2-S9-MULTICYCLE.md](../docs/GC2-S9-MULTICYCLE.md).

## Alternatives rejected

| Alternative | Why |
|-------------|-----|
| All classes multi-cycle | Out of slice |
| Duration other than 1 | Extra machinery |
| New room / project site | Hidden topology |
| `STRUCTURE_*` | Extra catalog |
| Help BUILD | S0 pin |
| Scar on in-progress salvage | Never live |

## Compatibility

Additive for `relay` only. Existing live relays stay live. Worlds ignoring S9 keep instant relay CONSTRUCT.

## Data / security

`in_progress` on the entity. Hidden rooms store none. WATCH silent.

## Validation

`check_gc2_s9`: public relay CONSTRUCT is `IN_PROGRESS`; after 1 committed cycle same `entity_id` is live; hidden reject; DISMANTLE of in-progress salvages with no live leftover; no new verbs.

## Rollback

Ignore `in_progress` (treat every relay as live immediately).

## Unresolved

CONNECT. Other-class multi-cycle. Institution ownership is [RFC-0067](RFC-0067-institution-own.md). Shared ownership.
