# Game-System Dependency Map

```text
GEOGRAPHY
    ↓
RESOURCES ←→ PRODUCTION
    ↓           ↓
INFRASTRUCTURE ←→ STORAGE
    ↓
TRADE ←→ ORGANIZATIONS
    ↓           ↓
TERRITORY / DIPLOMACY / CONFLICT / CRIME
    ↓
HISTORY + REPORTS + REALMS
```

## Rules

- Cross-links are mandatory. Isolated mechanics are defects ([CORE-GAME-LOOP.md](CORE-GAME-LOOP.md), [GAME-BALANCE.md](GAME-BALANCE.md)).
- Research instrumentation (Frontier, Observatory) observes and may change **conditions**; it does not replace this map as the primary game structure.

## Document index

| Node | Docs |
|------|------|
| Geography | [GEOGRAPHY.md](GEOGRAPHY.md), [CHAMBER-MAP.md](CHAMBER-MAP.md) |
| Resources / production | [RESOURCE-ECONOMY.md](RESOURCE-ECONOMY.md), [INFRASTRUCTURE.md](INFRASTRUCTURE.md) |
| Trade / orgs | [ACTION-CONTRACTS.md](ACTION-CONTRACTS.md), [DIPLOMACY.md](DIPLOMACY.md) |
| Territory / conflict | [TERRITORY-CONTROL.md](TERRITORY-CONTROL.md), [STRATEGIC-CONFLICT.md](STRATEGIC-CONFLICT.md) |
| History / reports / realms | [WORLD-REPORTS.md](WORLD-REPORTS.md), [REALMS.md](REALMS.md), [GAME-CYCLE.md](GAME-CYCLE.md) |
