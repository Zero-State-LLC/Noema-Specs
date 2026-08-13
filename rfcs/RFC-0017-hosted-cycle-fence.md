# RFC-0017 — Hosted Cycle Fence and Durable Settlement Recovery

## Status

**Accepted**

Narrow architecture pin. No gameplay. No `event-catalog/0.3`. No Genesis reseed. No stack change.

## Problem

RFC-0016 stores a reconstructable world head but left SERIALIZABLE settlement, writer-fence tokens, and stale-head recovery as SPEC GAP. A last-write-wins upsert can overwrite a newer durable head.

## Proposed change

One active writer per `world_id` (`NoemaWorldDO`). Durable head gains:

```text
revision              monotonic integer
ledger_head_event_id  last settled event_id
state_digest          digest of state_json (implementation-defined, stable)
writer_generation     DO generation / fence token
```

Settlement unit (hosted):

```text
expected_revision == durable.revision
  → write events (idempotent on event_id)
  → write head at revision+1 with new digest and ledger_head
  → ACK
expected_revision != durable.revision
  → STALE_HEAD
  → reload durable head
  → do not overwrite newer durable state
  → retry once under the loaded fence or fail closed
```

Preferred Postgres form: one `SERIALIZABLE` function/`CAS` on `(world_id, revision)`. Hosted REST equivalent: conditional update `revision=eq.expected`. Zero rows → `STALE_HEAD`.

Crash:

| Point | Required outcome |
|-------|------------------|
| Before durable write | No event, no head bump, retry safe |
| During write | SERIALIZABLE/CAS abort; retry from unchanged head |
| Commit then DO die before ACK | Retry same action; idempotent event_id; no second effect |
| Stale DO after newer head | STALE_HEAD; reload; no overwrite |
| Restart, valid head | Restore head; resume |
| Restart, missing/inconsistent head | INCIDENT / fail closed |

Unsettled backlog stays bounded (one extra mutating batch then BLOCKING). Retry is idempotent. After the bound: reject mutating PLAY; WATCH may continue.

DO restore: if local world missing, load durable head. If lineage cannot be proved, INCIDENT. Never reseed Genesis.

## Alternatives rejected

| Alternative | Why |
|-------------|-----|
| Last-write-wins head | Silent regression |
| New database | Stack freeze |
| Event-catalog 0.3 | Out of scope |
| Genesis reseed as recovery | First-world freeze |

## Compatibility

Extends RFC-0016 head. Frozen action/event catalogs unchanged.

## Validation

`check_rfc_0017`: Accepted; STALE_HEAD; SERIALIZABLE or CAS; no Genesis; no new verbs.

## Rollback

Stop sending revision; RFC-0016 upsert remains.

## Unresolved

Multi-row outbox in one PG transaction from the Worker without RPC; digest algorithm versioning.
