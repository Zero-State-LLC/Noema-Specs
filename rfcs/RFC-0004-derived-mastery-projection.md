# RFC-0004 — Derived Mastery Projection (GC1-S0)

## Status

**Accepted**

Approved for specification-only implementation on 2026-08-13. Does not expand `event-catalog`. Not v0.8 Phenomena. Runtime implementation of GC1-S0 may now follow [GC1-FIRST-SLICE.md](../docs/GC1-FIRST-SLICE.md).

## Problem

[MASTERY-SPECIALIZATION.md](../docs/MASTERY-SPECIALIZATION.md) settles that Players gain competence from demonstrated work, but leaves machine pins as SPEC GAP. A runtime agent cannot yet implement the smallest mastery slice without inventing tracks, thresholds, or events.

The completeness campaign must not open `event-catalog/0.3` or grant mechanical benefits in the first cut.

## Context

- Parent product authority: [MASTERY-SPECIALIZATION.md](../docs/MASTERY-SPECIALIZATION.md)
- Slice contract: [GC1-FIRST-SLICE.md](../docs/GC1-FIRST-SLICE.md)
- Campaign: [GAME-COMPLETENESS-PLAN.md](../docs/GAME-COMPLETENESS-PLAN.md)
- Frozen catalogs: `event-catalog/0.1` and `0.2`
- Research graphs: [CAPABILITY-GRAPH.md](../docs/CAPABILITY-GRAPH.md) / [LEARN.md](../docs/LEARN.md) MUST stay unused
- World-event envelope already has optional `actor_id` ([world-event.schema.json](../specs/world-event.schema.json))
- Player-originated events SHOULD carry `actor_id` ([DATA-MODEL.md](../docs/DATA-MODEL.md))

## Proposed change

Accept **GC1-S0 Derived Practice Projection** as the first mastery contract:

1. Four closed tracks: `track.explorer.01`, `track.surveyor.01`, `track.broker.01`, `track.engineer.01`.
2. Counts rebuilt from existing successful `LOOK`, `INSPECT`, `TRADE_ACCEPTED`, and player-attributed `ENTITY_UPDATE` (condition) events.
3. Lifecycle in this slice is only `UNTRACKED` / `PRACTICING`.
4. PLAY may show at most three pinned self-only prose lines. No integers. No XP.
5. WATCH shows nothing. Other Players see nothing. Affordances do not change.
6. No new verbs. No new event types. No WorldState fields.
7. Changing a counting rule requires a new catalog id (`mastery-catalog/gc1-s0` and successors).

Exact rules live in [GC1-FIRST-SLICE.md](../docs/GC1-FIRST-SLICE.md). This RFC does not duplicate them.

## Alternatives

| Alternative | Why rejected |
|-------------|--------------|
| Full GC1 with recognition and benefits | Requires magnitudes, leak tests, and likely events. Too large |
| GC2 Construction first | Needs `BUILD` and new structure events |
| GC3 Social Memory first | Needs relationship visibility and hidden-fact fixtures |
| New `PROFICIENCY_*` events now | Silent catalog expansion; forbidden by SUCCESSION / freeze |
| Universal XP | Forbidden by [PROGRESSION.md](../docs/PROGRESSION.md) |
| Reuse LEARN / capability graph | Research partition; would convert research into Player stats |
| All twelve example labels as classes | Those names are examples, not a character menu |

## Compatibility

Backward compatible with v0.1–v0.7 machine contracts. Additive derived projection only. Worlds that ignore this RFC remain conformant Chamber worlds.

Does not change `action-contracts`, `event-catalog`, agent protocol, or world-state schema.

## Data impact

No canonical new entity. Optional derived cache keyed by Player + `track_id` + counted `event_id`s. Cache MUST be rebuildable. No deletion of ledger history.

## Research impact

None on Lab / Compiler / LEARN. STUDY MAY observe practice trajectories in the research partition with claim labels. Practice is not a capability claim.

## Security impact

Private practice is Player-private. GUI MUST NOT leak another Player’s tracks. No new credentials or tools.

## Migration

Existing worlds start `UNTRACKED` and accumulate S0 counts from qualifying events already on the ledger (or, in a ledger-incomplete runtime, from events after the cache is introduced). Historical hosted events that lack `actor_id` do not create Engineer practice.

## Validation

- Catalog: [`specs/mastery-catalog.gc1-s0.json`](../specs/mastery-catalog.gc1-s0.json)
- Rebuild fixtures: [`examples/gc1-mastery/`](../examples/gc1-mastery/)
- Conformance: [`conformance/gc1-s0/`](../conformance/gc1-s0/) families M01–M03
- Validator: `check_gc1_s0` in `validation/validate_all.py` executes the rebuild

## Rollback

Leave Draft or mark Rejected. Remove S0 projection. No ledger rewrite required.

## Unresolved questions

1. Should Engineer wait until hosted `ENTITY_UPDATE` matches the catalog `{set, unset}` payload?
2. When should GC1-S1 (recognition + one benefit family) be specified?
3. Should `mastery-catalog/gc1-s0` become a JSON catalog at acceptance, or remain prose-normative?
