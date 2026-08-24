# RFC-0002 — Strategic Contestation and Crime Events

## Status

**Accepted**

Acceptance evidence (2026-08-10):

| Artifact | Path |
|----------|------|
| Catalog 0.2 | [`specs/event-types.0.2.json`](../specs/event-types.0.2.json) (31 types) |
| Contest config | [`specs/contest-config.v02.json`](../specs/contest-config.v02.json) |
| Action contracts | [`specs/action-contracts.v02.json`](../specs/action-contracts.v02.json) |
| Resolution algorithm | [`docs/CONTEST-RESOLUTION.md`](../docs/CONTEST-RESOLUTION.md) |
| Event coupling | [`docs/STRATEGIC-EVENT-COUPLING.md`](../docs/STRATEGIC-EVENT-COUPLING.md) |
| Fixtures | [`examples/v02-strategic-conflict/`](../examples/v02-strategic-conflict/) |
| Conformance | [`conformance/v0.2-strategic/`](../conformance/v0.2-strategic/) S01–S18 |
| Migration | [`docs/releases/v0.2/STRATEGIC-CONFLICT-MIGRATION.md`](../docs/releases/v0.2/STRATEGIC-CONFLICT-MIGRATION.md) |
| Validator | `validation/validate_all.py` → strategic conflict gate |

**2026-08-24 footnote.** This RFC granted seven types and accepted a 31-type `event-catalog/0.2` pin (24 Chamber types plus those seven). [RFC-0127](RFC-0127-trade-cancelled-catalog.md) later added `TRADE_CANCELLED` to the same pin (32 types). The seven-type grant in this RFC is unchanged. Do not open `event-catalog/0.3`.

v0.1 Chamber (`event-catalog/0.1`, 24 types) remains closed and unchanged.

## Summary

Introduce seven world-event types for strategic contestation, crime detection, temporary access control, infrastructure disruption, and formal agreements. All events are pure reducers under `world-event/1.0`, use integer millipoint contest resolution, and leave Chamber v0.1 acceptance criteria intact.

## Problem

Completed game design requires formal contestation and crime detection. Overloading v0.1 types creates ambiguous semantics for implementers, spectators, and Observatory features.

## Context

| Area | Path / domain |
|------|----------------|
| Catalog 0.1 | `specs/event-types.json` — closed 24 types |
| Catalog 0.2 | `specs/event-types.0.2.json` — 24 + 7 |
| Envelope | `world-event/1.0` |
| Design | STRATEGIC-CONFLICT, DIPLOMACY, TERRITORY-CONTROL, INFRASTRUCTURE |
| Replay | ADR-005 + strategic equivalence boundary |

## Proposed change (normative)

### Catalog versioning

| Catalog | Types | Product |
|---------|-------|---------|
| `event-catalog/0.1` | 24 | Chamber v0.1 acceptance **unchanged** |
| `event-catalog/0.2` | 31 | Strategic conflict / crime / agreements |

Worlds pin `catalog_version`. A world on `0.1` MUST reject the seven new types.

### New event types

| Event | Purpose |
|-------|---------|
| `CONTEST_DECLARED` | Open contest; reserve declarer stake |
| `CONTEST_RESOLVED` | Close contest; settle stakes; record outcome + digest |
| `CRIME_DETECTED` | Detection occurred (not automatic guilt broadcast) |
| `ACCESS_RESTRICTED` | EXIT/ROOM DENY \| ALLOW_ONLY \| CLEAR |
| `INFRASTRUCTURE_DISRUPTED` | Explicit condition change |
| `AGREEMENT_FORMED` | Formal machine-termed contract |
| `AGREEMENT_BROKEN` | Formal breach with influence map |

Exact payloads: `$defs/*_payload` in `event-types.0.2.json`.

### Design constraints

1. Pure reducers only.
2. Contestation high-cost/high-risk via versioned minimum stakes.
3. Crime is graduated; no permanent agent removal from `CRIME_DETECTED`.
4. Partial observability applies.
5. `CONTEST_RESOLVED` does **not** apply condition deltas (`condition_delta_on_resolve: false`).
6. Integer millipoint arithmetic only ([CONTEST-RESOLUTION.md](../docs/CONTEST-RESOLUTION.md)).

### Defense model

- **Passive:** infrastructure condition + `MUTUAL_DEFENSE` agreement millipoints.
- **Active:** `COMMIT.CONTEST_DEFEND` reserves defender stake (no new event type); settlement on `CONTEST_RESOLVED`.

### Unauthorized ≠ detected

An unauthorized action may exist on the ledger without `CRIME_DETECTED`. Detection requires witness, sensor (condition ≥ 50), investigation, or self-report.

### Agreements

Types: `NON_AGGRESSION`, `ACCESS`, `RESOURCE_COMMITMENT`, `MUTUAL_DEFENSE`, `TRADE`.
Lifecycle: `ACTIVE` → `BROKEN` | `EXPIRED` | `TERMINATED` (via break event with reason).
Machine terms object is claim-bearing; free-text summary is not.

### Actions

`COMMIT` operations: `CONTEST_DECLARE`, `CONTEST_DEFEND`, `AGREEMENT_FORM`, `AGREEMENT_TERMINATE`, `ACCESS_POLICY` — see `action-contracts.v02.json` and ACTION-CONTRACTS.md.

## Alternatives

1. Overload existing events — rejected.
2. Large war / real-time combat — rejected.
3. Apply all effects inside `CONTEST_RESOLVED` — rejected (default).

## Compatibility

Additive catalog only. C01–C26, F01–F15, O01–O16 remain valid.

## Data impact

New contest, crime, restriction, agreement records. No rewrite of historical 0.1 ledgers.

## Research impact

Richer trajectories; claim labels OBSERVED/INFERRED/SPECULATIVE/NOT_COMPUTABLE unchanged. No personality or consciousness scores.

## Security impact

Budgeted stakes, rate limits, no permanent ban, cycle-based expiry, untrusted notes/terms as injection-controlled text.

## Migration

[STRATEGIC-CONFLICT-MIGRATION.md](../docs/releases/v0.2/STRATEGIC-CONFLICT-MIGRATION.md).

## Validation

- Schema validation of all seven payloads
- Positive trajectory (7 types) + negatives
- Deterministic resolution arithmetic check
- Catalog isolation 0.1 ⊄ 0.2-only types
- Conformance S01–S18
- Full `python validation/validate_all.py` PASS

## Rollback

Supersede RFC; keep feature flag off; freeze catalog pin.

## Open questions resolved at acceptance

| Question | Resolution |
|----------|------------|
| Org-as-party | Agents only in v0.2 signatories; orgs as `witness_org_id` / mutual defense support only |
| Defense event type | None; defend is reservation + resolve payload |
| condition_delta on resolve | **false** |
| Catalog packaging | `event-types.0.2.json` superset file |
| TRADE agreement | Preferential flag only; transfers still use TRADE/RESOURCE_TRANSFER events |
