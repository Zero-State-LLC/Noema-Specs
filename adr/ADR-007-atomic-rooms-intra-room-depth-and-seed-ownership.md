# ADR-007 — Atomic Rooms, Intra-Room Exploration Depth, and Seed Content Ownership

## Status

Proposed

Date: 2026-08-18

Related docs: [CHAMBER-MAP.md](../docs/CHAMBER-MAP.md), [GEOGRAPHY.md](../docs/GEOGRAPHY.md), [WORLD-MODEL.md](../docs/WORLD-MODEL.md), [PARTIAL-OBSERVABILITY.md](../docs/PARTIAL-OBSERVABILITY.md), [COMMAND-DISCOVERY.md](../docs/COMMAND-DISCOVERY.md), [ACTION-CONTRACTS.md](../docs/ACTION-CONTRACTS.md), [WATCH-LIGHTWEIGHT-SPECTATOR.md](../docs/WATCH-LIGHTWEIGHT-SPECTATOR.md), [PLAYER-ACTION-MAP.md](../docs/PLAYER-ACTION-MAP.md), [examples/chamber-world/world-seed.json](../examples/chamber-world/world-seed.json)

Also binds: [ADR-006](ADR-006-world-bound-exit-visibility-and-location-discovery.md), [ADR-001](ADR-001-determinism-and-seeded-nondeterminism.md), [ADR-002](ADR-002-private-cognition-boundary.md), [EXPLORATION.md](../docs/EXPLORATION.md), [OBSERVATION.md](../docs/OBSERVATION.md).

This ADR does not open new verbs, new event types, Genesis reseed, or a full-graph join payload.

## Context

NOEMA v0.1 Chamber is a finite graph of strategically distinct rooms. Visual mapping (WATCH Phosphor + ASCII hybrid), agent knowledge, and research reproducibility all require a hard boundary on what a room is and how Players explore inside it.

Current canon already states:

- Hosted first world is exactly 10 rooms; Chamber family band is 8–15 ([ADR-006](ADR-006-world-bound-exit-visibility-and-location-discovery.md), [CHAMBER-MAP.md](../docs/CHAMBER-MAP.md)).
- Rooms are not decorative; each must have a strategic reason ([GEOGRAPHY.md](../docs/GEOGRAPHY.md)).
- Movement is exit-based ([ACTION-CONTRACTS.md](../docs/ACTION-CONTRACTS.md) `MOVE`).
- Agents discover via structured observations and `AVAILABLE_ACTIONS` ([COMMAND-DISCOVERY.md](../docs/COMMAND-DISCOVERY.md)).
- Hidden exits are omitted, not labeled, and are revealed locally ([ADR-006](ADR-006-world-bound-exit-visibility-and-location-discovery.md)).

Ambiguity remains around:

- Whether a room can contain nested spatial areas that require further movement.
- How much exploration is allowed inside a single room.
- Who owns room content and how it may change.

Without an explicit freeze, implementations can drift into sub-rooms, coordinate movement, decorative locations, or LLM-authored interiors. That would break map legibility, agent simplicity, and deterministic replay.

## Decision

### A. Atomic room rule

A room is one atomic node in the world graph.

- No sub-rooms.
- No continuous coordinates or internal grid.
- No areas, zones, or back rooms that require a second `MOVE` while remaining in the same `room_id`.
- Presence is binary: a Player is in `room_id` or is not.

Any need for a distinct spatial place MUST be expressed as a new room node plus one or more exits.

### B. Intra-room exploration = depth, not breadth

Exploration inside a room is limited to:

| Action / channel | Effect |
|------------------|--------|
| `LOOK` | Room projection: prose, visible entities, visible exits, local conditions |
| `INSPECT` | Deeper observation of a co-located entity (or the room itself if allowed) |
| Live state | Resource levels, infrastructure condition, pressure, presence, scars |
| Social / records | `MESSAGE`, boards, artifacts already present or brought in |
| Exit discovery | Revelation of previously hidden or conditional exits that **leave** the room ([ADR-006](ADR-006-world-bound-exit-visibility-and-location-discovery.md) §C) |

Novelty across cycles comes from state change and progressive revelation of what is already co-located, not from new internal geography.

### C. Strategic necessity

Every room in a first-world seed MUST declare one or more strategic roles from this closed set:

```text
resource | infrastructure | chokepoint | information | trade | starting_position
```

- Empty role sets are invalid.
- Purely decorative or flavor-only rooms are invalid.
- A room may hold multiple roles.

### D. Content ownership

| Source | Authority |
|--------|-----------|
| World seed | Initial room id, name, description template, entity set, exits, conditions, strategic roles |
| Runtime ledger | Entity state, resources, infrastructure integrity, presence, scars, documents, organization control |
| Observation rules | What this Player may see now |
| Genesis / world-revision | Only path to add, remove, or restructure rooms |

Runtime systems (including any LLM-facing layer) MUST NOT invent new room ids, sub-locations, or exits. They may only render or act on existing seeded and ledger state under observation rules.

### E. Seed schema requirements

Room objects in the seed MUST include:

```text
room_id              (required, stable)
name                 (required)
strategic_roles      (required, non-empty array from the closed set)
description          (or description_template)
entity_ids           (array, may be empty only if other strategic justification exists)
allows_substructure  false   (required literal for v0.1)
```

Seed validation MUST reject rooms that violate these constraints.

### F. Action and observation boundaries

- `MOVE` targets MUST resolve through an exit's `to_room_id`. Targets that are not exit destinations are invalid (`UNREACHABLE` or the existing `MOVE_REJECTED` equivalent that does not distinguish hidden-exit from no-exit).
- `INSPECT` targets MUST be the current room or a co-located entity id. Nested location targets are invalid.
- Observations MUST NOT emit nested room ids or area identifiers.
- Agent knowledge models accumulate room nodes and exit edges only.
- WATCH / public projections emit at most one node per public room.

## Consequences

Positive:

- WATCH and Player maps remain a stable, legible graph of ≤15 nodes.
- Agent discovery stays a walk over observations + `AVAILABLE_ACTIONS`.
- Research trajectories remain comparable; geography is not a hidden variable.
- Design pressure stays on deep coupled systems inside few rooms.

Trade-offs:

- Geographic novelty is limited; depth must come from entities, economy, institutions, and information.
- “The rear of the Archive” requires a real new room and exit, not a free interior.

Forbidden without a later RFC:

- Procedural or runtime room generation inside a cycle.
- Sub-room or coordinate movement models.
- Decorative-only rooms.
- Automatic expansion of the graph from Player text or LLM output.

## Implementation notes

1. `specs/world-seed.schema.json` requires `strategic_roles` and `allows_substructure: false` on every room.
2. chamber-world and conformance seeds that validate against that schema MUST pass.
3. Action reducers for `MOVE` and `INSPECT` reject non-room / non-entity targets. Runtime follow-on; no new verbs.
4. Observation `content.location` remains `additionalProperties: false`. Nested room or area identifiers fail the schema.
5. [CHAMBER-MAP.md](../docs/CHAMBER-MAP.md) and [GEOGRAPHY.md](../docs/GEOGRAPHY.md) point here.

Minimal conformance tests:

1. Seed room with empty `strategic_roles` → validation failure.
2. Seed room with `allows_substructure: true` → validation failure for v0.1.
3. `MOVE` to an id that is not an exit destination from the current room → rejected.
4. Observation payload containing a nested room or area id → schema failure.
5. WATCH projection emitting more nodes than the set of public rooms → failure (runtime pin; public-room filter already required by ADR-006).

## Alternatives considered

| Alternative | Why rejected |
|-------------|--------------|
| Continuous / tile-based rooms | Breaks text-first MUD model, complicates agents, destroys simple map projection |
| Sub-rooms as first-class objects without exits | Hidden second graph; observation and WATCH become ambiguous |
| Full graph given to every Player on join | Destroys exploration and asymmetric information ([ADR-006](ADR-006-world-bound-exit-visibility-and-location-discovery.md)) |
| LLM-authored interiors at runtime | Non-deterministic geography; breaks replay and seed authority |
| Decorative rooms for atmosphere | Violates “rooms are not decorative”; dilutes strategic density |

## Relation to prior decisions

This ADR is complementary to [ADR-006](ADR-006-world-bound-exit-visibility-and-location-discovery.md):

- ADR-006 freezes **how many** rooms and **how exits are revealed**.
- This ADR freezes **what a room is** and **how Players explore inside one**.

Together they close the v0.1 geography model for implementation, visual mapping, and agent runtime.
