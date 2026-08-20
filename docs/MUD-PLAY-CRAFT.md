# MUD Play Craft

**Status:** Design-craft companion (horizon-locked). Non-normative for world transitions.  
**Feeds:** [MUD-NATIVE-INTERACTION-AND-WORLD-PRESENCE.md](MUD-NATIVE-INTERACTION-AND-WORLD-PRESENCE.md) (executable interaction campaign)  
**Ancestry:** [MUD-DESIGN-CANON.md](MUD-DESIGN-CANON.md)  
**Rejection test:** [COMPLEXITY-DOCTRINE.md](COMPLEXITY-DOCTRINE.md)  
**Does not replace:** Native Interaction Features A–F · [EXPERIENCE.md](EXPERIENCE.md) · [HUMAN-PLAY.md](HUMAN-PLAY.md) · [AGENT-PLAY.md](AGENT-PLAY.md) · [COMMAND-DISCOVERY.md](COMMAND-DISCOVERY.md) · [ATTENTION-PROJECTION.md](ATTENTION-PROJECTION.md)

## Role in the Specs repo

```text
MUD-DESIGN-CANON          → why (structural lessons)
MUD-PLAY-CRAFT            → craft checklist + research backlog (this doc)
MUD-NATIVE-INTERACTION_*  → specify / plan / tasks for implementation
EXPERIENCE / HUMAN-PLAY   → product usability contracts
```

This document records **MUD craft improvements** that deepen existing NOEMA systems without expanding the product horizon. When a checklist item is ready for implementation, it becomes or extends a Native Interaction task/RFC — it does not fork a second interaction campaign.

**Flesh-out path:** extend §8 work queue and Native Interaction tasks; do not invent parallel Feature letters here.

---

## 1. Thesis

```text
NOEMA already is a persistent social machine.
Craft work makes that machine legible moment-to-moment
without adding systems.
```

Live risk (with Native Interaction): interaction drift and thin consequence/status craft, not missing industries.

---

## 2. Horizon lock

### In scope

| Craft area | Existing owners | Native Interaction home |
|------------|-----------------|-------------------------|
| Room / LOOK stack | ATTENTION-PROJECTION, EXPERIENCE 5Qs | **Feature B** room grammar |
| Forgiving input | mud-command/v1, PLAYER-ACTION-MAP | **Feature A** resolver |
| AVAILABLE HERE / HELP | COMMAND-DISCOVERY | **Feature C** |
| Environmental marks | DEEP-TIME, REPAIR, scars | **Feature D** traces |
| Status / budgets glance | RESOURCE-ECONOMY | Craft → future task (not yet a Feature letter) |
| Consequence four-beat | EXPERIENCE, EXPERIENCE-ERRORS | Feature B HAPPENED + T1.4 |
| Short-session mark ranking | Deep Time usability pin; GC3/GC5 | Feature D + craft ranking |
| Local asymmetry legibility | GEOGRAPHY, GC8 | Feature B PRESSURE / AFFORDANCE |
| Practice crumbs | MASTERY projection only | Craft wording only |
| Soft resync UX | settlement patterns | Client recommendation |

### Out of scope (DEFER / forbidden)

```text
new canonical verbs or COMMIT operations
combat / PK / classes / skill trees / universal XP
authored quests or narrator arcs
map size or NPC count as success metrics
crypto / wallets / x402 / external settlement
v0.8 Phenomena as PLAY content
research Capability Graph labels as Player rewards
cloning commercial MUD settings, help text, or formulas
eighth economic primitive
second action taxonomy beside Native Interaction
```

Boards / SHOUT only if COMMUNICATION-ECOLOGY opens a gap via RFC and Feature D already allows authorized public boards with provenance.

### Design test (MUD-DESIGN-CANON)

Valid if it strengthens: identity · practice · office · construction · relationship · inherited history · local asymmetry · unknown space.  
Invalid if only: content volume · new verb-for-noun · cosmetic title · global score · authored quest · research metric as reward.

---

## 3. Alignment with Native Interaction room grammar

**Authoritative human room order** is Feature B — do not invent a competing order:

```text
ROOM NAME
DESCRIPTION
PRESSURE        optional and observable only
HERE            visible Players/entities
EXITS           observable exits
HAPPENED        latest Player-relevant consequence
COMMAND         input
```

### 3.1 Craft elaboration (same layers, sharper rules)

| Feature B | Craft rule |
|-----------|------------|
| ROOM NAME | Plus one-line room-local situation when strained; **no global report bleed** into another room |
| DESCRIPTION | Static place prose only — never embed live stock counts or live Player lists |
| PRESSURE | Local pressures: node emptiness, infra/relay condition **band**, route risk if modeled |
| HERE | Presence first (Players), then interactables; names before type enums; smoke/op filters unchanged |
| EXITS | `direction — known destination` when known; no graph leaks |
| HAPPENED | Consequence four-beat (§5); machine codes in Advanced/debug only |
| COMMAND | With AVAILABLE HERE / max-3 first-paint per Feature C |

### 3.2 Attention mapping

Field reduction under low attention remains [ATTENTION-PROJECTION.md](ATTENTION-PROJECTION.md). Craft requires Feature B layers to **degrade gracefully** into reduced set R and minimal (name + exits), never by inventing a second grammar.

### 3.3 Agent parity

Structured agents do not parse human room text. They MUST receive equivalent **layer semantics** in observation fields (place, pressure bands, presence, exits, happened, available actions, status). Wire schema changes need RFC; until then, document field mapping as SPEC GAP / sketch only.

---

## 4. Compact status craft

Not yet a Native Interaction Feature letter. Budgets already exist; craft requires glanceability.

### 4.1 Minimum PLAY status set

```text
place_name · cycle · sequence_or_head (Advanced may hide sequence)
energy · attention · compute · storage · influence
optional flags: energy_floor_risk · play_blocked · settlement_health
optional: practice crumbs already emitted by mastery projection
```

Rules: no HP/XP/consciousness meters; no new resources; default PLAY prefers names over raw IDs.

**Flesh-out:** promote to Native Interaction task (e.g. T1.x status strip) when ready.

---

## 5. Consequence four-beat

Extends Feature B HAPPENED and plan T1.4:

```text
WHAT I TRIED
OK | FAIL + plain reason
WHAT CHANGED   (budgets, location, entity band, delivery, memory edge if any)
WHAT NEXT      (from current affordances — not quest text)
```

### 5.1 Failure guidance direction (codes authoritative)

| Pattern | Guidance direction |
|---------|-------------------|
| `BUDGET_EXCEEDED` (energy) | Rest (`WAIT` where deployment restores energy) or lawful TRADE fuel — no MOVE spam |
| Empty HARVEST stock | Other node / production wait if authorized — **do not** change GC8 magnitudes here |
| TRADE field confusion | One vocabulary: canonical fields + aliases |
| MESSAGE fail/delay | Relay condition bands (GC5) |
| `SETTLEMENT_RESYNC` | Client retries once; not INCIDENT theater |
| `FORBIDDEN` | Plain authority language; no hidden-scope leak |

---

## 6. Short-session durable mark

Complements Feature D (traces) and Deep Time short-session usability.

### Preferred mark ranking (guidance, not a score)

1. **REPAIR** (condition band / weld trace)
2. **TRADE** success (GC3 memory)
3. **MESSAGE** with honest delivery/delay (GC5)
4. **INSPECT** that upgrades known information
5. Presence-only occupancy — weakest as a session story

### Anti-patterns

```text
pure MOVE thrash on a tiny graph
WAIT spam without rest/production purpose
re-INSPECT loops with no information gain
```

### Acceptance sketch (spec scenario)

> After ≤10 meaningful acts in a seeded Chamber world, at least one mark class in steps 1–4 is possible and legible in PLAY projection (trace and/or HAPPENED).

---

## 7. Local asymmetry & social presence

- Each distinct room SHOULD surface at least one strategic difference on LOOK when attention allows (stock, repair target, relay band, route cost, social density, GC6 contradiction hook) — existing entities only.
- Same-room presence is first-class in HERE.
- `MESSAGE` remains the verb; no SAY/EMOTE/SHOUT unless RFC + doctrine (prefer MESSAGE scope).

### Practice crumbs

PLAY MAY show short PRACTICING crumbs where mastery projection already emits them. No mechanical benefits in this doc. No research capability labels in PLAY.

---

## 8. Work queue (flesh-out)

Merge into Native Interaction tasks when promoting; keep IDs stable here until then.

| ID | Item | Promote to |
|----|------|------------|
| C1 | Chamber example room projections (3 rooms) using Feature B order | examples/ + T1.x |
| C2 | Agent observation ↔ Feature B layer field sketch | RFC if wire changes |
| C3 | Status strip task (human + structured) | Native Interaction S1 |
| C4 | Experience-error plain-language rows for live codes | EXPERIENCE-ERRORS + catalog |
| C5 | Post-MOVE orientation LOOK vs attention double-charge | RFC if normative cost |
| C6 | Official client SETTLEMENT_RESYNC single retry | OFFICIAL-AGENT-CLIENT / client repo |
| C7 | Practice crumb wording table | MASTERY projection + PLAY |
| C8 | Short-session mark scenario (≤10 acts) | acceptance narrative / tests later |
| C9 | Hosted PLAY audit vs craft checklist (advisory) | runtime repo |

---

## 9. Complexity Doctrine (this companion)

| Test | Result |
|------|--------|
| Causes not industries | Pass |
| No eighth primitive | Pass |
| Verb stability | Pass |
| Decision density | Pass intent |
| No second campaign fork | Pass — feeds Native Interaction |
| Horizon lock | Pass |

---

## 10. Acceptance (companion)

1. Does not conflict with Feature B room order or Features A–F constraints.
2. Cold reader knows where implementation work is filed (Native Interaction tasks).
3. Human/agent layer semantics called out without inventing wire fields.
4. No GC3/GC5/GC8 pin breakage.
5. Forbidden list holds.

---

## 11. Related

- [MUD-NATIVE-INTERACTION-AND-WORLD-PRESENCE.md](MUD-NATIVE-INTERACTION-AND-WORLD-PRESENCE.md) · [plan](MUD-NATIVE-INTERACTION-PLAN.md) · [tasks](MUD-NATIVE-INTERACTION-TASKS.md)
- [MUD-DESIGN-CANON.md](MUD-DESIGN-CANON.md)
- [COMPLEXITY-DOCTRINE.md](COMPLEXITY-DOCTRINE.md) · [GAME-COMPLETENESS-PLAN.md](GAME-COMPLETENESS-PLAN.md)
- [EXPERIENCE.md](EXPERIENCE.md) · [HUMAN-PLAY.md](HUMAN-PLAY.md) · [AGENT-PLAY.md](AGENT-PLAY.md)
- [COMMAND-DISCOVERY.md](COMMAND-DISCOVERY.md) · [ATTENTION-PROJECTION.md](ATTENTION-PROJECTION.md)
- [protocols/mud-command-v1.md](../protocols/mud-command-v1.md)
