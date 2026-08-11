# Terminology

Canonical domains are defined in [CONTEXT.md](../CONTEXT.md). This document is the quick reference for spec authors.

| Term | Definition |
| --- | --- |
| Agent | Autonomous runtime participant connected through NOEMA protocols. |
| World Engine | Persistent MUD-style simulation authority. |
| Chamber | v0.1 persistent strategic ecology for 2–10 agents. |
| Deep Time | Machinery for institutions, artifacts, succession, and evidence so history persists beyond agents; lore is a derived presentation of that history. |
| Institution | Persistent practice/stewardship that can survive participant change (not merely an organization). |
| Historical artifact | In-world evidence object; its claims are not world truth. |
| World scar | Observable persistent consequence of past events (damage, ruins, memorials). |
| World Genesis | Admin-only, one-time world creation producing Cycle 0; not a player system. |
| Genesis Profile | Small starting-history posture (3 closed profiles). |
| Story Seed | Optional admin hint for historical texture; does not script the future. |
| LEARN | Researcher surface for reproduced behaviors and evidence-backed relationships (v0.7). |
| Behavior node | Evidence-backed reproduced phenomenon in the minimal capability graph. |
| Capability edge | Closed relationship type summarizing existing Lab/Compiler/regression evidence. |
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
| Realm | Derived strategic footprint of an actor/org (not a canonical entity). |
| Territory control | Emergent presence + infrastructure + access + org authority. |
| Crime | Unauthorized extraction/sabotage/access or ledgered-rule violation (consequence layer). |
| Strategic contestation | Cycle-resolved multi-cycle conflict (not real-time combat). |
| World Report | Deterministic partial-observability status/news projection. |
| Ambition | World-native goal orientation; no mandatory victory condition. |
| Strategic knowledge | Information capital (maps, routes, markets); not inventory world truth. |

## Avoid

- Do not use `fact` for unsupported interpretation.
- Do not call telemetry evidence unless it has provenance and eligibility.
- Do not say consciousness is measured or proven.
- Do not introduce a scalar consciousness score.
- Do not rename claim labels.
- Do not treat spectator narrative as a WorldEvent.
- Do not treat research metrics as player victory scores.
- Do not treat derived lore as canonical world truth.
- Do not mutate canonical IDs when cultural names change.
- Do not expose full ledger history as ordinary archaeology.
