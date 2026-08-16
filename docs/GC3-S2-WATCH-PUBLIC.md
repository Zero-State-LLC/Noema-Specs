# GC3-S2 — WATCH Public Descriptor Bands

**Status:** Executable specification. Runtime authorized with RFC-0034.  
**Parent:** [SOCIAL-MEMORY.md](SOCIAL-MEMORY.md) · [GC3-FIRST-SLICE.md](GC3-FIRST-SLICE.md) · [GC3-S1-BETRAYAL.md](GC3-S1-BETRAYAL.md)  
**RFC:** [RFC-0034](../rfcs/RFC-0034-watch-public-descriptors.md)  
**Does not open:** `reputation = 72` · `REMEMBER` verb · GC3-S0/S1 on WATCH · `unknown` as a hint

S2 is the public-descriptor surface pinned in SOCIAL-MEMORY. It does **not** project private trade or private danger. Silence is absence.

---

## Doctrine decisions

| Temptation | Verdict |
|------------|---------|
| S0 `reliable` on WATCH | **REJECT.** Private dyadic counts |
| Emit `unknown` when silent | **REJECT.** Hint / leak |
| S1 private danger on WATCH | **REJECT.** Subject-only |
| New public recognition event | **REJECT.** No catalog expansion |

---

## Slice contract

| Field | Value |
|-------|--------|
| Slice id | `gc3-s2` |
| Catalog | `social-memory-catalog/gc3-s2` |
| Edge | Public actor handle → band |
| Evidence (closed) | Public hostile / breach / contradicted public ATTEST |
| State | Derived. Not WorldState |
| WATCH | Coarse bands only, or silent |

### Public evidence

| Event | Public? | Band | Object |
|-------|---------|------|--------|
| `CONTEST_RESOLVED` | Always | `dangerous` | `declarer_id` |
| `CRIME_DETECTED` | only `visibility=PUBLIC` | `dangerous` | `subject_id` |
| `AGREEMENT_BROKEN` | only `visibility=PUBLIC` | `deceptive` | `broken_by` |
| Contradicted `ATTEST` | both claims `visibility=PUBLIC` | `deceptive` | earlier attester |
| `TRADE_ACCEPTED` / `TRADE_REJECTED` / `MESSAGE` | never | none | — |

Replay of the same evidence id does not double-count. Institutional or private visibility does not credit.

### Threshold

| Distinct public evidence ids naming that object | WATCH / public PLAY line |
|-------------------------------------------------|--------------------------|
| 0 | omit (silent) |
| ≥ 1 dangerous | `{name} is publicly dangerous.` |
| ≥ 1 deceptive | `{name} is publicly deceptive.` |

Both lines MAY appear. Never `reliable`. Never `unknown`. `{name}` is the public handle.

### Visibility

| Audience | S2 |
|----------|----|
| WATCH | Public lines only |
| Any Player PLAY | Same public lines (not private S0/S1) |
| GUI | MUST NOT hide TRADE because a public band exists |

---

## A–J

| Test | Result |
|------|--------|
| A | Spectator + public event + information |
| B | Uncertainty: private trades stay off WATCH |
| C | No extra command |
| D | Public contest / breach only |
| E | No new verb |
| F | Public caution can form |
| G | Evidence refs are public event ids |
| H | Same rebuild for every spectator |
| I | Meaningful with STUDY hidden |
| J | Without this, WATCH cannot show public standing without leaking S0/S1 |

---

## Out of S2

```text
GC3-S0 / GC3-S1 WATCH projection
reliable / unknown / generous / loyal bands
institution-only records
MESSAGE text
```

---

## Runtime rule

Hosted Chamber MAY project S2 lines on `/watch` and as public PLAY copy when public evidence exists. If Perihelion has no qualifying public events, WATCH stays silent. Help unchanged. No Genesis change.
