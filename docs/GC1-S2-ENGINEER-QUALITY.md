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

## Extension Points

Non-normative maintenance and integration guidance; the contracts cited above remain authoritative.

### Document-specific seam

Extend REPAIR evidence with the acting Agent Player’s distinct successful-repair entity set and prior work on the specific target. Present the practiced-hands consequence only when that same-asset predicate holds, rather than adding a general Engineer meter.

### Compatibility and promotion

RFC-0040 pins the +20 versus +15 condition delta and cap 100; no cost discount or WATCH title is added. Only Agent Players perform gameplay repair. Personal or institutional payment never changes whose repair history is counted, and mastery cannot waive an occupied OPERATE_NAMED_ASSET grant.

### Verification before adoption

Compare recognized/prior, recognized/new-target, unrecognized/prior, and near-cap repairs. Replay successful ENTITY_UPDATE evidence and verify failed attempts cannot manufacture prior work. Preserve payer authority checks and confirm WATCH omits the quality bonus; changing these predicates requires a successor RFC, not copy polish.
