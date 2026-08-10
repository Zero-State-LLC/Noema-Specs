# Experiment Controls

| Role | Purpose |
|------|---------|
| `BASELINE` | No claim-bearing intervention |
| `POSITIVE_CONTROL` | Expected detectable effect |
| `NEGATIVE_CONTROL` | Effect should be absent |
| `SHAM_CONTROL` | Full pipeline, no claim-bearing change |
| `REPLICATION_CONTROL` | Boundary-matched repeat |

Each control declares: relationship, expected behavior, failure interpretation, required?

**Required control failure → experiment `INVALID`.**

Sham example: remove+restore identical configuration, or no-op intervention through the same execution path.
