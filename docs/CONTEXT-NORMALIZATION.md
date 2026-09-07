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

## Extension Points

Non-normative extension guidance; accepted authority controls.

- **Comparator seam:** Extend paired-context fixtures against the versioned hard mask: world version, feature version, risk regime band, and genome class when present. Retain soft-dimension differences and the declared controls rather than normalizing them away.
- **Invariants:** A hard mismatch forbids claim-bearing comparison; soft differences only support CONDITIONALLY_COMPARABLE with explicit controls. Raw behavioral similarity does not override context incompatibility.
- **Compatibility:** Additional MUD dimensions may be proposed with evidence of their effect, but do not silently alter the mask or invent TRADE verbs. Record comparator/mask versions so earlier verdicts remain reproducible.
- **Verification:** Test exact match, each hard mismatch, absent optional genome, and differing room/stock/partners with and without controls. Verify plugins display the computed verdict and reasons rather than promoting conditional results to comparable.
- **Research consumer:** An authorized comparison viewer can localize dimension descriptions and expose evidence-linked differences in semantic tables. Ops snapshots and Gate B planning references are not independent evidence of live mask enforcement.
