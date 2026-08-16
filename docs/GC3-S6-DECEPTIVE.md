# GC3-S6 — Deceptive as a Distinct Edge

**Status:** Executable specification. Runtime authorized with RFC-0038.  
**Parent:** [SOCIAL-MEMORY.md](SOCIAL-MEMORY.md) · [GC3-S1-BETRAYAL.md](GC3-S1-BETRAYAL.md)  
**RFC:** [RFC-0038](../rfcs/RFC-0038-deceptive-edge.md)  
**Does not open:** `TRADE_REJECTED` → deceptive · `LIE` verb · WATCH on this slice

S6 is promise-breaking and contradicted public attestation. It is not hostility (S1) and not a declined trade.

---

## Doctrine decisions

| Temptation | Verdict |
|------------|---------|
| `TRADE_REJECTED` → deceptive | **REJECT.** Legal decline |
| Merge into S1 danger | **REJECT.** Distinct band |
| MESSAGE text as a public lie | **REJECT.** Recipient-only |
| New LIE / ACCUSE verb | **REJECT.** |

---

## Slice contract

| Field | Value |
|-------|--------|
| Slice id | `gc3-s6` |
| Catalog | `social-memory-catalog/gc3-s6` |
| Edge | Directed subject → object |
| Evidence (closed) | `AGREEMENT_BROKEN`; contradicted public `ATTEST` |
| State | Derived. Not WorldState |
| WATCH | Empty on this slice (S2 may project public breaks) |

### Evidence rules

| Event | Who remembers whom | Evidence id |
|-------|--------------------|-------------|
| `AGREEMENT_BROKEN` | every other `party_id` → `broken_by` | `breach_id` or `event_id` |
| Contradicted public `ATTEST` | any observer of both public claims → earlier attester | later `event_id` |

`ATTEST` contradiction: two events, both `visibility=PUBLIC`, same `subject_entity_id`, opposite `archive_claim` (`DESTROYED` vs `OPERATING`). The object is the attester of the **earlier** claim.

`TRADE_REJECTED`, `CONTEST_DECLARED`, `CONTEST_RESOLVED`, and `MESSAGE` do not credit.

The same `AGREEMENT_BROKEN` MAY also credit S1 danger. Two edges, one event. Do not collapse.

### Threshold

| Distinct deceptive evidence ids | Self PLAY line |
|---------------------------------|----------------|
| 0 | omit |
| ≥ 1 | `You have found {name} deceptive.` |

---

## A–J

| Test | Result |
|------|--------|
| A | Player + broken agreement / public attest |
| B | Uncertainty: C does not see a private decline |
| C | No extra command |
| D | Agreement / archive claim already exist |
| E | No new verb |
| F | Caution or later restitution (S4) can form |
| G | Evidence refs are breach/attest ids |
| H | Same rebuild for human and agent |
| I | Meaningful with STUDY hidden |
| J | Without this, lying and declining a trade are the same |

---

## Out of S6

```text
TRADE_REJECTED as deception
CONTEST_RESOLVED as deception
MESSAGE as public reputation
WATCH titles on this slice
```

---

## Runtime rule

Hosted Chamber MAY project S6 on self PLAY. `AGREEMENT_FORM` stays at whatever thaw already exists; this slice rebuilds when `AGREEMENT_BROKEN` exists and does not thaw forming. Help unchanged. WATCH empty here.
