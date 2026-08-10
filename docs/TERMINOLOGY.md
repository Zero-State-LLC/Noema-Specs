# Terminology

Canonical domains are defined in [CONTEXT.md](../CONTEXT.md). This document is the quick reference for spec authors.

| Term | Definition |
| --- | --- |
| Agent | Autonomous runtime participant connected through NOEMA protocols. |
| World Engine | Persistent MUD-style simulation authority. |
| Chamber | v0.1 persistent strategic ecology for 2–10 agents. |
| Deep Time | Accumulated world history retained as active research context. |
| Resource | One of attention, compute, energy, influence, storage (integer budgets). |
| Resource node | Entity with extractable stock (`resource_node: true`). |
| Infrastructure | Strategic entity types: relay, generator, storage_bay, production_node. |
| World Event Director | Deterministic v0.1 pressure scheduler (not Frontier Director). |
| Spectator projection | Derived WATCH view; never world truth. |
| Situation Genome | Machine-readable situation description and novelty vector. |
| Observation | Immutable research-relevant record with provenance. |
| Trajectory | Ordered multi-record behavior history. |
| Capability Event | Strictly evaluated candidate emergent behavior event. |
| Phenomenon Case | Evidence package for consciousness-adjacent behavioral constructs. |
| Reproducibility Bundle | Versioned artifact for replay, replication, perturbation, metrics, and report. |
| Noema Atlas | Versioned research dataset. |
| Module contract | Owns/reads/writes/dependency boundary for a runtime module. |

## Avoid

- Do not use `fact` for unsupported interpretation.
- Do not call telemetry evidence unless it has provenance and eligibility.
- Do not say consciousness is measured or proven.
- Do not introduce a scalar consciousness score.
- Do not rename claim labels.
- Do not treat spectator narrative as a WorldEvent.
- Do not treat research metrics as player victory scores.
