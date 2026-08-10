# Scheduler and Cycle Model (v0.1)

Normative deterministic ordering for the Chamber. Wall-clock time is provenance only.

## Definitions

| Term | Meaning |
|------|---------|
| `cycle` | Canonical simulation clock (integer ≥ 0). Only world time. |
| `tick` | Implementation wake; MUST NOT advance world time by itself |
| `sequence` | Monotonic event order within the world ledger |
| accepted action | Passed authz, schema, budget reserve, and entered the cycle freeze set |
| external input | Declared seed stream or operator injection recorded before freeze |

## Cycle pipeline (normative)

Matches [WORLD-ENGINE.md](WORLD-ENGINE.md) reduce order:

```text
1. authenticate, authorize, schema-validate, deduplicate (idempotency_key)
2. freeze accepted action set for this cycle
3. sort accepted actions by deterministic order key
4. reserve budgets
5. reduce actions in order (movement, local, communication, trade, org, harvest/repair)
6. apply World Event Director + infrastructure/resource processes
7. append contiguous World Events (sequence++)
8. derive observations + spectator projections (no state mutation)
9. message delivery phase (MESSAGE_DELIVERED events)
10. commit world_state; snapshot if cycle % snapshot_interval == 0
```

## Deterministic action order key

Within a frozen cycle, accepted actions sort by:

```text
(server_receive_sequence, agent_id ASC, action_id ASC)
```

| Field | Definition |
|-------|------------|
| `server_receive_sequence` | Monotonic counter assigned at gateway accept time **before** freeze; stable in ledger provenance; independent of wall-clock ties |
| `agent_id` | Lexicographic ascending |
| `action_id` | Lexicographic ascending |

If two actions share the same `server_receive_sequence` (bug), `agent_id` then `action_id` break ties. Implementations MUST persist `server_receive_sequence` on the action accept record for replay.

Replay reconstructs order from ledger event order for already-committed cycles. Re-executing from seeds MUST assign the same receive sequences as recorded in fixtures.

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
2. Delivery phase emits `MESSAGE_DELIVERED` with `delivered_cycle = current cycle` if recipient still active.
3. If recipient offline, message remains `QUEUED`; deliver on next cycle when active (no ledger rewrite).
4. Retry of client delivery MUST NOT create a second `MESSAGE` event.

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
