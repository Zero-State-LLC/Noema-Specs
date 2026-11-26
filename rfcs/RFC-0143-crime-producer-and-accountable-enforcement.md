# RFC-0143: Deterministic `CRIME_DETECTED` Producer, Forensic `INVESTIGATE`, Accountable Institutional `SANCTION`, and Severity-Scaled Rehabilitation

## Status

**Accepted**

Owner approval: Danny, 2026-11-26.  
Intent: [2026-11-26-items-shops-barter-orin-and-stubs](../intent/2026-11-26-items-shops-barter-orin-and-stubs.md). Spec: [items-shops-barter-and-orin](../specify/items-shops-barter-and-orin.md).  
Machine contract: [`crime-enforcement-catalog.0.1.json`](../specs/crime-enforcement-catalog.0.1.json).

Supersedes draft proposals `RFC-PROPOSAL-CRIME-PRODUCER-COMPLETION`, `RFC-PROPOSAL-GC7-CRIME-EVIDENCE-ALGORITHM`, `RFC-PROPOSAL-GC7-CRIME-DETECTION-SANCTION`, `RFC-PROPOSAL-GC7-CRIME-ENFORCEMENT`, and `RFC-PROPOSAL-GC7-CRIME-REHABILITATION`, building on Accepted [RFC-0002](RFC-0002-strategic-contestation-and-crime-events.md), [RFC-0036](RFC-0036-decay-rehab.md), and [RFC-0129](RFC-0129-crime-detected-payload-reconciliation.md) while keeping `event-catalog/0.2` (32 types) and historical dated snapshot `SPEC-GAP-REGISTER-2026-08-25.md` intact.

## Problem

1. `CRIME_DETECTED` is schema-pinned in [`event-types.0.2.json`](../specs/event-types.0.2.json) and consumed by `social-memory.ts`, but has **no runtime producer**; `detection_base_millipoints` and `sensor_min_condition` (`50`) in [`contest-config.v02.json`](../specs/contest-config.v02.json) have no normative function.
2. Detection and sanction were conflated, institutional enforcement had no payer or jurisdiction, and rehabilitation required a flat `3` trades regardless of `MINOR` / `MODERATE` / `MAJOR` severity.

## Decisions

### 1. Deterministic Seeded Detection Producer (`crime-enforcement-catalog/0.1`)

1. **Eligible Incident Triggers:** Evaluated on `CONTEST_RESOLVED` (`outcome` in `{"SUCCESS", "PARTIAL_SUCCESS"}`) for:
   - `RESOURCE_SEIZURE` -> `category: "SEIZURE"`, `severity: "MAJOR"` if an item was seized or target is a `barter_stall`, else `"MODERATE"`.
   - `INFRASTRUCTURE_DISRUPTION` -> `category: "SABOTAGE"`, `severity: "MAJOR"` if `breach_charge` was used or `condition_after < 25`, else `"MODERATE"`.
   - `PRESENCE_PRESSURE` -> `category: "OTHER"`, `severity: "MINOR"` (`"MODERATE"` if weapon-assisted without office sanction jurisdiction).
   - Any contest declared in violation of an active `NON_AGGRESSION` agreement -> `category: "POLICY_VIOLATION"`, `severity: "MAJOR"`.
2. **Seeded Integer Detection Draw:**
   - Compute `h = SHA256(seed_stream_id || ":" || source_event_id || ":crime-detect/0.1")`, take first 4 bytes as big-endian `u32`, `draw = u32 % 1000` (`0..999`).
   - Compute integer threshold clamped to `[0, 950]`:
     `threshold_mp = min(950, detection_base_mp + weapon_sig_mp + sensor_bonus_mp + witness_bonus_mp)`
     where `sensor_bonus_mp = 250` when any operational (`!in_progress`, `!scar`) `relay` or `defensive_work` in `room_id` has `condition >= 50` (`sensor_min_condition`), and `witness_bonus_mp = 200 * min(2, witness_count)` for co-located active Agent Players other than `subject_id` (and outside `subject_id`'s `acting_for` organization).
3. **Immediate Detection vs. Forensic `CrimeResidue`:**
   - If `draw < threshold_mp`: emit `CRIME_DETECTED` immediately (`detection_method: "WITNESS"` when `witness_count > 0` else `"INFRASTRUCTURE_SENSOR"`, `visibility: "PUBLIC"`, co-extensive `"PUBLIC_HISTORY"` in `flags` per [RFC-0129](RFC-0129-crime-detected-payload-reconciliation.md), `victim_id` when identifiable).
   - If `draw >= threshold_mp`: record a room-scoped `CrimeResidue` (`expires_cycle = cycle + 12`). Any co-located Agent Player may execute `COMMIT` `operation: "INVESTIGATE"` (`cost: { attention: 2, compute: 1 }`, attention discounted by `chrono_lens` / `archive_annex`); `investigate_bonus_mp = 300` (`+250` extra when equipping `chrono_lens`, total `+550`). If `draw < min(980, threshold_mp + investigate_bonus_mp)`, emit `CRIME_DETECTED` (`detection_method: "INVESTIGATION"`, `visibility: "PUBLIC"`). Each residue can emit at most one `CRIME_DETECTED` (idempotent).

### 2. Detection vs. Sanction Separation & Accountable Enforcement (`COMMIT.SANCTION`)

1. **Detection-Only Emission:** Every `CRIME_DETECTED` event emitted by sensor, witness, or investigation sets `influence_delta: 0` and `influence_applied: 0` (satisfying `event-types.0.2.json` `maximum: 0` while honoring [RFC-0002](RFC-0002-strategic-contestation-and-crime-events.md): detection is not automatic world-administered sanction).
2. **Accountable Institutional Sanction (`COMMIT.SANCTION`):**
   - Within `16` cycles of an unsanctioned `CRIME_DETECTED` event, an occupied `GRANT_ACCESS` or `OPERATE_NAMED_ASSET` office holder of an active organization that owns/stewards infrastructure in `room_id` (or is the named `victim_id` organization) — or the harmed personal `victim_id` — may execute `COMMIT` `operation: "SANCTION"` (`detection_id`, optional `restrict_room: boolean`, optional `expel_member: boolean`):
   - **Enforcement Cost:** Authorizer (or authorizing org treasury) pays `{ influence: 2, compute: 2 }` (`{ influence: 1, compute: 2 }` when equipping `arc_lance`), debited via `BUDGET_CONSUMED`. Missing jurisdiction or insufficient enforcement budget fails closed (`FORBIDDEN` / `BUDGET_EXCEEDED`).
   - **Governed Effect:** Debits `subject_id` influence by `abs(crime_severity_defaults[severity].influence_delta)` (`MINOR: 3`, `MODERATE: 8`, `MAJOR: 15`, floored at `0`), optionally emits `ACCESS_RESTRICTED` (`scope: { kind: "ROOM", room_id }`, `mode: "DENY"`, `applies_to: "LIST"`, `agent_ids: [subject_id]`, `reason: "CRIME"`, `expires_cycle: cycle + 8`) when `ACCESS_REVIEW_ELIGIBLE` or stewarded room, and optionally emits `ORG_MEMBER_REMOVE` when `ORG_REVIEW_ELIGIBLE` and `subject_id` belongs to that organization. Each `detection_id` may be sanctioned at most once.

### 3. Severity-Scaled Rehabilitation (`social-memory-catalog/gc3-s8`)

Extending [RFC-0036](RFC-0036-decay-rehab.md), the distinct post-incident `TRADE_ACCEPTED` count (including [RFC-0140](RFC-0140-storefronts-barter-and-supersession.md) `barter_stall` `fulfill` settlements) with the harmed `victim_id` required to rehabilitate a `DangerMemoryState` edge derived from `CRIME_DETECTED` scales by highest active incident `severity`:
- `MINOR` (and non-crime contest/breach edges): `3` trades (unchanged from `RFC-0036`).
- `MODERATE`: `5` trades.
- `MAJOR`: `8` trades.

## Security, Determinism & Rollback

- Pure integer arithmetic and seeded `SHA256` draws; zero wall-clock randomness, zero rumor-as-detection, and zero duplicate witness counting.
- Rollback: disable `CRIME_DETECTED` emission, `INVESTIGATE`, and `SANCTION`, reverting `social-memory.ts` rehabilitation to flat `3`.
