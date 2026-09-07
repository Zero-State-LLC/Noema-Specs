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

## Extension Points

Non-normative knowledge-projection and exploration-fixture seams.

- Extend per-agent views distinguishing second-hand discovery, direct LOOK/INSPECT, repeated investigation and actionable understanding. Retain source and observation age so stale or conflicting knowledge is not displayed as current world truth.
- Preserve paid ordinary actions, partial observability and the ban on automatic map fill. Public WATCH and another Controller cannot supply hidden exits or private discoveries to an Agent Player merely because an explorer UI can draw a map.
- Compatibility/promotion: build on existing observation/entity-update patterns and strategic-knowledge rules; a new discovery event or world mechanic needs separate authority. Knowledge indicators remain derived presentation, not a new research score or automatic canonical state ladder.
- Verification proposal: compare two agents with different observations, a second-hand report, a changed route and a hidden exit. Assert each sees only permitted knowledge, MOVE retains cost and outdated reports stay distinguishable. A text route list and localized evidence-age labels should remain usable without spatial/color cues.
