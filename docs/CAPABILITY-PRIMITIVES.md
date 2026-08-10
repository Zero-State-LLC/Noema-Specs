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
