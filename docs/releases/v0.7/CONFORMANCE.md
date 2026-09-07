# v0.7 LEARN: Conformance

Suite: `conformance/v0.7/` · **K01–K12** · depends on v0.5/v0.6.

| Family | Topic |
|---|---|
| K01 | Behavior Identity |
| K02 | Edge Validation |
| K03 | Evidence Lineage |
| K04 | Reproduction Mapping |
| K05 | Dependency Mapping |
| K06 | Failure Mapping |
| K07 | Generalization Mapping |
| K08 | Version Difference Mapping |
| K09 | Contradictory Evidence |
| K10 | LEARN Projection |
| K11 | Not-Tested Distinction |
| K12 | No Unsupported Inference |

Fixtures: `examples/v07-capability-graph/`. Validator: `check_learn_v07`.


## Extension Points

Non-normative guidance for future maintenance; this section changes no current behavior or promotion status.

- LEARN cases can replace generic family assertions with explicit behavior-node, edge, evidence, and projection examples for K01–K12. Include not-tested, conflicting evidence, and failed reproduction as first-class cases rather than only successful graph edges.

- Preserve v0.5/v0.6 prerequisites, existing case identity, and the closed relationship semantics. New edge kinds or stronger inference need the governing schema/version review; graph presentation cannot promote an untested relationship or imply global capability from a scenario result.

- Run check_learn_v07 with schema/fixture validation and resolve requirement references. Confirm missing tests remain distinguishable from failure, contradictory evidence is retained, version comparisons cite their inputs, and simple LEARN projections make no claim stronger than the underlying evidence; case totals alone do not establish these checks ran.
