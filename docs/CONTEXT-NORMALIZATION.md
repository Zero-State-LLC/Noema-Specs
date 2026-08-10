# Context Normalization (v0.3)

Raw behavior cannot be compared without world context.

## Dimensions

world_version · room/location · resource availability/pressure · infrastructure condition · organization membership · agent count · active world events · Situation Genome · observation quality · attention state · tool availability · communication topology · partner/opponent composition

## Comparability

| Result | Meaning |
|--------|---------|
| `COMPARABLE` | all hard dimensions match (versioned mask) |
| `CONDITIONALLY_COMPARABLE` | soft dims differ; analysis MUST declare controls |
| `NOT_COMPARABLE` | hard mismatch; claim-bearing comparison forbidden |

Default hard mask (versioned in `specs/context-comparability.v03.json`):

```text
world_version, feature_version, risk_regime_band, genome_class (if any)
```

Soft dims: exact room, exact stock, partner set — may differ under CONDITIONALLY_COMPARABLE with declared confounds.
