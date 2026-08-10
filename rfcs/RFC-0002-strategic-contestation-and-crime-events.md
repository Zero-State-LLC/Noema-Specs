# RFC-0002 — Strategic Contestation and Crime Events

## Status

**Draft** — design-complete skeleton. Payload schemas and reducers are required before **Accepted**.

## Summary

Introduce the minimal event set required to support strategic contestation and crime consequences while preserving deterministic replay and existing v0.1 contracts.

## Motivation

The completed game design requires formal contestation and crime detection to make conflict, defense, and recovery meaningful ([docs/STRATEGIC-CONFLICT.md](../docs/STRATEGIC-CONFLICT.md), [docs/EVENT-CATALOG-AUDIT.md](../docs/EVENT-CATALOG-AUDIT.md)). These cannot be simulated purely through existing events without ambiguity.

## Context

Affected contracts:

- Closed v0.1 event catalog (`event-catalog/0.1`) — **additive** only via this RFC when Accepted
- [EVENT-CATALOG.md](../docs/EVENT-CATALOG.md), `specs/event-types.json`
- [ACTION-CONTRACTS.md](../docs/ACTION-CONTRACTS.md), [RESOURCE-ECONOMY.md](../docs/RESOURCE-ECONOMY.md)
- [DIPLOMACY.md](../docs/DIPLOMACY.md), [TERRITORY-CONTROL.md](../docs/TERRITORY-CONTROL.md)
- Replay / ADR-005 equivalence for new event types

## Proposed new event types

| Event | Purpose |
|-------|---------|
| `CONTEST_DECLARED` | Agent commits resources to begin a contest against a target (resource, infrastructure, access, or presence) |
| `CONTEST_RESOLVED` | Deterministic resolution of a contest; records outcome, costs, and any condition changes |
| `CRIME_DETECTED` | Records that an unauthorized action was observed by witnesses or infrastructure sensors |
| `ACCESS_RESTRICTED` | Temporary or policy-based change to exit or room access |
| `INFRASTRUCTURE_DISRUPTED` | Explicit result of sabotage or contest on infrastructure condition |
| `AGREEMENT_FORMED` | Formal diplomatic or access contract |
| `AGREEMENT_BROKEN` | Formal breach with mechanical consequences |

## Design constraints

- All new events must be pure reducers.
- Contestation is high-cost and high-risk.
- Crime detection produces history and graduated consequences only.
- No permanent agent removal.
- Partial observability still applies to who sees the events.
- Exact payload schemas and preconditions will be defined in the full RFC body and corresponding JSON Schema before acceptance.

## Alternatives

1. **Overload existing events only** — Rejected: ambiguous semantics for crime/contest.
2. **Immediate large war system** — Rejected: out of v0.2 scope.
3. **Real-time combat** — Rejected: violates cycle-resolved model.

## Compatibility

v0.1 Chamber acceptance criteria remain unchanged. These events are additive for v0.2. Worlds without contestation continue to use the 24-type catalog.

## Data impact

New event types and optional agreement/contest records. No rewrite of historical 24-type ledgers.

## Research impact

Creates richer observable conflict/diplomacy trajectories for Observatory. No research score becomes world truth.

## Security impact

Contestation and crime must remain budgeted, authorized, and containable. Detection must not leak hidden state improperly.

## Migration

Implementations enable contestation via feature flag / product version after schemas land. Pre-v0.2 history unchanged.

## Validation

Required before Accepted:

- JSON Schema for each payload
- Positive/negative fixtures
- Reducer purity and digest-chain tests
- Partial observability / spectator projection fixtures

## Rollback

Supersede RFC; disable feature flag; do not append new types to live worlds without migration plan.

## Problem

What issue requires a contract change?

Ambiguous conflict/crime semantics without dedicated pure ledger events.

## Proposed change

Add the event types listed above to a new catalog version (e.g. `event-catalog/0.2`) with reducers and schemas.
