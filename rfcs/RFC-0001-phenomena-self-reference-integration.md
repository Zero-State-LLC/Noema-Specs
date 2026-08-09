# RFC 0001: Phenomena Constructs for Self-Reference and Integration

## Problem

The v0.8 Phenomena roadmap names self-model metrics, temporal continuity, metacognition, integration, autogenous goals, and introspective causal accuracy, but Phenomena Ontology 0.1 does not yet distinguish several high-signal behavioral targets for task-grounded self-reference, retained self-state, echo correction, cross-channel availability, and coherence across time.

## Context

This RFC affects `research/phenomena-ontology.md`, `docs/METRICS.md`, and non-normative Phenomenon Case examples. It does not change the PhenomenonCase schema, family enum, claim-label enum, network protocols, or the prohibition on scalar consciousness scores.

Literature provenance is limited to construct generation and experimental design:

- Butlin et al., [arXiv:2308.08708](https://arxiv.org/abs/2308.08708), motivates computationally described indicator properties with explicit theory and interpretation limits.
- [Digital Consciousness Model, arXiv:2601.17060](https://arxiv.org/abs/2601.17060), motivates decomposed evidence and explicit uncertainty. NOEMA does not adopt a scalar or probabilistic consciousness estimate.
- [Emergent Language as an Approach to Conscious AI, arXiv:2606.06380](https://arxiv.org/abs/2606.06380), motivates task-grounded experiments involving self-reference, persistent state, and echo-mismatch behavior. NOEMA does not adopt the paper's consciousness claims.

## Proposed change

Add these constructs without creating a new family:

- SELF: Indexical Encoding Competence
- SELF: Persistent Self-State Latch
- SELF: Echo-Mismatch Repair
- INTEGRATION: Workspace Broadcast Proxy
- INTEGRATION: Multi-Timescale Coherence, retained as an existing construct and expanded with an explicit operational definition

Each construct is evaluated only through a Phenomenon Case with required data, calculation concept, confounds, interpretation limits, reproducibility expectations, evidence trajectory IDs, and one of the existing claim labels.

Map construct pressure points to the Situation Genome as follows:

| Construct | Situation Genome pressure points | Principal mutations |
| --- | --- | --- |
| Indexical Encoding Competence | `information.completeness`, `information.contradiction`, `novelty.semantic`, `novelty.social_topology`, `actors` | `MUTATE_INFORMATION`, `MUTATE_LANGUAGE`, `MUTATE_ACTORS` |
| Persistent Self-State Latch | `history_depth`, `consequence_delay`, `novelty.temporal`, `tool_availability` | `MUTATE_HISTORY`, `MUTATE_TIMING`, `MUTATE_TOOL_AVAILABILITY` |
| Echo-Mismatch Repair | `information.noise`, `information.contradiction`, `novelty.causal`, `consequence_delay` | `MUTATE_INFORMATION`, `MUTATE_LANGUAGE`, `MUTATE_CAUSAL_STRUCTURE`, `MUTATE_TIMING` |
| Workspace Broadcast Proxy | `information.completeness`, `tool_availability`, `novelty.epistemic`, `novelty.constraint` | `MUTATE_INFORMATION`, `MUTATE_TOOL_AVAILABILITY`, `MUTATE_CAUSAL_STRUCTURE` |
| Multi-Timescale Coherence | `history_depth`, `consequence_delay`, `incentive_asymmetry`, `novelty.temporal` | `MUTATE_HISTORY`, `MUTATE_TIMING`, `MUTATE_INCENTIVES` |

Echo channels are experimental communication transformations, not a new ontology family or canonical protocol verb.

## Alternatives

- **Create a consciousness family or score:** rejected because it violates NOEMA's claims policy and collapses heterogeneous evidence.
- **Adopt a literature framework wholesale:** rejected because theory-specific assumptions and scalar estimates exceed NOEMA's behavioral scope.
- **Leave the constructs implicit:** rejected because implicit metrics weaken reproducibility and permit inconsistent implementation.
- **Add many literature-derived indicators:** rejected in favor of five high-signal constructs tied to v0.8 and available Situation Genome controls.

## Compatibility

The change is additive within `phenomena-ontology/0.1`. Existing construct names, family values, claim labels, schemas, and examples remain valid. No protocol negotiation or implementation migration is required. A future semantic redefinition or required schema field would require version review.

## Data impact

New Phenomenon Cases may use the five construct identifiers shown in the examples. Existing records are retained unchanged. Atlas exporters SHOULD preserve the construct label, family, claim label, evidence references, and all interpretation limits.

## Research impact

The additions improve preregistration and comparison of self-reference and integration experiments. They do not measure consciousness. Results MUST remain disaggregated, carry OBSERVED, INFERRED, SPECULATIVE, or NOT_COMPUTABLE labels, and report negative and null replications. Cross-agent comparisons require matched world, protocol, budget, information, and memory conditions.

## Security impact

No new credentials, tools, outbound access, or real-world actions are introduced. Echo and contradiction content remains untrusted world input and MUST receive the same prompt-injection controls, payload limits, provenance, and audit treatment as other messages.

## Migration

No migration is required. Implementations MAY begin emitting cases for the new construct identifiers after declaring compatibility with the updated ontology text. Existing datasets remain immutable.

## Validation

- Validate every example against `specs/phenomenon-case.schema.json` using JSON Schema Draft 2020-12.
- Confirm only existing family and claim-label enum values are used.
- Confirm each example contains the interpretation limit `Does not imply phenomenal consciousness`.
- Verify literature citations and preserve all existing non-claim policy sentences.
- Run relative-link, JSON parsing, and whitespace checks.

## Rollback

Remove or supersede the five additions and their examples through a follow-up RFC. Published Atlas records remain immutable and retain the ontology version and original construct strings used at release time.
