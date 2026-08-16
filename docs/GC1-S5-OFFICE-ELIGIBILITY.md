# GC1-S5 — Office eligibility

**Status:** Executable specification. Runtime authorized with RFC-0055.  
**Depends on:** [GC1-S4-PRIOR-WORK.md](GC1-S4-PRIOR-WORK.md) · [GC4-S1-OFFICES.md](GC4-S1-OFFICES.md)  
**RFC:** [RFC-0055](../rfcs/RFC-0055-office-eligibility.md)  
**Does not open:** WATCH titles · class discounts · `ROLE_*` · evict-on-latent · Explorer/Surveyor gates

S5 lets a named office require a recognized Engineer or Broker. Others cannot sit that seat. It is not a title and not a cheaper verb.

---

## Doctrine decisions

| Temptation | Verdict |
|------------|---------|
| Gate every repair / treasury office | **REJECT.** Additive field only |
| WATCH titles | **REJECT.** |
| Class discount | **REJECT.** |
| Evict when LATENT | **REJECT.** Recognition remains |
| `ROLE_*` / new verb | **REJECT.** Existing `ORG_OFFICE_ASSIGN` |
| Explorer / Surveyor required | **DEFER.** |

---

## Slice contract

| Field | Value |
|-------|--------|
| Slice id | `gc1-s5` |
| Catalog | `mastery-catalog/gc1-s5` |
| Create | optional `requires_track` ∈ {`engineer`, `broker`} |
| Assign | existing `ORG_OFFICE_ASSIGN` |
| Eligible | recognized on that track (LATENT included) |
| Ineligible | `FORBIDDEN` |
| Unrestricted office | any current member |
| Events | `ENTITY_*` / `BUDGET_CONSUMED` |
| PLAY reject | `That office requires a recognized Engineer.` / `Broker.` |
| WATCH | silent |
| Help | unchanged |

---

## Out of S5

```text
WATCH / public titles
class discounts
ROLE_*
evict-on-latent
Explorer / Surveyor required tracks
FOCUS_DECLARED
```

---

## Runtime rule

Hosted Chamber MUST refuse `ORG_OFFICE_ASSIGN` (and designated succession seating) when `requires_track` is set and the target is not recognized on that track. Isolated tests only. Help unchanged. No Genesis change.
