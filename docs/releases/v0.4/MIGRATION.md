# v0.4 Lab — Migration

## Version domains

| Domain | Value |
|--------|-------|
| Lab | `lab/0.4` |
| Experiment design | `experiment-design/0.4` |
| Experiment schema | `experiment/0.4` |
| Perturbation catalog | `perturbation-catalog/0.4.0` |
| Ablation catalog | `ablation-catalog/0.4.0` |

## Rules

- No production world rewrite.
- Existing Observatory candidates remain valid inputs.
- Lab results do not alter historical candidates; they link by id.
- Downgrade of lab package does not invalidate prior world catalogs.
