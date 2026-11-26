# Intent: Recurring Perihelion Orbital Pressure Waves, Generator Recharge & Deep Time WATCH Projection

**Status:** `accepted`

**Next stage:** [RFC-0135](../rfcs/RFC-0135-perihelion-orbital-pressure-waves.md) and [RFC-0136](../rfcs/RFC-0136-generator-recharge-and-deeptime-watch-projection.md)

**Author:** Antigravity, for Danny

**Date:** 2026-11-26

This record is process only. It is not a spec, not a plan, and not an RFC. Danny approved the Phase 2 architecture plan (`orin_deeptime_mechanics_plan.md`) in chat on 2026-11-25.

## Problem

1. **Exogenous world pressure stops permanently after cycle 20 (`pressure.ts`):** `GC10-S1` caps all three pressure classes (`infrastructure_failure`, `resource_scarcity`, `access_restriction`) at `LAST_WINDOW_CYCLE = 20` and `MAX_ACTIVATIONS_1_20 = 1`. In a long-running persistent world (hundreds/thousands of cycles), the environment becomes permanently static, leaving custodians, emergency scopes, and `defensive_work` infrastructure with no recurring environmental challenge.
2. **Energy ceiling starves maintenance and under-utilizes built `generator`s (`NEXT.md` S19):** `REPAIR` costs 3 energy + cargo and cargo-carrying `MOVE` costs 2 energy, while `WAIT` yields only +2 energy per burned cargo (and rests only to 2 with an empty hold). Meanwhile, `generator` infrastructure built via treasury (`RFC-0133` amendment 1) has no active player charging loop.
3. **Deep Time & Culture state is invisible on `/watch`:** `deep-time.ts` (`scars`, `lore_attractors`, fossilization) and `culture.ts` (`CUSTOM` / `TRADITION` / `DORMANT` / `REVIVED` / `INHERITED` / `SCHISM`) already run deterministically in the World Engine, but `watch-live/1.0` does not project band-redacted room indicators for the Full-Screen 3D Room Cutaway.

## Proposed outcome

1. **Recurring Perihelion Orbital Pressure Waves (`RFC-0135`):** Keep the exact `GC10-S1` cycles 1–20 behavior unchanged for replay compatibility, and add deterministic recurring **60-cycle Perihelion Surge windows** for cycles `> 20` with mild safety floors (`MIN_CONDITION_AFTER = 25`, `MIN_STOCK_BEFORE = 4`), zero irreversible scars from pressure (`RFC-0051`), and mitigation from `defensive_work` infrastructure.
2. **Generator-Powered `RECHARGE` (`RFC-0136`):** Add a deterministic `RECHARGE` player action usable in any room with a ready, operational `generator` (`condition >= 25`), restoring `+4` energy (up to cap) without burning cargo, at a bounded per-player cooldown (`3` cycles) and gentle generator wear (`-2` condition, floored at `25`), creating a living logistics loop between generators, quartermasters, and custodians.
3. **Band-Redacted Deep Time & Culture Projection on `watch-live/1.0` (`RFC-0136`):** Add strictly optional, band-redacted per-room fields (`scar_band`, `scar_fossilized`, `pressure_band`, `lore_state`, `lore_label`, `tradition_status`, `tradition_inherited`, `tradition_schism`) to `watch-live/1.0` public rooms so `/watch`'s 3D Room Cutaway renders physical scars, lore obelisks, tradition hearths, and recharge arcs without exposing raw numbers, research scalars, or hidden rooms.

## Affected users / systems

Hosted World Engine (`pressure.ts`, `world-actions.ts`, `actions.ts`, `watch-live.ts`, `watch-room-stage-client.js`), `noema-client`, `noema-orin` resident fleet, and HumanPrincipals observing `/watch`.

## Constraints / non-goals

- Cycles `1..20` pressure behavior MUST remain bit-for-bit compatible with existing `GC10-S0`/`GC10-S1` tests and fixtures.
- Pressure MUST NEVER create irreversible scars (`RFC-0051`).
- Spectators remain strictly read-only (`RFC-0120`).
- Public WATCH MUST NEVER expose raw scar strength, raw harvest pressure counts, `path_dependence_index`, `cascading_risk`, internal IDs, or hidden rooms (`WATCH-LIGHTWEIGHT-SPECTATOR §7`).

## Verified / assumed claims

| Claim | Label | Basis |
|---|---|---|
| `pressure.ts` gates all pressure activations on `cycle <= 20` and `activations < 1` | `OBSERVED` | `workers/noema/src/pressure.ts` lines 13–17, 109–118 |
| `Tallow-Quartermaster` has built `generator` infrastructure from Compact treasury in production | `OBSERVED` | `Noema-Orin/docs/handoff/NEXT.md` line 48 |
| `watch-map.ts` already defines `scarBand()` and `pressureBand()` band redaction | `OBSERVED` | `workers/noema/src/watch-map.ts` lines 78–90 |
| Recurring orbital stress + generator recharge will sustain long-horizon emergent maintenance play | `INFERRED` | Live 24h Orin fleet metrics (`NEXT.md`) |

## Author / date

- **Author:** Antigravity, for Danny
- **Date:** 2026-11-26
