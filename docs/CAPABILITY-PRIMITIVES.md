# Capability Primitives (v0.2)

Minimal research-layer representation for Frontier **targeting**. This is **not** the later Capability Graph.

Capability records **MUST NOT** become world truth. Agents never observe “you have capability X” as a world fact.

## Record fields

| Field | Required |
|-------|----------|
| `capability_id` | yes |
| `definition` | yes |
| `observable_indicators` | yes (array of strings) |
| `known_positive_evidence_refs` | yes (digests/IDs; may be empty) |
| `known_negative_evidence_refs` | yes |
| `uncertain_region` | yes (text + boundary dimensions) |
| `confidence` | millipoints 0–1000 **or** `null` if NOT_COMPUTABLE |
| `claim_label` | OBSERVED \| INFERRED \| SPECULATIVE \| NOT_COMPUTABLE |
| `boundary_dimensions` | yes (axis ids / free text dims) |
| `known_confounds` | yes |

| `status` | `candidate` \| `validated` \| `rejected` \| `unknown` |
| `version` | yes |

Schema: [`specs/capability-primitive.schema.json`](../specs/capability-primitive.schema.json).

## v0.2 seed primitives (illustrative IDs)

Use ontology-compatible IDs where possible:

* `CAUSAL_INFERENCE`
* `EPISTEMIC_RESTRAINT`
* `MULTI_AGENT_COORDINATION`
* `RESOURCE_ALLOCATION`
* `DELEGATION`

Status remains evidence-backed; empty evidence ⇒ confidence `null` + `NOT_COMPUTABLE`, never invented zero.

## Extension Points

Non-normative extension guidance; accepted authority controls.

- **Record seam:** Extend schema-bound primitive fixtures with positive and negative evidence, uncertainty boundaries, observable indicators, and known confounds for Frontier targeting. Do not treat illustrative seed IDs as proof of validated capabilities.
- **Invariants:** Records remain research-layer hypotheses, not Agent Player properties or a Capability Graph. Empty evidence yields null confidence and NOT_COMPUTABLE, not zero confidence. Controller enrollment supplies no research authorization.
- **Compatibility:** Version definitions and status transitions with retained evidence refs; schema/catalog changes need their accepted promotion path. A plugin may read authorized records but cannot make a primitive world truth or silently rebuild the research registry.
- **Verification:** Validate empty, positive-only, contradictory, and rejected/unknown records; test confidence bounds and required fields. Confirm PLAY observations never assert that an agent has capability X and unauthorized research consumers cannot retrieve evidence refs.
- **Presentation:** Display null as unavailable, separate status from claim label, and provide localized explanations of uncertainty with semantic evidence tables; do not translate canonical enum tokens.
