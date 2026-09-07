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

Non-normative extension guidance; runtime, i18n, accessibility and gate verification remain separate.

### Filtered report rendering

Extend deterministic report presentation and provenance checks within the accepted WR-S0 slice.

### Preserved invariants

Reports derive only from canonical state/events and permitted views. WR-S0 retains the last one public infrastructure-condition report every five committed cycles; WATCH stays silent and NEWS is not a verb. Operator wall-clock digests are a different product.

### Compatibility and promotion

The broader modular section list is not permission to activate new report sections. RFC-0088/WR-S0 own current behavior; new sections, cadence or exposure need corresponding accepted authority. Controllers receive only authorized filtered observations; research-only metrics remain absent. Humans have separate authorized roles, not S0 privilege tiers.

### Validation fixtures before adoption

Compare report selection at four and five committed cycles and after another report replaces the retained item. A wall-clock tick alone produces none. Inject anomaly score, detector confidence or a private agreement and require exclusion from public output. Verify no WATCH line or NEWS affordance appears; localized presentation must not change event provenance.
