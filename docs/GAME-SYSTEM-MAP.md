# Game-System Dependency Map

Canonical chain also published as [GAME-SYSTEM-DEPENDENCY.md](GAME-SYSTEM-DEPENDENCY.md).

## Primary dependency chain

```text
GEOGRAPHY
    ↓
RESOURCES
    ↓
PRODUCTION
    ↓
INFRASTRUCTURE
    ↓
TRADE
    ↓
ORGANIZATIONS
    ↓
TERRITORY / DIPLOMACY / CONFLICT / CRIME
    ↓
HISTORY + REPORTS + REALMS
```

(With bidirectional coupling RESOURCES ↔ PRODUCTION, INFRASTRUCTURE ↔ STORAGE, TRADE ↔ ORGANIZATIONS where operations feed both ways.)

## Critical cross-links

- Exploration ↔ Knowledge ↔ Territory assessment
- Infrastructure condition ↔ Production ↔ Conflict targeting
- Crime ↔ Reputation ↔ Diplomacy ↔ Organization stability
- Loss ↔ Recovery ↔ Ambition reorientation
- World Reports ↔ Spectator drama ↔ Human engagement

## Emergence / complexity map

Higher-order complement. It does **not** replace the domain chain above. Authority: [COMPLEXITY-DOCTRINE.md](COMPLEXITY-DOCTRINE.md).

```text
PRIMITIVES
  (resource · asset · location · player/organization · trade · agreement · information)
    ↓
WORLD PRESSURES
  (scarcity · distance · dependency · uncertainty)
    ↓
PLAYER ACTIONS
  (stable verbs + targets + authority + state)
    ↓
PERSISTENT CONSEQUENCES
    ↓
REPEATED PATTERNS
    ↓
PRACTICES
    ↓
ORGANIZATIONS / INSTITUTIONS
    ↓
CULTURE / DEEP TIME
```

A company, guild, freight compact, or archive society is `ORGANIZATION + roles + assets + contracts + practices`, not a new runtime species.

## Completeness overlay

Post-core PLAY-depth systems couple into the primary chain. They do not replace it. Authority: [GAME-COMPLETENESS-PLAN.md](GAME-COMPLETENESS-PLAN.md).

```text
MASTERY  ↔  ACTIONS / AUTHORITY
CONSTRUCTION  ↔  GEOGRAPHY / RESOURCES / INFRASTRUCTURE / TERRITORY / DEEP TIME
SOCIAL MEMORY  ↔  TRADE / DIPLOMACY / CONFLICT / INSTITUTIONS
OFFICES  ↔  ORGANIZATIONS / INSTITUTIONS / SUCCESSION
COMMUNICATION  ↔  INFRASTRUCTURE / KNOWLEDGE / REPORTS
DISCOVERY  ↔  EXPLORATION / EVIDENCE / LORE BOUNDARY
CONFLICT v2  ↔  TERRITORY / TRADE / REPUTATION / INFRASTRUCTURE
ECONOMIC SPECIALIZATION  ↔  RESOURCES / PRODUCTION / TRADE
CULTURE  ↔  DEEP TIME / INSTITUTIONS / MEMORY
WORLD EVENT DIRECTOR  ↔  CONDITIONS (never Player objectives)
```

## Rule

- Cross-links are mandatory. Isolated mechanics are defects ([CORE-GAME-LOOP.md](CORE-GAME-LOOP.md), [GAME-BALANCE.md](GAME-BALANCE.md)).
- Research instrumentation (Frontier, Observatory) observes and may change **conditions**; it does not replace this map as the primary game structure.

## Document index

| Node | Docs |
|------|------|
| Geography | [GEOGRAPHY.md](GEOGRAPHY.md), [CHAMBER-MAP.md](CHAMBER-MAP.md), [STARTING-CONDITIONS.md](STARTING-CONDITIONS.md) |
| Resources / production | [RESOURCE-ECONOMY.md](RESOURCE-ECONOMY.md), [INFRASTRUCTURE.md](INFRASTRUCTURE.md) |
| Player actions / adapters | [ACTION-CONTRACTS.md](ACTION-CONTRACTS.md), [PLAYER-ACTION-MAP.md](PLAYER-ACTION-MAP.md), [../protocols/mud-command-v1.md](../protocols/mud-command-v1.md), [../protocols/agent-protocol-v1.md](../protocols/agent-protocol-v1.md) |
| Exploration / knowledge | [EXPLORATION.md](EXPLORATION.md), [STRATEGIC-KNOWLEDGE.md](STRATEGIC-KNOWLEDGE.md) |
| Trade / orgs | [ACTION-CONTRACTS.md](ACTION-CONTRACTS.md), [DIPLOMACY.md](DIPLOMACY.md) |
| Territory / conflict | [TERRITORY-CONTROL.md](TERRITORY-CONTROL.md), [STRATEGIC-CONFLICT.md](STRATEGIC-CONFLICT.md), [LOSS-RECOVERY.md](LOSS-RECOVERY.md) |
| History / reports / realms | [WORLD-REPORTS.md](WORLD-REPORTS.md), [REALMS.md](REALMS.md), [GAME-CYCLE.md](GAME-CYCLE.md), [SPECTATOR.md](SPECTATOR.md) |
| Complexity doctrine | [COMPLEXITY-DOCTRINE.md](COMPLEXITY-DOCTRINE.md) |
| Completeness campaign | [GAME-COMPLETENESS-PLAN.md](GAME-COMPLETENESS-PLAN.md), [MUD-DESIGN-CANON.md](MUD-DESIGN-CANON.md) |
| Mastery | [MASTERY-SPECIALIZATION.md](MASTERY-SPECIALIZATION.md), [PROGRESSION.md](PROGRESSION.md) |
| Construction | [CONSTRUCTION.md](CONSTRUCTION.md), [GC2-FIRST-SLICE.md](GC2-FIRST-SLICE.md), [INFRASTRUCTURE.md](INFRASTRUCTURE.md) |
| Social memory / offices | [SOCIAL-MEMORY.md](SOCIAL-MEMORY.md), [INSTITUTIONAL-AUTHORITY.md](INSTITUTIONAL-AUTHORITY.md), [INSTITUTIONS.md](INSTITUTIONS.md) |
| Communication / discovery | [COMMUNICATION-ECOLOGY.md](COMMUNICATION-ECOLOGY.md), [SYSTEMIC-DISCOVERY.md](SYSTEMIC-DISCOVERY.md) |
| Economic specialization / culture / WED | [ECONOMIC-SPECIALIZATION.md](ECONOMIC-SPECIALIZATION.md), [EMERGENT-CULTURE.md](EMERGENT-CULTURE.md), [WORLD-EVENT-DIRECTOR.md](WORLD-EVENT-DIRECTOR.md) |
