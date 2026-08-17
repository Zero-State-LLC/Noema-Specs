# GC2-S24 — SHARE family closeout

**Status:** Executable specification. Runtime authorized with RFC-0089.  
**Parent:** [GC2-S23-FIFTH-CO-OWNER.md](GC2-S23-FIFTH-CO-OWNER.md) · [CONSTRUCTION.md](CONSTRUCTION.md)  
**RFC:** [RFC-0089](../rfcs/RFC-0089-share-closeout.md)  
**Does not open:** sixth stamp · N-of-M roster · institution-as-Player · help BUILD · STRUCTURE_*  
**Next:** this SHARE leftover is closed

S24 stops the stamp march. Five co-owners is the cap. It is still not a title minigame.

---

## Doctrine decisions

| Temptation | Verdict |
|------------|---------|
| `co_owner_6_id` | **REJECT.** Family closed. |
| N-of-M roster | **REJECT.** |
| Co-owner SHARE | **REJECT.** Owner names. |
| Help BUILD | **REJECT.** |

---

## Slice contract

| Field | Value |
|-------|--------|
| Slice id | `gc2-s24` |
| Catalog | `construction-catalog/gc2-s24` |
| Verb | existing `BUILD` |
| Operation | `SHARE` (unchanged) |
| Cap | 5 co-owners |
| Family | closed |
| Sixth stamp | none |
| Events | existing `ENTITY_UPDATE` + `BUDGET_CONSUMED` |
| WATCH | silent |
| Help | still omits BUILD |

---

## Out of S24

```text
sixth stamp
N-of-M roster
Chamber help BUILD
```

---

## Runtime rule

Hosted Chamber MUST keep `SHARE` at five co-owners, reject a sixth SHARE, and MUST NOT add `co_owner_6_id` or a roster. Isolated tests only. Help unchanged. No Genesis change.
