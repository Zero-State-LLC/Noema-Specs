# Chamber Map Guidance

## Canonical product map

**10-room starting map (authoritative for play):** [`examples/chamber-world/`](../examples/chamber-world/)  
Machine seed: [`examples/chamber-world/world-seed.json`](../examples/chamber-world/world-seed.json)  
Start profiles: [`examples/chamber-world/start-distributions.json`](../examples/chamber-world/start-distributions.json)

## Target size

Canonical small map: **8–15 strategically distinct locations** (product default: **10**).

## Core set (chamber-world)

| Room ID | Name |
|---------|------|
| `room.civic-exchange` | Civic Exchange |
| `room.relay-quarter` | Relay Quarter |
| `room.foundry-corridor` | Foundry Corridor |
| `room.transit-ring` | Transit Ring |
| `room.infrastructure-vault` | Infrastructure Vault |
| `room.archive` | Archive |
| `room.outer-works` | Outer Works |
| `room.storage-district` | Storage District |
| `room.generator-hall` | Generator Hall |
| `room.frontier-gate` | Frontier Gate |

**Conformance note:** ADR-005 reducer fixtures remain [`examples/v01-seed/`](../examples/v01-seed/) (4 rooms + full 24-type trajectory). Product play SHOULD use chamber-world.

## Rules

- Every location must have a gameplay reason: resource, infrastructure, chokepoint, information, trade, or starting position ([GEOGRAPHY.md](GEOGRAPHY.md)). Seed rooms MUST declare `strategic_roles` from that closed set and `allows_substructure: false` ([ADR-007](../adr/ADR-007-atomic-rooms-intra-room-depth-and-seed-ownership.md)).
- A room is one atomic graph node. No sub-rooms, internal grids, or second `MOVE` that stays in the same `room_id`.
- Intra-room exploration is `LOOK` / `INSPECT` / live state / records — depth, not new geography.
- Routes, initial visibility, and starting hazards are defined in the seed ([ADR-006](../adr/ADR-006-world-bound-exit-visibility-and-location-discovery.md)).
- Rooms are not decorative.

## Routes

Exits carry direction, optional traversal cost, and conditions. Hidden/blocked exits create exploration value.
