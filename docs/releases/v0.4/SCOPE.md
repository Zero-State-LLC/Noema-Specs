# v0.4 Lab: Scope Delta

v0.4 adds controlled experimental evidence to v0.3 Observatory candidates: immutable designs, explicit plans, isolated forks/replay, interventions, controls, outcome comparison, replication, bounded generalization probes, audit, and a v0.5 readiness handoff.

It preserves C01–C26, F01–F15, O01–O16, S01–S18, replay guarantees, consent/containment, world/research separation, and claims discipline. The canonical subsystem contracts in `docs/` are authoritative; this package only defines the delta. Lab never mutates a production world or source trajectory and never makes Lab conclusions canonical truth.

Authority: [Experiment Lab](../../EXPERIMENT-LAB.md), [Design](../../EXPERIMENT-DESIGN.md), [Fork](../../EXPERIMENT-FORK.md), [Interventions](../../INTERVENTIONS.md), [Controls](../../EXPERIMENT-CONTROLS.md), [Replication](../../REPLICATION.md), and [Lab Audit](../../LAB-AUDIT.md).

## Extension Points

Non-normative guidance for future maintenance; no new behavior is authorized here.

- **Scope seam:** Add traceability examples showing which v0.4 evidence object or workflow closes a specific Observatory-to-Lab ambiguity. Keep this release delta subordinate to the linked subsystem contracts rather than restating experiment, fork, intervention, or control semantics independently.
- **Compatibility boundary:** Additional Lab scope needs explicit contract/version approval and compatibility against C01–C26, F01–F15, O01–O16, and S01–S18. Controlled experiments still do not mutate source trajectories or production worlds, and their conclusions remain research claims.
- **Validation expectations:** For a proposed extension, identify affected suites and exercise source immutability, isolated fork writes, consent/containment refusal, replay, and readiness handoff. Record actual results and untested dependencies; a scope statement is not evidence that every integration gate has passed.
