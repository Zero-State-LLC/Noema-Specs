# GC10-S2 — Irreversible Scar

**Status:** Executable specification. Runtime authorized with RFC-0051.  
**Parent:** [GC10-S1-PRESSURE.md](GC10-S1-PRESSURE.md) · [WORLD-EVENT-DIRECTOR.md](WORLD-EVENT-DIRECTOR.md) · [CONSTRUCTION.md](CONSTRUCTION.md)  
**RFC:** [RFC-0051](../rfcs/RFC-0051-irreversible-scar.md)  
**Does not open:** SCAR_* events · Admin spawn · pressure-to-zero · WATCH ticker · help BUILD

S2 leaves a public scar when live infrastructure is dismantled. The scar cannot be repaired.

---

## Doctrine decisions

| Temptation | Verdict |
|------------|---------|
| New events | **REJECT.** |
| Pressure scars | **REJECT.** S0/S1 stay recoverable |
| Repair the leftover | **REJECT.** |
| Hidden-room scar | **REJECT.** |
| Help BUILD | **REJECT.** |

---

## Slice contract

| Field | Value |
|-------|--------|
| Slice id | `gc10-s2` |
| Catalog | `pressure-catalog/gc10-s2` |
| Trigger | public `DISMANTLE` |
| Events | existing `ENTITY_DESTROY` then `ENTITY_CREATE` |
| Leftover | `RUIN` `scar=true` label `scarred-{class}` |
| Repair | forbidden |
| Hidden | no scar |
| Pressure | does not scar |
| PLAY | `A scar remains.` |
| WATCH | silent |

---

## Out of S2

```text
SCAR_* events
Admin spawn
pressure-to-zero scars
artifact emergence
Chamber help BUILD
```

---

## Runtime rule

Hosted Chamber MUST leave an irreparable public scar after DISMANTLE. Isolated tests only. Help unchanged. No Genesis change.
