# GC3-S4 — Decay and Rehabilitation Weights

**Status:** Executable specification. Runtime authorized with RFC-0036.  
**Parent:** [SOCIAL-MEMORY.md](SOCIAL-MEMORY.md) · [DEEP-TIME.md](DEEP-TIME.md)  
**RFC:** [RFC-0036](../rfcs/RFC-0036-decay-rehab.md)  
**Does not open:** wipe verb · ledger rewrite · paid reputation reset

S4 is a weight overlay on GC3-S0 / S1 / S3 / S6. Events stay. Lines may soften.

---

## Doctrine decisions

| Temptation | Verdict |
|------------|---------|
| Delete events | **REJECT.** Ledger never forgets |
| Paid wipe / FORGIVE | **REJECT.** |
| Decay after 1 idle cycle | **REJECT.** Too fast |
| Rehab on 1 trade | **REJECT.** Matches S0 floor of 3 |

---

## Slice contract

| Field | Value |
|-------|--------|
| Slice id | `gc3-s4` |
| Catalog | `social-memory-catalog/gc3-s4` |
| Input | S0/S1/S3/S6 evidence sets + `as_of_cycle` |
| Output | Weight 0 or 1 per family toward an object |
| WATCH | Uses the same weights for S2 |

### Decay

`decay_cycles = 12`.

For each family (trade, danger, deceptive, membership) toward each object: if `as_of_cycle - last_evidence_cycle >= 12`, weight = 0 and that family's line is omitted.

Membership “current member” is not decayed by idle time; it follows last ADD/REMOVE.

### Rehabilitation

If, after the latest danger or deceptive evidence id toward an object, the subject completes **3** distinct `TRADE_ACCEPTED` with that object, hostile weight toward that object becomes 0. Trade weight still follows S0 / S4 decay.

### Contested

When trade weight > 0 and hostile weight > 0, both lines MAY show. Do not collapse into one integer.

### Rebuild

1. Rebuild underlying S0/S1/S3/S6 evidence at full history.
2. Apply decay and rehab at `as_of_cycle`.
3. Emit only families with weight > 0.

---

## A–J

| Test | Result |
|------|--------|
| A | Time + existing evidence |
| B | Old hostility may fade; the report remains |
| C | No extra command |
| D | Coupled to TRADE / contest already specified |
| E | No new verb |
| F | Restitution trades can form a rehab habit |
| G | Same evidence ids; weights are derived |
| H | Same overlay for human and agent |
| I | Meaningful with STUDY hidden |
| J | Without this, scars never soften and wipe temptations win |

---

## Out of S4

```text
FORGIVE / WIPE verb
rewriting or deleting ledger rows
cycle-1 decay
one-trade rehab
```

---

## Runtime rule

Hosted Chamber MAY apply S4 when projecting S0/S1/S2/S3/S6. `as_of_cycle` is the world's current cycle. No Genesis change.
