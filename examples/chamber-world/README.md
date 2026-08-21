# Chamber World — Canonical Starting Map

## Design targets

- 10 strategically distinct locations
- Clear early scarcity and trade pressure
- Multiple viable opening strategies
- Natural chokepoints and information asymmetry
- Neutral infrastructure that creates early cooperation or contest
- Fits 2–10 agents without obvious forced optimal start

## Machine-readable seed

| File | Role |
|------|------|
| [`world-seed.json`](world-seed.json) | Genesis map (rooms, exits, infrastructure, nodes) validating `world-seed.schema.json` |
| [`start-distributions.json`](start-distributions.json) | Alternate ENTER_WORLD room assignment profiles (2–10 agents) |

Related design: [CHAMBER-MAP.md](../../docs/CHAMBER-MAP.md), [STARTING-CONDITIONS.md](../../docs/STARTING-CONDITIONS.md), [GEOGRAPHY.md](../../docs/GEOGRAPHY.md), [FIRST-20-CYCLES.md](../../docs/FIRST-20-CYCLES.md). Contestation events: [RFC-0002](../../rfcs/RFC-0002-strategic-contestation-and-crime-events.md).

**Note:** This package is the **canonical 10-room target map**. Existing `examples/v01-seed/` and `examples/v01-strategic/` remain the ADR-005 reducer fixtures (4 rooms + full catalog trajectory). Chamber product implementations SHOULD prefer this map for play; catalog conformance remains on v01-seed.

## Locations

| Room ID | Name | Strategic role |
|---------|------|----------------|
| `room.civic-exchange` | Civic Exchange | Central meeting / trade hub. High visibility. |
| `room.relay-quarter` | Relay Quarter | Primary communication infrastructure. Early degradation pressure. |
| `room.foundry-corridor` | Foundry Corridor | Production-focused. Resource nodes + production_node potential. |
| `room.transit-ring` | Transit Ring | Movement hub. Multiple exits. Chokepoint potential. |
| `room.infrastructure-vault` | Infrastructure Vault | Hardened storage and generator access. Defensible. |
| `room.archive` | Archive | Knowledge / document focus. Low material, high information. |
| `room.outer-works` | Outer Works | Edge location. Exploration gateway and risk. |
| `room.storage-district` | Storage District | High storage_bay potential. Logistics node. |
| `room.generator-hall` | Generator Hall | Power generation. Critical for production modifiers. |
| `room.frontier-gate` | Frontier Gate | Edge of known map. Leads toward later expansion. |

## Suggested initial routes (exits)

- Civic Exchange ↔ Relay Quarter
- Civic Exchange ↔ Transit Ring
- Civic Exchange ↔ Storage District
- Relay Quarter ↔ Infrastructure Vault
- Relay Quarter ↔ Generator Hall
- Foundry Corridor ↔ Transit Ring
- Foundry Corridor ↔ Generator Hall
- Transit Ring ↔ Outer Works
- Transit Ring ↔ Frontier Gate
- Storage District ↔ Infrastructure Vault
- Archive ↔ Civic Exchange (condition-gated ACCESS_TOKEN on Archive side entry optional)
- Outer Works ↔ Frontier Gate

Some exits start with mild conditions or higher traversal cost to create early choices.

### Route pressure (seed v1.1)

| Pattern | Exits / notes |
|---------|----------------|
| Archive gate | `exit.ce-ar-ab` carries `ACCESS_TOKEN` |
| Edge energy premium | Transit ↔ Outer Works / Frontier Gate and Outer ↔ Frontier use `traversal_cost.energy` 1–2 |
| Edge tags | `EDGE_HAZARD` / `FRONTIER_APPROACH` on selected outbound edge exits |
| Vault / foundry mild cost | Relay ↔ Vault and Foundry ↔ Generator: `energy` 1 |

Exact costs live on exit objects in `world-seed.json` (`traversal_cost`). MOVE still pays base energy plus traversal cost ([WORLD-ENGINE.md](../../docs/WORLD-ENGINE.md)).

## Initial infrastructure (neutral / imperfect)

- One `relay` in Relay Quarter (condition ~65–75)
- One `generator` in Generator Hall (condition ~60)
- One `storage_bay` in Storage District
- One `production_node` in Foundry Corridor

Condition values are intentionally imperfect so early REPAIR decisions matter.

## Starting resource nodes

Limited stock resource nodes in Foundry Corridor and Outer Works. Regen is modest. Early HARVEST creates local scarcity and trade incentive.

## Visibility and knowledge

Agents begin knowing only their starting room and immediately adjacent exits. Full map knowledge must be earned through movement and observation ([EXPLORATION.md](../../docs/EXPLORATION.md)).

## Starting positions

Symmetric opportunity: no start grants permanent material advantage ([STARTING-CONDITIONS.md](../../docs/STARTING-CONDITIONS.md)).

| Profile (`start-distributions.json`) | Rooms | Typical size |
|--------------------------------------|-------|--------------|
| `symmetric_hub` (default) | Civic Exchange | 2–4 |
| `light_central_spread` | Exchange, Transit Ring, Relay Quarter | 5–10 |
| `dual_pole` | Exchange ↔ Foundry Corridor (alternating) | 4–8 |

Default entry room on the seed remains `room.civic-exchange`. Operators select a profile at world open; registration order drives round-robin / alternate assignment.
