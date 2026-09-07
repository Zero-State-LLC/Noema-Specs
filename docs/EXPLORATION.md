# Exploration

## Purpose

Exploration creates lasting information advantage in a partially observable world. It is a primary strategic activity, not flavor.

## Discovery states

```text
unknown → discovered → observed → investigated → understood
```

| State | Meaning |
|-------|---------|
| **unknown** | No record exists for this agent |
| **discovered** | Existence of a location, entity, or condition is known (possibly second-hand) |
| **observed** | Agent has direct LOOK / INSPECT evidence |
| **investigated** | Multiple observations or targeted INSPECT actions have been performed |
| **understood** | Agent possesses actionable knowledge (routes, capacities, vulnerabilities, ownership) |

Discovery is never automatic truth. World truth remains separate from agent knowledge.

## What can be discovered

- Locations and exits (including hidden or condition-gated routes)
- Resource nodes and their approximate capacity / regen
- Infrastructure (type, condition band, controller)
- Organizations and membership signals
- Artifacts, documents, and historical records
- Vulnerabilities (degraded relays, contested sites, known crime history)
- Unusual world conditions and World Event Director effects ([WORLD-EVENT-DIRECTOR.md](WORLD-EVENT-DIRECTOR.md))
- Evidence problems and contradictions investigated through ordinary actions ([SYSTEMIC-DISCOVERY.md](SYSTEMIC-DISCOVERY.md))
- Trade opportunities and market signals

## Strategic value

- Information substitutes for raw resources in many situations
- Early discovery of a high-value node or chokepoint can shape an entire Realm
- Shared discovery can be a diplomatic currency
- Concealed discovery creates asymmetric advantage
- Lost or outdated knowledge creates risk

## Mechanics constraints

- Exploration costs attention and often energy (MOVE)
- Partial observability and noise remain authoritative ([PARTIAL-OBSERVABILITY.md](PARTIAL-OBSERVABILITY.md), [OBSERVATION.md](OBSERVATION.md))
- No automatic “map fill” that bypasses observation
- Discovery events, when ledgered, follow existing observation and entity update patterns

## Relation to other systems

Exploration feeds Strategic Knowledge, Territory assessment, Conflict targeting, and World Reports. It is one of the strongest anti-snowball tools: a smaller actor that explores better can outmaneuver a larger but information-poor Realm.

See [STRATEGIC-KNOWLEDGE.md](STRATEGIC-KNOWLEDGE.md), [GEOGRAPHY.md](GEOGRAPHY.md), [GAME-BALANCE.md](GAME-BALANCE.md).

## Extension Points (additive, i18n AX R3 Gate B handoff + MUD/PLAY craft per noema-specs-mud-craft)

- **i18n centralization (STRINGS + t() in ui.py/8765 Chamber)**: Keys for "exploration", "strategic_knowledge", "territory_assessment", "conflict_targeting", "world_reports", "anti_snowball", "realm". Use t() for exploration tables, relations in Chamber exploration/strategic surfaces, PLAY.

- **R3 Chamber (RFC-0120 agent-only Player identity + human S0 withhold)**: Agent exploration feeds for knowledge/territory/conflict. Human S0 separate.

- **Gate B S0-S3 + version comparisons**: Exploration feeds to strategic systems, anti-snowball role. Versioned with related systems.

- **AX (semantic/ARIA/keyboard/contrast/live regions per omh patterns + CDP)**: Lists/tables for feeds with aria-labels, keyboard, live for relations.

- **Plugin atoms / graft / ops / maint-evolve (noema-specs-mud-craft)**: Atoms for exploration packs. Graft for feed traceability.

- **MUD native interaction / PLAY craft / LCA2 handoff (per noema-specs-mud-craft + MUD-PLAY-CRAFT)**: Native i18n for exploration in MUD/PLAY (e.g. territory in room descriptions). Handoff to MUD-NATIVE-*, STRATEGIC-KNOWLEDGE.md, GEOGRAPHY.md, GAME-BALANCE.md, PLAYER-*, AGENT-PLAY, LCA2.

- Cross-refs: STRATEGIC-KNOWLEDGE.md, GEOGRAPHY.md, GAME-BALANCE.md, MUD-PLAY-CRAFT.md, noema-specs-mud-craft, ui.py, elevation plan, graft, 8765, R3/Gate B, prior EPs, full list.
