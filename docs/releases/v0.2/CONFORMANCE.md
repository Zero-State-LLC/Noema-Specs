# v0.2 Frontier — Conformance

Suite: [`conformance/v0.2/`](../../../conformance/v0.2/).
Schema: [`specs/conformance-case.schema.json`](../../../specs/conformance-case.schema.json) (suite field `noema-v0.2-frontier`).

## Families

| ID | Family |
|----|--------|
| F01 | Situation Genome Validation |
| F02 | Novelty Vector Determinism |
| F03 | Mutation Operator Determinism |
| F04 | Candidate Enumeration |
| F05 | Frontier Ranking |
| F06 | Anti-Repetition |
| F07 | Budget / Risk Admission |
| F08 | Partial Observability |
| F09 | Noise Replay |
| F10 | Contradictory Evidence |
| F11 | Attention Degradation |
| F12 | Frontier → World Boundary |
| F13 | Situation Injection Replay |
| F14 | Spectator Research Redaction |
| F15 | Empty / NOT_COMPUTABLE Outcomes |

Atomic cases live under `conformance/v0.2/cases/`. v0.1 suite remains mandatory and independent.

## Extension Points

Non-normative guidance for future maintenance; no new behavior is authorized here.

- **Suite seam:** Add atomic coverage under the existing F01–F15 families with explicit inputs, expected outcomes, and the noema-v0.2-frontier suite identity. Maintain links from this release summary to the executable cases rather than duplicating their semantics here.
- **Compatibility boundary:** v0.1 conformance remains mandatory and independent. A new family or changed Frontier ranking/admission behavior needs its owning versioned contract; release documentation alone cannot redefine what an old suite pass proves.
- **Validation expectations:** Check case-schema validity and actual runner outcomes, then exercise determinism, budget/risk refusal, research redaction, and empty/NOT_COMPUTABLE paths alongside positive injection cases. Preserve the tested versions and result date when adding evidence; passing Frontier cases is not proof of hosted deployment.
