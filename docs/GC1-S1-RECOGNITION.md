# GC1-S1 — Recognition Projection

**Status:** Executable specification (RFC-0005 Accepted). Runtime may project recognized self-lines.  
**Depends on:** [GC1-FIRST-SLICE.md](GC1-FIRST-SLICE.md) (GC1-S0, shipped)  
**RFC:** [RFC-0005](../rfcs/RFC-0005-mastery-recognition.md) (**Accepted**)  
**Does not implement:** mechanical benefits · new verbs · `event-catalog/0.3` · WATCH recognition  
**Doctrine:** [COMPLEXITY-DOCTRINE.md](COMPLEXITY-DOCTRINE.md) — self-only evidence identity, not a class or repair percent. Passes A–J as projection-only.

S1 makes a Player **legibly known to themselves** for demonstrated work. It does **not** satisfy full completeness scenario A (that still needs one world-native benefit in a later S2).

---

## Why S1 before any benefit

| Option | Verdict |
|--------|---------|
| Add REPAIR quality / cheaper costs now | Changes frozen v0.1 action-contract magnitudes. Needs its own RFC (S2) |
| Public titles on other Players / WATCH | Leak and presentation risk before recognition is stable |
| GC2 Construction | Still larger than recognition |
| Recognition as derived self-projection | Uses S0 units. No catalog events. Safe on cycle-0 worlds |

S2 (not this document) is the first **benefit** family. Candidate: recognized Engineer restores more condition on `REPAIR`, via an explicit action-contract increment. Do not invent S2 magnitudes here.

---

## Settled S1 answers

| Question | Settlement |
|----------|------------|
| Selected or earned? | **Earned / inferred.** No class picker. Focus still disabled |
| New events? | **No.** Recognition is derived from the same S0 evidence |
| Visible to others? | **No** in S1. Self PLAY only |
| WATCH? | **No** |
| Mechanical benefit? | **No.** Costs, quality, parameters, targets, eligibility unchanged |
| Can one Player hold several recognitions? | **Yes.** Same 1–3 PLAY line cap as S0 (`max_play_lines = 3`) |
| Cycle-0 worlds? | Recognition MUST NOT require the world cycle to advance. Anti-spike is **distinct units**, not distinct cycles |
| Canonical vs derived? | Still **derived**. Not WorldState. Not a reducer input |

---

## Thresholds (pinned)

S0 `PRACTICING` stays `count >= 1`.

S1 `RECOGNIZED` uses **distinct units**:

| `track_id` | Recognition unit | Threshold |
|------------|------------------|-----------|
| `track.explorer.01` | Distinct `room_id` from `LOOK` | **5** |
| `track.surveyor.01` | Distinct `entity_id` from `INSPECT` | **5** |
| `track.broker.01` | Distinct `trade_id` from `TRADE_ACCEPTED` | **3** |
| `track.engineer.01` | Distinct repaired `entity_id` | **3** |

Engineer S0 practicing still increments on each attributed repair `event_id` (so one repair still shows the practicing line). Engineer **recognition** counts distinct infrastructure IDs, so repairing the same relay ten times in cycle 0 does **not** recognize.

A later catalog version may add a cycle-span rule. It MUST NOT replace this distinct-unit rule for cycle-frozen worlds.

---

## PLAY lines

When a track is `RECOGNIZED`, its practicing line is **replaced**, not stacked.

| `track_id` | PRACTICING (S0) | RECOGNIZED (S1) |
|------------|-----------------|-----------------|
| `track.explorer.01` | You have been learning the rooms. | You know these rooms. |
| `track.surveyor.01` | You have been doing survey work. | You are known for survey work. |
| `track.broker.01` | You have been closing exchanges. | You are known for closing exchanges. |
| `track.engineer.01` | You have been keeping infrastructure alive. | You are known for keeping infrastructure alive. |

Order remains catalog `display_order`. Cap remains 3. Prefer recognized tracks first, then practicing, still capped at 3.

Never print counts, XP, levels, or research scores.

---

## Hosted cache implication

S0 stores Engineer units as repair `event_id`s. S1 MUST also retain the repaired `entity_id` (and MAY keep event ids for practicing). Migration: existing S0 caches stay `PRACTICING` until distinct entity ids can be reconstructed. Historical hosted repairs **cannot** be reconstructed from the DO snapshot (**NOT_COMPUTABLE**). New repairs after S1 ships accumulate entity ids.

---

## Non-goals

```text
new verbs
new event types
WATCH / other-Player titles
institutional certification
focus
decay / LATENT
cost or quality changes
affordance changes
HELP class menu
```

---

## Acceptance (narrower than scenario A)

1. A Player inspects five distinct entities and sees `You are known for survey work.` instead of the practicing line.
2. Repairing one relay five times does not recognize Engineer.
3. Repairing three distinct infrastructure entities does.
4. Another Player’s `players_here` and WATCH still omit practice and recognition.
5. `REPAIR` still costs energy 3 / compute 2 / storage 1 and still adds +15 condition.

Full scenario A waits for **GC1-S2** (one benefit family, separate RFC).
