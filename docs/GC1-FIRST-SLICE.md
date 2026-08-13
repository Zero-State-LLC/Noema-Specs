# GC1 First Slice — Derived Practice Projection

**Status:** Selected executable *specification* slice for later runtime. Not an executable release package.  
**Parent:** [MASTERY-SPECIALIZATION.md](MASTERY-SPECIALIZATION.md) · [GAME-COMPLETENESS-PLAN.md](GAME-COMPLETENESS-PLAN.md)  
**RFC:** [RFC-0004](../rfcs/RFC-0004-derived-mastery-projection.md) (**Draft**)  
**Does not open:** v0.8 · `event-catalog/0.3` · mechanical benefits · recognition

This document is the audit result and the slice contract. An implementation agent MUST implement **only** this slice unless a later RFC expands it.

---

## 1. Audit result

### Selected first slice

```text
GC1-S0  Derived Practice Projection
```

GC1 remains the first completeness *system*. Construction and Social Memory stay P0 specifications and do **not** precede this slice.

Why GC1 still goes first:

- Explorer / Surveyor / Broker evidence is already in `event-catalog/0.1`.
- No new verb.
- No geography mutation.
- No public recognition event.
- No mechanical benefit, so Chamber costs and contest math stay frozen.

Why Construction / Social Memory do **not** go first:

- GC2 needs a `BUILD` action-contract increment and new structure events.
- GC3 needs relationship-edge visibility rules and hidden-fact leak tests.
- Both are larger catalog or security surfaces.

### What existing events can prove

| Track | Attributable from current catalog? | Evidence |
|-------|--------------------------------------|----------|
| Explorer | **Yes** | `LOOK.payload.agent_id` + `room_id` |
| Surveyor | **Yes** | `INSPECT.payload.agent_id` + `entity_id` |
| Broker | **Yes** | `TRADE_ACCEPTED` + the open trade’s proposer/counterparty |
| Engineer | **Conditional** | Player-attributed `ENTITY_UPDATE` whose `set` contains `condition` ([DATA-MODEL.md](DATA-MODEL.md) requires `actor_id` on Player-originated events). `ENTITY_UPDATE` payload itself has **no** actor |
| Logistician | **No** (S0) | `MOVE` is too generic; lot transport is not typed |
| Diplomat / Strategist | **No** (S0) | Needs `event-catalog/0.2` and outcome quality rules |
| Archivist / Investigator | **No** (S0) | Document / contradiction joins are incomplete |
| Steward / Operator / Mediator | **No** (S0) | Need offices, World Services, or time-at-condition |

**OBSERVED:** `ENTITY_UPDATE` has no actor in payload. Attribution depends on envelope `actor_id`.  
**INFERRED:** v0.1 player-originated `condition` writes are `COMMIT.REPAIR`.  
**SPECULATIVE:** some runtimes may omit `actor_id` on follow-on updates; those events MUST NOT count.  
**NOT_COMPUTABLE:** whether Perihelion’s live ledger currently populates `actor_id` on repair follow-ons — inspect at implementation time.

### Explicitly out of this slice

```text
new verbs
new event types
recognition / MAINTAINED / LATENT
mechanical benefits (quality, cost, parameter, target, eligibility)
focus declaration
decay
teaching / certification
WATCH mastery lines
GUI affordances that appear only because of hidden proficiency
research capability scores on PLAY
universal XP
```

---

## 2. Slice contract (normative for GC1-S0)

### Identity

| Field | Value |
|-------|--------|
| Slice id | `gc1-s0` |
| Catalog id | `mastery-catalog/gc1-s0` |
| State class | **Derived only.** Rebuildable. Not WorldState. Not a reducer input |
| Replay identity | `mastery-catalog/gc1-s0` + ordered ledger + this document’s rules |

Derived practice MUST NOT be stored as authoritative world truth. A cache is allowed if and only if it rebuilds identically from the ledger.

### Closed track set

| `track_id` | Practice family | Qualifying events | Unit counted |
|------------|-----------------|-------------------|--------------|
| `track.explorer.01` | OBSERVE / MOVE | Successful `LOOK` where `payload.agent_id` is the Player | Distinct `room_id` |
| `track.surveyor.01` | OBSERVE | Successful `INSPECT` where `payload.agent_id` is the Player | Distinct `entity_id` |
| `track.broker.01` | TRADE | `TRADE_ACCEPTED` whose referenced trade lists the Player as proposer or counterparty | Distinct `trade_id` |
| `track.engineer.01` | INFRASTRUCTURE | `ENTITY_UPDATE` with envelope `actor_id` equal to the Player and `payload.set` containing key `condition` | Distinct `event_id` |

No other track is in S0. The twelve example labels in [MASTERY-SPECIALIZATION.md](MASTERY-SPECIALIZATION.md) remain examples, not this catalog.

### Counting rules

1. Walk accepted ledger events in `(cycle, sequence)` order.
2. Count each `event_id` at most once per track.
3. Successful catalog events only. `MOVE_REJECTED`, `TRADE_REJECTED`, `BUDGET_EXCEEDED`, and protocol/`FORBIDDEN` failures do not count.
4. `LOOK` / `INSPECT` events in the catalog are already successes. Do not also count `OBSERVATION_GENERATED`.
5. `TRADE_PROPOSED` does not count. Only `TRADE_ACCEPTED`.
6. If `TRADE_ACCEPTED` references a missing trade, skip (**not** an inferred success).
7. Engineer: if `actor_id` is null, missing, or a non-Player world actor, skip. Do not infer the actor from nearby `BUDGET_CONSUMED`.
8. Idempotent replay of the same event does not double-count.
9. Controller type is ignored. Human and agent Players use the same rules.

### Lifecycle in S0

```text
UNTRACKED   count == 0          → omit from PLAY
PRACTICING  count >= 1          → self projection only
```

`RECOGNIZED` and later states are **not** produced in S0 even if counts are large.

### Thresholds (pinned for S0)

| Gate | Value |
|------|-------|
| UNTRACKED → PRACTICING | `count >= 1` |
| PRACTICING → RECOGNIZED | **disabled** |
| Decay / latent | **disabled** |
| Focus | **disabled** (client preference only, not ledgered, not displayed as competence) |
| Benefit magnitudes | **disabled** (all zero) |

These pins close the S0 portion of the parent SPEC GAP. They do not close recognition or benefits for later slices.

### PLAY projection (self only)

After ordinary observation projection, the PLAY adapter MAY append at most **three** practice lines, ordered by `track_id` ascending, using only tracks in `PRACTICING`:

| `track_id` | Line |
|------------|------|
| `track.explorer.01` | `You have been learning the rooms.` |
| `track.surveyor.01` | `You have been doing survey work.` |
| `track.broker.01` | `You have been closing exchanges.` |
| `track.engineer.01` | `You have been keeping infrastructure alive.` |

Rules:

- Never print integer counts, ranks, XP, levels, or research confidence.
- Never print another Player’s practice lines.
- Never add or hide a contextual control because of practice state.
- `HELP` MUST NOT list classes or specializations as choosable.

### WATCH / STUDY / security

| Surface | S0 rule |
|---------|---------|
| WATCH | No mastery projection |
| STUDY | May record the rebuild in the research partition. MUST NOT label it a capability |
| GUI | No hidden-proficiency affordance |
| Other Players | `NOT_OBSERVABLE` |

### Failure / replay / migration

| Concern | Rule |
|---------|------|
| Failure | Missing or illegal events are skipped; rebuild continues |
| Replay | Same ledger + `mastery-catalog/gc1-s0` → same track counts and lines |
| Migration | A later catalog version MUST declare a mapping. Unmapped S0 evidence remains historical and uncounted for new tracks |
| Version | Changing a counting rule requires a new catalog id |

---

## 3. Machine contracts required later (still SPEC GAP)

Do **not** invent these in runtime. Add them only when RFC-0004 is accepted or superseded by a machine package:

```text
optional mastery-catalog JSON + schema
positive rebuild fixtures (explorer/surveyor/broker/engineer)
negative fixtures (rejected trade, missing actor_id, other-player leak)
conformance cases (recommended family prefix M01)
PLAY fixture extending examples/experience/play-view.json
```

Worked examples (non-authoritative): [examples/gc1-mastery/](../examples/gc1-mastery/).

S0 does **not** require:

```text
action-contracts version change
event-catalog version change
world-state schema change
protocol change
```

---

## 4. Runtime audit (reference implementation, read-only)

Inspected `Zero-State-LLC/Noema`. No runtime code was changed.

There are **two runtimes**. Do not assume they share a ledger or payload shape.

| Runtime | Role | Ledger? |
|---------|------|---------|
| Hosted Worker + `NoemaWorldDO` | Live PLAY | **No.** Snapshot at DO key `"world"`; `digest_events` last 2000 (operator); optional Supabase `noema_settled_events` |
| Python `src/noema` | v0.1 fixture / replay reference | **Yes.** Digest-chained `events` table |

### Hosted findings

| Finding | Label | Note |
|---------|-------|------|
| Apply path | OBSERVED | `POST /v1/command` → `NoemaWorldDO.applyCommand` → `applyWorldCommand` (`world-actions.ts`) |
| PLAY projection | OBSERVED | `buildObservation()` → `play.ts` `renderObs` / `statusFromObservation` |
| `PlayerRuntime` | OBSERVED | `room_id`, `entered`, `budgets`, `handle`, session, `last_seen_ms`, `actor_kind`. No practice fields |
| `pushEvent` | OBSERVED | `{event_id, event_type, sequence, payload}` only. No envelope `actor_id` |
| Hosted `ENTITY_UPDATE` | OBSERVED | `{entity_id, field, from, to, operation}` — **not** catalog `{entity_id, set, unset}` |
| Hosted `BUDGET_CONSUMED` | OBSERVED | `{player_id, cost_paid, reason}` — **not** catalog `{agent_id, resource, amount, action_id, remaining}` |
| `LOOK` vs `OBSERVE` | OBSERVED | Only `LOOK` emits events and spends attention. `OBSERVE` is free and silent. S0 counts `LOOK` only |
| Failures | OBSERVED | `fail(...)` emits no events. Idempotent replay returns the cached result **before** `pushEvent` |
| `unsettled` | OBSERVED | Declared on `WorldRuntime` and **never written** |
| `digest_events` | OBSERVED | Last 2000, operator-only. **Forbidden** as mastery source |
| Settlement row | OBSERVED | `settleEvent` stamps `player_id` on the Postgres row even when the payload lacks it |
| `ensurePlayer` inside `buildObservation` | OBSERVED | Refreshes `last_seen_ms`. Practice updates MUST stay on the **mutate** path so observe-only calls invent no practice |
| Contests | OBSERVED | Not hosted. S0 must not wait on v0.2 verbs |
| WATCH | OBSERVED | `redactedPublicWorld` has no player practice. Keep it that way |
| Python `acceptance_projection` | INFERRED | Adding practice there would break v0.1 fixture digests unless excluded |

### Hosted-runtime implication

```text
normative S0 identity     = rebuild from a complete catalog ledger
hosted Worker today       = snapshot + truncated digest + optional settlement
first runtime increment   = incremental derived counters on PlayerRuntime
                             updated only after a successful pushEvent batch
                             projected only from buildObservation (self)
forbidden                 = digest_events, deriveAffordances, HELP, WATCH,
                             operator digests, Python fixture digests
forbidden                 = changing REPAIR/TRADE costs
forbidden                 = treating the cache as canonical world truth
```

Suggested later hook order (non-normative):

1. Pure mapper over the successful event batch (hosted adapter: `LOOK`, `INSPECT`, `TRADE_ACCEPTED`, `ENTITY_UPDATE` + `operation: "REPAIR"`).
2. Merge onto optional `PlayerRuntime` derived fields in `applyWorldCommand` after events, before `success()`.
3. `buildObservation` attaches pinned self-only lines. Never on `players_here`, `affordances`, or WATCH.
4. Chamber STATUS may show those lines. No integers.

When a complete ledger exists, rebuild MUST match the incremental cache for the same events. Historical hosted play from before the cache is **NOT_COMPUTABLE** from the DO snapshot.

A runtime adapter MAY map hosted `operation: "REPAIR"` onto `track.engineer.01`. That mapping is an adapter concern. It does not change the catalog payload contract and MUST NOT invent a new event type.

Do **not** count hosted `HARVEST` as Engineer, and do **not** add Logistician in S0. Ignore `OBSERVATION_GENERATED`, `BUDGET_CONSUMED`, and `RESOURCE_TRANSFER` to avoid double-counting.

---

## 5. Acceptance for S0 (narrower than scenario A)

Scenario A in the completeness plan includes recognition and a world-native benefit. **S0 does not satisfy full scenario A.**

S0 acceptance:

1. A Player with no class performs `LOOK` in two rooms, `INSPECT` on two entities, and is party to one accepted trade.
2. Their PLAY view shows the matching practice lines and no numbers.
3. Another Player looking at them does not see those lines.
4. WATCH does not show them.
5. Repair/harvest/trade costs are unchanged.
6. Replay of the same ledger reproduces the same lines.
7. A `TRADE_REJECTED` does not create broker practice.

Full scenario A waits for a later GC1-S1 (recognition + one benefit family) with its own RFC.

---

## 6. Recommended next implementation work

**One bounded slice:** implement GC1-S0 as derived PLAY projection in the runtime, with fixtures added to Specs when RFC-0004 is accepted.

Do not implement GC2–GC10. Do not grant Engineer cost discounts. Do not add `BUILD`.
