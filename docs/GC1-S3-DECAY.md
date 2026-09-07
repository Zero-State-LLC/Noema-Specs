# GC1-S3 — Mastery Decay

**Status:** Executable specification. Runtime authorized with RFC-0043.  
**Depends on:** [GC1-S2-ENGINEER-QUALITY.md](GC1-S2-ENGINEER-QUALITY.md)  
**RFC:** [RFC-0043](../rfcs/RFC-0043-mastery-decay.md)  
**Does not open:** WATCH titles · other-track benefits · focus · `event-catalog/0.3`

S3 lets recognition rust without forgetting. The Engineer +5 is a maintained practice, not a permanent class.

---

## Doctrine decisions

| Temptation | Verdict |
|------------|---------|
| Wipe evidence | **REJECT.** |
| Bonus while LATENT | **REJECT.** |
| 1-work restore | **REJECT.** 3 works |
| WATCH “was Engineer” | **REJECT.** |

---

## Slice contract

| Field | Value |
|-------|--------|
| Slice id | `gc1-s3` |
| Catalog | `mastery-catalog/gc1-s3` |
| Latent after | 12 cycles with no qualifying work on that track |
| Rehab | 3 qualifying successes while LATENT |
| Bonus | +5 only if Engineer recognized **and** MAINTAINED **and** prior asset |
| PLAY | was-known line while LATENT |

Engineer LATENT line: `You were known for keeping infrastructure alive.`

---

## Out of S3

```text
WATCH / public titles
Explorer / Surveyor / Broker benefits
FOCUS_DECLARED
SPECIALIZATION_* events
```

---

## Runtime rule

Hosted Chamber MUST treat Engineer as LATENT after 12 idle cycles and restore after 3 repairs. Isolated tests only. Help unchanged. No Genesis change.

## Extension Points

Non-normative boundary-fixture and private recognition-display seams.

- Extend isolated cases at the idle threshold and during rehabilitation: 12 cycles without qualifying track work makes recognition LATENT; restoration requires 3 qualifying successes, not a single repair. Retain prior evidence throughout decay.
- Preserve Engineer +5 only for recognized, MAINTAINED practice on a prior asset. LATENT recognition supplies the existing private was-known line, not a bonus, WATCH title, Explorer/Surveyor/Broker benefit or new focus event.
- Compatibility/promotion: pin mastery-catalog/gc1-s3 and RFC-0043 when comparing decay behavior; later slices do not silently widen this slice. Presentation refinements change neither counters nor Genesis/help.
- Verification proposal: test the cycle immediately before latency, the threshold, partial rehabilitation and restoration; compare bonus eligibility on prior versus other assets. Confirm WATCH remains silent and replay retains recognition evidence. Translate the was-known caption while keeping state distinctions explicit in text rather than color.
