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
