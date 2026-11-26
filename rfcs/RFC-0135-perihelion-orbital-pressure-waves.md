# RFC-0135: Perihelion Orbital Pressure Waves (Recurring Exogenous Pressure Past Cycle 20)

## Status

**Accepted**

Owner approval: Danny, in chat, 2026-11-25 (`orin_deeptime_mechanics_plan.md`).

This RFC extends [RFC-0027](RFC-0027-additional-world-pressure.md) (`GC10-S1`) strictly for cycles `> 20`. Cycles `1..20` keep exact `GC10-S0` / `GC10-S1` semantics unchanged. All boundaries of [RFC-0051](RFC-0051-irreversible-scar.md) remain in force: exogenous pressure NEVER creates irreversible scars.

## Problem

`pressure.ts` currently hard-stops all three exogenous pressure classes (`infrastructure_failure`, `resource_scarcity`, `access_restriction`) at `LAST_WINDOW_CYCLE = 20` with `MAX_ACTIVATIONS_1_20 = 1`. Once a persistent hosted world passes cycle 20, exogenous environmental stress ceases forever, starving maintenance traditions (`culture.ts`), `ORG_EMERGENCY_*` scopes, and `defensive_work` infrastructure of ongoing purpose.

## Decisions

### 1. Deterministic 60-Cycle Perihelion Surge Cadence (Cycles > 20)

1. For cycles `1..20`, existing `GC10-S1` rules apply unchanged:
   - `infrastructure_failure`: first cycle 4, max 1 activation in cycles `1..20`.
   - `resource_scarcity`: first cycle 8, max 1 activation in cycles `1..20`.
   - `access_restriction`: first cycle 12, max 1 activation in cycles `1..20`.
2. For cycles `> 20`, define deterministic **Perihelion Orbital Epochs** of length `ORBITAL_PERIOD_CYCLES = 60` (`epoch = Math.floor((cycle - 1) / 60)`, starting at `epoch >= 1` for cycles `>= 61`; plus a mild first post-seed wave in cycles `41..52` or aligned to `cycle % 60` window):
   - Specifically, define `ORBITAL_PERIOD_CYCLES = 60` with an active **Perihelion Surge window** at offsets `0..11` inside each wave starting at cycle `60`:
     - Wave `k` (`k = 1, 2, 3, ...`) spans cycles `[60 * k, 60 * k + 11]`:
       - `infrastructure_failure`: eligible at offset `>= 0` (`cycle >= 60 * k`), at most 1 activation per wave (`last_cycle < 60 * k`).
       - `resource_scarcity`: eligible at offset `>= 4` (`cycle >= 60 * k + 4`), at most 1 activation per wave (`last_cycle < 60 * k`).
       - `access_restriction`: eligible at offset `>= 8` (`cycle >= 60 * k + 8`), at most 1 activation per wave (`last_cycle < 60 * k`).
3. **Bounded Mildness & Safety Floors:**
   - `infrastructure_failure`: condition delta remains `CONDITION_DELTA = 15` (reduced to `Math.ceil(15 / 2) = 8` when the target relay's room contains a ready `defensive_work`!), strictly gated by `after >= MIN_CONDITION_AFTER` (`25`).
   - `resource_scarcity`: stock delta remains `STOCK_DELTA = 4`, strictly gated by `stock >= MIN_STOCK_BEFORE` (`4`).
   - `access_restriction`: duration remains `ACCESS_DURATION_CYCLES = 4`, targeting a public exit; rooms containing a ready `route_link` are deprioritized behind unprotected exits.
   - Pressure NEVER creates an irreversible scar (`scar: true`) and NEVER destroys an entity (`condition` stays `>= 25`).
4. **Public WATCH Pulse:**
   - Reuses existing `WATCH_INFRA_PULSE`, `WATCH_RESOURCE_PULSE`, and `WATCH_ACCESS_PULSE` (plus optional `"Perihelion surge stresses the Reach's relays."` on wave onset), keeping `PLAY` free of internal WED/research terminology.

## Security, Determinism & Replay Invariants

1. **Pure determinism:** Wave activation depends solely on `(cycle, class_activations, last_by_class)` and deterministic entity sorting — zero wall-clock or nondeterministic randomness.
2. **Backward compatibility:** Existing `GC10-S0`/`GC10-S1` cycle `1..20` test vectors remain bit-for-bit identical.
3. **No admin spawn or hidden room leakage:** Exogenous waves only touch already-public rooms and public relays/nodes/exits (`!room.hidden`).

## Rollback

Revert `classDue()` in `pressure.ts` to gate strictly on `cycle <= LAST_WINDOW_CYCLE`. Persisted `PressureState` fields remain schema-compatible.
