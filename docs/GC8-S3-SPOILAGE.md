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

## Extension Points

Non-normative guidance for future maintenance; no new behavior is authorized here.

- **Resource lifecycle seam:** Extend cases for WORN resource keys across cycle commits, including multiple keys and exhaustion. Keep SOUND holdings unchanged and retain integer one-unit loss rather than percentages or elapsed-time decay.
- **Compatibility boundary:** RFC-0047 and economy-catalog/gc8-s3 own this spoilage rule. Transport and later economic slices need their own pins; neither the note nor an extra fixture opens v0.6B, currency, or order-book behavior.
- **Validation expectations:** Check positive remaining stock, exactly one remaining unit, multiple WORN keys, and a SOUND comparison. At zero, verify grade and origin clear together with no negative balance; compare replayed holdings and ensure no duplicate cycle loss or WATCH feed.
