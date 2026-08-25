# Scheduler and Cycle Model (v0.1)

Normative deterministic ordering for the Chamber. Wall-clock time is provenance only.

**Review-stage compatibility note.** [RFC-0128](../rfcs/RFC-0128-player-tempo-and-cycle-admission.md) proposes a version-pinned admission phase around this unchanged canonical pipeline. Until that RFC is Accepted and implemented, RFC-0019 WAIT quorum remains the hosted cycle trigger. The proposal does not change the order key, reducer inputs, settlement, or replay in this document.

## Definitions

| Term | Meaning |
|------|---------|
| `cycle` | Canonical simulation clock (integer ≥ 0). Only world time. |
| `tick` | Implementation wake; MUST NOT advance world time by itself |
| `sequence` | Monotonic event order within the world ledger |
| accepted action | Passed authz, schema, budget reserve, and entered the cycle freeze set |
| `action_priority` | Versioned world-rules integer assigned by the server from the action contract; lower values resolve first |
| `client_action_sequence` | Client-supplied monotonically increasing integer scoped to `(world_id, agent_id, session_epoch)`; required on accepted mutating actions |
| external input | Declared seed stream or operator injection recorded before freeze |

## Cycle pipeline (normative)

Matches [WORLD-ENGINE.md](WORLD-ENGINE.md) reduce order:

```text
1. authenticate, authorize, schema-validate, deduplicate (`idempotency_key`), and validate `client_action_sequence`
2. freeze the accepted action set for this cycle
3. assign versioned server-side `action_priority` and sort by the canonical order key
4. reserve budgets
5. reduce actions in order (movement, local, communication, trade, org, harvest/repair)
6. apply World Event Director + infrastructure/resource processes
7. emit deterministic `MESSAGE_DELIVERED` events for eligible queued messages
8. append the contiguous cycle event batch and atomically commit `world_state`
9. derive observations + spectator projections from the committed post-delivery state (no state mutation)
10. snapshot if `cycle % snapshot_interval == 0`
```

## Deterministic action order key

Within a frozen cycle, accepted actions sort by:

```text
(action_priority ASC, agent_id ASC, client_action_sequence ASC, action_id ASC)
```

| Field | Definition |
|-------|------------|
| `action_priority` | Integer assigned from the pinned world-rules verb/operation priority table; clients cannot choose it |
| `agent_id` | Typed stable agent ID, lexicographic ascending |
| `client_action_sequence` | Monotonic integer scoped to `(world_id, agent_id, session_epoch)` |
| `action_id` | Typed stable action ID, lexicographic ascending final tie-breaker |

Gateway arrival order, wall-clock time, socket scheduling, and network latency MUST NOT participate in canonical resolution. A stale or reused `client_action_sequence` with a new idempotency key is `CONFLICT`; an exact idempotent retry returns the original result. The complete key and session epoch MUST be retained in action provenance.

Replay reconstructs committed order from ledger order. Re-execution from accepted actions sorts the recorded canonical keys and MUST produce the same event order regardless of recorded receive timestamps.

## Same-cycle concurrency

| Case | Rule |
|------|------|
| Different agents, different resources | both apply in order |
| Different agents, same resource node harvest | first in order wins stock; later may `BUDGET_EXCEEDED` / insufficient node stock → reject without partial debit |
| Trade open + transfer | reservations prevent double spend |
| MOVE vs capacity | first mover occupies; later may `MOVE_REJECTED` CAPACITY_EXCEEDED |
| Duplicate `idempotency_key` | return original result; no second charge |
| Duplicate `action_id` different key | reject second as `CONFLICT` |

## Message delivery

1. `MESSAGE` creates `QUEUED` record in reduce phase.
2. Before the cycle batch commits, the delivery phase emits `MESSAGE_DELIVERED` with `delivered_cycle = current cycle` if the recipient is active.
3. The event and resulting inbox state commit in the same contiguous cycle batch before observation projection; an authorized post-cycle observation may therefore include the message.
4. If the recipient is offline, the message remains `QUEUED`; delivery is reconsidered in the next cycle without rewriting history.
5. Retrying transport notification or protocol redelivery MUST NOT create a second `MESSAGE` or `MESSAGE_DELIVERED` event.

## World Event Director timing

Runs in phase 6 only. Inputs: `world_seed`, `cycle`, named stream `world_event_director.v1`, declared schedule table ([resource-economy.v01.json](../specs/resource-economy.v01.json) `world_event_director`).

MUST NOT choose outcomes to induce a research capability in an agent.

## Snapshots

Default `NOEMA_SNAPSHOT_INTERVAL=100` cycles. Genesis snapshot at cycle 0. Snapshot head recorded in runtime manifest.

## Reconnect / timeout

| Event | World effect |
|-------|----------------|
| Client disconnect | no rollback; undelivered observations redeliver |
| Action timeout before accept | no ledger entry |
| Action accepted then client gone | still reduces |
| Resume | AUTH + last acked observation/sequence; no cycle rewind |

## External inputs

Only:

- world seed / seed streams
- declared operator injections (ledgered as events, e.g. `SITUATION_INJECTED`)
- accepted authenticated agent actions

Undeclared wall-clock or network jitter MUST NOT change reduce results.

## Conformance

**C23** — Deterministic Scheduler Conflicts.

Replay order, unknown-stream hard-fail, and golden-trajectory requirements: [ADR-008](../adr/ADR-008-replay-conformance-and-deterministic-hardening.md).
