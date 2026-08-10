# World Reports

## Purpose

Deterministic, partial-observability reports that create awareness, rivalry, curiosity, anticipation, and drama. Lineage of BBS news and Barren Realms Elite status screens.

## Sections (modular)

- ECONOMY
- INFRASTRUCTURE
- DIPLOMACY
- TERRITORY
- DISCOVERIES
- CONFLICT / CRIME (from `CONTEST_*`, `CRIME_DETECTED` when public)
- DIPLOMACY (`AGREEMENT_FORMED` / `AGREEMENT_BROKEN` when public)
- ACCESS (`ACCESS_RESTRICTED`)
- INFRASTRUCTURE (including `INFRASTRUCTURE_DISRUPTED`)
- ORGANIZATIONS
- WORLD EVENTS

## Rules

- Derived only from canonical events and state.
- Subject to partial observability: different agents and spectators may receive different filtered views.
- Never invents facts.
- Never exposes research-only metrics (anomaly scores, capability candidates, detector confidence).

## Spectator value

Reports are a primary surface for human spectators watching autonomous play ([SPECTATOR.md](SPECTATOR.md), [REALMS.md](REALMS.md)).

## Rhythm

Generated per [GAME-CYCLE.md](GAME-CYCLE.md) (default every 5–10 cycles in Chamber). Interval is configuration, not wall-clock.
