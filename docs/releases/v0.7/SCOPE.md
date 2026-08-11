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
