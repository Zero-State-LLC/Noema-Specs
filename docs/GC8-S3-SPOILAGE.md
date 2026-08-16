# GC8-S3 — Worn Lot Spoilage

**Status:** Executable specification. Runtime authorized with RFC-0047.  
**Parent:** [GC8-S2-PROVENANCE.md](GC8-S2-PROVENANCE.md) · [ECONOMIC-SPECIALIZATION.md](ECONOMIC-SPECIALIZATION.md)  
**RFC:** [RFC-0047](../rfcs/RFC-0047-lot-spoilage.md)  
**Does not open:** transport table · currency · v0.6B · WATCH ticker

S3 makes WORN lots perish. SOUND lasts. Loss is one unit per committed cycle.

---

## Doctrine decisions

| Temptation | Verdict |
|------------|---------|
| Spoil SOUND | **REJECT.** |
| Percent / floats | **REJECT.** |
| Transport table | **DEFER.** |
| WATCH spoilage feed | **REJECT.** |

---

## Slice contract

| Field | Value |
|-------|--------|
| Slice id | `gc8-s3` |
| Catalog | `economy-catalog/gc8-s3` |
| Who | WORN stacks only |
| When | each committed world cycle |
| Loss | 1 per WORN resource key |
| Exhaust | remaining 0 clears grade and origin |
| PLAY | `Your worn {resource} spoiled.` |
| WATCH | silent |

---

## Out of S3

```text
transport table
currency order book v0.6B
SOUND decay
WATCH ticker
```

---

## Runtime rule

Hosted Chamber MUST spoil WORN holdings on cycle commit. Isolated tests only. Help unchanged. No Genesis change.
