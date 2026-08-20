# MUD Play Craft

**Status:** Design-craft companion (horizon-locked). Non-normative for world transitions.  
**Feeds:** [MUD-NATIVE-INTERACTION-AND-WORLD-PRESENCE.md](MUD-NATIVE-INTERACTION-AND-WORLD-PRESENCE.md) (executable interaction campaign)  
**Ancestry:** [MUD-DESIGN-CANON.md](MUD-DESIGN-CANON.md)  
**Rejection test:** [COMPLEXITY-DOCTRINE.md](COMPLEXITY-DOCTRINE.md)  
**Does not replace:** Native Interaction Features A–F · [EXPERIENCE.md](EXPERIENCE.md) · [HUMAN-PLAY.md](HUMAN-PLAY.md) · [AGENT-PLAY.md](AGENT-PLAY.md) · [COMMAND-DISCOVERY.md](COMMAND-DISCOVERY.md) · [ATTENTION-PROJECTION.md](ATTENTION-PROJECTION.md) · [PLAYER-ACTION-MAP.md](PLAYER-ACTION-MAP.md)

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
| Status / budgets glance | RESOURCE-ECONOMY | **Feature B STATUS** + **T1.6** (C3) |
| Consequence four-beat | EXPERIENCE, PLAYER-ACTION-MAP §7 | Feature B HAPPENED + **T1.4** (C4) |
| Short-session mark ranking | Deep Time usability pin; GC3/GC5 | Feature D + **T1.7** S-MARK-10 (C8) |
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
extending research experience-error-catalog for PLAY commands
```

Boards / SHOUT only if COMMUNICATION-ECOLOGY opens a gap via RFC and Feature D already allows authorized public boards with provenance.

### Design test (MUD-DESIGN-CANON)

Valid if it strengthens: identity · practice · office · construction · relationship · inherited history · local asymmetry · unknown space.  
Invalid if only: content volume · new verb-for-noun · cosmetic title · global score · authored quest · research metric as reward.

---

## 3. Alignment with Native Interaction room grammar

**Authoritative human room order** is Feature B (STATUS is an additive presentation layer from C3):

```text
ROOM NAME
DESCRIPTION
PRESSURE        optional and observable only
HERE            visible Players/entities
EXITS           observable exits
STATUS          compact budgets + flags (§4)
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
| STATUS | §4 compact budgets; Advanced may hide cycle/sequence |
| HAPPENED | Consequence four-beat (§5); machine codes in Advanced/debug only |
| COMMAND | With AVAILABLE HERE / max-3 first-paint per Feature C |

### 3.2 Attention mapping

Field reduction under low attention remains [ATTENTION-PROJECTION.md](ATTENTION-PROJECTION.md). Craft requires Feature B layers to **degrade gracefully** into reduced set R and minimal (name + exits + critical energy if possible), never by inventing a second grammar.

### 3.3 Agent parity

Structured agents do not parse human room text. They MUST receive equivalent **layer semantics** in observation fields (place, pressure bands, presence, exits, status/budgets, happened, available actions). Wire schema changes need RFC; until then, document field mapping as SPEC GAP / sketch only.

---

## 4. Compact status craft (C3 — fleshed)

**Implementation home:** Native Interaction Feature B `STATUS` + task **T1.6**.  
Budgets already exist in [RESOURCE-ECONOMY.md](RESOURCE-ECONOMY.md). Craft requires glanceability without a dashboard rail.

### 4.1 Minimum PLAY status set

| Field | Human default | Structured agent (conceptual) | Notes |
|-------|---------------|-------------------------------|-------|
| Place | room display name | `location.name` / Advanced `room_id` | Prefer name |
| Cycle | when useful | `cycle` | MAY be Advanced if first paint is tight |
| Energy | `energy N` | `budgets.energy` | Always on default PLAY |
| Attention | `attention N` | `budgets.attention` | Always |
| Compute | `compute N` | `budgets.compute` | Always |
| Storage | `storage N` | `budgets.storage` | Always |
| Influence | `influence N` | `budgets.influence` | Always |
| Sequence / head | Advanced/debug only | optional | T1.3 — not required for comprehension |
| `energy_floor_risk` | plain flag when energy ≤ deployment floor | boolean | Only if runtime knows floor |
| `play_blocked` / settlement | plain flag when blocked | from `/ready` equivalent | Not INCIDENT theater copy |
| Practice crumb | short text if mastery emits | optional list | No class / research labels |

### 4.2 Human templates (illustrative)

```text
Civic Exchange · e7 a6 c64 s4 i12
```

Expanded / low-noise:

```text
STATUS
energy 7 · attention 6 · compute 64 · storage 4 · influence 12
```

### 4.3 Rules

1. No HP, XP, consciousness, or research scores.
2. No new resource types.
3. Default PLAY prefers human-readable names; IDs in Advanced.
4. Flags only when already known to the session.
5. Feature F low-noise keeps numeric budgets as text; no glyph-only status.
6. Agents get the same facts as structured fields; they MUST NOT be required to parse the human one-liner.

### 4.4 Acceptance (C3)

1. After LOOK or successful MOVE, a human can read energy and at least one other budget without a side panel.
2. Structured observation includes the same budget keys when human STATUS would show them.
3. Sequence/controller/research labels remain Advanced-only by default.

---

## 5. Consequence four-beat + PLAY failure language (C4 — fleshed)

Extends Feature B HAPPENED, plan **T1.4**, and [PLAYER-ACTION-MAP.md](PLAYER-ACTION-MAP.md) §7.  
**Does not** extend research [EXPERIENCE-ERRORS.md](EXPERIENCE-ERRORS.md) / `experience-error-catalog.json` (STUDY path). PLAY command failures stay in the action/adapter error model.

### 5.1 Four-beat template

```text
WHAT I TRIED     — verb + target in world language
OK | FAIL        — plain outcome + reason
WHAT CHANGED     — budgets, location, entity band, delivery, memory edge if any
WHAT NEXT        — from current affordances only (Feature C), never quest text
```

**Success (illustrative):**

```text
You repair the scarred conduit.
OK — condition improves (worn → serviceable).
energy −2 · attention −1.
Try: inspect conduit · wait · walk east.
```

**Failure (illustrative):**

```text
You try to walk east.
FAIL — not enough energy (need 1, have 0).
Nothing moves.
Try: wait · trade for fuel when a counterparty is here.
```

Machine `error.code` remains in Advanced/debug and structured `CommandResult`.

### 5.2 PLAY plain-language table (codes authoritative)

| Code / pattern | Simple message direction | Next-action hint (affordances only) | Must not |
|----------------|--------------------------|-------------------------------------|----------|
| `BUDGET_EXCEEDED` (energy) | Not enough energy; show cost when known | `WAIT` if it restores energy on this deployment; TRADE fuel when counterparty visible | Spam MOVE; invent free energy |
| `BUDGET_EXCEEDED` (other) | Name the scarce budget + cost when known | Narrow the act; WAIT/LOOK; never debit on reject | Hide which budget failed |
| Empty HARVEST / no stock | Node has nothing left to take | Other visible node; WAIT only if production tick is real | Change GC8 harvest magnitudes in copy |
| `MOVE_REJECTED` | Route unavailable / blocked / cost failed (observable only) | Other exit; repair if route asset is the blocker | Reveal hidden exits |
| `TRADE_REJECTED` / phase errors | Declined, expired, bad terms, or insufficient side | Re-propose with visible lots; cancel own open trade | Leak private holdings |
| TRADE field confusion | One vocabulary: canonical fields + documented aliases | Example `offer=` / `want=` or structured keys | Different errors for same mistake |
| `UNREACHABLE` / delayed MESSAGE | Path failed or delayed; relay **condition bands** (GC5) | Local MESSAGE; repair relay if local and allowed | Silent drop; fake instant delivery |
| `FORBIDDEN` | Not authorized for this act or target | Different target; office path if already public | Leak hidden scopes |
| `SETTLEMENT_RESYNC` | World head resynced; safe to retry | Client **retries once** when possible | INCIDENT panic; infinite retry |
| Ambiguous target (Feature A) | Which one? numbered local choices | Clarification only; no world mutate | Guess |
| Unknown command | Cannot do that here | Suggestions from **current** affordances only | Suggest hidden acts |

### 5.3 HAPPENED composition rules

1. One primary sentence for ordinary success/fail; details secondary.
2. Budget deltas only when observable and caused by this act (or clearly marked regen/rest).
3. Do not attribute unrelated world events to the Player.
4. Partial success uses honest partial language (e.g. delayed MESSAGE).
5. Four-beat MAY collapse to two lines on narrow UI if WHAT CHANGED and WHAT NEXT remain recoverable.

### 5.4 Acceptance (C4)

1. For each §5.2 row the deployment emits, human PLAY shows a plain reason without requiring the raw code.
2. Advanced/debug still exposes the machine code.
3. Research experience-error catalog is unchanged.
4. PLAYER-ACTION-MAP §7 remains adapter authority; this table specializes craft wording.

---

## 6. Short-session durable mark (C8 — fleshed)

Complements Feature D (traces) and Deep Time short-session usability. **Not a score.**  
**Implementation home:** task **T1.7** (S-MARK-10).

### 6.1 Preferred mark ranking

| Rank | Act family | Legible residue |
|------|------------|-----------------|
| 1 | `REPAIR` / conservation on repairable asset or artifact | Condition band change; Feature D weld/plate trace when provenance allows |
| 2 | `TRADE` success | GC3 dyadic/institutional memory; public closure crumb if already public |
| 3 | `MESSAGE` delivered, delayed, or honestly failed | Inbox/receipt; relay-band language on fail |
| 4 | `INSPECT` that upgrades known information | Exploration/knowledge state change in observation |
| 5 | Presence-only | Occupancy — weakest as a session story |

### 6.2 Anti-patterns

```text
pure MOVE thrash on a tiny graph
WAIT spam without rest/production purpose
re-INSPECT loops with no information gain
harvest thrash on empty nodes
```

### 6.3 Spec scenario S-MARK-10 (Chamber-oriented)

**Setup:** Seeded Chamber map ([examples/chamber-world/](../examples/chamber-world/)); single fresh Player; energy sufficient for at least one REPAIR or TRADE path **or** a co-located fuel counterparty when testing TRADE.

**Budget:** ≤10 meaningful acts (MOVE/LOOK/WAIT count only if required to reach the mark; thrash does not satisfy).

**Pass:** At least one rank 1–4 mark is:

1. **Possible** under current pins (no new verbs); and  
2. **Legible** in PLAY via HAPPENED and/or Feature D trace and/or knowledge upgrade in observation.

**Illustrative path (non-normative):**

```text
ENTER → LOOK (Relay Quarter pressure)
→ INSPECT degraded relay
→ REPAIR relay
→ HAPPENED shows condition band change
→ (optional) leave room; trace remains for later Player
```

**Fail:** Only MOVE/WAIT/empty HARVEST/re-INSPECT with no durable or informational residue.

### 6.4 Acceptance (C8)

1. S-MARK-10 is documented and implementable as a manual or automated presentation test without Genesis change.
2. Ranking does not create achievements, XP, or research metrics.
3. Feature D provenance rules still apply to any trace text.

---

## 7. Local asymmetry & social presence

- Each distinct room SHOULD surface at least one strategic difference on LOOK when attention allows (stock, repair target, relay band, route cost, social density, GC6 contradiction hook) — existing entities only.
- Same-room presence is first-class in HERE.
- `MESSAGE` remains the verb; no SAY/EMOTE/SHOUT unless RFC + doctrine (prefer MESSAGE scope).

### Practice crumbs

PLAY MAY show short PRACTICING crumbs where mastery projection already emits them. No mechanical benefits in this doc. No research capability labels in PLAY.

### Chamber pressure hints (illustrative, seed-owned)

| Chamber room | Asymmetry to surface when true |
|--------------|--------------------------------|
| Relay Quarter | Relay condition band / MESSAGE range pressure |
| Foundry Corridor | Production/resource node stock |
| Archive | Knowledge/inspect depth; low material |
| Generator Hall | Power/infra criticality |
| Outer Works / Frontier Gate | Exploration edge / risk |
| Civic Exchange | Social density / trade presence |

---

## 8. Work queue (flesh-out)

| ID | Item | Status | Promote to |
|----|------|--------|------------|
| C3 | Status strip | **Fleshed** §4 | Feature B STATUS + **T1.6** |
| C4 | PLAY failure plain language | **Fleshed** §5 | T1.4 + PLAYER-ACTION-MAP §7 pointer |
| C8 | Short-session mark scenario | **Fleshed** §6 | **T1.7** S-MARK-10 |
| C1 | Chamber example full room projections (3 rooms) | open | examples/ + T1.x |
| C2 | Agent observation ↔ Feature B field sketch | open | RFC if wire changes |
| C5 | Post-MOVE orientation LOOK vs attention double-charge | open | RFC if normative cost |
| C6 | Official client SETTLEMENT_RESYNC single retry | open | OFFICIAL-AGENT-CLIENT / client |
| C7 | Practice crumb wording table | open | MASTERY projection + PLAY |
| C9 | Hosted PLAY audit vs craft checklist | open | runtime repo (advisory) |

---

## 9. Complexity Doctrine (this companion)

| Test | Result |
|------|--------|
| Causes not industries | Pass |
| No eighth primitive | Pass |
| Verb stability | Pass |
| Decision density | Pass intent (C3–C8) |
| No second campaign fork | Pass — feeds Native Interaction |
| Horizon lock | Pass |

---

## 10. Acceptance (companion)

1. Does not conflict with Feature B room order or Features A–F constraints (STATUS is additive presentation).
2. Cold reader knows implementation homes: T1.4 / T1.6 / T1.7.
3. Human/agent layer semantics called out without inventing wire fields.
4. No GC3/GC5/GC8 pin breakage; research experience-error catalog untouched.
5. Forbidden list holds.
6. C3, C4, C8 sections are detailed enough to implement presentation tests.

---

## 11. Related

- [MUD-NATIVE-INTERACTION-AND-WORLD-PRESENCE.md](MUD-NATIVE-INTERACTION-AND-WORLD-PRESENCE.md) · [plan](MUD-NATIVE-INTERACTION-PLAN.md) · [tasks](MUD-NATIVE-INTERACTION-TASKS.md)
- [MUD-DESIGN-CANON.md](MUD-DESIGN-CANON.md)
- [COMPLEXITY-DOCTRINE.md](COMPLEXITY-DOCTRINE.md) · [GAME-COMPLETENESS-PLAN.md](GAME-COMPLETENESS-PLAN.md)
- [EXPERIENCE.md](EXPERIENCE.md) · [HUMAN-PLAY.md](HUMAN-PLAY.md) · [AGENT-PLAY.md](AGENT-PLAY.md)
- [PLAYER-ACTION-MAP.md](PLAYER-ACTION-MAP.md) §7 · [COMMAND-DISCOVERY.md](COMMAND-DISCOVERY.md) · [ATTENTION-PROJECTION.md](ATTENTION-PROJECTION.md)
- [protocols/mud-command-v1.md](../protocols/mud-command-v1.md)
- [examples/chamber-world/](../examples/chamber-world/)
