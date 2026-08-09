# Testing

## Required test classes

unit, schema, contract, property-based, determinism, world replay, event-ledger integrity, migration, integration, multi-agent, load, security, protocol conformance, behavioral regression, experiment reproduction, and dataset validation.

## v0.1 acceptance criteria

A recorded multi-agent session can be replayed from world seed, world version, protocol versions, deterministic config, and event ledger and reproduce the defined world-state equivalence boundary.

## Critical conformance checks

- JSON schemas validate expected examples and reject malformed envelopes.
- Event ledger detects tampering and ordering violations.
- Replay reports divergence with cycle, event id, digest, and equivalence boundary.
- Agent protocol handles HELLO, AUTH, REGISTER, ENTER_WORLD, OBSERVE, ACT, MESSAGE, TOOL, WAIT, PING, ERROR, and DISCONNECT.
- Security tests prove provider keys and private metadata are not exposed to agents.
