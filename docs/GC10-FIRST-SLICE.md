# GC10 First Slice — Seeded Mild Relay Pressure

**Status:** Executable specification. Not a runtime implementation.  
**Parent:** [WORLD-EVENT-DIRECTOR.md](WORLD-EVENT-DIRECTOR.md) · [COMPLEXITY-DOCTRINE.md](COMPLEXITY-DOCTRINE.md)  
**RFC:** [RFC-0014](../rfcs/RFC-0014-wed-schedule-pressure.md)  
**Does not open:** `event-catalog/0.3` · `SITUATION_INJECTED` as WED · Admin “spawn content” · forced Player objectives · Frontier ID sharing

S0 is the smallest World Event Director increment that still satisfies scenario J’s *shape* (a bounded condition change; Players may respond differently; replay matches; PLAY has no correct answer). It reuses `ENTITY_UPDATE` on an existing relay. It is not Frontier and not a minigame.

---

## Doctrine decisions

| Temptation | Verdict |
|------------|---------|
| New `WED_*` / pressure event types | **REJECT.** Reuse `ENTITY_UPDATE` condition drop |
| Carry WED on `SITUATION_INJECTED` | **REJECT in S0.** That type is Frontier ([FRONTIER-DIRECTOR.md](FRONTIER-DIRECTOR.md), [OPERATOR-INTERVENTIONS.md](OPERATOR-INTERVENTIONS.md)). IDs must not be shared |
| Admin Live spawn button | **REJECT.** First-world Admin is not world-edit |
| Player / LLM / STUDY inject | **REJECT** |
| Forced “you should REPAIR” | **REJECT.** No required response |
| Research class name in PLAY | **REJECT.** Symptoms only (existing condition observation) |
| Grant lots to a favored Player | **REJECT** |
| Rewrite history / uncatalogued entity | **REJECT** |
| Drop relay below the GC5 band on first fire | **REJECT.** Mild: keep condition ≥ 25 |

Pressures: **scarcity** (condition is a real bottleneck) and **uncertainty** (Players are not told the exam name).

---

## Slice contract

| Field | Value |
|-------|--------|
| Slice id | `gc10-s0` |
| Catalog | `pressure-catalog/gc10-s0` |
| Class | `infrastructure_failure` only |
| Activate event | Existing `ENTITY_UPDATE` (`set.condition` or `field=condition`) |
| Default authorizer | Seeded **schedule** |
| Also allowed | Authorized operator after preview |
| First schedule cycle | **4** ([FIRST-20-CYCLES.md](FIRST-20-CYCLES.md) band 4–7) |
| Intensity | Condition **−15** (the existing `REPAIR` increment, inverted) |
| Chamber seed relay | ~70 → 55. Still above GC5 long-range band 25 |

### Activation path

```text
preview (condition_before − 15 → condition_after)
  → authorizer ∈ {schedule, operator}
  → ENTITY_UPDATE
  → audit receipt (authorizer, preview digest, event_id, cycle)
```

Preview of the same inputs MUST equal activation. Replaying the ledger without this schedule MUST NOT invent the drop.

### Responses (none required)

Players MAY `REPAIR`, `MOVE`, `TRADE`, `WAIT`, `HARVEST`, or do nothing. S0 names no correct verb. Recovery of this class is existing `COMMIT.REPAIR` (+15).

### Visibility

| Surface | S0 |
|---------|----|
| PLAY | Existing condition / LOOK / INSPECT. No `WED`, no class id, no “Event:” |
| WATCH | Public infra condition already allowed. No research label |
| STUDY | MAY name `infrastructure_failure` in the research partition only |
| Admin Live | MUST NOT expose spawn |

### Cooldown

At most **one** schedule activation of this class in cycles 1–20. Further classes and operator storms are out of S0.

---

## A–J

| Test | Result |
|------|--------|
| A | Asset + location. No eighth “event” primitive |
| B | Scarcity + uncertainty |
| C | No Player command added |
| D | Couples to REPAIR, GC5 relay bands, GC9 custom, trade, movement |
| E | Verb-stable |
| F | Hoard / repair / leave habits can diverge without a crisis engine |
| G | `ENTITY_UPDATE` remains attributable |
| H | Human and agent Players see the same condition |
| I | Meaningful with STUDY hidden |
| J | Without this, “mild pressure after a few cycles” is an unpinned sentence |

---

## Out of S0

```text
resource scarcity / migration / outage / artifact / institutional crisis / unknown signal
SITUATION_INJECTED as WED
WED_* event-catalog/0.3
Admin spawn
operator storm / multi-class schedule
irreversible scar class
forced objectives
Frontier request IDs
```

---

## Runtime rule

This document does not add a production schedule to Perihelion Reach and does not thaw Admin injects. Hosted condition stays as seeded until an implementation pass is authorized. Do not activate or reseed Genesis.

## Acceptance (narrower than scenario J)

1. Schedule at cycle 4 drops a named live relay by 15 via `ENTITY_UPDATE`.
2. Preview equals activation.
3. `REPAIR` / `MOVE` / `TRADE` / `WAIT` are all legal responses; none is required.
4. PLAY lines contain no research class name.
5. Player/LLM authorizer, Frontier ID reuse, and forced response are rejected.

Full scenario J (divergent trajectories under research observation, additional classes) is **GC10-S1**.
