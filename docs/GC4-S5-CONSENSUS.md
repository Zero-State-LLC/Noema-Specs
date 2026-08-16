# GC4-S5 — CONSENSUS succession

**Status:** Executable specification. Runtime authorized with RFC-0060.  
**Parent:** [GC4-S4-SUCCESSION.md](GC4-S4-SUCCESSION.md) · [SUCCESSION.md](SUCCESSION.md)  
**RFC:** [RFC-0060](../rfcs/RFC-0060-consensus-succession.md)  
**Does not open:** elections · RULE_BASED · SUCCESSION_* · emergency consensus

S5 fills a vacant office when current members consent. It is not an election and not a recall.

---

## Doctrine decisions

| Temptation | Verdict |
|------------|---------|
| Elections / parties | **REJECT.** |
| RULE_BASED | **DEFER.** |
| Vote out an occupant | **REJECT.** |
| Emergency-scope consensus | **DEFER.** |
| `SUCCESSION_*` | **REJECT.** |

---

## Slice contract

| Field | Value |
|-------|--------|
| Slice id | `gc4-s5` |
| Catalog | `authority-catalog/gc4-s5` |
| Operation | `ORG_SUCCESSION_CONSENT` |
| Place | VACANT office of an ACTIVE org |
| Who | current members |
| Threshold | `ceil(members/2)` for one candidate |
| Cost | compute 1 |
| Events | `ENTITY_UPDATE` + `BUDGET_CONSUMED` |
| WATCH | existing succession pulse on seat only |
| Help | unchanged |

---

## Out of S5

```text
elections / parties
RULE_BASED
SUCCESSION_*
emergency consensus
Chamber help advertising
```

---

## Runtime rule

Hosted Chamber MUST record member consents on a vacant office and seat a candidate at `ceil(members/2)`. Isolated tests only. Help unchanged. No Genesis change.
