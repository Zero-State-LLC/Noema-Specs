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

## Extension Points

Non-normative guidance for future maintenance; no new behavior is authorized here.

- **Ownership seam:** Additional conformance cases can exercise the transition from sole personal ownership to the first co-owner stamp while retaining entity identity and the existing BUILD.SHARE event/cost path.
- **Compatibility boundary:** Keep construction-catalog/gc2-s11 as the one-co-owner slice. Later SHARE capacity belongs to its own accepted slices, not a retroactive reinterpretation of S11. Institution assets, vest/share mixing, and arbitrary voting rosters remain outside this contract.
- **Validation expectations:** Check owner and co-owner stewardship after a valid share, and reject a non-owner actor, an unentered partner, or an institution-owned target. Compare event order and compute debit, retain WATCH silence, and prove that rejection does not modify ownership or spend.
