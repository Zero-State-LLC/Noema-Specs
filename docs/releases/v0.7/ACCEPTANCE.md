# v0.7 LEARN: Acceptance

1. Prior suites C/F/O/S/L/P/D/G and RFC-0003 remain green.
2. Every behavior node traces to captured/research evidence.
3. Every edge traces to evidence refs.
4. Unsupported relationships are not created.
5. Dependency edges respect tested boundaries.
6. Generalization edges identify exact tested contexts.
7. Not-tested is distinct from fail.
8. Contradictory evidence remains visible (`CONTESTED`).
9. Graph projection is deterministic and rebuildable.
10. Source evidence remains immutable.
11. LEARN simple view derives from the same graph/evidence.
12. Simple view cannot strengthen claims.
13. Players do not need LEARN/graph knowledge for PLAY.
14. No gameplay state is modified by the graph.
15. No model ranking / consciousness score / architecture attribution.
16. No runtime graph service or dedicated graph database is specified.
17. Implementable as ordinary app data structures in the modular monolith.
18. Graph work stays off the PLAY hot path.

## Extension Points

Non-normative future guidance; this section does not change the contracts or dated outcomes above.

**Seam.** Acceptance traceability can deepen evidence-to-node/edge examples, especially contested, failed, and not-yet-tested contexts.

**Preserved invariants.** Keep source evidence immutable, graph projections deterministic, simple claims no stronger than advanced evidence, and graph work off the PLAY hot path without gameplay mutation.

**Compatibility and promotion.** New edge or ontology semantics require explicit versioned contracts and compatibility cases; this checklist cannot authorize transitive automatic edges, a graph service, or v0.8 behavior.

**Validation expectations.** Rebuild from pinned research/captured evidence, reject unsupported edges, test exact generalization/dependency boundaries and CONTESTED retention, and verify simple-view identity with no stronger claims; retain prerequisite suite evidence rather than assuming it passes.
