# Replication

## Classes

| Class | Invariant focus |
|-------|-----------------|
| `EXACT_REPLAY` | Full declared boundary |
| `SAME_AGENT` | Agent id |
| `SAME_AGENT_VERSION` | Agent version pin |
| `CROSS_AGENT_VERSION` | Version may vary |
| `CROSS_MODEL` | Model may vary |
| `CROSS_WORLD_CONTEXT` | World context may vary |
| `CROSS_SITUATION` | Situation may vary |

## Outcomes

`REPRODUCED` | `PARTIALLY_REPRODUCED` | `NOT_REPRODUCED` | `NOT_COMPARABLE` | `NOT_COMPUTABLE`

Do not force binary labels under partial boundaries.
