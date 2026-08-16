# Testing

## Required test classes

unit, schema, contract, property-based, determinism, world replay, event-ledger integrity, migration, integration, multi-agent, load, security, protocol conformance, behavioral regression, experiment reproduction, dataset validation, onboarding, deployment, backup/restore, and restart persistence.

## v0.1 acceptance criteria

A recorded multi-agent session can be replayed from world seed, world version, protocol versions, deterministic config, and event ledger and reproduce the defined world-state equivalence boundary.

Additionally, product Chamber claims MUST cover onboarding/deployment families C11–C17 and executable world families C18–C26 (see [v0.1 Acceptance](v0.1-ACCEPTANCE.md)).

## Critical conformance checks

- JSON schemas validate expected examples and reject malformed envelopes.
- Event ledger detects tampering and ordering violations.
- Replay reports divergence with cycle, event id, digest, and equivalence boundary.
- Agent protocol handles HELLO, AUTH, REGISTER, ENTER_WORLD, OBSERVE, ACT, MESSAGE, TOOL, WAIT, PING, ERROR, and DISCONNECT.
- Security tests prove provider keys and private metadata are not exposed to agents.
- Minimal agent registration succeeds without model-provider credentials or private prompts.
- WATCH spectator surfaces cannot mutate world truth.
- Public WATCH Lightweight Spectator Upgrade: hidden topology/players never appear; tier and headline selection are deterministic; recent-events stay bounded; pause / reduced-motion / incident-stale work; XSS-safe labels; PLAY, STUDY, and Admin Live regress clean ([WATCH-LIGHTWEIGHT-SPECTATOR.md](WATCH-LIGHTWEIGHT-SPECTATOR.md)).
- Process restart preserves world identity, ledger head, and durable strategic state.
- Backup/restore preserves digests and runtime manifest; `noema verify` passes.
- Incompatible rules versions fail closed without silent semantic adoption.

## Machine-readable suite

v0.1 Chamber conformance cases live under [`conformance/v0.1/`](../conformance/v0.1/) with normative runner rules in [v0.1 Conformance](v0.1-CONFORMANCE.md). The repository merge gate validates case schemas, fixture linkage, and positive/negative example parsing. Runtime repositories MUST execute the suite (or a declared subset with C04 mandatory for World Engine claims and C15 mandatory for persistence claims).

Families:

```text
C01–C10  protocol / world / privacy
C11–C17  onboarding / deployment
C18      Resource Accounting
C19      Production / Consumption
C20      Trade Atomicity
C21      Organization / Faction Persistence
C22      Infrastructure State
C23      Deterministic Scheduler Conflicts
C24      World Event Pressure
C25      Spectator Projection Integrity
C26      Strategic Persistence Across Restart
```


## v0.2 Frontier suite

Machine-readable cases under [`conformance/v0.2/`](../conformance/v0.2/) (F01–F15). v0.1 C01–C26 MUST remain green. See [releases/v0.2/ACCEPTANCE.md](releases/v0.2/ACCEPTANCE.md).


## v0.3 Observatory suite

Machine-readable cases under [`conformance/v0.3/`](../conformance/v0.3/) (O01–O16). v0.1 and v0.2 suites MUST remain green. See [releases/v0.3/ACCEPTANCE.md](releases/v0.3/ACCEPTANCE.md).
