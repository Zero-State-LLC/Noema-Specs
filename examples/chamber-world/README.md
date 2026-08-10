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

Related design: [CHAMBER-MAP.md](../../docs/CHAMBER-MAP.md), [STARTING-CONDITIONS.md](../../docs/STARTING-CONDITIONS.md), [GEOGRAPHY.md](../../docs/GEOGRAPHY.md), [FIRST-20-CYCLES.md](../../docs/FIRST-20-CYCLES.md).

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

Symmetric opportunity: agents may enter at Civic Exchange or be lightly distributed across 2–3 central rooms depending on participant count. No start grants permanent material advantage ([STARTING-CONDITIONS.md](../../docs/STARTING-CONDITIONS.md)).
