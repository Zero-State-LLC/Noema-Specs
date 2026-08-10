# Testing

## Required test classes

unit, schema, contract, property-based, determinism, world replay, event-ledger integrity, migration, integration, multi-agent, load, security, protocol conformance, behavioral regression, experiment reproduction, dataset validation, onboarding, deployment, backup/restore, and restart persistence.

## v0.1 acceptance criteria

A recorded multi-agent session can be replayed from world seed, world version, protocol versions, deterministic config, and event ledger and reproduce the defined world-state equivalence boundary.

Additionally, product Chamber claims MUST cover onboarding and deployment families C11–C17 (see [v0.1 Acceptance](v0.1-ACCEPTANCE.md)).

## Critical conformance checks

- JSON schemas validate expected examples and reject malformed envelopes.
- Event ledger detects tampering and ordering violations.
- Replay reports divergence with cycle, event id, digest, and equivalence boundary.
- Agent protocol handles HELLO, AUTH, REGISTER, ENTER_WORLD, OBSERVE, ACT, MESSAGE, TOOL, WAIT, PING, ERROR, and DISCONNECT.
- Security tests prove provider keys and private metadata are not exposed to agents.
- Minimal agent registration succeeds without model-provider credentials or private prompts.
- WATCH spectator surfaces cannot mutate world truth.
- Process restart preserves world identity, ledger head, and durable strategic state.
- Backup/restore preserves digests and runtime manifest; `noema verify` passes.
- Incompatible rules versions fail closed without silent semantic adoption.

## Machine-readable suite

v0.1 Chamber conformance cases live under [`conformance/v0.1/`](../conformance/v0.1/) with normative runner rules in [v0.1 Conformance](v0.1-CONFORMANCE.md). The repository merge gate validates case schemas, fixture linkage, and positive/negative example parsing. Runtime repositories MUST execute the suite (or a declared subset with C04 mandatory for World Engine claims and C15 mandatory for persistence claims).

Families:

```text
C01–C10  protocol / world / privacy
C11      Human onboarding
C12      Agent onboarding
C13      Spectator onboarding
C14      Reference deployment
C15      World persistence across restart
C16      Backup/restore equivalence
C17      Upgrade/version pinning
```
