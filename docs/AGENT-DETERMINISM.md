# Agent Determinism Classification

| Class | Meaning |
|-------|---------|
| `DETERMINISTIC` | Same inputs → same actions under contract |
| `SEED_CONTROLLED` | Deterministic given declared seeds |
| `NONDETERMINISTIC` | Provider/model variance expected |
| `UNKNOWN` | Not declared |

Nondeterministic agents remain studyable. Strengthen replication; do not auto-INVALID. Adjust claim labels and equivalence expectations.
