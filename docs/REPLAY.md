# Replay

## Purpose

Replay reconstructs a recorded execution from declared, versioned inputs and determines whether the reconstruction satisfies a declared equivalence boundary. Replay is evidence infrastructure, not proof that an agent will produce identical outputs when an external model or other nondeterministic dependency is invoked again.

This document operationalizes [`replay-protocol/v1`](../protocols/replay-protocol-v1.md) and preserves the claim discipline, privacy partitioning, provenance, consent, retention, and security requirements defined elsewhere in this repository.

## Normative inputs

A replay request MUST resolve the following immutable inputs before execution:

| Input | Exact requirement |
|---|---|
| `request_id` | Stable, unique replay-request identifier. |
| `replay_mode` | One of `deterministic-world`, `deterministic-protocol`, `stochastic-agent`, or `behavioral-equivalence`. |
| `world_seed` | Exact seed bytes plus encoding. |
| `world_version` | Immutable world ruleset identifier and content digest. |
| `protocol_versions` | Ordered map from protocol name to immutable version and schema digest. |
| `deterministic_config` | Canonical configuration object, including named random streams, scheduling policy, numeric rules, locale, and time source. |
| `initial_state` | Snapshot bytes or canonical state object, its cycle, schema version, and digest. |
| `event_ledger` | Ordered ledger records, ledger version, first and last sequence, and root digest. |
| `external_inputs` | Content-addressed observations, provider responses, tool results, clock values, and operator interventions consumed by the recorded run. An empty list is explicit. |
| `equivalence_boundary` | The exact comparison contract defined below. |
| `stop_condition` | Inclusive target cycle/event, predicate, or first-divergence rule. |

A URI is not sufficient identity. Every referenced input MUST carry a digest over the bytes actually consumed. Missing required bytes, versions, schemas, or digests make the replay `NOT_COMPUTABLE`; the implementation MUST NOT silently substitute a current default.

## Canonicalization and identity

Canonical JSON uses UTF-8, lexicographically sorted object keys, no insignificant whitespace, JSON literals for booleans and null, and repository-defined canonical number serialization. Arrays retain declared order. Binary artifacts are hashed as raw bytes. Timestamps used as evidence are inputs, never freshly generated comparison fields.

The replay input identity is:

```text
input_digest = SHA-256(canonical_json({
  replay_mode,
  world_seed_digest,
  world_version,
  world_digest,
  protocol_versions,
  deterministic_config,
  initial_state_digest,
  event_ledger_root_digest,
  external_input_digests,
  equivalence_boundary,
  stop_condition
}))
```

Implementations MUST record the canonicalization version and hash algorithm. Unknown canonicalization versions or algorithms fail closed as `NOT_COMPUTABLE`.

## v0.1 mandatory equivalence profile

For NOEMA v0.1 acceptance, the declared boundary MUST require all of the following for the replay interval and focal agents:

1. identical ordered event digests;
2. an identical final canonical WorldState digest; and
3. identical observation digests at every declared focal-agent observation point.

The replay loads a full serializable WorldState snapshot identified by cycle, sequence number, schema version, content digest, and world version, then applies events in strict sequence order through the versioned reducers. Any permitted nondeterminism MUST use a named and recorded stream such as `noise_stream_id`. An implementation MAY declare stricter comparisons, but it MUST NOT weaken this profile while claiming v0.1 replay acceptance.

## Equivalence boundary

The boundary MUST contain all of these fields:

```json
{
  "boundary_version": "equivalence-boundary/v1",
  "exact_paths": ["/room_states", "/resource_balances"],
  "ignored_paths": ["/runtime/host_pid"],
  "ordered_collection_paths": ["/message_delivery"],
  "unordered_collection_paths": [],
  "numeric_tolerances": {},
  "semantic_predicates": [],
  "observation_points": [{"cycle": 18444, "phase": "cycle-commit"}],
  "divergence_policy": "stop-first",
  "claim_invalidation": "any-required-mismatch"
}
```

`exact_paths` are compared after canonical serialization and MUST match byte for byte. `ignored_paths` are excluded and MUST be justified in the audit record. Ordered collections preserve order. Unordered collections MUST declare a stable element identity and are sorted by that identity before comparison. Numeric tolerances MUST name a path, absolute tolerance, relative tolerance, unit, and non-finite-value policy. Semantic predicates MUST be versioned, pure, total functions whose implementation digest is recorded. Observation points state exactly when comparisons occur.

A field MUST NOT be both required and ignored. Wildcards, implicit defaults, implementation-dependent iteration order, and prose-only predicates are invalid. Invalid boundaries are `NOT_COMPUTABLE`.

The boundary is deliberately narrower than full process identity. Matching it supports only the stated replay claim. It does not establish identical hidden reasoning, consciousness, general capability, causality, or transfer beyond the tested conditions.

## Deterministic replay algorithm

Given resolved inputs `I` and boundary `B`:

1. Validate request, schemas, versions, authorization, consent, retention, and private/public access before loading protected payloads.
2. Verify every content digest, ledger hash link, sequence number, and idempotency key. Reject duplicate or missing sequence numbers unless the declared ledger protocol explicitly represents them.
3. Build the runtime exclusively from the declared world version, protocols, configuration, snapshot, and external inputs. Disable undeclared network, wall-clock, entropy, locale, and filesystem inputs.
4. Derive each seeded decision as `HMAC-SHA-256(world_seed, stream_name || 0x00 || decision_point || 0x00 || draw_index)`. Convert bytes to the required value with a versioned rejection-sampling rule, never modulo bias. A stream name, decision point, and monotonically increasing draw index MUST be recorded for every draw.
5. Process ledger records in ascending `(cycle, phase_ordinal, sequence)` order. Equal or absent ordering keys are an integrity failure unless resolved by the pinned ledger version.
6. Before applying a record, verify its precondition digest and referenced external-input digests. Apply exactly one versioned transition. Record the post-transition state digest.
7. At every observation point, project expected and observed states through `B`, canonicalize each projection, and compare exact fields, normalized collections, tolerances, and semantic predicates.
8. On mismatch, emit a divergence record. Stop or continue exactly as `divergence_policy` declares. Continuing MUST NOT overwrite the first divergence.
9. Evaluate the explicit stop condition. Exhausting the ledger before the condition is a failure, not success.
10. Emit the replay result and immutable audit record. The result is `EQUIVALENT` only when every required observation passes and all integrity checks succeed.

Pseudocode:

```text
replay(I, B):
  validate_and_verify(I, B) or return NOT_COMPUTABLE
  runtime := instantiate_pinned_runtime(I)
  divergences := []
  for event in canonical_event_order(I.event_ledger):
    verify_preconditions(runtime, event) or return INVALID_EVIDENCE
    runtime := transition(runtime, event, declared_external_inputs(event))
    append_checkpoint(event, digest(runtime.state))
    if is_observation_point(event, B):
      comparison := compare(project(expected(event), B), project(runtime.state, B), B)
      if not comparison.equivalent:
        divergences.append(divergence(event, comparison))
        if B.divergence_policy == "stop-first": break
    if stop_condition_met(runtime, event, I.stop_condition): break
  return classify(integrity, stop_condition, divergences, B.claim_invalidation)
```

## Outputs

A replay produces exactly these logical outputs:

1. `replay-result.json` with `status` (`EQUIVALENT`, `DIVERGENT`, `NOT_COMPUTABLE`, `INVALID_EVIDENCE`, or `ABORTED`), input digest, boundary digest, first/last processed event, observation counts, divergence count, claim-invalidating boolean, and audit-record digest.
2. `replay-audit.jsonl`, an append-only ordered audit stream.
3. `divergences.jsonl`, possibly empty.
4. `checkpoints.jsonl`, containing cycle, event id, pre-state digest, post-state digest, and named random draws.
5. Optional protected diagnostic artifacts, partitioned from public outputs and referenced by digest.

## Audit records

Every audit record MUST include:

```json
{
  "audit_version": "replay-audit/v1",
  "request_id": "replay-001",
  "record_index": 17,
  "record_type": "comparison",
  "cycle": 18444,
  "event_id": "evt-18444-003",
  "input_digest": "sha256:...",
  "boundary_digest": "sha256:...",
  "implementation": {"name": "noema-replay", "version": "...", "digest": "sha256:..."},
  "schema_digests": {},
  "previous_record_digest": "sha256:...",
  "record_digest": "sha256:...",
  "decision": "equivalent",
  "reason_codes": [],
  "claim_label": "OBSERVED",
  "private_artifact_digests": []
}
```

The audit stream MUST cover validation, input resolution, integrity checks, runtime construction, each state transition, random draw, comparison, divergence, stop decision, and final classification. Records are hash chained. Corrections append superseding records and never rewrite history. Sensitive values remain in the appropriate private partition; public records carry safe identifiers and digests only.

## Failure handling

| Condition | Required result |
|---|---|
| Missing input, artifact, schema, version, digest, external response, or executable predicate | `NOT_COMPUTABLE` |
| Digest mismatch, broken ledger chain, impossible ordering, forged provenance, or snapshot inconsistency | `INVALID_EVIDENCE` |
| Required comparison mismatch | `DIVERGENT` |
| Operator cancellation, budget exhaustion, or containment shutdown | `ABORTED` |
| Unsupported stochastic dependency in a deterministic mode | `NOT_COMPUTABLE` |
| Equivalent boundary with failed non-required diagnostic | `EQUIVALENT` only if the diagnostic is explicitly non-claim-bearing; record the failure |

Failures MUST retain partial audit and checkpoints, identify the earliest known failing cycle/event, and state whether the failure invalidates the tested claim. Retries create new request IDs linked to the prior request. No failure may be converted to equivalence by widening the boundary after observing the result. A changed boundary is a new experiment.

## Research and security limits

Replay outputs use `OBSERVED`, `INFERRED`, `SPECULATIVE`, and `NOT_COMPUTABLE` labels from the Research Method. An `EQUIVALENT` result is an observation under a declared boundary. Interpretations remain separately labeled. Consent, retention, exclusion, prompt-injection, secret handling, provider-key isolation, and public/private partitioning apply during replay exactly as during collection.

## Implementation order

1. Canonical JSON, artifact hashing, immutable version resolution, and schema validation.
2. Event-ledger integrity and canonical ordering verification.
3. Equivalence-boundary validator and pure projection/comparison engine.
4. Deterministic world replay with disabled undeclared inputs and named random streams.
5. Checkpoint, divergence, and hash-chained audit writers.
6. Deterministic protocol replay.
7. Behavioral equivalence predicates and tolerance support.
8. Stochastic-agent replay with recorded external responses and explicit claim limits.
9. Property, tamper, migration, privacy, and end-to-end reproduction tests.

Later stages MUST NOT be used to bypass an unmet earlier integrity or determinism requirement.
