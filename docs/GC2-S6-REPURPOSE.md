# GC2-S6 — workshop REPURPOSE

**Status:** Executable specification. Runtime authorized with RFC-0057.  
**Parent:** [GC2-S5-UPGRADE.md](GC2-S5-UPGRADE.md) · [CONSTRUCTION.md](CONSTRUCTION.md)  
**RFC:** [RFC-0057](../rfcs/RFC-0057-workshop-repurpose.md)  
**Does not open:** CONNECT · RESTORE · STRUCTURE_* · help BUILD · other conversions

S6 changes one function class. An owned public workshop can be repurposed as a storage bay. The same `entity_id` remains.

---

## Doctrine decisions

| Temptation | Verdict |
|------------|---------|
| Other conversions | **REJECT.** Closed table only |
| New `entity_id` | **REJECT.** |
| `STRUCTURE_REPURPOSED` | **REJECT.** |
| CONNECT as REPURPOSE | **REJECT.** |
| Help BUILD | **REJECT.** |

---

## Slice contract

| Field | Value |
|-------|--------|
| Slice id | `gc2-s6` |
| Catalog | `construction-catalog/gc2-s6` |
| Verb | existing `BUILD` |
| Operation | `REPURPOSE` |
| Target | live public `workshop` the actor owns |
| Conversion | `workshop` → `storage_bay` only |
| Identity | same `entity_id` |
| Cost | energy 4, compute 2, storage 2, influence 1 |
| Events | `ENTITY_UPDATE` + `BUDGET_CONSUMED` |
| PLAY | `The workshop was repurposed as a storage bay.` |
| WATCH | silent |
| Help | still omits BUILD / repurpose |

---

## Out of S6

```text
CONNECT RESTORE
abandonment — closed in [GC2-S7-ABANDON.md](GC2-S7-ABANDON.md)
other conversions
STRUCTURE_*
Chamber help BUILD
```

---

## Runtime rule

Hosted Chamber MUST accept `BUILD.REPURPOSE` on an owned public workshop and change that entity’s class to `storage_bay` without changing `entity_id`. Isolated tests only. Help unchanged. No Genesis change.

## Extension Points

Non-normative guidance for future work; existing authorities and closed-slice boundaries remain unchanged.

- **Seam and invariants.** Conversion validation can gain clearer failure examples for the closed workshop-to-storage_bay mapping. Preserve owned live public targets, entity identity, the pinned debit and existing event types.
- **Compatibility and validation.** Test unsupported reverse/other conversions, non-owner and non-live targets, insufficient budget and unchanged entity_id on success. Any additional conversion belongs in an Accepted RFC and new construction-catalog scope; it must not silently broaden gc2-s6 or advertise new help commands.
