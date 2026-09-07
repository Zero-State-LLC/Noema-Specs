# v0.3 Observatory — Conformance

Suite: [`conformance/v0.3/`](../../../conformance/v0.3/).
Depends on: `noema-v0.1-chamber`, `noema-v0.2-frontier`.

| ID | Family |
|----|--------|
| O01 | Trajectory Integrity |
| O02 | Feature Extraction |
| O03 | Context Comparability |
| O04 | Baseline Construction |
| O05 | Anomaly Detection |
| O06 | Behavior Shift Detection |
| O07 | Agent-Version Comparison |
| O08 | Capability Candidate Generation |
| O09 | Unknown Candidate Preservation |
| O10 | Contradiction Analysis |
| O11 | External Cognition Signals |
| O12 | Coordination Signals |
| O13 | Observatory Audit Replay |
| O14 | World-Truth Isolation |
| O15 | Research Overlay Redaction |
| O16 | Missing Evidence / NOT_COMPUTABLE |

## Extension Points

Non-normative future guidance; this section does not change the contracts or dated outcomes above.

**Seam.** Coverage mapping can add edge-case fixtures within the O01–O16 families for trajectory integrity, comparability, unknown candidates, and evidence failure.

**Preserved invariants.** Keep Observatory read-only with respect to world truth, preserve unknowns and contradictions, and return NOT_COMPUTABLE rather than filling missing evidence.

**Compatibility and promotion.** New feature, detector, or baseline semantics require the relevant pinned contract and compatibility fixtures; this suite index does not define those semantics or establish a validated capability.

**Validation expectations.** Verify family-to-case traceability, deterministic audit replay, redacted research overlays, and missing/incompatible-context cases; run prerequisite Chamber/Frontier checks as well and record actual case results rather than equating listed IDs with executed coverage.
