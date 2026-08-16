# GC8-S2 — Lot Provenance

**Status:** Executable specification. Runtime authorized with RFC-0046.  
**Parent:** [GC8-S1-LOT-QUALITY.md](GC8-S1-LOT-QUALITY.md) · [ECONOMIC-SPECIALIZATION.md](ECONOMIC-SPECIALIZATION.md)  
**RFC:** [RFC-0046](../rfcs/RFC-0046-lot-provenance.md)  
**Does not open:** hidden-room leak · WATCH ticker · spoilage · v0.6B

S2 remembers the public room a stack came from. Mixed origins forget. Hidden places leave no stamp.

---

## Doctrine decisions

| Temptation | Verdict |
|------------|---------|
| Stamp hidden rooms | **REJECT.** |
| List every contributing room | **REJECT.** |
| WATCH origin feed | **REJECT.** |
| Public room name on PLAY | **ACCEPT.** |

---

## Slice contract

| Field | Value |
|-------|--------|
| Slice id | `gc8-s2` |
| Catalog | `economy-catalog/gc8-s2` |
| Stamp | public `room_id` + `producer_id` on HARVEST |
| Hidden | no stamp |
| Mix | different rooms → clear |
| PLAY | `Your {resource} is from {room name}.` |
| WATCH | silent |

---

## Out of S2

```text
hidden room ids
WATCH ticker
storage spoilage
transport table
v0.6B
```

---

## Runtime rule

Hosted Chamber MUST stamp public harvests and clear mixed origins. Isolated tests only. Help unchanged. No Genesis change.
