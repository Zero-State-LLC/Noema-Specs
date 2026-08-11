# Phenomenon Compiler

## Purpose

The Phenomenon Compiler converts interesting live-world behavior into minimal reproducible state, replayable fixture, behavioral regression test, and Reproducibility Bundle. It is delta debugging for autonomous cognition.

**Executable package (v0.5):** [releases/v0.5/](releases/v0.5/) · schemas under `specs/*` · fixtures [`examples/v05-compiler/`](../examples/v05-compiler/) · conformance **P01–P30**. Ordinary product entry is STUDY **CAPTURE AS TEST** via [Capture Intent Compilation](CAPTURE-INTENT-COMPILATION.md). This document remains subsystem authority; release packages define only the delta.

### Usability invariant (v0.5)

v0.5 MUST reduce implementation ambiguity without increasing ordinary-user conceptual burden. Machine concepts remain internal or have plain-language STUDY projections. Complexity may increase internally while conceptual burden decreases externally.

## Pipeline

1. Ingest candidate event or trajectory.
2. Verify consent, retention, and security labels.
3. Minimize world state while preserving behavior under equivalence criteria.
4. Minimize agent-visible observations and messages.
5. Generate perturbations and controls.
6. Validate replay.
7. Package fixture, metrics, and report.
8. Register candidate in Capability Graph or Phenomena Lab.

## Admission gates

No bundle may be promoted without schema validity, provenance, replay attempt, claim labels, confounds, private/public partitioning, and version declarations.

## Exact input contract

Compilation begins from one immutable request:

| Field | Exact requirement |
|---|---|
| `compile_id` | Unique compilation request ID. |
| `candidate_id` | Stable candidate phenomenon/capability event ID. |
| `source_trajectory` | Content-addressed ordered event ledger plus snapshot, world seed, world version, protocol versions, deterministic config, and external inputs. |
| `candidate_interval` | Inclusive start and end cycle/event IDs. |
| `target_behavior` | Versioned executable observation/outcome predicates and claim label. |
| `equivalence_boundary` | Exact, ignored, tolerated, and semantic comparison fields as defined in [Replay](REPLAY.md). |
| `removable_units` | Stable IDs for state objects, events, observations, messages, agents, tools, and configuration fields eligible for minimization. |
| `dependency_graph` | Versioned directed dependencies and closure rules among removable units. |
| `required_controls` | Positive, negative, replay, leakage, seed, resource, and other applicable controls. |
| `perturbation_space` | Finite typed operators, parameter domains, and canonical enumeration order. |
| `budgets` | Maximum oracle calls, replay cycles, wall time, storage, and perturbations. |
| `policy_context` | Consent, retention, exclusions, security labels, and public/private export classes. |
| `compiler_version` | Compiler, replay oracle, schema, ontology, and canonicalization versions and digests. |

The target behavior MUST be declared before minimization. It cannot be replaced with a weaker predicate after seeing failures. Missing artifacts, dependencies, or executable predicates yield `NOT_COMPUTABLE`.

## Behavioral oracle

The compiler's only claim-bearing oracle is:

```text
oracle(fixture, target, boundary, replication_plan) ->
  PRESERVED | NOT_PRESERVED | INCONCLUSIVE | INVALID
```

`PRESERVED` requires valid replay and satisfaction of every target and boundary predicate at every required observation point. `NOT_PRESERVED` is an observed valid replay that misses a required predicate. `INCONCLUSIVE` covers permitted stochastic replay that does not meet the predeclared replication decision rule or exhausts its budget. `INVALID` covers schema, integrity, provenance, policy, or replay failures.

For stochastic agents, the replication plan MUST declare seeds or recorded provider responses, run count, success threshold, confidence calculation, and stopping rule before compilation. An inconclusive result is never treated as preserved.

## Deterministic minimization algorithm

The compiler uses dependency-closed hierarchical delta debugging. Given removable units sorted by stable ID:

1. Validate policy, provenance, schemas, digests, source replay, target predicate, boundary, dependency graph, and budgets. The unmodified source MUST return `PRESERVED`; otherwise compilation stops.
2. Partition units by layer in this order: world/configuration, entities and agents, events/actions, observations/messages, tools/resources, then non-claim-bearing metadata. A unit assigned to multiple layers is processed in the earliest layer.
3. For each layer, run `ddmin` over the current removable set. Start with granularity `n = 2`. Partition the sorted units into `n` contiguous chunks whose sizes differ by at most one.
4. For each chunk in order, propose removing that chunk, then compute dependency closure. If a retained unit depends on a removed unit, either remove the dependent unit when it is eligible or reject the proposal when it is protected. Never synthesize replacement evidence.
5. Canonicalize the proposed fixture and use its digest as the oracle-cache key together with target, boundary, replay, and replication-plan digests.
6. If the oracle returns `PRESERVED`, accept the removal, record it, set the candidate set to the remaining units, and set `n = max(n - 1, 2)`.
7. If no chunk can be removed, test complements in the same canonical order. Accept the first `PRESERVED` complement.
8. If neither chunks nor complements succeed, set `n = min(2n, unit_count)`. Stop the layer when `n == unit_count` and no single unit can be removed.
9. `INCONCLUSIVE`, `INVALID`, timeout, or budget exhaustion never authorizes removal. Record the result and retain the units.
10. Repeat complete layer passes until a pass accepts no removal. Then perform a final one-unit sweep over all remaining removable units in stable-ID order.

Pseudocode:

```text
fixture := source
assert oracle(fixture) == PRESERVED
for layer in ordered_layers:
  fixture := ddmin_dependency_closed(fixture, sorted(units(layer)))
repeat:
  changed := false
  for unit in sorted(all_remaining_units):
    proposal := dependency_closed_remove(fixture, {unit})
    if oracle(proposal) == PRESERVED:
      fixture := proposal
      changed := true
until not changed
```

The result is 1-minimal over declared units and closure rules: no single remaining eligible unit can be removed while preserving the oracle. It is not claimed to be globally minimum. Oracle cache entries are reusable only under identical canonical compiler, input, target, boundary, replay, and replication identities.

## Perturbations and controls

After minimization, enumerate perturbations by `(operator_id, canonical_parameter_tuple)` and derive any seeded value with `HMAC-SHA-256(source_seed, compile_id || operator_id || parameter_tuple)`. Each perturbation changes only its declared independent variables. Controls run against the same minimized fixture and replay boundary.

Required control failure does not delete the bundle. It blocks promotion and is reported with `OBSERVED` results, confounds, and failed-control reasons. Prompt or environment leakage, undeclared instruction presence, or provenance failure invalidates the affected interpretation.

## Outputs

The compiler emits a Reproducibility Bundle matching [Reproducibility](REPRODUCIBILITY.md), plus:

1. `compile-result.json`: status (`COMPILED`, `NOT_COMPUTABLE`, `INVALID_EVIDENCE`, `INCONCLUSIVE`, `ABORTED`, or `BUDGET_EXHAUSTED`), source/minimal digests, target and boundary digests, unit counts, oracle counts, promotion status, and audit root digest.
2. `minimization-audit.jsonl`: every proposal, dependency closure, oracle result, cache decision, acceptance, and rejection.
3. `unit-manifest.json`: stable unit IDs, layers, protection status, dependencies, and final disposition.
4. `controls.jsonl` and `perturbations.jsonl`: exact changed variables, seeds, outcomes, metrics, and claim labels.
5. `replay-result.json` and divergence artifacts from final validation.
6. `report.md`: operational definition, result, confounds, limits, failed controls, and links to evidence. It MUST NOT exceed the supported claim.

## Compile receipt and audit records

Every compilation, including `NOT_COMPUTABLE`, emits a receipt containing:

```json
{
  "receipt_version": "phenomenon-compile-receipt/v1",
  "compile_id": "compile-NP-000381-001",
  "status": "COMPILED",
  "compiler_identity": {"version": "...", "digest": "sha256:..."},
  "corpus_identity": {"version": "...", "digest": "sha256:..."},
  "schema_bundle_identity": {"version": "...", "digest": "sha256:..."},
  "provider_adapter_identity": {"version": "...", "digest": "sha256:..."},
  "command": ["phenomenon-compiler", "compile"],
  "command_digest": "sha256:...",
  "normalized_input_digest": "sha256:...",
  "source_trajectory_digest": "sha256:...",
  "target_digest": "sha256:...",
  "equivalence_boundary_digest": "sha256:...",
  "minimal_fixture_digest": "sha256:...",
  "audit_root_digest": "sha256:..."
}
```

The corpus identity names the content-addressed template, ontology, control, and predicate corpus used by the compiler. Provider-adapter identity is required even when no provider is invoked; use a canonical `none` adapter identity rather than omitting it. Command identity covers the exact argument vector after path-independent normalization. These identities establish deterministic provenance and MUST be present for unsuccessful results.

Each audit record includes audit version, compile ID, monotonic record index, phase, proposal ID and digest, removed and closure unit IDs, oracle identity and result, replay request/result digest, budget before and after, decision and reason codes, previous-record digest, record digest, and protected-artifact references. Audit logs are append-only. Corrections supersede prior records without erasing lineage.

## Equivalence boundary

The source and minimized fixture are equivalent only with respect to the predeclared replay and target boundary. The compiler MUST compare:

- exact state and observation paths;
- ordered and normalized unordered collections;
- declared numeric tolerances and semantic predicates;
- target behavior at every observation point;
- required protocol validation and event ordering outcomes.

Excluded host metadata, timestamps, provider request IDs, or log formatting must be named before compilation. Fixture equivalence does not imply identical hidden reasoning, causal mechanism, transfer performance, general capability, emergence, or consciousness. A new target, predicate implementation, tolerance, observation point, or ignored field creates a new compilation identity.

## Failure handling

- Policy, consent, retention, or security violation: stop before further payload access, emit a redacted receipt, preserve authorized audit evidence, and block promotion.
- Missing input/version/schema/predicate or unavailable replay dependency: `NOT_COMPUTABLE`.
- Broken digest, ledger chain, snapshot lineage, or forged provenance: `INVALID_EVIDENCE` and quarantine.
- Source does not preserve target behavior: `INCONCLUSIVE` or `INVALID_EVIDENCE` according to replay validity; do not minimize.
- Oracle disagreement for the same identity: invalidate the cache and compilation, retain both results, and open a determinism defect.
- Budget exhaustion: return the smallest verified fixture reached, status `BUDGET_EXHAUSTED`, no minimality claim, and no automatic promotion.
- Cancellation or containment shutdown: `ABORTED`, retaining partial audit and last verified fixture.
- Required-control failure: compilation may complete, but promotion is blocked and the failed control is reported.

Retries create linked compile IDs. No retry may silently change the target, boundary, source, versions, control plan, or policy context.

## Promotion decision

Promotion is a deterministic gate, not editorial judgment. A bundle is promotable only when schema and digest validation pass, the final source-to-fixture replay is `EQUIVALENT`, the target is `PRESERVED`, all mandatory controls have determinate acceptable outcomes, provenance is complete, claim labels and confounds are present, policy checks pass, version declarations are complete, and public/private partition validation succeeds. Otherwise the bundle remains a candidate with explicit blocking reasons.

Promotion supports only a reproducible behavior claim under stated conditions. Research interpretations continue to follow [Research Method](RESEARCH-METHOD.md), including `OBSERVED`, `INFERRED`, `SPECULATIVE`, and `NOT_COMPUTABLE` labels. The compiler MUST NOT infer consciousness or create a scalar consciousness score.

## Implementation order

1. Canonicalization, content hashing, receipt identities, schema/version resolution, and policy gates.
2. Replay oracle integration and executable equivalence/target predicate validation.
3. Stable unit extraction, dependency graph validation, and protected-unit rules.
4. Deterministic dependency-closed `ddmin` with memoized oracle calls.
5. Final one-unit minimality sweep and minimality report.
6. Perturbation/control enumeration and predeclared replication decisions.
7. Reproducibility Bundle packaging, partition enforcement, and hash-chained audit.
8. Deterministic promotion gate and registry integration.
9. Property, mutation, tamper, stochastic-boundary, privacy, budget, and end-to-end reproduction tests.

Each stage MUST be independently testable. Registry integration MUST NOT precede reliable replay, provenance, policy, and promotion gates.
