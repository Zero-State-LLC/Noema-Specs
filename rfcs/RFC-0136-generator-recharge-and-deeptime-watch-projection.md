# RFC-0136: Generator-Powered `RECHARGE` Action and Band-Redacted Deep Time WATCH Projection

## Status

**Accepted**

Owner approval: Danny, in chat, 2026-11-25 (`orin_deeptime_mechanics_plan.md`).

This RFC adds one bounded infrastructure-coupled player verb (`RECHARGE`) and extends public `watch-live/1.0` additively with strictly band-redacted Deep Time and Culture room indicators for the Full-Screen 3D Place View ([RFC-0134](RFC-0134-watch-room-view-and-resident-visibility.md)).

## Problem

1. **Energy bottleneck & generator utility (`NEXT.md` S19):** Agents carrying cargo pay 2 energy to `MOVE` and 3 energy to `REPAIR`, while `WAIT` only yields `+2` energy per burned cargo (and rests only to 2 with an empty hold). Built `generator` infrastructure currently only passively modifies harvest production and offers no active charging loop.
2. **Deep Time & Culture invisibility on `/watch`:** `deep-time.ts` (`scars`, fossilization, `lore_attractors`) and `culture.ts` (`CUSTOM`, `TRADITION`, `DORMANT`, `REVIVED`, `INHERITED`, `SCHISM`) are invisible in `watch-live/1.0`, leaving the Full-Screen 3D Room Cutaway unable to visualize historical scars, crystallized lore, or active maintenance traditions.

## Decisions

### 1. Generator-Powered `RECHARGE` Verb

1. **Availability:** Advertised as an affordance (`action: "RECHARGE"`, `operation: "RECHARGE"`, `cmd: "recharge <entity_id>"`) whenever the player is co-located in a room with a **ready** (`!in_progress`), operational (`condition >= 25`, `!scar`) `generator` entity (`infraClassOf(e) === "generator"`).
2. **Preconditions & Cooldown:**
   - Target must be a ready `generator` in the player's current room with `condition >= 25` (`RECHARGE_MIN_GENERATOR_CONDITION = 25`).
   - Per-player cooldown: `RECHARGE_COOLDOWN_CYCLES = 3` cycles (`pl.last_recharge_cycle`). If attempted earlier, return `COOLDOWN_ACTIVE` / `FORBIDDEN` with plain copy `"You must wait before drawing power from a generator again."`.
   - Player must currently be below max energy (`energy < RECHARGE_ENERGY_CAP`, where `RECHARGE_ENERGY_CAP = 10`).
3. **Effects:**
   - Restores `+4` energy (`RECHARGE_ENERGY_GRANT = 4`), clamped at `RECHARGE_ENERGY_CAP = 10` (or leaves higher energy unchanged). Burns `0` cargo.
   - Applies gentle wear to the generator: `condition = Math.max(25, condition - 2)` (`RECHARGE_GENERATOR_WEAR = 2`), emitting an `ENTITY_UPDATE` event (`operation: "RECHARGE"`, `set: { condition }`, `actor_id: player_id`, `energy_delta`).
   - Consumes the player's normal mutating-action tempo slot (`PLAYER-TEMPO`).
4. **Public WATCH Projection:**
   - On a public generator in a public room, `ENTITY_UPDATE` with `operation: "RECHARGE"` projects into `rooms[].room_activity[]` with `verb: "recharge"`, `target_label: <generator label>`, and `kind: "deed"` (`"<actor> recharged at <generator>"` for `public_activity: true` residents; `"Power was drawn at <site>"` for non-resident actors).

### 2. Band-Redacted Deep Time & Culture Projection on `watch-live/1.0`

Each public room in `watch-live/1.0` (`rooms[]`) MAY carry the following optional, strictly additive, band-redacted fields:
- `scar_band?: "faint" | "marked" | "deep"` — derived exclusively from `publicScarsForRoom()` using the same `scarBand()` thresholds as `watch-map/1.0` (`< 0.05` omitted, `< 0.2` `"faint"`, `< 0.6` `"marked"`, `>= 0.6` `"deep"`).
- `scar_fossilized?: boolean` — `true` only when at least one public scar in that room has `fossilized === true`.
- `pressure_band?: "low" | "moderate" | "high"` — derived via `pressureBand()` (`<= 5` `"low"`, `<= 15` `"moderate"`, `> 15` `"high"`, `<= 0` omitted).
- `lore_state?: "forming" | "crystallized"` and `lore_label?: string` — derived from the highest-weight `lore_attractor` scoped to that public room (sanitized through internal-ID redaction, max 48 chars).
- `tradition_status?: "CUSTOM" | "TRADITION" | "DORMANT" | "REVIVED"` — highest-tier maintenance culture state among public entities in that room (`culture.ts`).
- `tradition_inherited?: boolean` and `tradition_schism?: boolean` — derived from `siteMarks()` on a live tradition (`TRADITION` or `REVIVED`) in that public room.

## Security & Privacy Invariants

1. **Bands only (`WATCH-LIGHTWEIGHT-SPECTATOR §7`):** Raw scar strengths, raw harvest pressure counts, `path_dependence_index`, `cascading_risk`, `image_score`, and `evidence_fragments` counts MUST NEVER appear on `watch-live/1.0`.
2. **Hidden room & entity isolation:** Hidden rooms, hidden entities, and non-public scars (`visibility !== "public"`) NEVER project into `rooms[]` or `room_activity[]`.
3. **Zero ID leaks:** `lore_label` and `target_label` pass the internal-ID redaction filter (`player.*`, `room.*`, `entity.*`, `org.*`, etc.).
4. **Backward compatibility:** `watch_live` remains `"watch-live/1.0"`; all added fields are strictly optional.

## Rollback

Remove `RECHARGE` affordance advertising and omit the optional Deep Time/Culture fields from `watch-live.ts`. No ledger schema migration is required.
