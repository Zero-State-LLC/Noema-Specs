# GC2-S21 — third co-owner

**Status:** Executable specification. Runtime authorized with RFC-0085.  
**Parent:** [GC2-S20-SECOND-CO-OWNER.md](GC2-S20-SECOND-CO-OWNER.md) · [CONSTRUCTION.md](CONSTRUCTION.md)  
**RFC:** [RFC-0085](../rfcs/RFC-0085-third-co-owner.md)  
**Does not open:** N-of-M roster · fourth co-owner · institution-as-Player · help BUILD · STRUCTURE_*  
**Next:** [GC2-S22-FOURTH-CO-OWNER.md](GC2-S22-FOURTH-CO-OWNER.md)

S21 lets the personal owner name one more Player on a public constructible. It is still not a title minigame.

---

## Doctrine decisions

| Temptation | Verdict |
|------------|---------|
| N-of-M roster | **REJECT.** Three co-owners. |
| Fourth-and-later | **REJECT.** |
| Co-owner SHARE | **REJECT.** Owner names. |
| Share institution assets | **REJECT.** |
| Vest after share | **REJECT.** |
| Institution-as-Player | **REJECT.** |
| Help BUILD | **REJECT.** |

---

## Slice contract

| Field | Value |
|-------|--------|
| Slice id | `gc2-s21` |
| Catalog | `construction-catalog/gc2-s21` |
| Verb | existing `BUILD` |
| Operation | `SHARE` |
| Target | public live constructible the actor personally owns |
| Partner | one entered Player who is not already a steward |
| First stamp | `co_owner_id` (S11) |
| Second stamp | `co_owner_2_id` (S20) |
| Third stamp | `co_owner_3_id` |
| Cap | 3 co-owners |
| Cost | compute 1 |
| Events | `ENTITY_UPDATE` + `BUDGET_CONSUMED` |
| Steward after | owner and all three co-owners |
| PLAY | `You share the {label} with {handle}.` |
| WATCH | silent |
| Help | still omits BUILD |

---

## Out of S21

```text
fourth co-owner is [GC2-S22-FOURTH-CO-OWNER.md](GC2-S22-FOURTH-CO-OWNER.md)
fifth co-owner is [GC2-S23-FIFTH-CO-OWNER.md](GC2-S23-FIFTH-CO-OWNER.md)
SHARE family closeout is [GC2-S24-SHARE-CLOSEOUT.md](GC2-S24-SHARE-CLOSEOUT.md)
N-of-M roster
share / vest mix
STRUCTURE_*
Chamber help BUILD
```

---

## Runtime rule

Hosted Chamber MUST accept a third `BUILD.SHARE` from the personal owner, set `co_owner_3_id` to one other entered Player, treat owner and all three co-owners as stewards, and reject a fourth SHARE. Isolated tests only. Help unchanged. No Genesis change.

## Extension Points

Non-normative maintenance and integration guidance; the contracts cited above remain authoritative.

### Document-specific seam

Extend ownership views with the ordered co_owner_id, co_owner_2_id, and co_owner_3_id stamps and their existing stewardship consequences. Show an eligible entered partner without exposing unobserved Player data or presenting co-owners as new institutional roles.

### Compatibility and promotion

RFC-0085 is the third-stamp slice: only the personal owner shares a public live constructible; no institution asset or share/vest mix. Its fourth-SHARE refusal is scoped to S21. Accepted S22/S23/S24 successors govern later pins; this EP neither reopens them nor invents an N-of-M roster.

### Verification before adoption

Test owner versus co-owner submission, duplicate partner, unentered partner, non-live target, and institutional ownership. Verify one compute charge and unchanged entity_id on success. Run fourth-stamp refusal against S21 specifically and keep successor fixtures separate so version comparison does not misclassify accepted later behavior.
