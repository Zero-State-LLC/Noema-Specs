# RFC-0049 — GC2-S1 route_link

## Status

**Accepted**

No new verbs. No `event-catalog/0.3`. No hidden-room leak. No freight company.

## Problem

[CONSTRUCTION.md](../docs/CONSTRUCTION.md) scenario C needs infrastructure that changes movement. GC2-S0 can build the four v0.1 classes. Adding a new public exit would require choosing a destination without leaking hidden topology.

## Proposed change

Accept GC2-S1. Add constructible class `route_link` on existing `BUILD.CONSTRUCT` / `DISMANTLE`:

- Costs match `relay`: energy 8, compute 4, storage 4, influence 2; salvage 2
- One live `route_link` per public room. Hidden rooms stay unbuildable
- Effect: a live `route_link` **waives the GC8-S4 cargo extra** for `MOVE` that leaves that room. Empty and carrying both cost energy 1
- No new exit. No `to_room_id`. No invented rooms
- DISMANTLE is S0 (owner, energy 4, compute 2) and restores cargo extra
- PLAY MAY say a route was opened, or that the link carries lots. WATCH silent
- Chamber help still omits BUILD

Catalog: [`construction-catalog.gc2-s1.json`](../specs/construction-catalog.gc2-s1.json).  
Slice: [GC2-S1-ROUTE-LINK.md](../docs/GC2-S1-ROUTE-LINK.md).

## Alternatives rejected

| Alternative | Why |
|-------------|-----|
| New public exit to a named room | Destination choice leaks or invents topology |
| CONNECT / UPGRADE verb | New operation |
| Courier / freight company | Doctrine |
| WATCH route ticker | Spectator leak |
| Chamber help BUILD | S0 pin |

## Compatibility

Additive class. Worlds ignoring S1 keep the four S0 classes and cargo MOVE 2.

## Data / security

No hidden `room_id`. Existing `ENTITY_CREATE` / `ENTITY_DESTROY` only.

## Validation

`check_gc2_s1`: class present; cargo waived; hidden construct rejected; no new verbs; no STRUCTURE_*.

## Rollback

Ignore `route_link` (CLASS_FORBIDDEN). Cargo extra stays.

## Unresolved

`workshop`, `defensive_work`, `archive_annex`, UPGRADE/CONNECT, scars.
