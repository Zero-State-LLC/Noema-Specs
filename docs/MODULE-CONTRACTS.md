# Module Contracts (v0.1)

Machine-readable authority: [`specs/module-contracts.v01.json`](../specs/module-contracts.v01.json) · schema: [`module-contracts.schema.json`](../specs/module-contracts.schema.json).

These contracts bind the modular-monolith reference deployment ([DEPLOYMENT.md](DEPLOYMENT.md)). Module extraction into services MUST preserve these boundaries.

## Hard dependency rules

| Rule | MUST |
|------|------|
| Observation Engine | MUST NOT mutate canonical WorldState |
| Spectator Projection | MUST NOT mutate canonical WorldState |
| Research Capture | MUST NOT mutate canonical WorldState |
| Observatory / research interpretation | MUST NOT become world truth |
| Operator surfaces | MUST NOT bypass Action Router for world mutations |
| Event Ledger | MUST NOT accept arbitrary unauthenticated producer writes |
| World Engine state changes | MUST be explainable through canonical catalog events |
| Canonical writer | Exactly one active fenced writer may mutate a `world_id` |
| Cycle persistence | One PostgreSQL `SERIALIZABLE` transaction commits each cycle batch |
| Protocol delivery | Acks mutate delivery bookkeeping only, never world truth |

## Module index (v0.1)

| Module | Owns | Mutates WorldState? |
|--------|------|---------------------|
| `gateway` | connections, framing | no |
| `auth` | principals, tokens | no |
| `agent_registry` | agent identity/manifests | no (registry only) |
| `action_router` | action validation, routing | no (forwards only) |
| `world_engine` | reducers, rules | **yes** (via events) |
| `world_state` | durable canonical state store | **yes** (under engine) |
| `event_ledger` | append-only events | append-only |
| `observation_engine` | permissioned projections | **no** |
| `message_service` | message queue/delivery indexes | via MESSAGE events only |
| `scheduler` | cycle freeze, order, deadlines | no (orders inputs) |
| `snapshot_service` | snapshots | no (reads state) |
| `replay_engine` | replay / equivalence | no (offline) |
| `spectator_projection` | WATCH surfaces | **no** |
| `research_capture` | consented trajectories | **no** |
| `operator_api` | ops/admin HTTP | mutations only via Action Router |
| `frontier_director` (v0.2) | plans/audits (research) | **no** (proposes only) |
| `observatory` (v0.3) | trajectories, features, candidates, audits | **no** |

### `frontier_director` (v0.2)

| Field | Value |
|-------|--------|
| purpose | Enumerate/rank high-information situations near capability uncertainty |
| owns_state | frontier plans, candidate ledgers, audits (research partition) |
| reads | capability primitives, trajectory digests, genomes, public world digests |
| writes | research artifacts only |
| forbidden_dependencies | direct world_state writes; opaque claim-bearing rankers |
| outputs | plan, ledger, audit, replay-context; **proposals** for `SITUATION_INJECTED` |
| determinism | fixed-point scores; seed only for ties |
| conformance | F01–F15 |

### `observatory` (v0.3)

| Field | Value |
|-------|--------|
| purpose | Detect unusual/shifted behavior; emit research candidates |
| owns_state | trajectories, features, baselines, candidates, analysis runs |
| writes | research partition only |
| forbidden | WorldState mutation; situation injection; opaque claim-bearing detectors |
| conformance | O01–O16 |

Full field definitions for v0.1 modules live in the JSON contract.

## Transaction boundary (normative)

A cycle batch is the v0.1 canonical persistence unit:

```text
freeze ordered accepted actions
→ reserve budgets
→ reduce all actions and scheduled processes
→ append one contiguous event batch
→ update ledger head and world_state revision
→ settle reservations
→ commit
```

The complete batch MUST commit in one PostgreSQL `SERIALIZABLE` transaction guarded by the expected prior world revision and the active writer fencing token. Unique constraints MUST reject duplicate event ids, duplicate idempotency keys for the same logical mutation, and non-contiguous or reused event sequences for the world. Failure after reservation MUST release reservations without partial world mutation (except committed ledgered rejection events such as `MOVE_REJECTED`, `BUDGET_EXCEEDED`, `TRADE_REJECTED`).

Exactly one fenced canonical writer may hold mutation authority for a `world_id`. Losing the fence, detecting a stale revision, hitting a serialization failure, or failing a sequence/digest constraint aborts the batch. The next attempt starts from the unchanged committed head. Observation projection, spectator projection, research capture, protocol delivery, and acknowledgements are derived or bookkeeping surfaces and MUST NOT advance canonical world revision.

Crash reconciliation MUST compare world revision, ledger head, event sequence head, digest chain, snapshot head, and unresolved reservations before accepting new mutations. Clean canonical commits MAY rebuild delivery windows; divergent state or ambiguous writer fencing MUST fail closed.

## See also

- [ACTION-CONTRACTS.md](ACTION-CONTRACTS.md)
- [SCHEDULER.md](SCHEDULER.md)
- [RESOURCE-ECONOMY.md](RESOURCE-ECONOMY.md)
- [SPECTATOR.md](SPECTATOR.md)
