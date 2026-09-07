# GC3-S1 — Dangerous from Formal Contest or Breach

**Status:** Executable specification. Runtime authorized with RFC-0022.  
**Parent:** [GC3-FIRST-SLICE.md](GC3-FIRST-SLICE.md) · [SOCIAL-MEMORY.md](SOCIAL-MEMORY.md)  
**RFC:** [RFC-0022](../rfcs/RFC-0022-betrayal-dangerous.md)  
**Does not open:** `reputation = 72` · `REMEMBER` verb · WATCH titles · trade-refusal automation · `event-catalog/0.3`

S1 is the smallest increment that still satisfies scenario B’s *betrayal* shape: a formal hostile or breach event changes a private descriptor. Cooperation memory (GC3-S0) stays. `TRADE_REJECTED` is still not deceptive.

---

## Doctrine decisions

| Temptation | Verdict |
|------------|---------|
| Reputation integer / subtract reliability | **REJECT.** Keep a separate danger edge |
| `TRADE_REJECTED` → deceptive | **REJECT.** Legal decline |
| New relationship events | **REJECT.** Rebuild from existing 0.1/0.2 types |
| WATCH “dangerous trader” | **REJECT.** Leak / presentation |
| Name hidden methods in the line | **REJECT.** |
| Auto trade friction / refuse | **DEFER** |

Pressures: **dependency** (you remember who contested you) and **uncertainty** (C does not see A–B danger).

---

## Slice contract

| Field | Value |
|-------|--------|
| Slice id | `gc3-s1` |
| Catalog | `social-memory-catalog/gc3-s1` |
| Edge | Directed victim → actor |
| Evidence (closed) | Distinct ids on `CONTEST_RESOLVED`, `AGREEMENT_BROKEN`, `CRIME_DETECTED` |
| State | Derived. Not WorldState |
| Public S1 projection | **None** |

### Evidence rules

| Event | Who remembers whom | Evidence id |
|-------|--------------------|-------------|
| `CONTEST_RESOLVED` | `defender_id` → `declarer_id` if both present; also `target.agent_id` → `declarer_id` when target kind is `AGENT` | `contest_id` |
| `AGREEMENT_BROKEN` | every other `party_id` → `broken_by` | `breach_id` or `event_id` |
| `CRIME_DETECTED` | named `victim_id` → `subject_id` only (no omniscient public mark) | `detection_id` |

`CONTEST_DECLARED` alone does not credit. Unresolved contests do not credit. Replay of the same evidence id does not double-count.

### Threshold

| Distinct danger evidence ids toward that object | Self PLAY line |
|-------------------------------------------------|----------------|
| 0 | omit danger line |
| ≥ 1 | `You have found {name} dangerous.` |

`{name}` is the object’s public handle. Never amounts, routes, hidden ids, contest form, or crime method.

GC3-S0 trade lines still apply independently. A Player MAY see both reliable-in-trade and dangerous for the same object (`CONTESTED` in parent prose; S1 does not collapse them).

### Visibility

## Extension Points

Non-normative private-edge reconstruction and redaction seams.

- Extend distinct-evidence fixtures for directed victim-to-actor danger from resolved contests, breaches and named-victim detections. Exercise both defender and AGENT target paths, agreement parties, missing participant IDs and duplicate contest/breach/detection IDs without inventing an unspecified fallback identity.
- Preserve derived rather than WorldState storage, threshold of one distinct admitted danger reference and independence from reliable-in-trade memory. A legal TRADE_REJECTED or unresolved/declared-only contest is not danger or deception evidence; no reputation scalar or automatic refusal is introduced.
- Compatibility/promotion: pin social-memory-catalog/gc3-s1 and RFC-0022 with existing event versions. Historical human/agent prose grants no human Player identity under RFC-0120; Controllers receive no extra victim memory. Future institutional or decay rules do not silently alter this slice.
- Verification proposal: rebuild duplicate and mixed reliable/danger evidence, then inspect self, unrelated Player, WATCH and GUI projections. Only authorized self PLAY may show the existing public-handle danger line; methods, stock, routes and private IDs remain absent, including accessible labels and translated text. No public danger badge is an extension seam.

## A–J

| Test | Result |
|------|--------|
| A | Player + contest/breach + information |
| B | Dependency + uncertainty |
| C | No extra command |
| D | Contest / later agreements; not a price engine |
| E | No new verb |
| F | Avoidance or compact-with-caution can form |
| G | Evidence refs are contest/breach/detection ids |
| H | Same rebuild for human and agent |
| I | Meaningful with STUDY hidden |
| J | Without this, betrayal has no private scar |

---

## Out of S1

```text
reputation scalar
WATCH titles
trade refusal automation
institution edges
decay / wipe
MESSAGE text as public reputation
```

---

## Runtime rule

Hosted Chamber credits danger from `CONTEST_RESOLVED` already emitted by GC7-S0. `AGREEMENT_BROKEN` / `CRIME_DETECTED` rebuild when those events exist; this slice does not thaw `AGREEMENT_FORM`. Help unchanged. WATCH empty.
