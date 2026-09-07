# GC2-S4 — archive_annex

**Status:** Executable specification. Runtime authorized with RFC-0053.  
**Parent:** [GC2-S3-DEFENSIVE-WORK.md](GC2-S3-DEFENSIVE-WORK.md) · [CONSTRUCTION.md](CONSTRUCTION.md) · [SYSTEMIC-DISCOVERY.md](SYSTEMIC-DISCOVERY.md)  
**RFC:** [RFC-0053](../rfcs/RFC-0053-archive-annex.md)  
**Does not open:** QUEST · oracle · help BUILD/ATTEST · hidden rooms

S4 adds a reading room. A live `archive_annex` saves one attention on INSPECT and ATTEST in that room.

---

## Doctrine decisions

| Temptation | Verdict |
|------------|---------|
| QUEST / oracle | **REJECT.** |
| Invented evidence | **REJECT.** |
| Annex required to ATTEST | **REJECT.** Soft-lock |
| Help BUILD / ATTEST | **REJECT.** |

---

## Slice contract

| Field | Value |
|-------|--------|
| Slice id | `gc2-s4` |
| Catalog | `construction-catalog/gc2-s4` |
| Class | `archive_annex` |
| Construct | energy 6, compute 4, storage 4, influence 2 |
| Salvage | 2 |
| Slot | one live per public room |
| Effect | in-room INSPECT and ATTEST attention −1 (floor 0) |
| PLAY | `An archive annex is open.` |
| WATCH | silent |
| Help | still omits BUILD and ATTEST |

---

## Out of S4

```text
UPGRADE — closed in [GC2-S5-UPGRADE.md](GC2-S5-UPGRADE.md)
CONNECT QUEST
Chamber help BUILD ATTEST
```

---

## Runtime rule

Hosted Chamber MUST accept `BUILD.CONSTRUCT class=archive_annex` in a public room and discount in-room INSPECT/ATTEST attention by 1. Isolated tests only. Help unchanged. No Genesis change.

## Extension Points

Non-normative guidance for future work; this section changes no current contract.

### Archive-annex cost composition

Additional fixtures can exercise the annex discount alongside already-authorized cost modifiers and access checks. The annex is a local attention discount, never an evidence source, oracle or prerequisite for ATTEST.

Preserve RFC-0053 costs, public-room slot and floor-zero semantics; route upgrades to the existing S5 authority instead of reopening them here. Validate INSPECT and ATTEST in and outside the room, zero-floor behavior, absent/non-live annexes and removal of the discount after dismantle, without WATCH or help expansion.
