# GC8-S1 — Lot Quality

**Status:** Executable specification. Runtime authorized with RFC-0045.  
**Parent:** [GC8-FIRST-SLICE.md](GC8-FIRST-SLICE.md) · [ECONOMIC-SPECIALIZATION.md](ECONOMIC-SPECIALIZATION.md)  
**RFC:** [RFC-0045](../rfcs/RFC-0045-lot-quality.md)  
**Does not open:** currency · yield bonus · provenance schema · spoilage · v0.6B

S1 stamps harvested holdings SOUND or WORN. Worn storage costs one extra on CONSTRUCT. Amounts stay S0.

---

## Doctrine decisions

| Temptation | Verdict |
|------------|---------|
| More than two grades | **REJECT.** |
| Harvest +N from SOUND nodes | **REJECT.** Yield bonus |
| Currency | **REJECT.** |
| Provenance / spoilage | **DEFER.** |

---

## Slice contract

| Field | Value |
|-------|--------|
| Slice id | `gc8-s1` |
| Catalog | `economy-catalog/gc8-s1` |
| Grades | `SOUND` · `WORN` |
| Worn if | node condition < 50 |
| Mix | SOUND + WORN → WORN |
| Construct | WORN storage adds +1 storage |
| Repair | unchanged |

---

## Out of S1

```text
currency order book v0.6B
harvest yield bonus
provenance schema
storage spoilage
WATCH price ticker
```

---

## Runtime rule

Hosted Chamber MUST grade HARVEST and charge WORN construct storage +1. Isolated tests only. Help unchanged. No Genesis change.

## Extension Points

Non-normative guidance for future work; existing authorities and closed-slice boundaries remain unchanged.

- **Seam and invariants.** Lot-quality fixtures can expand at harvest, mixing and construction boundaries while retaining only SOUND/WORN, unchanged harvest amounts and unchanged REPAIR. Quality remains a bounded input to the existing economy, not currency or a price oracle.
- **Compatibility and validation.** Check node condition just below/at 50, mixed-grade holdings, WORN storage charging and insufficient-storage rejection. A changed grade set or debit needs accepted versioned economy authority and compatibility cases; provenance, spoilage and v0.6B remain outside this slice.
