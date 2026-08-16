# GC2-S5 — workshop UPGRADE

**Status:** Executable specification. Runtime authorized with RFC-0056.  
**Parent:** [GC2-S4-ARCHIVE-ANNEX.md](GC2-S4-ARCHIVE-ANNEX.md) · [CONSTRUCTION.md](CONSTRUCTION.md)  
**RFC:** [RFC-0056](../rfcs/RFC-0056-workshop-upgrade.md)  
**Does not open:** CONNECT · REPURPOSE · STRUCTURE_* · help BUILD · other-class upgrades

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
REPURPOSE CONNECT RESTORE
other-class UPGRADE
STRUCTURE_*
Chamber help BUILD
```

---

## Runtime rule

Hosted Chamber MUST accept `BUILD.UPGRADE` on an owned public workshop and raise that room’s workshop storage save from 1 to 2. Isolated tests only. Help unchanged. No Genesis change.
