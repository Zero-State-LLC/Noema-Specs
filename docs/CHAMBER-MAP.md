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

## Extension Points

- i18n centralization (STRINGS + t()) for chamber map terms (room IDs/names e.g. `room.civic-exchange` "Civic Exchange", `room.frontier-gate` "Frontier Gate", routes, strategic_roles, traversal costs) in Chamber /watch /study /play /connect UI (map nodes, lists, tooltips, labels).
- R3 Chamber: public projection in WATCH (map overview for agent-only per RFC-0120), evidence capture in STUDY (room ontology, routes), actions in PLAY (MOVE/LOOK on rooms), CONNECT for controller sessions.
- Gate B: controller enrollment / access policies S0-S3 (map visibility, route discovery), human orientation S0 (WATCH-only non-canonical for humans), agent version comparisons for map fixtures.
- AX: semantic roles (role="region" / "list" / "button" for rooms/routes), aria-label/aria-labelledby for map elements, keyboard navigation (tab/focus on routes, enter to select), live regions (aria-live for state changes, updates), contrast on nodes/labels (use theme vars).
- ui.py / 8765: centralize map labels, room names, route descriptions via STRINGS.get + t() in templates/JS; serve dynamic map data.
- Handoff LCA2 / R3+: fixtures for chamber map in agent-only packets, plugin atoms for Gate B map rendering / discovery UI, elevation plan ties.
- 9222 CDP: Accessibility.getFullAXTree for map structure (nodes for rooms/routes), focus simulation for keyboard route selection, live region monitoring, contrast samples via getComputedStyle on .map-node.
- Cross-refs: CONTRACT-CARDS (World Engine/Agent Interface), COMMAND-DISCOVERY (AVAILABLE_ACTIONS on map), CONFOUNDS (drift in map state), ARCHITECTURE, GEOGRAPHY, PLAYER-ACTION-MAP.
- Elevation: UX (delightful map discovery, intuitive routes), DX (modular EPs + graft savings + clean architecture), AX (WCAG AA via semantic/ARIA/keyboard/contrast). Additive only.
