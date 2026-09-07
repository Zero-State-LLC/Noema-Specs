# GC2-S7 — abandonment

**Status:** Executable specification. Runtime authorized with RFC-0058.  
**Parent:** [GC2-S6-REPURPOSE.md](GC2-S6-REPURPOSE.md) · [CONSTRUCTION.md](CONSTRUCTION.md)  
**RFC:** [RFC-0058](../rfcs/RFC-0058-abandonment.md)  
**Does not open:** RESTORE · scar-on-abandon · evict · help BUILD · STRUCTURE_*

S7 makes neglect a world fact. After 12 committed idle cycles a public constructible is `UNCLAIMED`. Anyone may dismantle it.

---

## Doctrine decisions

| Temptation | Verdict |
|------------|---------|
| Auto-delete | **REJECT.** |
| Scar on abandon | **REJECT.** |
| Evict the Player | **REJECT.** |
| Hidden abandon | **REJECT.** |
| WATCH ticker | **REJECT.** |

---

## Slice contract

| Field | Value |
|-------|--------|
| Slice id | `gc2-s7` |
| Catalog | `construction-catalog/gc2-s7` |
| Window | 12 committed cycles |
| Reset | owner `REPAIR` or `UPGRADE` |
| Place | public rooms only |
| Result | `UNCLAIMED`; entity kept |
| Dismantle | any colocated Player |
| Events | `ENTITY_UPDATE` |
| PLAY | `The {label} is unclaimed.` |
| WATCH | silent |
| Help | unchanged |

---

## Out of S7

```text
RESTORE — closed in [GC2-S8-RESTORE.md](GC2-S8-RESTORE.md)
CONNECT
scar on abandon
evict / delete
STRUCTURE_*
Chamber help BUILD
```

---

## Runtime rule

Hosted Chamber MUST mark a public constructible `UNCLAIMED` after 12 committed cycles with no owner REPAIR/UPGRADE, and MUST allow any colocated Player to DISMANTLE it. Isolated tests only. Help unchanged. No Genesis change.

## Extension Points

Non-normative guidance for future maintenance; no new behavior is authorized here.

- **Lifecycle seam:** Extend boundary fixtures around the committed-cycle idle counter and owner REPAIR/UPGRADE resets. Keep the entity and its stable identity when it becomes UNCLAIMED; abandonment is neither deletion nor a scar producer.
- **Compatibility boundary:** RFC-0058 and construction-catalog/gc2-s7 own the 12-cycle rule. RESTORE is already closed by S8, not a new proposal here. Different windows or triggers require explicit versioned authority rather than local scheduler defaults.
- **Validation expectations:** Compare the state immediately before and at expiry, a qualifying reset before expiry, hidden-room exclusion, and colocated versus remote dismantling attempts. Rebuild after replay and confirm no eviction, auto-delete, WATCH ticker, or hidden extra event.
