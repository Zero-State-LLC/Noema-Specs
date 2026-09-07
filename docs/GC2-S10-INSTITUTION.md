# GC2-S10 — institution-owned constructibles

**Status:** Executable specification. Runtime authorized with RFC-0067.  
**Parent:** [GC2-S9-MULTICYCLE.md](GC2-S9-MULTICYCLE.md) · [GC4-S1-OFFICES.md](GC4-S1-OFFICES.md) · [CONSTRUCTION.md](CONSTRUCTION.md)  
**RFC:** [RFC-0067](../rfcs/RFC-0067-institution-own.md)  
**Does not open:** institution-as-Player · CONNECT · help BUILD · STRUCTURE_*  
**Next:** [GC2-S11-SHARED.md](GC2-S11-SHARED.md)

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
institution-as-Player
STRUCTURE_*
Chamber help BUILD
```

---

## Runtime rule

Hosted Chamber MUST accept `BUILD.VEST` from a personal owner who holds an occupied `OPERATE_NAMED_ASSET` office, set `owner_id` to that org, and treat that office holder as steward. Isolated tests only. Help unchanged. No Genesis change.

## Extension Points

Non-normative VEST conformance and ownership-projection seams under RFC-0067.

- Extend isolated validation cases across actor ownership, public/live constructible status and the occupied OPERATE_NAMED_ASSET office in the target org. The transfer keeps entity_id, sets owner_id to that org and assigns the office holder as steward; the institution never becomes a Player.
- Preserve compute 1 and ENTITY_UPDATE plus BUDGET_CONSUMED, WATCH silence and omitted BUILD help. No SHARED ownership, UNCLAIMED/scar/in-progress vesting, CONNECT entitlement, STRUCTURE_* event or new property law follows from a projection adapter.
- Compatibility/promotion: pin construction-catalog/gc2-s10 and office authority, compare existing BUILD.VEST serialization and do not borrow S11 behavior into this slice. An absent or revoked office cannot be repaired by Controller provenance or account-holder approval alone.
- Verification proposal: exercise one eligible personal owner and refusals for a wrong org, vacant office, non-owner, private target and in-progress constructible. Assert unchanged identity, permitted owner/steward result, exact cost/event path and no WATCH entry. Localize “The {label} is held by {org}.” with readable ownership context while retaining protocol identifiers and authorization boundaries.
