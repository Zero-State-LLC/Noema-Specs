# GC2-S5 — workshop UPGRADE

**Status:** Executable specification. Runtime authorized with RFC-0056.  
**Parent:** [GC2-S4-ARCHIVE-ANNEX.md](GC2-S4-ARCHIVE-ANNEX.md) · [CONSTRUCTION.md](CONSTRUCTION.md)  
**RFC:** [RFC-0056](../rfcs/RFC-0056-workshop-upgrade.md)  
**Does not open:** CONNECT · STRUCTURE_* · help BUILD · other-class upgrades

S5 increases one built dimension. An owned public workshop can be upgraded once. The room then saves 2 storage on CONSTRUCT and REPAIR.

---

## Doctrine decisions

| Temptation | Verdict |
|------------|---------|
| Upgrade every class | **REJECT.** |
| Repeatable UPGRADE | **REJECT.** |
| `STRUCTURE_UPGRADED` | **REJECT.** |
| CONNECT as UPGRADE | **REJECT.** |
| Help BUILD | **REJECT.** |

---

## Slice contract

| Field | Value |
|-------|--------|
| Slice id | `gc2-s5` |
| Catalog | `construction-catalog/gc2-s5` |
| Verb | existing `BUILD` |
| Operation | `UPGRADE` |
| Target | live public `workshop` the actor owns |
| Cost | energy 4, compute 2, storage 2, influence 1 |
| Effect | storage save **2** on in-room CONSTRUCT/REPAIR |
| Once | `tier` 0 → 1 |
| Events | `ENTITY_UPDATE` + `BUDGET_CONSUMED` |
| PLAY | `The workshop was upgraded.` |
| WATCH | silent |
| Help | still omits BUILD / upgrade |

---

## Out of S5

```text
REPURPOSE — closed in [GC2-S6-REPURPOSE.md](GC2-S6-REPURPOSE.md)
CONNECT RESTORE
other-class UPGRADE
STRUCTURE_*
Chamber help BUILD
```

---

## Runtime rule

Hosted Chamber MUST accept `BUILD.UPGRADE` on an owned public workshop and raise that room’s workshop storage save from 1 to 2. Isolated tests only. Help unchanged. No Genesis change.

## Extension Points

Non-normative extension guidance; this section does not change accepted behavior or prove runtime completion.

- Extend one-time workshop UPGRADE conformance around ownership and tier transitions. Preserve the live public owned target, tier 0→1, published energy/compute/storage/influence cost and storage save of two for in-room CONSTRUCT/REPAIR.

- Use existing BUILD.UPGRADE, ENTITY_UPDATE and BUDGET_CONSUMED only. Repeat upgrades, other classes, CONNECT reinterpretation, STRUCTURE_* events, WATCH output and help advertisement stay excluded.

- Pin construction-catalog/gc2-s5 and RFC-0056. A new tier, discount or target family needs separately accepted authority; do not import later REPURPOSE or RESTORE behavior into S5. Preserve isolated tests and Genesis boundaries.

- Validate a valid owned workshop plus wrong owner, private/non-live target, wrong class, insufficient budget and already-upgraded tier. Assert exactly one upgrade effect and unchanged resources/state on denial; compare post-upgrade room costs with the pinned effect.
