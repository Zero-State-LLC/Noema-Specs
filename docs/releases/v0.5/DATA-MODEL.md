# v0.5 Compiler: Data Model Delta

## New record types

| Record | Schema | schema_version |
|---|---|---|
| CaptureIntent | `specs/capture-intent.schema.json` | `capture-intent/0.5` |
| CompilationRequest | `specs/compilation-request.schema.json` | `compilation-request/0.5` |
| PhenomenonCandidate | `specs/phenomenon-candidate.schema.json` | `phenomenon-candidate/0.5` |
| DependencyGraph | `specs/phenomenon-dependency-graph.schema.json` | `phenomenon-dependency-graph/0.5` |
| UnitManifest | `specs/compiler-unit-manifest.schema.json` | `compiler-unit-manifest/0.5` |
| MinimizationRecord | `specs/minimization-record.schema.json` | `minimization-record/0.5` |
| BehavioralOracle | `specs/behavioral-oracle.schema.json` | `behavioral-oracle/0.5` |
| CompilerResult | `specs/compiler-result.schema.json` | `compiler-result/0.5` |
| CompileReceipt | `specs/phenomenon-compile-receipt.schema.json` | `phenomenon-compile-receipt/v1` |
| CompilerAuditRecord | `specs/compiler-audit-record.schema.json` | `compiler-audit-record/0.5` |
| CapturedTest | `specs/captured-test.schema.json` | `captured-test/0.5` |
| RegressionResult | `specs/regression-result.schema.json` | `regression-result/0.5` |

## Catalogs

- `specs/capture-defaults.v05.json` — versioned ordinary CAPTURE defaults
- `specs/capture-status-catalog.json` — machine status → simple status
- `specs/compiler-reason-catalog.v05.json` — reason codes + next actions

## Authority

Derived artifacts only. v0.5 MUST NOT rewrite world history, Observatory candidates, Lab experiments, or Lab results.
