# GC4-S7 — INHERITED_BY_ORGANIZATION

**Status:** Executable specification. Runtime authorized with RFC-0070.  
**Parent:** [GC4-S6-RULE.md](GC4-S6-RULE.md) · [SUCCESSION.md](SUCCESSION.md)  
**RFC:** [RFC-0070](../rfcs/RFC-0070-inherited-org.md)  
**Does not open:** institution-as-Player · elections · SUCCESSION_* · emergency inherit

S7 publishes that the organization keeps the seat. Vacancy does not auto-seat a person and does not retire the office.

---

## Doctrine decisions

| Temptation | Verdict |
|------------|---------|
| Institution-as-Player | **REJECT.** |
| Auto-seat | **REJECT.** |
| Retire on vacate | **REJECT.** |
| Emergency inherit | **REJECT.** |
| `SUCCESSION_*` | **REJECT.** |

---

## Slice contract

| Field | Value |
|-------|--------|
| Slice id | `gc4-s7` |
| Catalog | `authority-catalog/gc4-s7` |
| Operation | existing `ORG_SUCCESSION_RULE` |
| Rule | `INHERITED_BY_ORGANIZATION` |
| Place | office of an ACTIVE org |
| Who | founder or officer publishes |
| On vacate | stay `VACANT`; office kept |
| Cost | compute 1 |
| Events | `ENTITY_UPDATE` + `BUDGET_CONSUMED` |
| WATCH | silent |
| Help | unchanged |

---

## Out of S7

```text
institution-as-Player
other rule ids
emergency inherit
SUCCESSION_*
Chamber help advertising
```

---

## Runtime rule

Hosted Chamber MUST accept `COMMIT.ORG_SUCCESSION_RULE rule_id=INHERITED_BY_ORGANIZATION` from a founder or officer. On holder vacate/leave the office MUST stay `VACANT` on that org and MUST NOT be retired. Isolated tests only. Help unchanged. No Genesis change.
