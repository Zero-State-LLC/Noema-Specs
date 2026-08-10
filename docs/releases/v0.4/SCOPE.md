# v0.4 Lab — Scope

Product: NOEMA `0.4.0` (The Lab).
Builds on: v0.1 Chamber, v0.2 Frontier, v0.3 Observatory, RFC-0002 strategic catalog (optional for game forks).

## Progression

```text
v0.1 Chamber      → persistent strategic behavior
v0.2 Frontier     → informative situations
v0.3 Observatory  → candidates (anomaly / shift / capability / unknown)
v0.4 Lab          → controlled interventions test candidates
```

## Required scope

| Area | Authority |
|------|-----------|
| Experiment identity | [EXPERIMENT-IDENTITY.md](../../EXPERIMENT-IDENTITY.md) |
| Lifecycle | [EXPERIMENT-LIFECYCLE.md](../../EXPERIMENT-LIFECYCLE.md) |
| Design | [EXPERIMENT-DESIGN.md](../../EXPERIMENT-DESIGN.md) |
| Interventions | [INTERVENTIONS.md](../../INTERVENTIONS.md) |
| Variables | [EXPERIMENT-VARIABLES.md](../../EXPERIMENT-VARIABLES.md) |
| Fork | [EXPERIMENT-FORK.md](../../EXPERIMENT-FORK.md) |
| Counterfactual | [COUNTERFACTUAL-REPLAY.md](../../COUNTERFACTUAL-REPLAY.md) |
| Controls | [EXPERIMENT-CONTROLS.md](../../EXPERIMENT-CONTROLS.md) |
| Outcomes | [EXPERIMENT-OUTCOMES.md](../../EXPERIMENT-OUTCOMES.md) |
| Replication | [REPLICATION.md](../../REPLICATION.md) |
| Isolation / audit | [EXPERIMENT-ISOLATION.md](../../EXPERIMENT-ISOLATION.md), [LAB-AUDIT.md](../../LAB-AUDIT.md) |
| Schemas | `experiment`, `intervention`, `experiment-plan`, `experiment-run`, `lab-result`, `lab-audit`, `experiment-fork` |
| Catalogs | `perturbation-catalog/0.4`, `ablation-catalog/0.4` |
| Fixtures | [`examples/v04-lab/`](../../../examples/v04-lab/) |
| Conformance | [`conformance/v0.4/`](../../../conformance/v0.4/) **L01–L16** |

## Product constraint

Lab answers: *Does the candidate behavior survive controlled change?*  
It does **not** promote outcomes to world truth or permanent capability claims. Compiler readiness is a handoff flag only.
