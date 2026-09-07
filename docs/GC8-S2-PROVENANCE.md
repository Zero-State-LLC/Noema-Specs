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

## Extension Points

Non-normative origin projection and stack-merge regression seams.

- Extend provenance fixtures for public HARVEST stamps (room_id and producer_id), hidden harvest with no stamp, and merging different-room lots to clear origin. Render an authorized public room name rather than exposing storage IDs.
- Preserve forgotten mixed origins, silent WATCH, unchanged help and no hidden-room stamp even in metadata, translated placeholders or accessible labels. No contributor-room list, spoilage or transport economy is introduced.
- Compatibility/promotion: pin economy-catalog/gc8-s2/RFC-0046 with S1 quality so origin display neither replaces quality nor silently upgrades old unstamped lots. Any new provenance field requires accepted schema review rather than a UI-derived guess.
- Verification proposal: harvest public/hidden, merge same/different origins, replay and inspect PLAY/WATCH payloads. Check mixed/unstamped output does not falsely claim a source and producer storage is not automatically public. Keep resource and room placeholders intact across localized wrappers.
