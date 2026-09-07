# v0.5 Compiler: Examples

Package: [`examples/v05-compiler/`](../../../examples/v05-compiler/)

| Artifact | Path |
|---|---|
| READY Lab Result | `source-lab-result-ready.json` |
| Capture intent | `capture-intent.json` |
| Compilation request | `compilation-request.json` |
| Phenomenon candidate | `phenomenon-candidate.json` |
| Dependency graph | `dependency-graph.json` |
| Unit manifest | `unit-manifest.json` |
| Behavioral oracle | `behavioral-oracle.json` |
| Minimization records | `minimization-records.jsonl` |
| Compiler result | `compiler-result.json` |
| Receipt | `compile-receipt.json` |
| Audit ledger | `compiler-audit-ledger.jsonl` |
| Captured test package | `captured-test/` |
| Simple / advanced views | `simple-capture-result.json`, `advanced-capture-result.json` |
| Budget / privacy / failed | `simple-budget-exhausted.json`, `simple-privacy-block.json`, `simple-failed-capture.json` |
| Regression | `regression-result.json`, `regression-result-fail.json` |

Experience mirrors under `examples/experience/capture-*.json`.

## Extension Points

Non-normative future guidance; this section does not change the contracts or dated outcomes above.

**Seam.** The artifact inventory can add traceable Compiler fixture scenarios linking source Lab results, requests, minimization audits, receipts, captured tests, and regression outcomes.

**Preserved invariants.** Examples remain conformance fixtures rather than authority; preserve a single identity/evidence chain across simple and advanced views and retain budget, privacy, and failure outcomes.

**Compatibility and promotion.** New fields or statuses need the governing schema/catalog version before being illustrated; fixture additions do not by themselves promote a captured behavior or authorize public export.

**Validation expectations.** Validate each artifact against its pinned schema, resolve internal digests/references, compare experience mirrors with their source results, and exercise success plus failed-regression/privacy/exhaustion cases without fabricating a READY source.
