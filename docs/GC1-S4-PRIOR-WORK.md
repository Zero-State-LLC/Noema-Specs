# GC1-S4 — Prior-Work Track Benefits

**Status:** Executable specification. Runtime authorized with RFC-0044.  
**Depends on:** [GC1-S3-DECAY.md](GC1-S3-DECAY.md)  
**RFC:** [RFC-0044](../rfcs/RFC-0044-prior-work-benefits.md)  
**Does not open:** WATCH titles · class discounts · seal bypass · `event-catalog/0.3`

S4 gives Explorer, Surveyor, and Broker a benefit only when they have already done the work on that room, entity, or counterparty.

---

## Doctrine decisions

| Temptation | Verdict |
|------------|---------|
| Cheaper MOVE / blanket INSPECT | **REJECT.** Class discount |
| Repeat LOOK/INSPECT free on a **known** object | **ACCEPT.** Prior work |
| Broker waives caution for a **prior** party | **ACCEPT.** |
| Bypass sealed INSPECT | **REJECT.** |
| WATCH titles | **REJECT.** |

---

## Slice contract

| Field | Value |
|-------|--------|
| Slice id | `gc1-s4` |
| Catalog | `mastery-catalog/gc1-s4` |
| Explorer | recognized + MAINTAINED + room already visited → LOOK attention 0 |
| Surveyor | recognized + MAINTAINED + entity already inspected → INSPECT attention 0 |
| Broker | recognized + MAINTAINED + prior settled trade with this party → TRADE_CAUTION extra 0 |
| First time | full cost / caution unchanged |
| LATENT | full cost / caution |

---

## Out of S4

```text
WATCH / public titles
FOCUS_DECLARED
office eligibility — closed by [GC1-S5-OFFICE-ELIGIBILITY.md](GC1-S5-OFFICE-ELIGIBILITY.md)
parameter-access upgrades
SPECIALIZATION_* events
```

---

## Runtime rule

Hosted Chamber MUST waive only the three prior-work costs above. Isolated tests only. Help unchanged. No Genesis change.
