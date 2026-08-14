# GC10-S1 — Additional World Pressure Classes

**Status:** Executable specification. Runtime authorized with RFC-0027.  
**Parent:** [GC10-FIRST-SLICE.md](GC10-FIRST-SLICE.md) · [WORLD-EVENT-DIRECTOR.md](WORLD-EVENT-DIRECTOR.md) · [COMPLEXITY-DOCTRINE.md](COMPLEXITY-DOCTRINE.md)  
**RFC:** [RFC-0027](../rfcs/RFC-0027-additional-world-pressure.md)  
**Does not open:** quest/drama/NPC director · rubber-band · weather/famine/plague/war engines · `event-catalog/0.3` · Admin spawn · Genesis reseed

S1 widens the range of world conditions. It does not widen the game-engine ontology. GC10-S0 remains valid.

---

## Doctrine

```text
existing world cause
+ bounded parameter change
+ deterministic trigger
+ canonical transition
+ visible consequences
+ recoverability
```

```text
WORLD PRESSURE
≠ QUEST
≠ TARGETED PLAYER PUNISHMENT
≠ DIFFICULTY SCALING
≠ BALANCE RUBBER-BAND
≠ OPERATOR RAW EDIT
```

Hard rule: world pressure changes conditions. It must not select a desired Player outcome.

| Temptation | Verdict |
|------------|---------|
| New `WED_*` / `PRESSURE_*` events | **REJECT.** Reuse `ENTITY_UPDATE` / `ACCESS_RESTRICTED` |
| Communication outage engine | **REJECT.** Compose GC5 via relay condition |
| Distinct route engine | **REJECT.** Access restriction is the route primitive |
| Weather simulation | **REJECT.** No existing weather state |
| WAR / FAMINE / PLAGUE primitives | **REJECT.** Model causes, not genres |
| Player score / research metric targeting | **REJECT** |
| Rubber-band difficulty | **REJECT** |
| Admin spawn / raw SQL edit | **REJECT** |
| Forced “you should REPAIR / HARVEST / REROUTE” | **REJECT** |

Pressures: **scarcity**, **distance**, **dependency**, **uncertainty**.

---

## Class decisions

| Candidate | Verdict | Why |
|-----------|---------|-----|
| `INFRASTRUCTURE_PRESSURE` / `infrastructure_failure` | **KEEP (S0)** | Condition drop on live relay; couples to REPAIR, GC5, GC9, movement |
| `RESOURCE_PRESSURE` / `resource_scarcity` | **ACCEPT** | Stock drop on existing harvest node; couples to HARVEST, trade, travel |
| `ACCESS_PRESSURE` / `access_restriction` | **ACCEPT** | Temporary public-exit `ACCESS_RESTRICTED`; couples to MOVE, trade, contest context |
| `COMMUNICATION_PRESSURE` | **REJECT as engine** | S0 infra already changes GC5 reachability/delay |
| `ROUTE_PRESSURE` | **REJECT as engine** | Access restriction already changes traversal |
| `ENVIRONMENTAL_PRESSURE` | **REJECT** | Would add weather; &lt; 2 real couplings without a new subsystem |

Table-removal test: no new canonical pressure object. Scheduled transition + existing events express the lifecycle.

---

## Slice contract

| Field | Value |
|-------|--------|
| Slice id | `gc10-s1` |
| Catalog | `pressure-catalog/gc10-s1` |
| Extends | `pressure-catalog/gc10-s0` |
| Authorizers | `schedule`, `operator` |
| Forbidden authorizers | `player`, `llm`, `study` |
| Window | cycles 1–20; **one** activation per accepted class |
| Trigger | Deterministic world-cycle schedule (RFC-0019 commit). Seeded replay. No LLM. |
| New verbs / events | none |

### Accepted classes

| Class | Family | Cycle | Event | Magnitude | Floor | Duration | Preferred subject |
|-------|--------|-------|-------|-----------|-------|----------|-------------------|
| `infrastructure_failure` | INFRASTRUCTURE | 4 | `ENTITY_UPDATE` `condition` | −15 | 25 | Persistent until `REPAIR` | `entity.relay-7` |
| `resource_scarcity` | RESOURCE | 8 | `ENTITY_UPDATE` `stock_amount` | −4 | 0; require before ≥ 4 | Immediate stock change | `entity.storage-cell-cache` |
| `access_restriction` | ACCESS | 12 | `ACCESS_RESTRICTED` EXIT DENY `*` | 1 restriction | n/a | Temporary; `expires_cycle = start + 4` | `room.relay-quarter` `east` |

If the preferred subject is missing or the preview violates the floor, skip that class (do not adapt magnitude). Later cycles in 1–20 may still fire once a valid subject exists.

### Rejected classes (must fail closed)

```text
communication_outage
environmental_weather
route_engine
war
famine
plague
```

---

## Endogenous vs exogenous

| Kind | Examples | S1 schedule |
|------|----------|-------------|
| Endogenous | load, depletion, congestion, overuse | Not synthesized as a new engine. Existing harvest/repair already express them. |
| Exogenous | bounded WED schedule, authorized operator experiment | S1 fires are exogenous schedule with `authorizer=schedule` and cause class retained on the audit receipt / Admin surface. |

Do not blur them. PLAY still sees only the world-native consequence.

---

## Envelope (conceptual; not a new table)

```text
pressure_id          schedule:{class}:{cycle}
pressure_class
world_id
subject_refs[]
start_cycle
end_cycle?           access only
cause_class          EXOGENOUS_SCHEDULE | EXOGENOUS_OPERATOR
cause_ref
parameters           integer magnitude / field / floor
rule_version         gc10-s1
status               APPLIED | SKIPPED | EXPIRED
```

Recorded as the existing event plus optional Admin projection. No `PRESSURE_STARTED` / `PRESSURE_ENDED`.

---

## Scope, magnitude, duration

- Scope is local: one asset, one node, or one public exit. No world-global pressure in S1.
- Magnitude is integer / existing fixed-point. No prose-only effect. No hidden adaptive scaling.
- Duration uses world-time. Worker delay must not extend duration.
  - Infrastructure: persistent until repaired (`COMMIT.REPAIR` +15).
  - Resource: immediate; stock stays at the new amount.
  - Access: temporary; existing `expires_cycle` semantics (`denied` while `cycle <= expires_cycle`).
- Cancellation / expiry does not erase already-applied consequences. Expiry of access ≠ repair of infrastructure.

---

## Concurrent pressures

Multiple classes MAY affect the same world on the same cycle if a jump made several due. Apply in this order:

```text
infrastructure_failure → resource_scarcity → access_restriction
```

Same-class restack in the 1–20 window is forbidden (idempotent no-op). Two condition decreases compose by ordered application and the class floor. No hidden multiplicative stacking.

---

## Anti-targeting / anti-rubber-band

Selection uses canonical world state only:

```text
entity class, preferred id, live condition, harvest stock, public exit
```

Forbidden selectors:

```text
Player score
Player success rate
research intelligence metric
wealth ranking
human vs agent controller type
operator preference
```

```text
RESEARCH METRIC ↛ PRESSURE TARGETING
```

Do not implement “leading Player gets harder events” or “losing faction gets bonus resources.”

---

## Visibility

| Surface | S1 |
|---------|----|
| PLAY | Condition, stock, blocked route. No `WED`, no class id, no “Event:” |
| WATCH | Consequence pulses only (below). No schedule, operator rationale, or class name |
| STUDY | MAY name classes in the research partition |
| Admin Live | Class, cause, scope, start/end cycle, rule version, resulting event ids. **No spawn** |

WATCH pulses (public, no ids):

| Pulse | When |
|-------|------|
| `A relay in the hub has degraded.` | Infrastructure class applied this window |
| `Extraction at a storage cache has fallen.` | Resource class applied this window |
| `Traffic through a public corridor has slowed.` | Access restriction is still active |

---

## Coupling (accepted classes)

**infrastructure_failure**

1. Relay condition → GC5 reachability / delay.
2. Repair cost / GC9 custom → maintenance habit.
3. Movement and trade that depend on the corridor.

**resource_scarcity**

1. Harvest yield / remaining stock.
2. Trade and travel to another node.
3. Construction / contest stake budgets that consume that resource.

**access_restriction**

1. MOVE cost / availability on that exit.
2. Trade and coordination that needed the corridor.
3. Contest *context* (route, presence) without deciding the verdict.

---

## GC5 / GC7 / GC9

- GC5: do not add a second communication model. Relay condition remains the band input. GC5-S2 rumor stays out.
- GC7: pressure may change route or infrastructure context. It must not emit `CONTEST_RESOLVED` or name a winner.
- GC9: later Players may call a failure a tradition. GC10 emits cause and consequence only.

---

## Institutions

An institution-maintained relay or cache may degrade. That does not revoke institution control. Condition ≠ authority. Institution TRADE/REPAIR follow-through stays out of this slice unless an already-existing verb is the Player response (`REPAIR`, `HARVEST`, `MOVE`, `TRADE`).

---

## Recovery (none required)

Players MAY `REPAIR`, harvest elsewhere, reroute, trade, wait, or do nothing. S1 names no correct verb. Pressure must not accidentally remove all future agency.

---

## Frequency

Not content-generation volume. At most one fire per accepted class in cycles 1–20. No per-cycle random condition chatter.

---

## Human / agent parity

Same state, cost, availability, consequence, and information boundary. Presentation may differ. Controller type is not a selector.

---

## Security

- Clients cannot inject WED.
- Player text cannot invoke pressure.
- Pressure ids do not grant operator access.
- Replay of the same ledger + schedule produces the same result.
- Duplicate scheduled class in-window is idempotent.
- Stale-head settlement fails safely.
- Cross-world subject refs rejected.
- Research layer cannot mutate pressure.
- Admin privilege remains separate. No raw `UPDATE entity SET condition`.

---

## A–J

| Test | Result |
|------|--------|
| A | Asset + location + access. No eighth “event” primitive |
| B | Scarcity + distance + dependency + uncertainty |
| C | No Player command added |
| D | Each accepted class has ≥ 2 cross-system couplings |
| E | Verb-stable |
| F | Hoard / repair / reroute habits can diverge without a crisis engine |
| G | Existing `ENTITY_UPDATE` / `ACCESS_RESTRICTED` remain attributable |
| H | Human and agent Players see the same condition |
| I | Meaningful with STUDY hidden |
| J | Without this, “more pressure classes” is an unpinned sentence |

---

## Out of S1

```text
COMMUNICATION / ROUTE / ENVIRONMENT engines
WAR / FAMINE / PLAGUE / REVOLUTION primitives
PRESSURE_STARTED / PRESSURE_ENDED / WED_*
SITUATION_INJECTED as WED
Admin spawn
operator storm
irreversible scar class
Player targeting / rubber-band
GC5-S2 rumor
GC1-S2 benefits
crypto / Genesis reseed
```

---

## Runtime rule

Hosted RFC-0019 cycle commit may apply each accepted class once in cycles 1–20 when preview stays legal. PLAY / help / Admin spawn still omit WED. Do not activate or reseed Genesis.

## Acceptance

1. S0 cycle-4 relay drop still holds.
2. Cycle-8 harvest-node stock drop via `ENTITY_UPDATE` when stock ≥ 4.
3. Cycle-12 public-exit `ACCESS_RESTRICTED` expires by world-time.
4. Preview equals activation. Duplicate class fire is a no-op.
5. No Player-score, controller, or research targeting. No rubber-band. No contest verdict.
6. PLAY / WATCH contain no research class name.
7. Human and agent Players observe the same world consequence.
