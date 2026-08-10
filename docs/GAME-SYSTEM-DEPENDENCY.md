# Game System Dependency Map

Canonical alias for the primary dependency chain. Detailed document index: [GAME-SYSTEM-MAP.md](GAME-SYSTEM-MAP.md).

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

## Critical cross-links

- Exploration ↔ Knowledge ↔ Territory assessment
- Infrastructure condition ↔ Production ↔ Conflict targeting
- Crime ↔ Reputation ↔ Diplomacy ↔ Organization stability
- Loss ↔ Recovery ↔ Ambition reorientation
- World Reports ↔ Spectator drama ↔ Human engagement

## Rule

Every major mechanic must affect at least one other strategic system. Isolated mechanics are defects ([CORE-GAME-LOOP.md](CORE-GAME-LOOP.md), [GAME-BALANCE.md](GAME-BALANCE.md)).
