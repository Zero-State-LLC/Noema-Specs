# GC2-S10 — institution-owned constructibles

**Status:** Executable specification. Runtime authorized with RFC-0067.  
**Parent:** [GC2-S9-MULTICYCLE.md](GC2-S9-MULTICYCLE.md) · [GC4-S1-OFFICES.md](GC4-S1-OFFICES.md) · [CONSTRUCTION.md](CONSTRUCTION.md)  
**RFC:** [RFC-0067](../rfcs/RFC-0067-institution-own.md)  
**Does not open:** institution-as-Player · SHARED · CONNECT · help BUILD · STRUCTURE_*

S10 lets an occupied named-asset office hold a public constructible. The org is not a Player.

---

## Doctrine decisions

| Temptation | Verdict |
|------------|---------|
| Institution-as-Player | **REJECT.** |
| SHARED this slice | **REJECT.** |
| Vest UNCLAIMED / scar / in-progress | **REJECT.** |
| New property law | **REJECT.** |
| Help BUILD | **REJECT.** |

---

## Slice contract

| Field | Value |
|-------|--------|
| Slice id | `gc2-s10` |
| Catalog | `construction-catalog/gc2-s10` |
| Verb | existing `BUILD` |
| Operation | `VEST` |
| Target | public live constructible the actor personally owns |
| Authority | occupied `OPERATE_NAMED_ASSET` in `org_id` |
| Identity | same `entity_id`; `owner_id` = org |
| Cost | compute 1 |
| Events | `ENTITY_UPDATE` + `BUDGET_CONSUMED` |
| Steward after | that office holder |
| PLAY | `The {label} is held by {org}.` |
| WATCH | silent |
| Help | still omits BUILD |

---

## Out of S10

```text
CONNECT
SHARED ownership
institution-as-Player
STRUCTURE_*
Chamber help BUILD
```

---

## Runtime rule

Hosted Chamber MUST accept `BUILD.VEST` from a personal owner who holds an occupied `OPERATE_NAMED_ASSET` office, set `owner_id` to that org, and treat that office holder as steward. Isolated tests only. Help unchanged. No Genesis change.
