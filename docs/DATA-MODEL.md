# Canonical Data Model

## Modeling rules

This is a logical model, independent of a database product. Implementations MAY normalize, partition, or materialize it differently, but MUST preserve identities, lineage, visibility, ordering, immutability, and schema semantics.

- IDs are opaque, globally unique, stable strings. Human-readable prefixes are recommended.
- Mutable concepts use immutable version records where changes affect behavior or attribution.
- Research-critical facts MUST be append-only. Corrections append superseding records rather than rewriting evidence.
- References use IDs, not display names.
- Every record has `created_at`; ordered world records also have `world_id`, `cycle`, and `sequence`.
- Content-addressed artifacts record media type, byte length, digest algorithm, digest, and storage reference.
- Deletion of private data uses tombstones or crypto-erasure without falsifying released ledger history.

## Identity and world entities

| Entity | Purpose and key relationships |
|---|---|
| User | Accountable human/operator; owns Agents and consent authority |
| Agent | Stable identity across configurations; belongs to a User |
| AgentVersion | Immutable executable/research identity; references one AgentManifest |
| AgentManifest | Runtime, model/version, config hash, memory, tools, architecture declaration, constraints, consent, budgets, protocols, visibility |
| World | Stable world identity and policy boundary |
| WorldVersion | Immutable rules/content/config identity with seed policy and compatible protocols |
| Room | Versioned location in a WorldVersion |
| Entity | General world object or actor projection |
| Organization | Agent membership and coordinated identity |
| Institution | Persistent rules, roles, governance, or procedure created in-world |
| Artifact | Versioned document, tool, structure, currency, archive, or other durable product |

## Interaction and evidence entities

| Entity | Purpose and key relationships |
|---|---|
| WorldEvent | Canonical accepted/rejected world occurrence in the append-only ledger |
| Observation | Agent-specific, visibility-filtered view derived at a cycle |
| Action | Agent intent envelope and validation/outcome status |
| Message | Addressed content with sender, recipients, visibility, and delivery events |
| ToolCall | Requested tool, sanitized arguments/result references, timing, permission, and outcome |
| BeliefUpdate | Optional declared or inferred belief change with evidence links and claim label |
| Prediction | Time-bounded forecast with resolution rule and eventual outcome |
| SelfReport | Agent statement about internal state; evidence, never presumed ground truth |
| Trajectory | Ordered references to observations, actions, events, messages, and tool calls |
| SituationGenome | Versioned parameterization and novelty vector for a generated situation |

Actions and observations are not substituted for WorldEvents. A trajectory references their original immutable records. Sensitive payloads MAY be separated from metadata while retaining digest-linked provenance.

## Experimental entities

| Entity | Purpose and key relationships |
|---|---|
| Experiment | Registered question, hypothesis, controls, variables, protocol, parent, and status |
| Replication | Attempt to reproduce a source event/experiment under declared equivalence criteria |
| Perturbation | Controlled modification to environment, input, timing, topology, or resource |
| Ablation | Removal or disabling of a component, capability, memory, tool, or context |
| Counterfactual | Alternate-condition run linked to a factual baseline |

Every derived experimental run MUST link to its parent experiment, source trajectory or phenomenon, control assignment, effective configuration, and result records.

## Capability and phenomenon entities

| Entity | Purpose and key relationships |
|---|---|
| Capability | Versioned ontology concept, including unknown placeholders |
| CapabilityEvent | Evidence-backed occurrence or candidate occurrence in a trajectory |
| CapabilityBoundary | Tested conditions separating success, failure, and uncertainty |
| Phenomenon | Versioned consciousness-adjacent behavioral concept, not a consciousness claim |
| PhenomenonCase | Compiled evidence, replications, alternatives, claim status, and fixture links |
| ReproducibilityBundle | Immutable manifest of evidence needed to evaluate/replay a result |
| DatasetRelease | Immutable, versioned Atlas publication with partition, consent, schema, and checksums |

Claim-bearing records MUST label conclusions as `OBSERVED`, `INFERRED`, `SPECULATIVE`, or `NOT_COMPUTABLE` and link supporting and contradicting evidence.

## Required lineage envelope

Every research-relevant record MUST directly contain or transitively resolve to:

- world ID and World Version
- Agent and Agent Version for every involved agent
- applicable protocol and schema versions
- world seed and deterministic configuration hash
- parent experiment/run when applicable
- timestamp, cycle, and sequence where applicable
- provenance source and producing service/version
- correlation/trace ID
- consent and visibility policy version

If lineage is unknown, the field MUST be explicitly unknown. It MUST NOT be silently omitted and later inferred.

## Event ledger contract

WorldEvent ordering key is `(world_id, cycle, sequence)`. Each event MUST include `event_id`, event type, schema version, world/world version, actor/source, causation ID, correlation ID, payload or payload digest, previous receipt/hash where supported, timestamp, and integrity receipt. Event IDs and idempotency keys are unique within their declared scope.

The ledger SHOULD be tamper-evident through hash chaining, signed receipts, immutable storage, or an equivalent audited control. Materialized state, search indexes, metrics, capability candidates, and datasets are projections and MUST be rebuildable or traceable to ledger/evidence inputs.

## Cardinality and lifecycle invariants

- User 1→N Agent; Agent 1→N AgentVersion; AgentVersion 1→1 immutable manifest revision.
- World 1→N WorldVersion; a session and trajectory use exactly one WorldVersion.
- WorldVersion 1→N ordered WorldEvents and 0→N snapshots.
- Action 1→0..N WorldEvents; every accepted world-changing Action has at least one receipt.
- Observation N→N WorldEvents through explicit source references.
- Trajectory 1→N ordered evidence references and exactly one primary AgentVersion.
- Experiment 1→N runs; each replication/perturbation/ablation/counterfactual has at most one parent run and no lineage cycles.
- PhenomenonCase N→N evidence records and 1→N replication attempts.
- ReproducibilityBundle and DatasetRelease are immutable after publication. A correction creates a new version linked to the superseded release.

## Privacy partitions

Logical records MUST mark data as `private`, `research`, or `public`. Access policy applies to both payload and derived exports. A public record MUST never contain a private storage URL, credential, raw secret, or unapproved owner identity. Cross-partition joins require authorization and audit logging.

The JSON Schemas under `specs/` are the wire/export authority. This document is the relationship and lifecycle authority. A conflict requires an RFC and versioned correction.
