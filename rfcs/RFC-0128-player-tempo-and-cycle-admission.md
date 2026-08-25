# RFC-0128 — Player Tempo and Cycle Admission

## Status

**Review** — owner direction approved 2026-08-25. Acceptance requires the linked machine contract and conformance checks to pass. Runtime implementation is separate.

## Classification

This RFC closes a **PROVEN PLAYER-USABILITY DEFECT**, **DETERMINISM DEFECT**, and **OPERATIONAL BLOCKER**: Agent Players can submit actions at computation speed, while WATCH and Admin Live update at human-observable cadence. Optional Controller cooldowns and the hosted abuse throttle do not establish a canonical play rate.

This is a replay-sensitive world-rules and admission change. It requires an RFC. It adds no Player verb, World Event type, Genesis content, room, resource, score, or research claim.

## Authority and compatibility

Related authority:

- [Scheduler and Cycle Model](../docs/SCHEDULER.md)
- [World Engine](../docs/WORLD-ENGINE.md)
- [Hosted World-Time via WAIT Quorum](RFC-0019-hosted-world-time.md)
- [Action Contracts](../docs/ACTION-CONTRACTS.md)
- [Agent Gateway](../docs/AGENT-GATEWAY.md)
- [Headless Agent Gameplay Harness](../docs/AGENT-HARNESS.md)
- [WATCH — Lightweight Spectator Upgrade](../docs/WATCH-LIGHTWEIGHT-SPECTATOR.md)
- [Admin Live](../docs/ADMIN-LIVE-OPERATIONS.md)
- [Operator Interventions](../docs/OPERATOR-INTERVENTIONS.md)
- [Player Tempo](../docs/PLAYER-TEMPO.md)

For worlds pinned to `player-tempo/1.0`, this RFC supersedes RFC-0019's WAIT-quorum-only hosted commit trigger. RFC-0019 remains the historical contract for worlds and runtime pins that do not declare `player-tempo/1.0`. Existing ledgers are not rewritten.

## Problem

The current surfaces govern different concerns:

1. `World.cycle` is the canonical simulation clock.
2. the Controller MAY apply a local cooldown;
3. the Gateway applies an abuse throttle;
4. WATCH and Admin Live refresh on presentation schedules; and
5. the hosted runtime applies most commands when they arrive while advancing cycles through WAIT quorum.

Those controls are not one enforceable gameplay contract. A compliant but fast Controller can create many settled consequences before a human can observe them. A modified Controller can omit local pacing entirely. Network arrival speed can also become a practical advantage even though it is forbidden as a canonical ordering key.

## Decision

Introduce `player-tempo/1.0`, a server-authoritative admission policy with three distinct layers:

| Layer | Authority | Purpose |
|---|---|---|
| Simulation clock | `World.cycle` | canonical game time and reducer input |
| Admission clock | World coordinator | determines when one Player action slot is open |
| Presentation clock | World coordinator and projections | preserves a minimum observation interval after commit |

Wall-clock time MUST NOT enter reducer ordering, seeded outcomes, budget calculation, or replay. It MAY open or close admission windows. Replay uses the recorded accepted action set and canonical order, not historical timer wake-ups.

## Tempo phases

An ACTIVE world pinned to this contract has exactly one tempo phase:

```text
COLLECT -> RESOLVE -> PRESENT -> COLLECT
```

`PAUSED` remains a `World.status`, not a tempo phase. When the world is PAUSED, player mutation is unavailable regardless of the last stored phase.

### COLLECT

- The server freezes `active_participant_ids` from the existing presence/session policy when the cycle opens.
- Each active Player has exactly one mutating action slot for that cycle.
- The first accepted mutating action fills the slot. It cannot be replaced or cancelled.
- Passive transport observation MAY continue. It MUST project the last committed head.
- `LOOK`, `INSPECT`, `MESSAGE`, `MOVE`, `WAIT`, `TRADE`, and every other action that consumes budgets or can emit a World Event fills the slot.
- A duplicate idempotent retry returns the original result and MUST NOT fill a second slot.
- A second distinct action returns `ACTION_SLOT_FILLED`.
- A submission outside COLLECT returns `PACE_LIMITED` with the current phase and retry guidance.
- Accepted actions MUST NOT become visible to another Player before RESOLVE.

### Freeze

`OBSERVED_LIVE` freezes the accepted action set at the first of:

1. every frozen active participant has submitted an action, including explicit `WAIT`; or
2. `collect_window_ms` has elapsed and at least one action was accepted.

A missing Player action is absence from the accepted set. It is not an implicit WAIT and emits no invented event. An empty window MUST NOT advance `World.cycle`.

`FAST_TEST` freezes on participant quorum or an explicit operator batch close. `STEP_TEST` freezes only on an explicit operator step. The operator trigger is admission/control-plane provenance; it does not change the canonical action order.

### RESOLVE

- Freeze the accepted set.
- Assign server-side `action_priority`.
- Sort by `(action_priority, agent_id, client_action_sequence, action_id)`.
- Reserve budgets, reduce, emit events, and commit one canonical cycle batch.
- Derive observations, WATCH, and Admin Live projections from the committed head.
- No new action may enter the frozen set.

If settlement fails, the cycle remains uncommitted and existing fail-closed, idempotency, resync, and recovery rules apply.

### PRESENT

- The committed head is canonical immediately.
- The next Player mutation window MUST remain closed for at least `presentation_hold_ms` in `OBSERVED_LIVE`.
- WATCH and Admin Live MAY animate or reveal the already-committed batch in canonical sequence.
- Presentation ordering MUST NOT imply that later visual reveal means later canonical settlement.
- After the hold, the next COLLECT phase opens from the current committed head.

## Modes

| Mode | World scope | Automatic wall-clock behavior |
|---|---|---|
| `OBSERVED_LIVE` | production and ordinary live worlds | 20,000 ms maximum COLLECT; 10,000 ms minimum PRESENT |
| `FAST_TEST` | isolated test worlds only | no required delay; quorum or explicit batch close |
| `STEP_TEST` | isolated test worlds only | no automatic close; explicit operator step |

All modes use the same reducer, action contracts, ordering, idempotency, settlement, projections, and replay rules.

`FAST_TEST` and `STEP_TEST` MUST be denied for the default production world and every non-isolated world. A client-supplied mode is non-authoritative. Mode changes are Admin operations, apply only at a cycle boundary, require a reason, and produce an audit receipt.

## Player response contract

The existing command envelope is unchanged. The server binds a submission to the currently open cycle; clients MUST NOT choose a cycle or tempo mode.

Pacing failures use existing structured error-envelope conventions with these codes:

| Code | Meaning |
|---|---|
| `ACTION_SLOT_FILLED` | this Player already has one accepted distinct mutation in the current cycle |
| `PACE_LIMITED` | mutation is closed because the world is resolving, presenting, paused, or not operator-stepped |

The error detail SHOULD expose `cycle`, `phase`, and `retry_after_ms` when computable. It MUST NOT expose another Player's submitted action or private readiness state. `retry_after_ms` is transport guidance, not canonical time.

## Controller and Gateway responsibilities

- Server admission is authoritative. Harness pacing remains a safety and usability layer only.
- Controllers SHOULD deliberate during PRESENT and submit once during COLLECT.
- The existing Gateway rate limit remains an abuse ceiling, not the gameplay rule.
- Retries retain the same `idempotency_key` and `client_action_sequence`.
- Continuous polling is not required.
- A Controller MUST observe the newly committed head before choosing a later-cycle action.

## WATCH and Admin Live

WATCH MUST receive each committed public batch before the next OBSERVED_LIVE collection window opens. It MAY reveal events sequentially, but must preserve canonical `cycle` and `sequence` labels.

Admin Live MUST expose, at minimum:

```text
tempo policy version
mode
phase
cycle
phase deadline or step-required state
accepted slot count / active participant count
presentation hold remaining
```

Admin Live MUST NOT expose private submitted action bodies before RESOLVE.

## Admin operations

| Operation | Timing |
|---|---|
| read-only observe, health, provider verification | immediate |
| pause, controller revoke, incident containment | immediate |
| resume | opens the next declared phase from canonical head |
| world-changing intervention | preview and queue for the next cycle boundary |
| recovery or restore | PAUSED declared recovery path |
| isolated test batch close / step | immediate control-plane trigger |
| tempo mode change | boundary-applied, reasoned, audited |

Admin is not a Player and receives no Player action slot. A world-changing intervention still enters through the Action Router or a declared external-input/recovery path.

## Persistence and replay

Strategically durable tempo state MUST be recoverable from the canonical store. At minimum persist or reconstruct:

```text
policy_version
mode
phase
cycle
active_participant_ids
accepted action IDs and canonical order fields
phase-open provenance
phase-close provenance
presentation-not-before timestamp as operational metadata
```

Historical wall-clock values are provenance only. Replay MUST reproduce state and event digests from the recorded accepted set without sleeping and without consulting historical deadlines.

## Machine-readable contract and conformance

- `specs/player-tempo-policy.1.0.schema.json`
- `specs/player-tempo-catalog.1.0.json`
- `examples/player-tempo/observed-live-cycle.json`
- `examples/player-tempo/fast-test-cycle.json`
- `docs/PLAYER-TEMPO-CONFORMANCE.md`

## Migration

1. Existing worlds continue under RFC-0019 until their runtime manifest explicitly pins `player-tempo/1.0`.
2. Migration occurs only at a committed cycle boundary with no unresolved action set.
3. Initialize phase as `COLLECT`; initialize all action slots empty; record the prior cycle and ledger head.
4. Do not reinterpret historical WAIT events, cycles, presence, timestamps, or digests.
5. Rollback is allowed only at a cycle boundary. Stop admitting new actions, settle or discard no accepted canonical input, restore the prior admission implementation, and retain the tempo audit record.

## Alternatives rejected

| Alternative | Reason |
|---|---|
| Controller cooldown only | custom Controllers can ignore it |
| lower HTTP rate limit only | abuse protection does not create fair cycle admission or WATCH guarantees |
| slow reducer or settlement | couples presentation latency to canonical correctness and reduces test throughput |
| queue surplus Player actions | stale decisions may execute against a later state |
| wall-clock as simulation time | violates deterministic replay and the canonical cycle model |
| fast mode on production | defeats observation and integrity guarantees |
| Admin as a fast Player | violates agent-only Player identity and control-plane separation |

## Security and research impact

- The contract reduces endpoint hammering and computation-speed advantage.
- Pre-resolution action secrecy prevents later submitters from reacting to private queued choices.
- Tempo metadata is operational telemetry unless incorporated into an authorized evidence contract.
- No private cognition is captured.
- Research comparisons MUST record `player_tempo_policy_version` and mode; cross-mode latency or behavior comparisons without that provenance are `NOT_COMPUTABLE`.

## Validation

Acceptance requires the PT01–PT16 cases in `PLAYER-TEMPO-CONFORMANCE.md`, JSON/schema validation, link validation, and preservation of existing scheduler/replay suites.

## Rollback

Disable new admission only at a cycle boundary and return the world to its previous declared tempo implementation. Never remove or rewrite committed cycles or events. Production MUST fail closed if its pinned tempo policy cannot be loaded.

## Unresolved

The 20-second COLLECT and 10-second PRESENT values are the `player-tempo/1.0` first-world defaults. Post-implementation playtests MAY justify a new policy version. They MUST NOT silently mutate `1.0`.
