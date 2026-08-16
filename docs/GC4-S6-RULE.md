# GC4-S6 — RULE_BASED succession

**Status:** Executable specification. Runtime authorized with RFC-0069.  
**Parent:** [GC4-S5-CONSENSUS.md](GC4-S5-CONSENSUS.md) · [SUCCESSION.md](SUCCESSION.md)  
**RFC:** [RFC-0069](../rfcs/RFC-0069-rule-based-succession.md)  
**Does not open:** elections · rule language · implicit jump · SUCCESSION_* · emergency rules

S6 publishes one roster rule on an office. Vacancy walks stored membership order. It is not an election.

---

## Doctrine decisions

| Temptation | Verdict |
|------------|---------|
| Rule language | **REJECT.** One id: `MEMBER_ORDER`. |
| Implicit oldest / nearest | **REJECT.** Unpublished stays vacant. |
| Elections / parties | **REJECT.** |
| Emergency-scope rules | **REJECT.** |
| `SUCCESSION_*` | **REJECT.** |

---

## Slice contract

| Field | Value |
|-------|--------|
| Slice id | `gc4-s6` |
| Catalog | `authority-catalog/gc4-s6` |
| Operation | `ORG_SUCCESSION_RULE` |
| Rule | `MEMBER_ORDER` only |
| Place | office of an ACTIVE org |
| Who | founder or officer publishes |
| On vacate | first remaining eligible member in stored order |
| Empty | stay `VACANT` |
| Cost | compute 1 |
| Events | `ENTITY_UPDATE` + `BUDGET_CONSUMED` |
| WATCH | existing succession pulse on seat only |
| Help | unchanged |

---

## Out of S6

```text
elections / parties
other rule ids
INHERITED_BY_ORGANIZATION
emergency RULE_BASED
SUCCESSION_*
Chamber help advertising
```

---

## Runtime rule

Hosted Chamber MUST accept `COMMIT.ORG_SUCCESSION_RULE rule_id=MEMBER_ORDER` from a founder or officer, and on holder vacate/leave MUST seat the first remaining eligible member in stored membership order or leave the office vacant. Isolated tests only. Help unchanged. No Genesis change.
