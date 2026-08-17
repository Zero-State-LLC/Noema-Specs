# GC2-S22 — fourth co-owner

**Status:** Executable specification. Runtime authorized with RFC-0086.  
**Parent:** [GC2-S21-THIRD-CO-OWNER.md](GC2-S21-THIRD-CO-OWNER.md) · [CONSTRUCTION.md](CONSTRUCTION.md)  
**RFC:** [RFC-0086](../rfcs/RFC-0086-fourth-co-owner.md)  
**Does not open:** N-of-M roster · fifth co-owner · institution-as-Player · help BUILD · STRUCTURE_*  
**Next:** fifth-and-later co-owners

S22 lets the personal owner name one more Player on a public constructible. It is still not a title minigame.

---

## Doctrine decisions

| Temptation | Verdict |
|------------|---------|
| N-of-M roster | **REJECT.** Four co-owners. |
| Fifth-and-later | **REJECT.** |
| Co-owner SHARE | **REJECT.** Owner names. |
| Share institution assets | **REJECT.** |
| Vest after share | **REJECT.** |
| Institution-as-Player | **REJECT.** |
| Help BUILD | **REJECT.** |

---

## Slice contract

| Field | Value |
|-------|--------|
| Slice id | `gc2-s22` |
| Catalog | `construction-catalog/gc2-s22` |
| Verb | existing `BUILD` |
| Operation | `SHARE` |
| Target | public live constructible the actor personally owns |
| Partner | one entered Player who is not already a steward |
| First stamp | `co_owner_id` (S11) |
| Second stamp | `co_owner_2_id` (S20) |
| Third stamp | `co_owner_3_id` (S21) |
| Fourth stamp | `co_owner_4_id` |
| Cap | 4 co-owners |
| Cost | compute 1 |
| Events | `ENTITY_UPDATE` + `BUDGET_CONSUMED` |
| Steward after | owner and all four co-owners |
| PLAY | `You share the {label} with {handle}.` |
| WATCH | silent |
| Help | still omits BUILD |

---

## Out of S22

```text
fifth-and-later co-owners
N-of-M roster
share / vest mix
STRUCTURE_*
Chamber help BUILD
```

---

## Runtime rule

Hosted Chamber MUST accept a fourth `BUILD.SHARE` from the personal owner, set `co_owner_4_id` to one other entered Player, treat owner and all four co-owners as stewards, and reject a fifth SHARE. Isolated tests only. Help unchanged. No Genesis change.
