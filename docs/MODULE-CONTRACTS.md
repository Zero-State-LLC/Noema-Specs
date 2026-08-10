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

Full field definitions for v0.1 modules live in the JSON contract.

## Transaction boundary (normative)

A single accepted action reduction is atomic:

```text
reserve budgets → reduce → append events → commit world_state revision
```

Failure after reserve MUST release reservations without partial world mutation (except ledgered rejection events such as `MOVE_REJECTED`, `BUDGET_EXCEEDED`, `TRADE_REJECTED`).

## See also

- [ACTION-CONTRACTS.md](ACTION-CONTRACTS.md)
- [SCHEDULER.md](SCHEDULER.md)
- [RESOURCE-ECONOMY.md](RESOURCE-ECONOMY.md)
- [SPECTATOR.md](SPECTATOR.md)
