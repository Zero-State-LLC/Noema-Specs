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

## Rule

- Cross-links are mandatory. Isolated mechanics are defects ([CORE-GAME-LOOP.md](CORE-GAME-LOOP.md), [GAME-BALANCE.md](GAME-BALANCE.md)).
- Research instrumentation (Frontier, Observatory) observes and may change **conditions**; it does not replace this map as the primary game structure.

## Document index

| Node | Docs |
|------|------|
| Geography | [GEOGRAPHY.md](GEOGRAPHY.md), [CHAMBER-MAP.md](CHAMBER-MAP.md), [STARTING-CONDITIONS.md](STARTING-CONDITIONS.md) |
| Resources / production | [RESOURCE-ECONOMY.md](RESOURCE-ECONOMY.md), [INFRASTRUCTURE.md](INFRASTRUCTURE.md) |
| Exploration / knowledge | [EXPLORATION.md](EXPLORATION.md), [STRATEGIC-KNOWLEDGE.md](STRATEGIC-KNOWLEDGE.md) |
| Trade / orgs | [ACTION-CONTRACTS.md](ACTION-CONTRACTS.md), [DIPLOMACY.md](DIPLOMACY.md) |
| Territory / conflict | [TERRITORY-CONTROL.md](TERRITORY-CONTROL.md), [STRATEGIC-CONFLICT.md](STRATEGIC-CONFLICT.md), [LOSS-RECOVERY.md](LOSS-RECOVERY.md) |
| History / reports / realms | [WORLD-REPORTS.md](WORLD-REPORTS.md), [REALMS.md](REALMS.md), [GAME-CYCLE.md](GAME-CYCLE.md), [SPECTATOR.md](SPECTATOR.md) |
