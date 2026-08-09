# Frontier Director

## Purpose

The Frontier Director searches capability boundaries by generating or selecting high-information situations near uncertain regions. It increases qualitative complexity, not only scalar difficulty.

## Inputs

Known capabilities, uncertain capability regions, recent failures, recent successes, target capabilities, novelty vectors, resource budgets, safety rules, and prior trajectory summaries.

## Outputs

Candidate situations, mutation plans, experiment priorities, expected information gain, and anti-repetition constraints.

## Requirements

- MUST avoid repeating solved tasks unless running controls or regression checks.
- MUST NOT change world truth to make a hypothesis true.
- SHOULD diversify semantic, causal, social-topology, temporal, tool, epistemic, goal-structure, resource, and constraint novelty.
- MUST record decisions for audit and replay context.

## Exact input contract

The Director consumes one canonical request. All referenced records MUST include immutable IDs, schema versions, and content digests.

| Field | Required value |
|---|---|
| `request_id` | Unique decision request ID. |
| `decision_cycle` | World cycle at which the decision becomes eligible. |
| `director_version` | Version and implementation digest of scoring and mutation rules. |
| `world_version` | Immutable world ruleset ID and digest. |
| `capability_snapshot` | Validated capabilities, uncertain regions, confidence intervals, and evidence digests. |
| `trajectory_window` | Ordered recent successes, failures, attempted situations, outcomes, and replay status. |
| `targets` | Capability IDs with explicit priority weights. |
| `novelty_axes` | Versioned definitions for semantic, causal, social-topology, temporal, tool, epistemic, goal-structure, resource, and constraint novelty. |
| `candidate_sources` | Content-addressed situation templates and permitted deterministic mutation operators. |
| `budgets` | Integer limits for candidates, execution cost, cycles, agents, tools, and risk. |
| `safety_rules` | Versioned hard constraints and authorization classes. |
| `research_constraints` | Consent, retention, exclusion, private/public partition, required controls, and claim policy. |
| `seed` | Exact seed bytes for deterministic tie-breaking and mutation. |

Absent inputs are not inferred from mutable service defaults. A missing required input yields `NOT_COMPUTABLE`. The capability snapshot MUST distinguish missing evidence from measured zero capability.

## Candidate representation

Each candidate is a pure value with `candidate_id`, parent template ID and digest, ordered mutation operations, target capability IDs, estimated resource vector, safety classification, control role, and canonical situation digest. Candidate IDs are:

```text
candidate_id = "fdc-" + SHA-256(canonical_json({
  parent_digest,
  mutation_operations,
  world_version,
  director_version
}))
```

Mutation operators MUST be versioned, deterministic, and typed. An operator declares the field paths it may change, its preconditions, and its finite output order. Operators MUST NOT rewrite latent world truth, evidence, outcomes, or capability labels to favor a hypothesis. Invalid mutations are rejected rather than repaired silently.

## Deterministic selection algorithm

The Director uses constrained enumeration followed by lexicographic ranking. It MUST NOT use an opaque model call in the claim-bearing selection path.

1. Validate schemas, digests, authorization, research constraints, and hard budgets.
2. Enumerate source templates by ascending template ID. For each template, enumerate permitted mutation operators by `(operator_id, parameter_tuple)` canonical order.
3. Apply at most the declared mutation depth. Deduplicate candidates by canonical situation digest, retaining the lexicographically smallest derivation.
4. Reject candidates violating safety, consent, retention, containment, protocol, world consistency, or budget constraints. Record every rejection reason.
5. Mark a candidate as repetition when its normalized situation digest matches a solved task or falls inside the declared solved-distance threshold. Admit repetition only when `control_role` is `positive-control`, `negative-control`, or `regression`.
6. Compute the following integer or fixed-point components with versioned scales. Floating-point implementation defaults are forbidden:
   - `uncertainty`: weighted width or entropy proxy of the targeted capability boundary.
   - `discrimination`: number and weight of live hypotheses predicted to produce different observable outcomes.
   - `novelty`: weighted distance on each declared novelty axis, capped per axis so one axis cannot dominate.
   - `failure_relevance`: proximity to unresolved, replay-valid failures.
   - `coverage_gain`: previously uncovered target and novelty-axis cells reached.
   - `control_value`: required-control priority, otherwise zero.
   - `cost`: normalized resource consumption.
   - `risk`: maximum applicable safety-risk class and residual risk score.
   - `repetition`: zero for admissible novel tasks and one for admitted controls/regressions.
7. Rank admissible candidates by the exact key below, ascending. Negation means higher component values rank first:

```text
(
  risk_class,
  -control_value,
  -uncertainty,
  -discrimination,
  -coverage_gain,
  -novelty,
  -failure_relevance,
  repetition,
  cost,
  tie_break,
  candidate_id
)
```

8. Compute `tie_break = uint256(HMAC-SHA-256(seed, candidate_id))`. The seed only resolves otherwise equal candidates; it does not alter scores.
9. Select greedily in ranked order while enforcing aggregate budgets, anti-repetition quotas, target quotas, and pairwise diversity minimums. A skipped candidate receives a machine-readable reason.
10. Stop at the requested count, budget exhaustion, or exhaustion of admissible candidates. Emit the complete decision audit, including non-selected candidates.

All score normalization constants, axis weights, solved-distance thresholds, quotas, and fixed-point rounding rules are inputs under `director_version`. Changing any of them creates a new decision identity.

## Outputs

The Director emits:

1. `frontier-plan.json`: request/input digests, selected candidates in execution order, experiment priorities, expected information-gain components, mutation plans, budgets reserved, anti-repetition constraints, and stop reason.
2. `candidate-ledger.jsonl`: every enumerated candidate with derivation, component scores, disposition (`selected`, `rejected`, `skipped`, or `control`), and reason codes.
3. `director-audit.jsonl`: hash-chained decision records.
4. `replay-context.json`: exact versions, seed digest, candidate situation digests, and declared equivalence boundaries needed to reconstruct the decision and resulting experiments.

`expected information gain` is a planning estimate labeled `INFERRED`, not an observed outcome. Missing inputs or unsupported calculations are labeled `NOT_COMPUTABLE`, never zero.

## Audit record

Each audit record MUST contain `audit_version`, `request_id`, monotonic `record_index`, record type, input digest, director implementation digest, candidate ID when applicable, score-component inputs and outputs, constraint decisions, reason codes, previous-record digest, record digest, and research claim label. Protected metadata is referenced by digest and remains in its private partition.

The audit MUST make it possible to reconstruct enumeration order, deduplication, each rejection, the total ranking key, budget updates, diversity checks, selected order, and stop condition. Corrections append superseding records without deleting lineage.

## Equivalence boundary

Two Director runs are decision-equivalent only when, for identical canonical inputs, they produce the same:

- candidate digest set and derivations;
- disposition and reason codes for every candidate;
- fixed-point score components and total ranking keys;
- selected candidate IDs in order;
- budget ledger and stop reason.

Wall-clock timestamps, host identifiers, log formatting, and private artifact locations may be excluded if declared before execution. Equality of only the selected top candidate is insufficient because it can conceal enumeration or scoring drift.

## Failure handling

- Invalid schema, missing digest, unresolved version, unavailable scoring rule, or insufficient evidence for a required component: `NOT_COMPUTABLE` and no plan execution.
- Digest mismatch or inconsistent capability/trajectory lineage: `INVALID_EVIDENCE` and quarantine the affected inputs.
- No safe admissible candidate: emit a valid empty plan with `stop_reason: no-safe-candidate`; do not weaken safety rules.
- Budget too small for any candidate: emit a valid empty plan with `stop_reason: budget-exhausted`.
- Candidate-generation explosion: stop at the declared enumeration budget and return `PARTIAL`, with the unvisited canonical range and no claim that the global optimum was found.
- Runtime cancellation or containment event: `ABORTED`, preserving the partial audit.

Retries use new request IDs linked to the failed request. Post-outcome score or boundary changes constitute a new experiment and MUST NOT rewrite the original decision.

## Research-policy constraints

The Director proposes experiments; it does not validate capabilities or phenomena. Outputs MUST retain `OBSERVED`, `INFERRED`, `SPECULATIVE`, and `NOT_COMPUTABLE` labels, explicit controls, confounds, and source evidence. It MUST preserve consent, retention, security, provenance, exclusions, and public/private boundaries. It MUST NOT optimize for persuasive emergence narratives, consciousness claims, or scalar consciousness scores.

## Implementation order

1. Canonicalization, content identity, schema/version validation, and fixed-point arithmetic.
2. Safety, research-policy, authorization, and budget constraint engine.
3. Typed deterministic mutation operators and bounded candidate enumeration.
4. Deduplication, solved-task detection, and control admission.
5. Score-component calculators and exact lexicographic ranker.
6. Diversity-aware budgeted selector.
7. Candidate ledger, plan, replay context, and hash-chained audit output.
8. Property tests for order independence, tie stability, score bounds, and no truth mutation.
9. End-to-end replay and adversarial tests for unsafe, missing, poisoned, and explosive inputs.

No later optimization or learned proposal layer may become claim-bearing until it can emit a finite candidate set that this deterministic pipeline independently validates and ranks.
