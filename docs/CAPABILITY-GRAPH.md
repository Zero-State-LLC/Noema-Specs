# Capability Graph (v0.7 — Minimal LEARN layer)

## Purpose

v0.7 defines the **smallest useful** evidence-backed behavior-relationship layer that completes:

```text
PLAY → NOTICE → TEST → CAPTURE → LEARN
```

Ordinary product concept: **LEARN**.  
Internal representation: a rebuildable **behavior / capability graph projection**.

> Graph edges summarize evidence that already exists. The graph does not create evidence.

## Complexity rule

> Prefer the smallest architecture that preserves the intended behavior.

No graph database, graph service, leaderboard, consciousness score, architecture attribution, automatic ontology induction, or causal discovery.

Implementable as ordinary application data structures and queries in the modular monolith. Outside the PLAY hot path.

## Authority hierarchy

1. Captured tests, Lab results, regression/replication/generalization evidence (sources)
2. Behavior nodes + capability edges (derived projection)
3. LEARN simple views (presentation)

Historical broader-ontology language in earlier drafts is **deferred** beyond this minimal model. Seed research ontology remains non-exhaustive at [research/capability-ontology.md](../research/capability-ontology.md) and is **not** required for LEARN.

## Primary node class: BEHAVIOR

One primary node class:

```text
BEHAVIOR
```

Maps existing Observatory/Lab language carefully:

| Existing term | v0.7 mapping |
|---|---|
| Capability candidate / unknown candidate | may seed a behavior after capture |
| Captured test / phenomenon | grounds `behavior_id` |
| Capability primitive (research seed) | optional condition/context vocabulary only |

Do not invent parallel classes skill/trait/competence for v0.7.

Schema: [`behavior-node.schema.json`](../specs/behavior-node.schema.json).

## Closed edge taxonomy

| edge_type | Meaning |
|---|---|
| `OBSERVED_IN` | Observed under a declared context |
| `REPRODUCED_BY` | Reproduced by an agent/version under a captured test |
| `DEPENDS_ON` | Lab evidence supports dependence **within tested boundaries** |
| `FAILS_WITHOUT` | Behavior failed/disappeared when a declared dependency was removed |
| `GENERALIZES_TO` | Reproduced in a declared different context |
| `DIFFERS_ACROSS_VERSION` | Outcome differs between controlled agent/runtime versions |

No additional edge types in v0.7.

Schema: [`capability-edge.schema.json`](../specs/capability-edge.schema.json).

## Target classes (bounded)

`AGENT_VERSION` · `CONDITION` · `CONTEXT` · `BEHAVIOR`

Conditions/contexts reference existing experiment variables, interventions, and scenario identities — no new ontology.

## Claim labels

`OBSERVED` · `INFERRED` · `SPECULATIVE` · `NOT_COMPUTABLE`

Speculative relationships must not appear as ordinary LEARN facts. Missing/incompatible evidence → **no edge** (`NOT_COMPUTABLE`).

## Relationship status

`SUPPORTED` · `CONTESTED` · `INSUFFICIENT`

Contested edges retain both supporting and counterevidence refs. Do not silently overwrite.

## Forbidden inferences

- No automatic transitive closure (`A→B`, `B→C` ⇏ `A→C`)
- No automatic family induction (`COLLECTIVE_INTELLIGENCE` etc.)
- No strengthening of claim labels beyond source evidence
- Compiler minimization removals are **not** universal independence claims — phrase within test boundary

## Derived, rebuildable projection

```text
source evidence → deterministic graph projection
```

Materialized graph is a **disposable index**. If deleted:

```text
source evidence → rebuild
```

Optional snapshot schema: [`capability-graph.schema.json`](../specs/capability-graph.schema.json) with `rebuildable: true`, `mutable_source_of_truth: false`.

## Update semantics

New captured tests / Lab / regression results may update the projection. Source evidence remains immutable. Updates occur after research artifacts settle — not every game cycle.

## PLAY isolation

LEARN / graph never modifies gameplay, grants buffs, rankings, or player labels. Default PLAY must not expose research graph detail.

## LEARN surface

See [LEARN.md](LEARN.md).

Executable package: [releases/v0.7/](releases/v0.7/).
