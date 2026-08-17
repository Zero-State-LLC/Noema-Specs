# GC2-S23 — fifth co-owner

**Status:** Executable specification. Runtime authorized with RFC-0087.  
**Parent:** [GC2-S22-FOURTH-CO-OWNER.md](GC2-S22-FOURTH-CO-OWNER.md) · [CONSTRUCTION.md](CONSTRUCTION.md)  
**RFC:** [RFC-0087](../rfcs/RFC-0087-fifth-co-owner.md)  
**Does not open:** N-of-M roster · sixth co-owner · institution-as-Player · help BUILD · STRUCTURE_*  
**Next:** [GC2-S24-SHARE-CLOSEOUT.md](GC2-S24-SHARE-CLOSEOUT.md)

S23 lets the personal owner name one more Player on a public constructible. It is still not a title minigame.

---

## Doctrine decisions

| Temptation | Verdict |
|------------|---------|
| N-of-M roster | **REJECT.** Five co-owners. |
| Sixth-and-later | **REJECT.** |
| Co-owner SHARE | **REJECT.** Owner names. |
| Share institution assets | **REJECT.** |
| Vest after share | **REJECT.** |
| Institution-as-Player | **REJECT.** |
| Help BUILD | **REJECT.** |

---

## Slice contract

| Field | Value |
|-------|--------|
| Slice id | `gc2-s23` |
| Catalog | `construction-catalog/gc2-s23` |
| Verb | existing `BUILD` |
| Operation | `SHARE` |
| Target | public live constructible the actor personally owns |
| Partner | one entered Player who is not already a steward |
| First stamp | `co_owner_id` (S11) |
| Second stamp | `co_owner_2_id` (S20) |
| Third stamp | `co_owner_3_id` (S21) |
| Fourth stamp | `co_owner_4_id` (S22) |
| Fifth stamp | `co_owner_5_id` |
| Cap | 5 co-owners |
| Cost | compute 1 |
| Events | `ENTITY_UPDATE` + `BUDGET_CONSUMED` |
| Steward after | owner and all five co-owners |
| PLAY | `You share the {label} with {handle}.` |
| WATCH | silent |
| Help | still omits BUILD |

---

## Out of S23

```text
SHARE family closeout is [GC2-S24-SHARE-CLOSEOUT.md](GC2-S24-SHARE-CLOSEOUT.md)
N-of-M roster
share / vest mix
STRUCTURE_*
Chamber help BUILD
```

---

## Runtime rule

Hosted Chamber MUST accept a fifth `BUILD.SHARE` from the personal owner, set `co_owner_5_id` to one other entered Player, treat owner and all five co-owners as stewards, and reject a sixth SHARE. Isolated tests only. Help unchanged. No Genesis change.
