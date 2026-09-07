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

## Emergence / complexity map

Complementary, not a replacement: [GAME-SYSTEM-MAP.md](GAME-SYSTEM-MAP.md) · [COMPLEXITY-DOCTRINE.md](COMPLEXITY-DOCTRINE.md).

## Completeness overlay

See [GAME-SYSTEM-MAP.md](GAME-SYSTEM-MAP.md) and [GAME-COMPLETENESS-PLAN.md](GAME-COMPLETENESS-PLAN.md). Mastery, construction, social memory, offices, communication ecology, systemic discovery, conflict v2, economic specialization, emergent culture, and the World Event Director couple into this chain. Isolated completeness minigames are defects.

## Rule

Every major mechanic must affect at least one other strategic system. Isolated mechanics are defects ([CORE-GAME-LOOP.md](CORE-GAME-LOOP.md), [GAME-BALANCE.md](GAME-BALANCE.md)).

## Extension Points

Non-normative guidance for future work; existing authorities and closed-slice boundaries remain unchanged.

- **Seam and invariants.** New dependency annotations can explain how an already-authorized mechanic couples geography, production, institutions and historical projections. Keep this file an alias and relationship map, not an alternate subsystem specification.
- **Compatibility and validation.** Check each added edge against both linked subsystem contracts and GAME-SYSTEM-MAP; distinguish implemented coupling from proposed integration. A change to a transition or projection exposure needs its owning RFC/schema revision before the map can describe it as available.
