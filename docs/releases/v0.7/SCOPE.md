# v0.7 Capability Graph / LEARN: Scope Delta

v0.7 adds the **minimal LEARN layer**: evidence-backed behavior nodes and a closed edge taxonomy so researchers can see what was reproduced, by whom, under which conditions, where it generalized, where it failed, and what remains untested.

## Complexity rule

> Prefer the smallest architecture that preserves the intended behavior.

## In scope

- BEHAVIOR node identity
- Closed edges: OBSERVED_IN, REPRODUCED_BY, DEPENDS_ON, FAILS_WITHOUT, GENERALIZES_TO, DIFFERS_ACROSS_VERSION
- Evidence lineage from captured tests / Lab / regression
- Simple LEARN projection + progressive disclosure
- Rebuildable derived graph projection (no second source of truth)

## Out of scope

Architecture attribution, phase transitions, ontology induction, causal discovery, intelligence/consciousness scores, model ranking, graph DB/service, v0.8 Phenomena work.

Authority: [CAPABILITY-GRAPH.md](../../CAPABILITY-GRAPH.md), [LEARN.md](../../LEARN.md).

## Extension Points

Non-normative guidance for future maintenance; no new behavior is authorized here.

- **Minimal-graph seam:** Extend evidence-backed examples using BEHAVIOR nodes and the six declared edge types. Show how a reproduced behavior, dependency, version difference, or generalization is bounded by its supporting captured-test/Lab/regression evidence.
- **Compatibility boundary:** A new edge meaning or node class requires versioned CAPABILITY-GRAPH authority, not expansion through LEARN display copy. Preserve the release's closed taxonomy and exclusions: no causal discovery, model ranking, consciousness scores, graph-service requirement, or v0.8 activation.
- **Validation expectations:** Trace each proposed example to eligible evidence, rebuild it deterministically, and test absent/non-comparable evidence separately from failure. Confirm that both simple and advanced views retain tested conditions and that graph projections never manufacture source records or modify PLAY.
