# PSR-1 & Hosted STUDY Promotion Receipts (`#421`, `#422`, `#423`)

Per [ADR-0009](../../docs/adr/0009-psr1-and-study-promotion-evidence.md), commit redacted, PII-free promotion receipts here:

- `psr1_tier3_enrollment.json` (`#421`) — first external `Tier-3 Operator` `/connect` enrollment receipt
- `psr1_cohort_summary.json` (`#422`) — single-pinned-Worker `>=6` Controller `Δcycle >= 24` two-style cohort summary
- `hosted_study_promotion.json` (`#423`) — harvested natural-play pack redaction (`exit 0`) + Steward 3-artifact spot-check sign-off

Validate any committed receipts with:

```bash
python3 tools/check_psr1_readiness.py \
  --enrollment evidence/psr1-study/psr1_tier3_enrollment.json \
  --cohort evidence/psr1-study/psr1_cohort_summary.json \
  --study evidence/psr1-study/hosted_study_promotion.json
```
