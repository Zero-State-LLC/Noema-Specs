# v0.5 Compiler: Conformance

Suite: `conformance/v0.5/` · **P01–P30** · 90 atomic cases · depends on v0.4 Lab.

| Family | Topic |
|---|---|
| P01 | Capture Intent Compilation |
| P02 | Admission |
| P03 | Compilation Identity |
| P04 | Source Replay |
| P05 | Phenomenon Extraction |
| P06 | Unit Manifest |
| P07 | Dependency Closure |
| P08 | Minimization Ordering |
| P09 | ddmin Chunk Removal |
| P10 | Complement Testing |
| P11 | One-Unit Sweep |
| P12 | Minimality Status |
| P13 | Oracle Validation |
| P14 | Oracle Cache Identity |
| P15 | Oracle Disagreement |
| P16 | Over-Minimization Protection |
| P17 | Budget Exhaustion |
| P18 | Required Controls |
| P19 | Stochastic Replication |
| P20 | Compile Receipt |
| P21 | Audit Chain |
| P22 | Compiler Result |
| P23 | Captured Test |
| P24 | STUDY Capture Projection |
| P25 | Progressive Disclosure Equivalence |
| P26 | Regression Result |
| P27 | Generalization Boundary |
| P28 | Counterexample Preservation |
| P29 | Privacy / Partition |
| P30 | RFC-0003 Provenance Reuse |

Fixtures: `examples/v05-compiler/`. Validator gate: `check_compiler_v05`.

## Extension Points

Non-normative future guidance; no behavior is introduced by this section.

Compiler conformance may add fixtures within P01–P30 or propose separately reviewed families, while keeping the published 90-case baseline distinguishable from later suite revisions. Pin compiler, oracle, dependency and fixture versions in run receipts; changed minimization or oracle identity semantics require owning-contract compatibility review, not silently updated goldens. Promotion evidence should run check_compiler_v05 with Lab prerequisites and exercise budget exhaustion, oracle disagreement, dependency closure, counterexample retention, privacy partitioning and RFC-0003 provenance. Added cases should state their family, inputs, expected outcome and failure reason; counts change only with enumerated fixtures and observed validator results, never inferred coverage.
