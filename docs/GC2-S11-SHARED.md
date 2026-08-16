# GC2-S11 — shared constructible ownership

**Status:** Executable specification. Runtime authorized with RFC-0068.  
**Parent:** [GC2-S10-INSTITUTION.md](GC2-S10-INSTITUTION.md) · [CONSTRUCTION.md](CONSTRUCTION.md)  
**RFC:** [RFC-0068](../rfcs/RFC-0068-shared-own.md)  
**Does not open:** N-of-M roster · institution-as-Player · help BUILD · STRUCTURE_*  
**Next:** [GC2-S12-CONNECT.md](GC2-S12-CONNECT.md)

S11 names one other Player on a public constructible. It is not a title minigame.

---

## Doctrine decisions

| Temptation | Verdict |
|------------|---------|
| N-of-M roster | **REJECT.** One co-owner. |
| Share institution assets | **REJECT.** |
| Vest after share | **REJECT.** |
| Institution-as-Player | **REJECT.** |
| Help BUILD | **REJECT.** |

---

## Slice contract

| Field | Value |
|-------|--------|
| Slice id | `gc2-s11` |
| Catalog | `construction-catalog/gc2-s11` |
| Verb | existing `BUILD` |
| Operation | `SHARE` |
| Target | public live constructible the actor personally owns alone |
| Partner | one entered Player |
| Identity | same `entity_id`; `co_owner_id` set |
| Cost | compute 1 |
| Events | `ENTITY_UPDATE` + `BUDGET_CONSUMED` |
| Steward after | owner and co-owner |
| PLAY | `You share the {label} with {handle}.` |
| WATCH | silent |
| Help | still omits BUILD |

---

## Out of S11

```text
third co-owner
share / vest mix
STRUCTURE_*
Chamber help BUILD
```

---

## Runtime rule

Hosted Chamber MUST accept `BUILD.SHARE` from a sole personal owner, set `co_owner_id` to one entered Player, and treat both as stewards. Isolated tests only. Help unchanged. No Genesis change.
