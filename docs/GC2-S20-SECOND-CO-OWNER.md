# GC2-S20 — second co-owner

**Status:** Executable specification. Runtime authorized with RFC-0079.  
**Parent:** [GC2-S11-SHARED.md](GC2-S11-SHARED.md) · [CONSTRUCTION.md](CONSTRUCTION.md)  
**RFC:** [RFC-0079](../rfcs/RFC-0079-second-co-owner.md)  
**Does not open:** N-of-M roster · fourth co-owner · institution-as-Player · help BUILD · STRUCTURE_*  
**Next:** [GC2-S21-THIRD-CO-OWNER.md](GC2-S21-THIRD-CO-OWNER.md)

S20 lets the personal owner name one more Player on a public constructible. It is still not a title minigame.

---

## Doctrine decisions

| Temptation | Verdict |
|------------|---------|
| N-of-M roster | **REJECT.** Two co-owners. |
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
| Slice id | `gc2-s20` |
| Catalog | `construction-catalog/gc2-s20` |
| Verb | existing `BUILD` |
| Operation | `SHARE` |
| Target | public live constructible the actor personally owns |
| Partner | one entered Player who is not already a steward |
| First stamp | `co_owner_id` (S11) |
| Second stamp | `co_owner_2_id` |
| Cap | 2 co-owners |
| Cost | compute 1 |
| Events | `ENTITY_UPDATE` + `BUDGET_CONSUMED` |
| Steward after | owner and both co-owners |
| PLAY | `You share the {label} with {handle}.` |
| WATCH | silent |
| Help | still omits BUILD |

---

## Out of S20

```text
third co-owner is [GC2-S21-THIRD-CO-OWNER.md](GC2-S21-THIRD-CO-OWNER.md)
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

Hosted Chamber MUST accept a second `BUILD.SHARE` from the personal owner, set `co_owner_2_id` to one other entered Player, treat owner and both co-owners as stewards, and reject a third SHARE. Isolated tests only. Help unchanged. No Genesis change.

## Extension Points

Non-normative guidance for future maintenance; no new behavior is authorized here.

- **Stamp compatibility:** Extend fixtures for filling co_owner_2_id without changing the existing co_owner_id or entity identity. Stewardship can be checked across owner and both co-owners without introducing a roster engine.
- **Promotion boundary:** RFC-0079 and construction-catalog/gc2-s20 retain their two-co-owner cap. The linked S21–S24 successors describe later capacity under their own authority; do not rewrite S20 rejection expectations to match a later world pin.
- **Validation expectations:** Cover first-stamp compatibility, a distinct entered second partner, duplicate steward rejection, co-owner-initiated SHARE rejection, and a third SHARE under the S20 pin. Verify one compute debit on success, no mutation on refusal, and no WATCH or help expansion.
