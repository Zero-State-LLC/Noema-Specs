# v0.3 Observatory — Scope

Product: NOEMA `0.3.0` (The Observatory).
Builds on: v0.1 Chamber (C01–C26), v0.2 Frontier (F01–F15).

## Progression

```text
v0.1 Chamber   → interesting strategic behavior occurs
v0.2 Frontier  → NOEMA selects/creates informative situations
v0.3 Observatory → NOEMA detects unusual or meaningfully changing behavior
```

## Required scope

| Area | Authority |
|------|-----------|
| Trajectory | [TRAJECTORY.md](../../TRAJECTORY.md), `trajectory/0.3` |
| Behavior features | [BEHAVIOR-FEATURES.md](../../BEHAVIOR-FEATURES.md) |
| Context normalization | [CONTEXT-NORMALIZATION.md](../../CONTEXT-NORMALIZATION.md) |
| Baselines | [BASELINES.md](../../BASELINES.md) |
| Anomaly detection | [ANOMALY-DETECTION.md](../../ANOMALY-DETECTION.md) |
| Behavior shift | [BEHAVIOR-SHIFT.md](../../BEHAVIOR-SHIFT.md) |
| Agent-version comparison | [AGENT-VERSION-COMPARISON.md](../../AGENT-VERSION-COMPARISON.md) |
| Capability candidates | [CAPABILITY-CANDIDATES.md](../../CAPABILITY-CANDIDATES.md) |
| Unknown candidates | preserved UNKNOWN_* markers |
| Contradiction analysis | [CONTRADICTION-ANALYSIS.md](../../CONTRADICTION-ANALYSIS.md) |
| External cognition | [EXTERNAL-COGNITION.md](../../EXTERNAL-COGNITION.md) |
| Coordination signals | [COORDINATION-SIGNALS.md](../../COORDINATION-SIGNALS.md) |
| Emergence candidates | [EMERGENCE-CANDIDATES.md](../../EMERGENCE-CANDIDATES.md) |
| Analysis run + audit | [OBSERVATORY-AUDIT.md](../../OBSERVATORY-AUDIT.md) |
| Fixtures | [`examples/v03-observatory/`](../../../examples/v03-observatory/) |
| Conformance | [`conformance/v0.3/`](../../../conformance/v0.3/) O01–O16 |

## Product constraint

Observatory answers: *What is unusual, changed, or potentially capability-relevant?*
It does **not** claim: *The agent definitively possesses capability X.*

Outputs are research candidates. They do not mutate world truth, alter incentives, or expose research scores to ordinary players.
