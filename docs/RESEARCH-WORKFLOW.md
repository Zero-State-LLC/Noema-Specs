# Research Workflow

## First meaningful study in five minutes

1. Open **WATCH** and select an **Interesting Behavior** card.
2. Read its observed evidence and limits.
3. Select **TEST THIS**.
4. Choose **Does it happen again?**.
5. Run the recommended replication plan and review its result.

The card is a presentation of an Observatory candidate, never proof. The recommended intent deterministically selects its versioned plan template. The plan runs under Lab isolation and controls, and the result retains counterevidence, confounds, non-comparability, and exact labels.

## Intent-first TEST

| Question | Deterministic translation |
|---|---|
| Does it happen again? | `REPEAT_BEHAVIOR` → `REPLICATION` |
| Does it require the shared ledger or communication? | `REMOVE_DEPENDENCY` → external `ABLATION` |
| Does scarcity or another condition matter? | `CHANGE_CONDITION` → `PERTURBATION` or declared `COUNTERFACTUAL` |
| Does another version do it? | `COMPARE_VERSION` → `VERSION_DIFFERENTIAL` |
| Does it generalize? | `TEST_GENERALIZATION` → bounded replication probe |

Internal lesions are only an advanced, adapter-authorized extension and return `NOT_COMPUTABLE` when unsupported. Every template pins the normal Lab identity, fork, controls, measures, seed policy, budgets, and equivalence boundary. [Custom experiment](STUDY.md) is the escape hatch.

## Result

A simple result shows Question, answer **within tested conditions**, evidence counts, limits, and next valid actions. It never replaces the complete Lab result or claims automatic causality/capability. See [EXPERIMENT-LAB.md](EXPERIMENT-LAB.md).

## Deterministic compilation boundary

The simple request is a compact [`ExperimentIntent`](../specs/experiment-intent.schema.json), not an informal instruction to invent a study. It compiles by [`EXPERIMENT-INTENT-COMPILATION.md`](EXPERIMENT-INTENT-COMPILATION.md) into the same isolated Lab records used by advanced users. The returned simple result is the deterministic [`Simple Result Projection`](SIMPLE-RESULT-PROJECTION.md), with `CAPTURE AS TEST` available only when the machine Lab result is `READY`.

## CAPTURE (v0.5)

When a Lab result is capture-ready, one action — **CAPTURE AS TEST** — compiles by [`CAPTURE-INTENT-COMPILATION.md`](CAPTURE-INTENT-COMPILATION.md) into a canonical [compilation request](../specs/compilation-request.schema.json) using versioned [capture defaults](../specs/capture-defaults.v05.json). The [Phenomenon Compiler](PHENOMENON-COMPILER.md) emits a [captured test](CAPTURED-TEST-FORMAT.md) with receipt and audit. Simple STUDY views project required/removed conditions and validation without Compiler jargon; advanced views share the same `captured_test_id`.

## LEARN (v0.7)

Captured tests and Lab/regression evidence project into a minimal [Capability Graph](CAPABILITY-GRAPH.md) for the [LEARN](LEARN.md) surface: reproduced behaviors, version associations, dependencies, fails-without, generalization, and not-tested contexts. The graph is derived and rebuildable; it does not create evidence or modify PLAY.