# RFC-0003 — Deterministic Contract Hardening

## Status

**Accepted**

Approved for specification-only implementation on 2026-08-11. Runtime implementation is explicitly out of scope for this repository.

## Summary

Harden NOEMA's deterministic world contracts so independently implemented engines agree on action order, message visibility, canonical bytes, exact quantities, typed identifiers, event-catalog validation, persistence atomicity, protocol recovery, and evidence integrity.

This RFC resolves contradictions discovered during the v0.1 architecture review without changing the Chamber's game verbs, economy, map, event meanings, or research claims boundary.

## Problem

The current specification validation gate passes while several interoperability-critical rules remain contradictory or prose-only:

1. Scheduler and World Engine name different contention order keys.
2. Message-delivery events and observation projection have ambiguous same-cycle order.
3. Canonical number serialization is referenced but not fully defined.
4. Typed ID and exact-quantity rules are not consistently schema-enforced.
5. The generic WorldEvent envelope accepts arbitrary event names and payloads despite closed catalog pins.
6. Canonical WorldState leaves replay-critical lineage and revision obligations underconstrained.
7. Atomic state/ledger persistence, single-writer fencing, resume acknowledgement, and evidence receipt profiles need exact contracts.
8. Existing conformance validates structure more strongly than these cross-contract invariants.

## Decisions (normative)

### 1. Canonical action order

For actions in one frozen cycle, the canonical key is:

```text
(action_priority ASC, agent_id ASC, client_action_sequence ASC, action_id ASC)
```

- `action_priority` is a versioned world-rules value, never supplied by the client.
- `client_action_sequence` is a monotonically increasing integer scoped to `(world_id, agent_id, session_epoch)` and is required on mutating actions.
- Gateway arrival order, wall-clock time, socket scheduling, and network latency MUST NOT affect canonical resolution.
- Duplicate or stale client sequences fail deterministically. A repeated idempotency key returns its original result.
- The frozen action set and complete keys are ledger provenance and replay inputs.

This favors strategic fairness and reproducibility over latency advantage, which is appropriate for a cycle-based persistent world.

### 2. Message delivery and observations

A cycle commits one contiguous canonical event batch:

```text
freeze → order → reserve → reduce actions → world processes →
message delivery events → append ledger + commit state → derive observations
```

`MESSAGE_DELIVERED` is therefore committed before post-cycle observation projection. A post-cycle observation MAY contain a same-cycle delivered message when visibility and permission allow it. Transport notification and client acknowledgement remain noncanonical protocol effects.

### 3. Canonical bytes and exact quantities

NOEMA canonical JSON profile `noema-jcs/1` uses RFC 8785 JSON Canonicalization Scheme over I-JSON-compatible values, with these additional rules:

- non-I-JSON values, duplicate keys, non-finite numbers, and implementation-dependent numeric coercion are invalid;
- replay-critical quantities use integers in a declared fixed-point scale or explicitly schema-declared rational representation;
- canonical timestamps are RFC 3339 UTC using `Z`, with precision declared by the containing schema;
- binary artifacts are hashed as raw bytes;
- strings are hashed exactly as represented under JCS and MUST NOT be silently Unicode-normalized;
- every digest-bearing artifact records `canonicalization_version` and `hash_algorithm`.

### 4. Typed identifiers

Normative schemas MUST enforce the typed prefixes in `id-rules.v01.json`. Existing hyphenated examples are corrected rather than grandfathered. IDs are opaque after prefix validation and MUST NOT encode mutable meaning.

### 5. Closed catalog schemas

The generic `world-event/1.0` schema is an envelope building block, not sufficient ledger admission validation. A world MUST validate events against the composed schema for its pinned catalog. Each composed schema binds every `event_type` to its exact payload schema and rejects unknown or wrong-version types.

### 6. Canonical state

Canonical WorldState MUST carry world/version/catalog lineage, monotonic revision, current cycle, last committed sequence, and digest-bearing collections required for replay. Extensible implementation metadata MUST be outside canonical digest-bearing state or explicitly excluded by a versioned equivalence boundary.

### 7. Persistence and writer fencing

Each world has exactly one active fenced canonical writer. A cycle batch commits in one PostgreSQL `SERIALIZABLE` transaction with:

- expected world revision;
- active writer fencing token;
- unique contiguous event sequences;
- event digest-chain update;
- state revision and ledger-head update;
- budget reservation settlement.

Serialization failure, stale revision, or stale fencing token retries from the unchanged committed head. Partial canonical commit is forbidden. `noema verify` detects and fails on state/ledger divergence.

### 8. Resume and acknowledgements

Protocol acknowledgements are cumulative per logical delivery stream and identify the highest contiguous observation/event delivery position. Resume tokens are world-, principal-, stream-, and session-epoch-scoped, expire, and never authorize mutation by themselves. Servers retain a bounded redelivery window and return a stable resynchronization error when the requested position is no longer retained. Redelivery never creates new world events or charges budgets.

### 9. Evidence receipts

Signed receipts are:

- optional for the local gameplay profile;
- mandatory for research-isolated execution, reproducibility bundles, and public evidence export.

The evidence profile records algorithm, key identifier, signature, signed digest, issuance time, and verification policy. Key rotation preserves verification of historical receipts. Missing or invalid required signatures make evidence `INVALID_EVIDENCE`, never silently unsigned evidence.

## Compatibility

These changes clarify intended v0.1 semantics but tighten wire and schema validation. Implementations using gateway arrival order, hyphenated typed IDs, floating canonical quantities, generic-only event validation, or implicit resume state are nonconforming after adoption.

The event meanings and catalog membership remain unchanged. Historical ledgers retain their pinned schema/canonicalization versions and are not rewritten.

## Data impact

- New action sequence and provenance fields.
- Explicit canonicalization/hash fields on digest-bearing artifacts.
- Stronger canonical WorldState lineage/head fields.
- Catalog-specific schema entrypoints.
- Writer fencing and receipt metadata in runtime/audit contracts.

## Research impact

Deterministic attribution and third-party reproducibility improve. Research interpretation remains outside world truth. Claim labels and the prohibition on consciousness scoring are unchanged.

## Security impact

The RFC reduces split-brain mutation, replay ambiguity, cross-session resume confusion, malformed ledger admission, and unverifiable evidence export. It does not expand agent authority or tool access.

## Migration

1. Pin existing historical artifacts to their original schema and canonicalization versions.
2. Introduce `noema-jcs/1`, typed IDs, client action sequences, and composed catalog validators at a declared compatibility boundary.
3. Reject mixed-version cycle batches.
4. Require explicit world migration or a new `world_version` where stored canonical representations change.
5. Preserve original bytes and digests for historical evidence.

## Validation

Acceptance requires:

- one canonical order key across prose, schemas, fixtures, and machine contracts;
- deterministic contention fixtures independent of receive order;
- same-cycle delivery/observation fixtures;
- canonicalization vectors and invalid-number rejection;
- typed-ID negative fixtures;
- closed catalog and exact-payload rejection fixtures;
- canonical-state lineage and monotonic-head checks;
- stale revision/fencing and interrupted-commit cases;
- resume duplicate/gap/expiry cases;
- signed evidence receipt verification cases;
- full `python validation/validate_all.py` PASS.

## Rollback

Supersede this RFC and keep affected worlds pinned to their prior world, schema, protocol, and canonicalization versions. Never reinterpret or rewrite an existing ledger under rolled-back rules.

## Resolved questions

| Question | Resolution |
|----------|------------|
| Canonical action ordering | Rule priority, agent ID, client sequence, action ID; never gateway arrival order |
| Same-cycle messages | Delivery event commits before post-cycle projection |
| Canonical JSON | RFC 8785 JCS with NOEMA I-JSON, exact-quantity, timestamp, and digest restrictions |
| Typed ID migration | Strict for new artifacts; historical artifacts remain version-pinned |
| Catalog packaging | Generic envelope plus mandatory catalog-specific composed entrypoints |
| Signed receipts | Mandatory for evidence profiles, optional for local gameplay |
| Version treatment | Tightening is compatibility-significant; historical pins remain immutable |
