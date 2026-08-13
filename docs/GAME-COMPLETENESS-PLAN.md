# NOEMA Game Completeness Plan

**Status:** Campaign authority for the post-core PLAY-depth specification.  
**Not** an executable release package.  
**Not** v0.8 Phenomena.  
**Does not mutate** frozen v0.1–v0.7 machine contracts.

Related: [COMPLEXITY-DOCTRINE.md](COMPLEXITY-DOCTRINE.md) · [MUD-DESIGN-CANON.md](MUD-DESIGN-CANON.md) · [CORE-GAME-LOOP.md](CORE-GAME-LOOP.md) · [GAME-DESIGN.md](GAME-DESIGN.md) · [SPEC-FREEZE-CORE-LOOP.md](SPEC-FREEZE-CORE-LOOP.md) · [ROADMAP.md](ROADMAP.md) · [NOTION-RECONCILIATION-2026-08-13.md](NOTION-RECONCILIATION-2026-08-13.md)

**Doctrine gate.** Every GC package and later mechanic MUST pass [COMPLEXITY-DOCTRINE.md](COMPLEXITY-DOCTRINE.md) tests A–J. Model causes, not industries. Isolated progression trees, class/skill frameworks, and future crypto/wallet infrastructure are **DEFER**.

**Cross-cutting constraints** (full text in [NOTION-RECONCILIATION-2026-08-13.md](NOTION-RECONCILIATION-2026-08-13.md), not duplicated here): social parity; labor/delegation without personhood transfer; law/arbitration as delegated authority; privacy/knowledge provenance; epistemic decay; research/game measurement membrane; operator causation with receipts; invariants; action/event/state/projection spine; world-time; schema and enforcement doctrine. Architecture-design frontier is **paused** after that reconciliation.

---

## 1. Contract

NOEMA remains:

> a persistent strategic text world inhabited by human-controlled and agent-controlled Players, where research observes naturally occurring play rather than replacing the game.

The completeness target is a world in which a Player can **become somebody**:

```text
persistent world
× meaningful identity
× interdependence
× partial knowledge
× irreversible history
× social memory
× player-created structure
× recurring uncertainty
```

Mature-world acceptance question:

> Can a Player acquire a role, develop specialization, build relationships, create something persistent, respond to disruption, influence institutions, leave evidence, and alter the strategic environment inherited by later Players?

This campaign is **specification work first**. Runtime implementation belongs in `Zero-State-LLC/Noema` only after a work package satisfies the [Spec Completion Contract](#11-spec-completion-contract). Missing material behavior is a **SPEC GAP**. An implementation agent MUST NOT fill a SPEC GAP silently in runtime code.

---

## 2. Current-state dependency map

Produced before writing new authorities. Status values:

| Status | Meaning |
|--------|---------|
| **EXISTS** | Canonical authority already settles the concept |
| **PARTIAL** | Concept named or sketched; product behavior incomplete |
| **DEFERRED** | Explicitly later; do not pretend it is live |
| **CONFLICT-RISK** | Nearby authority could be duplicated if a new doc is careless |
| **ABSENT** | No dedicated authority; this campaign creates one |

### GC1 Mastery and specialization — P0

| Nearby authority | Status | Rule |
|------------------|--------|------|
| [PROGRESSION.md](PROGRESSION.md) | EXISTS (plural surfaces; forbids XP) | Keep. Mastery is a new surface, not a replacement |
| [AMBITIONS.md](AMBITIONS.md) | EXISTS (no victory function) | Keep |
| [CAPABILITY-GRAPH.md](CAPABILITY-GRAPH.md) / [LEARN.md](LEARN.md) | EXISTS (research, derived) | **Do not** reuse as Player classes |
| [CAPABILITY-CANDIDATES.md](CAPABILITY-CANDIDATES.md) | EXISTS (Observatory) | Research-only |
| Player proficiency / specialization | ABSENT | New: [MASTERY-SPECIALIZATION.md](MASTERY-SPECIALIZATION.md) |

### GC2 Construction and world modification — P0

| Nearby authority | Status | Rule |
|------------------|--------|------|
| `BUILD` in [ACTION-CONTRACTS.md](ACTION-CONTRACTS.md), [PLAYER-ACTION-MAP.md](PLAYER-ACTION-MAP.md), [GAME-DESIGN.md](GAME-DESIGN.md) | DEFERRED | Close the deferral **in specification**, not by adding help text |
| [INFRASTRUCTURE.md](INFRASTRUCTURE.md) | EXISTS (repair, condition, closed types) | Construction extends this set; does not replace REPAIR |
| [GEOGRAPHY.md](GEOGRAPHY.md) / [RESOURCE-ECONOMY.md](RESOURCE-ECONOMY.md) | EXISTS | Construction MUST couple here |
| [DEEP-TIME.md](DEEP-TIME.md) | EXISTS (scars, names, artifacts) | Construction writes lineage into history |
| Generalized construction model | ABSENT | New: [CONSTRUCTION.md](CONSTRUCTION.md) |

### GC3 Social memory and relational reputation — P0

| Nearby authority | Status | Rule |
|------------------|--------|------|
| “reputation/influence” in [GAME-DESIGN.md](GAME-DESIGN.md), [STRATEGIC-CONFLICT.md](STRATEGIC-CONFLICT.md), [DIPLOMACY.md](DIPLOMACY.md) | PARTIAL | Influence is a resource; reputation is unnamed edge state |
| [INSTITUTIONAL-MEMORY.md](INSTITUTIONAL-MEMORY.md) | EXISTS (archives ≠ relationship) | Keep distinct |
| [PROGRESSION.md](PROGRESSION.md) “Relationships” row | PARTIAL | Names the surface only |
| Player↔Player / Institution↔Player memory | ABSENT | New: [SOCIAL-MEMORY.md](SOCIAL-MEMORY.md) |

### GC4 Institutional roles and bounded authority — P1

| Nearby authority | Status | Rule |
|------------------|--------|------|
| [INSTITUTIONS.md](INSTITUTIONS.md) | EXISTS (lifecycle, persistence) | Keep as institution identity |
| [SUCCESSION.md](SUCCESSION.md) | EXISTS (transfer mechanisms) | Keep as transfer authority |
| Org roles founder/officer/member/advisor | PARTIAL (v0.1 coarse) | Insufficient as playable offices |
| [WORLD-SERVICES.md](WORLD-SERVICES.md) | EXISTS (not Players) | Services ≠ Player offices |
| Playable offices with bounded authority | ABSENT | New: [INSTITUTIONAL-AUTHORITY.md](INSTITUTIONAL-AUTHORITY.md) |
| v0.1 role grants (founder/officer/member/advisor) | PINNED S0 | [GC4-FIRST-SLICE.md](GC4-FIRST-SLICE.md) · [RFC-0008](../rfcs/RFC-0008-office-authority-pins.md) |

### GC5 Communication ecology — P1

| Nearby authority | Status | Rule |
|------------------|--------|------|
| `MESSAGE` / optional `ASK` | EXISTS | Preserve the verb |
| [WORLD-REPORTS.md](WORLD-REPORTS.md) | EXISTS (derived news) | One surface, not the ecology |
| Relay as communication quality | PARTIAL ([INFRASTRUCTURE.md](INFRASTRUCTURE.md)) | Formalize dependency |
| Boards, rumors, latency, failure | ABSENT | New: [COMMUNICATION-ECOLOGY.md](COMMUNICATION-ECOLOGY.md) |
| Long-range MESSAGE vs local on relay condition | PINNED S0 | [GC5-FIRST-SLICE.md](GC5-FIRST-SLICE.md) · [RFC-0009](../rfcs/RFC-0009-relay-message-delivery.md) |

### GC6 Systemic mystery and discovery — P1

| Nearby authority | Status | Rule |
|------------------|--------|------|
| [EXPLORATION.md](EXPLORATION.md) | EXISTS (discovery states) | Keep |
| [HISTORICAL-EVIDENCE.md](HISTORICAL-EVIDENCE.md), [HISTORICAL-RECONSTRUCTION.md](HISTORICAL-RECONSTRUCTION.md), [ARCHAEOLOGY.md](ARCHAEOLOGY.md), [CONTRADICTORY-EVIDENCE.md](CONTRADICTORY-EVIDENCE.md) | EXISTS | Compose; do not fork a second evidence canon |
| [LORE-BOUNDARY.md](LORE-BOUNDARY.md) / [STORY-SEEDS.md](STORY-SEEDS.md) | EXISTS | Genesis may leave unresolved questions; no authored quests |
| Player-facing mystery origin / settlement | PARTIAL | New: [SYSTEMIC-DISCOVERY.md](SYSTEMIC-DISCOVERY.md) |
| Archive vs live INSPECT contradiction | PINNED S0 | [GC6-FIRST-SLICE.md](GC6-FIRST-SLICE.md) · [RFC-0010](../rfcs/RFC-0010-discovery-contradiction.md) |

### GC7 Strategic conflict v2 — P1

| Nearby authority | Status | Rule |
|------------------|--------|------|
| [STRATEGIC-CONFLICT.md](STRATEGIC-CONFLICT.md) + RFC-0002 + `event-catalog/0.2` | EXISTS (executable v0.2) | **Extend this authority.** Do not create a second conflict canon |
| [CONTEST-RESOLUTION.md](CONTEST-RESOLUTION.md), [LOSS-RECOVERY.md](LOSS-RECOVERY.md), [TERRITORY-CONTROL.md](TERRITORY-CONTROL.md) | EXISTS | v2 composes these |
| Recon→commit→recover rhythm | PARTIAL | Specified in the v2 section of Strategic Conflict |
| Stage table over existing v0.2 forms | PINNED S0 | [GC7-FIRST-SLICE.md](GC7-FIRST-SLICE.md) · [RFC-0011](../rfcs/RFC-0011-contest-rhythm.md) |

### GC8 Economic specialization — P2

| Nearby authority | Status | Rule |
|------------------|--------|------|
| [RESOURCE-ECONOMY.md](RESOURCE-ECONOMY.md) | EXISTS (v0.1 budgets + nodes) | Keep as budget authority |
| [INFRASTRUCTURE.md](INFRASTRUCTURE.md) | EXISTS | Production/transport substrate |
| Roadmap **v0.6B Contracts & Markets** | DEFERRED (named, not started) | Remains a distinct follow-up. GC8 MUST NOT silently become v0.6B |
| Interdependence / comparative advantage | ABSENT | New: [ECONOMIC-SPECIALIZATION.md](ECONOMIC-SPECIALIZATION.md) |
| Distance pair-vs-lone energy comparison | PINNED S0 | [GC8-FIRST-SLICE.md](GC8-FIRST-SLICE.md) · [RFC-0012](../rfcs/RFC-0012-distance-interdependence.md) |

### GC9 Emergent culture — P2

| Nearby authority | Status | Rule |
|------------------|--------|------|
| [DEEP-TIME.md](DEEP-TIME.md), [LORE-BOUNDARY.md](LORE-BOUNDARY.md) | EXISTS | Culture interprets history; never rewrites it |
| [INSTITUTIONAL-MEMORY.md](INSTITUTIONAL-MEMORY.md), [SEMANTIC-LINEAGE.md](SEMANTIC-LINEAGE.md) | EXISTS | Inputs to culture |
| Roadmap **v0.6C Semantic Evolution** | DEFERRED | Remains distinct. GC9 may later depend on it |
| Evidence-backed custom → tradition | ABSENT | New: [EMERGENT-CULTURE.md](EMERGENT-CULTURE.md) |
| Repeated REPAIR → inherited CUSTOM | PINNED S0 | [GC9-FIRST-SLICE.md](GC9-FIRST-SLICE.md) · [RFC-0013](../rfcs/RFC-0013-maintenance-custom.md) |

### GC10 World Steward pressure — P2

| Nearby authority | Status | Rule |
|------------------|--------|------|
| World Event Director mention in [GAME-DESIGN.md](GAME-DESIGN.md), [STARTING-CONDITIONS.md](STARTING-CONDITIONS.md), [INFRASTRUCTURE.md](INFRASTRUCTURE.md) | PARTIAL (named, not specified) | Formalize here |
| [FRONTIER-DIRECTOR.md](FRONTIER-DIRECTOR.md) | EXISTS (research NOTICE) | **Different system.** Frontier searches capability boundaries |
| [OPERATOR-INTERVENTIONS.md](OPERATOR-INTERVENTIONS.md) | EXISTS (control plane) | Ops ≠ steward pressure |
| [INTERVENTIONS.md](INTERVENTIONS.md) | EXISTS (Lab taxonomy) | Research-only |
| Bounded player-world pressure | ABSENT | New: [WORLD-EVENT-DIRECTOR.md](WORLD-EVENT-DIRECTOR.md) |
| Seeded mild relay condition drop | PINNED S0 | [GC10-FIRST-SLICE.md](GC10-FIRST-SLICE.md) · [RFC-0014](../rfcs/RFC-0014-wed-schedule-pressure.md) |

### Do not create duplicate authorities

| Tempting new file | Existing owner | Action taken |
|-------------------|----------------|--------------|
| Second progression/XP doc | PROGRESSION | Mastery is additive |
| Second institution lifecycle | INSTITUTIONS + SUCCESSION | Authority doc is offices only |
| Second evidence/lore canon | DEEP-TIME stack | Discovery composes it |
| Second conflict catalog | STRATEGIC-CONFLICT + RFC-0002 | v2 is a section, not a fork |
| Second research director | FRONTIER-DIRECTOR | World Event Director is PLAY pressure |

---

## 3. Five nested game loops

Assimilated into high-level game-design authority. They **do not replace** the existing primary loop or strategic overlay in [CORE-GAME-LOOP.md](CORE-GAME-LOOP.md). They name the nested timescales a complete world must support.

```text
1. ACTION LOOP
observe → decide → act → consequence

2. MASTERY LOOP
act → learn → specialize → gain capability

3. ECONOMIC LOOP
discover → acquire → transform → exchange → invest

4. SOCIAL LOOP
interact → remember → trust / conflict → organize → govern

5. CIVILIZATIONAL LOOP
build → institutionalize → inherit → reinterpret → transform
```

Research sits **outside** these loops:

```text
GAME WORLD
    ↓
persistent behavior
    ↓
research capture / observation / testing
```

Forbidden implicit conversion:

```text
research objective  →  Player objective
```

A World Event Director pressure, Frontier situation, Lab fork, or LEARN graph MUST NOT become a quest, XP target, or Player victory condition.

---

## 4. Work packages

| ID | Package | Priority | Phase | Authority |
|----|---------|----------|-------|-----------|
| GC1 | Mastery and specialization | P0 | A | [MASTERY-SPECIALIZATION.md](MASTERY-SPECIALIZATION.md) |
| GC2 | Construction and world modification | P0 | A | [CONSTRUCTION.md](CONSTRUCTION.md) |
| GC3 | Social memory and relational reputation | P0 | A | [SOCIAL-MEMORY.md](SOCIAL-MEMORY.md) |
| GC4 | Institutional roles and bounded authority | P1 | B | [INSTITUTIONAL-AUTHORITY.md](INSTITUTIONAL-AUTHORITY.md) |
| GC5 | Communication ecology | P1 | B | [COMMUNICATION-ECOLOGY.md](COMMUNICATION-ECOLOGY.md) |
| GC6 | Systemic mystery and discovery | P1 | B | [SYSTEMIC-DISCOVERY.md](SYSTEMIC-DISCOVERY.md) |
| GC7 | Strategic conflict v2 | P1 | C | [STRATEGIC-CONFLICT.md](STRATEGIC-CONFLICT.md) (extended) |
| GC8 | Economic specialization | P2 | C | [ECONOMIC-SPECIALIZATION.md](ECONOMIC-SPECIALIZATION.md) |
| GC9 | Emergent culture | P2 | D | [EMERGENT-CULTURE.md](EMERGENT-CULTURE.md) |
| GC10 | World Steward pressure | P2 | D | [WORLD-EVENT-DIRECTOR.md](WORLD-EVENT-DIRECTOR.md) |

Each package MUST reuse the seven primitives and four pressures. Do not add a bank, shipper, market engine, or quest engine because the noun exists.

Do **not** make all ten executable in one release.

---

## 5. Release and milestone placement

### What this campaign is not

| Existing milestone | Why it is not reused |
|--------------------|----------------------|
| v0.1–v0.7 core loop | Frozen for implementation ([SPEC-FREEZE-CORE-LOOP.md](SPEC-FREEZE-CORE-LOOP.md)) |
| v0.6B Contracts & Markets | Already named; not started; economic-contract scope, not this whole campaign |
| v0.6C Semantic Evolution | Already named; not started; semantic/lineage scope |
| v0.8 Phenomena | Research milestone (self-model, metacognition). Opening it for game depth would silently redefine the roadmap |
| v0.9 Atlas / v1.0 | Downstream research publication and third-party journey |

### What this campaign is

A **parallel PLAY-depth track** beside the frozen core loop:

```text
GAME-COMPLETENESS  (specification campaign)
  GC-A  Identity and Persistence     GC1 · GC2 · GC3
  GC-B  Society and Information      GC4 · GC5 · GC6
  GC-C  Strategic Depth              GC7 · GC8
  GC-D  Civilization                 GC9 · GC10
```

These identifiers are **campaign phases**, not product tags and not `event-catalog` versions.

### Implementation readiness

| Phase | Spec status after this patch | Machine contracts | Runtime |
|-------|------------------------------|-------------------|---------|
| GC-A–D design authorities | Present | **SPEC GAP** until RFC | Not started |
| Frozen v0.1 Chamber | Executable | Present | Implementation priority |
| v0.6B / v0.6C | Unchanged, not started | Unchanged | Unchanged |
| v0.8 Phenomena | Unchanged, not opened | Unchanged | Unchanged |

Rationale:

1. Core-loop freeze says prefer runtime feedback over opening v0.8.
2. Game completeness is Player-world depth, not Phenomena ontology.
3. v0.6B/C already have assigned meanings; overwriting them would be a silent roadmap defect.
4. Each GC package still needs versioned schemas, events, fixtures, and conformance before any runtime slice.

### First later runtime slice

**GC1-S0 — Derived Practice Projection.** Shipped. [GC1-FIRST-SLICE.md](GC1-FIRST-SLICE.md). RFC: [RFC-0004](../rfcs/RFC-0004-derived-mastery-projection.md) (**Accepted**).

**GC1-S1 — Recognition.** [GC1-S1-RECOGNITION.md](GC1-S1-RECOGNITION.md). RFC: [RFC-0005](../rfcs/RFC-0005-mastery-recognition.md) (**Accepted**). Self-only lines. No benefits.

**GC2-S0 — Construct/dismantle existing infrastructure.** [GC2-FIRST-SLICE.md](GC2-FIRST-SLICE.md). RFC: [RFC-0006](../rfcs/RFC-0006-construction-existing-events.md) (**Accepted**). Hosted PLAY shipped (Noema #79). No `event-catalog/0.3`. Chamber help still omits `BUILD`.

**GC3-S0 — Dyadic trade memory.** [GC3-FIRST-SLICE.md](GC3-FIRST-SLICE.md). RFC: [RFC-0007](../rfcs/RFC-0007-dyadic-trade-memory.md) (**Accepted**). Hosted PLAY shipped (Noema #70). No reputation integer.

**GC4–GC10 S0** are specified and hosted. Closeout: [GC-S0-CLOSEOUT-2026-08-13.md](GC-S0-CLOSEOUT-2026-08-13.md). Next specification order: [GC-S1-ORDER.md](GC-S1-ORDER.md). `COMMIT.ATTEST` is RFC-0020 (spec only).

Why GC1-S0 was first, historically:

- Explorer / Surveyor / Broker evidence is already in `event-catalog/0.1`.
- No new verb, no map mutation, no mechanical benefit.
- Full scenario A (recognition + benefit) is **GC1-S2**, still deferred.

The hosted Worker now has S0 PLAY slices plus RFC-0019 world-time. It still has no complete reconstructable Postgres head until operator SQL is applied.

---

## 6. Guardrails

Preserve all of:

```text
Humans and agents are both Players.
Controller type is not a gameplay caste.
Research does not become world truth.
Research rewards do not become Player rewards.
No universal consciousness/intelligence score.
No universal XP score unless future evidence requires one.
No autonomous LLM mutation authority.
No authored quest system replacing world-state problems.
No hidden-information leaks through GUI affordances.
No new runtime verb solely because a new noun exists.
No cosmetic institution roles without bounded authority.
No construction system isolated from other strategic systems.
No irreversible loss state with no skillful recovery path.
No single dominant victory function.
```

Stable-verb rule (from [PLAYER-ACTION-MAP.md](PLAYER-ACTION-MAP.md)):

```text
stable verbs
+ richer targets
+ richer parameters
+ authority
+ Player state
= richer gameplay
```

---

## 7. Acceptance matrix — complete world

High-level design proof. Not a conformance suite. Each scenario MUST remain satisfiable after later RFCs.

### A. Identity

A Player enters without a fixed class, repeatedly performs meaningful work, develops a recognized specialization, and gains new world-native opportunities without receiving a global intelligence score.

**Owner:** GC1 · [MASTERY-SPECIALIZATION.md](MASTERY-SPECIALIZATION.md)

### B. Social memory

Two Players build trust through repeated successful cooperation. A later betrayal changes their relationship and relevant institutional expectations without revealing hidden facts.

**Owner:** GC3 · [SOCIAL-MEMORY.md](SOCIAL-MEMORY.md)

### C. Construction

A Player or institution builds infrastructure that changes movement, trade, production, or strategic value and remains historically attributable after the original builders leave.

**Owner:** GC2 · [CONSTRUCTION.md](CONSTRUCTION.md)

### D. Institutional authority

A Player receives a bounded office, performs permitted actions, cannot perform actions outside that office, leaves office, and authority transfers correctly.

**Owner:** GC4 · [INSTITUTIONAL-AUTHORITY.md](INSTITUTIONAL-AUTHORITY.md)

### E. Communication

Infrastructure damage affects communication capability or latency through deterministic world state without breaking ordinary action semantics.

**Owner:** GC5 · [COMMUNICATION-ECOLOGY.md](COMMUNICATION-ECOLOGY.md)

### F. Mystery

Players discover conflicting evidence, investigate through normal actions, reach different beliefs, and eventually produce a better-evidenced reconstruction without an authored quest oracle.

**Owner:** GC6 · [SYSTEMIC-DISCOVERY.md](SYSTEMIC-DISCOVERY.md)

### G. Conflict

Two groups enter a strategic conflict with meaningful reconnaissance, counterplay, escalation, commitment, and recovery.

**Owner:** GC7 · [STRATEGIC-CONFLICT.md](STRATEGIC-CONFLICT.md)

### H. Economy

Several specialized Players become more effective through exchange and cooperation than one Player attempting every function.

**Owner:** GC8 · [ECONOMIC-SPECIALIZATION.md](ECONOMIC-SPECIALIZATION.md)

### I. Culture

Repeated practices persist into a later generation as evidence-backed custom or institutional tradition without rewriting the event ledger.

**Owner:** GC9 · [EMERGENT-CULTURE.md](EMERGENT-CULTURE.md)

### J. World pressure

An authorized operator introduces a bounded world condition; Players respond differently; the event is replayable and research can observe the divergence without the perturbation forcing a target result.

**Owner:** GC10 · [WORLD-EVENT-DIRECTOR.md](WORLD-EVENT-DIRECTOR.md)

---

## 8. Machine-contract inventory

Do **not** invent schemas in this campaign. Every future machine contract MUST have a prose authority first.

| Package | Likely later contracts | Invent now? |
|---------|------------------------|-------------|
| GC1 | proficiency/evidence schema; optional derived-state fields; fixtures; conformance | No |
| GC2 | `action-contracts` increment; `BUILD` operation enum; constructible catalog; events; migration | No — RFC required |
| GC3 | relationship-edge schema; visibility rules; fixtures | No |
| GC4 | role/office schema; authority-scope catalog; events (`ROLE_*` already flagged later in SUCCESSION) | No — no silent `event-catalog/0.3` |
| GC5 | delivery/latency model; rumor provenance schema; MESSAGE policy extension | No if MESSAGE can carry it |
| GC6 | mostly composition of existing Deep Time / contradiction schemas | Prefer reuse |
| GC7 | possible later contest-config / catalog increment | No — do not mutate `event-catalog/0.2` here |
| GC8 | quality/scarcity/transport fields; maybe v0.6B overlap | No |
| GC9 | custom/tradition derived records; must not become lore canon | No |
| GC10 | pressure-event catalog; preview/audit/receipt; distinct from Frontier schemas | No |

**OBSERVED:** no GC machine contracts exist on this branch.  
**INFERRED:** first implementation slice (GC1) can begin as rebuildable derived state from the existing ledger, which may delay a catalog RFC.  
**SPECULATIVE:** GC2 will require the first PLAY-facing catalog increment after v0.2.  
**NOT_COMPUTABLE:** exact numeric thresholds, event type IDs, and schema versions until those RFCs exist.

---

## 9. Dependency order

Use this sequencing unless later repository evidence proves a better one:

```text
PHASE A — IDENTITY AND PERSISTENCE
  GC1 Mastery
  GC2 Construction
  GC3 Social Memory

PHASE B — SOCIETY AND INFORMATION
  GC4 Institutional Authority
  GC5 Communication Ecology
  GC6 Systemic Mystery

PHASE C — STRATEGIC DEPTH
  GC7 Strategic Conflict v2
  GC8 Economic Specialization

PHASE D — CIVILIZATION
  GC9 Emergent Culture
  GC10 World Steward Pressure
```

Cross-phase notes:

- GC4 consumes GC1 recognition and GC3 institutional memory.
- GC5 consumes infrastructure from GC2 when relays become constructible/damageable beyond v0.1 condition.
- GC6 consumes Deep Time plus GC2 scars and GC5 rumor surfaces.
- GC7 consumes GC3 reputation effects and GC2 territorial/infrastructure targets.
- GC8 consumes GC1 specializations and GC2 production assets.
- GC9 consumes repeated GC3/GC4/GC5 behavior and Deep Time.
- GC10 may perturb any prior system; it MUST NOT require all of them to exist.

---

## 10. Game-design coupling

Every completeness mechanic MUST touch at least one other node of [GAME-SYSTEM-MAP.md](GAME-SYSTEM-MAP.md). Isolated minigames are defects ([GAME-BALANCE.md](GAME-BALANCE.md)).

Completeness overlay (does not replace the primary chain):

```text
MASTERY  ↔  ACTIONS / AUTHORITY
CONSTRUCTION  ↔  GEOGRAPHY / RESOURCES / INFRASTRUCTURE / TERRITORY / DEEP TIME
SOCIAL MEMORY  ↔  TRADE / DIPLOMACY / CONFLICT / INSTITUTIONS
OFFICES  ↔  ORGANIZATIONS / INSTITUTIONS / SUCCESSION
COMMUNICATION  ↔  INFRASTRUCTURE / KNOWLEDGE / REPORTS
DISCOVERY  ↔  EXPLORATION / EVIDENCE / LORE BOUNDARY
CONFLICT v2  ↔  TERRITORY / TRADE / REPUTATION / INFRASTRUCTURE
ECONOMIC SPECIALIZATION  ↔  RESOURCES / PRODUCTION / TRADE
CULTURE  ↔  DEEP TIME / INSTITUTIONS / MEMORY
WORLD EVENT DIRECTOR  ↔  CONDITIONS (never Player objectives)
```

---

## 11. Spec Completion Contract

A game-completeness work package is **not** ready for runtime implementation until an implementation agent can determine, without inventing product behavior:

```text
exact state
lifecycle
exact transitions
canonical actions
parameters
preconditions
costs
authority
events
visibility
partial-observability behavior
deterministic ordering
idempotency
failure semantics
replay behavior
migration/version behavior
positive fixtures
negative fixtures
acceptance tests
PLAY projection
WATCH projection
research capture boundary
security boundary
```

This patch settles **product behavior** for GC1–GC10. It does **not** claim the machine half of this contract. Remaining gaps are listed in each domain authority under **SPEC GAP**.

---

## 12. Final product principle

NOEMA should not merely test whether an agent can solve tasks or win.

It should create enough persistent social, economic, informational, institutional, and historical structure that an intelligent actor can **become somebody inside the world**.
