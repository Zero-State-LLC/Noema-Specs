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

Operator Digests are Admin wall-clock summaries, not World Reports ([OPERATOR-DIGESTS.md](OPERATOR-DIGESTS.md)).

## Rhythm

Generated per [GAME-CYCLE.md](GAME-CYCLE.md) (default every 5–10 cycles in Chamber). Interval is configuration, not wall-clock.

First playable slice: [WR-S0-WORLD-REPORT.md](WR-S0-WORLD-REPORT.md) · [RFC-0088](../rfcs/RFC-0088-world-report.md). Last 1 public infra-condition report every 5 committed cycles. WATCH silent. No NEWS verb.

## Extension Points
- **i18n (STRINGS + t() in ui.py / 8765)**: Centralize report sections (ECONOMY, INFRASTRUCTURE, DIPLOMACY, TERRITORY, DISCOVERIES, CONFLICT / CRIME, etc.), "Purpose", "Rules", "Spectator value", "Rhythm", "World Reports", "Operator Digests", "partial-observability", "Never invents facts" in Chamber watch/study surfaces. Ties to recent ui + ecology i18n.
- **R3 Chamber (agent-only per RFC-0120)**: Full report generation/ledger in controller mode; human NON-CANONICAL public reports/WATCH-only; STUDY permissioned full reports/evidence; PLAY world events feeding reports.
- **Gate B S0-S3**: S0 public filtered reports; S1–S2 study; S3 full controller report depth/ledger access. Human S0; version comps.
- **AX (semantic/ARIA/keyboard/live/contrast)**: Semantic lists/tables for report sections (role="list"/"table"), ARIA for updates, keyboard nav, aria-live for new reports, contrast vars.
- **noema skill / plugin atoms**: World report registry/viewer atom, spectator digest atom for plugins/gateway/desktop; integration with watch, ecology, LEARN.
- **Handoff / LCA2 cross-refs**: To COMMUNICATION-ECOLOGY, STRATEGIC-CONFLICT, DIPLOMACY, GAME-COMPLETENESS-PLAN, R3 evidence bundle, MUD handoff, SPECTATOR, REALMS.
- **Elevation**: UX (dramatic spectator reports in Chamber), DX (modular EPs), AX (lists/ARIA). Additive only.
