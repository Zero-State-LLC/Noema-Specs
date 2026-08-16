# GC1-S2 — Same-Asset Engineer Quality

**Status:** Executable specification. Runtime authorized with RFC-0040.  
**Depends on:** [GC1-S1-RECOGNITION.md](GC1-S1-RECOGNITION.md)  
**RFC:** [RFC-0040](../rfcs/RFC-0040-engineer-quality.md)  
**Does not open:** decay · public titles · other-track benefits · new verbs · `event-catalog/0.3`

S2 is the first world-native mastery benefit. Extra condition is **prior work on that machine**, not a class buff.

---

## Doctrine decisions

| Temptation | Verdict |
|------------|---------|
| +N on every REPAIR | **REJECT.** Level percent |
| Workshop required | **REJECT** for this slice (no class on Perihelion) |
| Only post-recognition history | **REJECT.** Re-taxes prior work |
| Change REPAIR cost | **REJECT.** |
| WATCH “Engineer” | **REJECT.** |

---

## Slice contract

| Field | Value |
|-------|--------|
| Slice id | `gc1-s2` |
| Catalog | `mastery-catalog/gc1-s2` |
| Who | S1-recognized Engineer (3 distinct repaired entities) |
| Prior work | Acting Player has ≥1 successful REPAIR on this `entity_id` |
| Delta | +20 if recognized and prior; else +15 |
| Cap | 100 |
| Payer | Personal or `acting_for` + occupied `OPERATE_NAMED_ASSET` |
| Evidence | Acting Player |

PLAY line on bonus: `You work this {label} with practiced hands.`

---

## Rebuild

Walk this Player’s successful repair `ENTITY_UPDATE`s. Distinct `entity_id`s are the S1 set. If that set size ≥ 3 and the current `entity_id` is already in the set, delta is 20.

---

## Out of S2

```text
decay / latent / focus
WATCH / public titles
Explorer / Surveyor / Broker benefits
SPECIALIZATION_* events
workshop class
```

---

## Runtime rule

Hosted Chamber MUST apply +20 only when `repairConditionDelta` says bonus 5. Isolated tests only. Help still omits BUILD. No Genesis change.
