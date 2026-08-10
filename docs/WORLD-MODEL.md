# World Model

## Scope

The World Engine is a persistent MUD-style simulation of rooms, geography, movement, economy, resources, infrastructure, organizations, markets, communication, institutions, local state, persistent history, and Deep Time.

## Chamber thesis

v0.1 Chamber is a **persistent strategic ecology** for 2–10 agents, not a thin protocol sandbox. Mechanics are fully specified in [GAME-DESIGN.md](GAME-DESIGN.md), [RESOURCE-ECONOMY.md](RESOURCE-ECONOMY.md), and [ACTION-CONTRACTS.md](ACTION-CONTRACTS.md).

## State domains

- **Canonical state:** authoritative private truth used for resolution.
- **Observable state:** mediated room, entity, resource, message, and event descriptions.
- **Agent state:** connection, budgets, capabilities, permissions, and declared metadata.
- **Research state:** trajectories, observations, events, predictions, self-reports, and provenance.
- **Spectator state:** derived projections only; never world truth ([SPECTATOR.md](SPECTATOR.md)).

## Resolution

State transitions MUST be deterministic under world version, seed, deterministic config, prior state, and ordered event ledger. Seeded nondeterminism MUST name the stream and decision point. Ordering: [SCHEDULER.md](SCHEDULER.md).

## Coupled strategic systems (v0.1)

```text
rooms/exits ↔ movement energy
resource nodes ↔ infrastructure condition ↔ production
agent budgets ↔ harvest/trade/repair
organizations ↔ influence regen ↔ cooperation/rivalry
messages ↔ asymmetric information
World Event Director ↔ scarcity pressure
```

## Deep Time objects

The world retains old treaties, dead agents, previous organizations, abandoned infrastructure, obsolete currencies, agent-written documents, historical misinformation, cultural conventions, ruins, artifacts, and institutional memory.

## Unknown Ontology

World content and research records MUST support unknown identifiers such as `UNKNOWN_CAPABILITY_<id>` and `UNKNOWN_PHENOMENON_<id>` without requiring immediate taxonomy.

## Persistence

Application lifecycle ≠ world lifecycle. Restart MUST preserve resources, organizations, infrastructure, cycles, and ledger ([DEPLOYMENT.md](DEPLOYMENT.md)).
