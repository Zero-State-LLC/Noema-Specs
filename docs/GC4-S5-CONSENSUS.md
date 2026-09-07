# GC4-S5 — CONSENSUS succession

**Status:** Executable specification. Runtime authorized with RFC-0060.  
**Parent:** [GC4-S4-SUCCESSION.md](GC4-S4-SUCCESSION.md) · [SUCCESSION.md](SUCCESSION.md)  
**RFC:** [RFC-0060](../rfcs/RFC-0060-consensus-succession.md)  
**Does not open:** elections · SUCCESSION_* · emergency consensus  
**Next:** [GC4-S6-RULE.md](GC4-S6-RULE.md)

S5 fills a vacant office when current members consent. It is not an election and not a recall.

---

## Doctrine decisions

| Temptation | Verdict |
|------------|---------|
| Elections / parties | **REJECT.** |
| RULE_BASED | **DEFER** to [GC4-S6-RULE.md](GC4-S6-RULE.md). |
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
SUCCESSION_*
emergency consensus
Chamber help advertising
```

---

## Runtime rule

Hosted Chamber MUST record member consents on a vacant office and seat a candidate at `ceil(members/2)`. Isolated tests only. Help unchanged. No Genesis change.

## Extension Points

Non-normative membership/consent regression and vacancy-presentation seams.

- Extend isolated consensus cases over current membership, a VACANT office and ACTIVE organization; record consent for one candidate and verify seating at ceil(members/2). This is vacancy filling, not a ballot to remove an occupant.
- Preserve compute 1, existing ENTITY_UPDATE/BUDGET_CONSUMED, succession WATCH pulse only on seating, unchanged help and no Genesis changes. No elections, parties, emergency consensus or SUCCESSION_* events are introduced.
- Compatibility/promotion: pin authority-catalog/gc4-s5 and RFC-0060 against SUCCESSION and S4; S6 rule-based succession remains a separate accepted boundary rather than an implied fallback.
- Verification proposal: test below/exact threshold, nonmember consent, occupied office and inactive org; confirm rejection does not seat and replay does not duplicate seating. Localized vacancy/consent summaries must distinguish pending from seated without publicizing membership details outside the existing visibility contract.
