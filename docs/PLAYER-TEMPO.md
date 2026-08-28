# Player Tempo

**Review-stage authority.** Candidate first-world contract for separating Agent Player admission speed from canonical simulation time and human observation time. RFC: [RFC-0128](../rfcs/RFC-0128-player-tempo-and-cycle-admission.md). Proposed machine pin: [`player-tempo/1.0`](../specs/player-tempo-catalog.1.0.json). Runtime implementation and RFC acceptance remain separate.

This document defines the behavior implementers and product surfaces share. It does not add Player verbs or weaken settlement.

## Governing rule

> Players may compute without limit outside NOEMA; NOEMA admits at most one distinct mutating action per active Player per canonical cycle.

| Concern | Clock or control |
|---|---|
| World consequences | integer `World.cycle` and ledger `sequence` |
| Player fairness | server-owned per-cycle action slot |
| Human comprehension | post-commit presentation hold |
| Endpoint safety | Gateway rate limit |
| Controller safety | optional local harness cooldown |

Only the first three are gameplay timing. Rate limits and client cooldowns do not replace admission.

## State machine

```text
COLLECT
  -> freeze accepted set
RESOLVE
  -> atomic canonical commit
PRESENT
  -> minimum observation hold
COLLECT
```

`PAUSED` is a World status. It is not another phase.

## First-world policy

```text
policy_version: player-tempo/1.0
mode: OBSERVED_LIVE
collect_window_ms: 20000
presentation_hold_ms: 10000
max_mutating_actions_per_player_per_cycle: 1
empty_window_advances: false
surplus_action_policy: REJECT
```

The exact timer values are versioned configuration. They are not reducer inputs.

## Action-slot behavior

1. The World coordinator opens cycle `N` from the last committed head and freezes the active participant IDs.
2. Each participant can fill one slot with one accepted mutating action.
3. Exact idempotent retries return the original acceptance/result.
4. A distinct second mutation returns `ACTION_SLOT_FILLED`.
5. During RESOLVE or PRESENT, a mutation returns `PACE_LIMITED`.
6. Submitted action bodies stay private until canonical consequences are projected after commit.
7. Missing actions are absent. NOEMA does not manufacture WAIT.
8. An empty collection window does not advance the cycle.

Passive session health and delivery acknowledgement do not fill a slot. An action that consumes a Player budget, changes canonical state, or may emit a World Event does fill it. Therefore LOOK and INSPECT remain actions, even when their consequences are private.

## Freeze and resolution

In `OBSERVED_LIVE`, freeze on participant quorum or the collection deadline when at least one action exists. In `FAST_TEST`, freeze on quorum or explicit batch close. In `STEP_TEST`, freeze only on explicit step.

Every frozen set uses the Scheduler order:

```text
(action_priority ASC, agent_id ASC, client_action_sequence ASC, action_id ASC)
```

Arrival time and hardware speed never enter this order.

## Presentation

The committed state becomes canonical before presentation begins. PRESENT only closes mutation admission and gives WATCH, Admin Live, and Controllers time to consume the committed batch.

WATCH and Admin Live may animate events in ledger order. They must display the canonical cycle/sequence and must not imply that animation timing is settlement timing.

## Modes and containment

| Mode | Allowed world | Delay |
|---|---|---|
| `OBSERVED_LIVE` | ordinary/live, including production | configured collect + present |
| `FAST_TEST` | isolated test only | zero minimum |
| `STEP_TEST` | isolated test only | explicit operator step |

Production and the configured default world MUST refuse fast and step modes. Test speed bypasses holds only; it never bypasses authorization, action contracts, budgets, deterministic ordering, settlement, projections, or replay.

## Operator model

Admin read operations and incident containment remain immediate. Canonical interventions queue for a boundary unless a declared recovery path requires PAUSED state. Mode changes are boundary-applied, reasoned, and audited. Admin never receives a Player slot.

## Client model

The official client and headless harness SHOULD:

- observe after each committed action;
- deliberate during PRESENT;
- submit once during COLLECT;
- honor `retry_after_ms` without busy polling;
- retain idempotency on transport retry; and
- stop on unknown policy or phase.

Local cooldown remains defense in depth. The server is final authority.

## Replay boundary

Replay consumes the persisted accepted action set and canonical order. It never sleeps, replays timer wakes, or recalculates which action met a historical deadline. Tempo timestamps are operational provenance.

## Surface requirements

| Surface | Required projection |
|---|---|
| Controller response | cycle, phase, slot/pacing failure, retry guidance when computable |
| WATCH | every public committed batch before the next live collection opens |
| Admin Live | policy, mode, phase, deadline/step state, slot counts, hold remaining |
| Runtime manifest | `player_tempo_policy_version` and mode |
| Research export | tempo policy and mode when behavior may depend on cadence |

Conformance: [PLAYER-TEMPO-CONFORMANCE.md](PLAYER-TEMPO-CONFORMANCE.md).
