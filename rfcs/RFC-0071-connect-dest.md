# RFC-0071 — GC2-S12 CONNECT dest pin

## Status

**Accepted**

Specification-only until hosted. No new exits. No `CONNECT` verb. No `STRUCTURE_*`. No `event-catalog/0.3`. Help still omits BUILD.

## Problem

[CONSTRUCTION.md](../docs/CONSTRUCTION.md) lists `CONNECT`. GC2-S1 `route_link` waives cargo extra but names no destination. An implementer would add a public exit or leak hidden topology.

## Proposed change

Accept GC2-S12. `BUILD.CONNECT` on a live **public** `route_link` the actor stewards:

- `dest` is an existing **public** neighbor of the current public room
- That neighbor MUST already have a **public reverse exit** back here
- Same `entity_id`. Stamps `dest_room_id`. Overwrite allowed
- Hidden current room, hidden dest, missing public pair, or one-way public exit: `NOT_OBSERVABLE` with one non-leaking reason
- Does **not** add, remove, or hide exits
- Cargo waiver stays the S1 in-room rule
- Cost: compute 1. Events: `ENTITY_UPDATE` + `BUDGET_CONSUMED`. No `STRUCTURE_*`
- PLAY MAY say `The route link faces {dest}.` WATCH silent
- Human alias `connect <link> to <dir|room>` is accepted and **not** listed in Chamber help

Catalog: [`construction-catalog.gc2-s12.json`](../specs/construction-catalog.gc2-s12.json).  
Slice: [GC2-S12-CONNECT.md](../docs/GC2-S12-CONNECT.md).

## Alternatives rejected

| Alternative | Why |
|-------------|-----|
| New exit / new `to_room_id` | Hidden topology |
| Distinct fail for hidden dest | Leak |
| Require dest for cargo waiver | Breaks S1 |
| `CONNECT` verb | Extra command |
| `STRUCTURE_CONNECTED` | Extra catalog |
| Help BUILD | S0 pin |

## Compatibility

Additive stamp on `route_link`. Worlds ignoring S12 keep unpinned links and the S1 waiver.

## Data / security

`dest_room_id` on the existing entity. Hidden rooms store none. Failure does not name hidden rooms or missing reverse exits.

## Validation

`check_gc2_s12`: public two-way dest accepted; hidden dest / no reverse share `not_observable`; no new exits; no new verbs.

## Rollback

Ignore `CONNECT` (`INVALID_REQUEST`).

## Unresolved

Workshop multi-cycle is [RFC-0072](RFC-0072-workshop-cycle.md). Remaining-class multi-cycle. Third-and-later co-owners.
