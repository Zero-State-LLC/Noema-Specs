# Strategic Conflict Conformance

Suite: `conformance/v0.2-strategic/`  
Fixture package: `examples/v02-strategic-conflict/`  
Depends on: Chamber v0.1 suite (catalog 0.1 still valid).

Families **S01–S18** (see acceptance doc). Cases are machine-readable under `cases/`.

Implementations claiming RFC-0002 support MUST pass this suite in addition to C01–C26 (unchanged).


## Extension Points

Non-normative guidance for future maintenance; this section changes no current behavior or promotion status.

- Suite maintenance can replace vague coverage with concrete S01–S18 scenarios carrying cited requirements, explicit action inputs, and expected events or rejection codes. Keep RFC-0002 support scoped to the strategic fixture package rather than a general product readiness claim.

- Preserve C01–C26 prerequisites and catalog-0.1 compatibility when adding cases under the declared strategic version. Changed contest or crime semantics require accepted contract/catalog review; new fixtures alone cannot revise the release's success criteria.

- Validate manifest and fixture paths, resolve each requirement reference, and run both strategic and Chamber suites. Retain failure evidence for unauthorized contests, settlement/replay mismatch, and private crime projection; report executed assertions separately from manifest case counts.
