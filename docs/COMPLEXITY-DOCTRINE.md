# Complexity Doctrine

**Status:** Design-gate authority for all current and future game-system work.  
**Does not replace:** [GAME-DESIGN.md](GAME-DESIGN.md) · [CORE-GAME-LOOP.md](CORE-GAME-LOOP.md) · [GAME-BALANCE.md](GAME-BALANCE.md) · [GAME-SYSTEM-MAP.md](GAME-SYSTEM-MAP.md) · [GAME-COMPLETENESS-PLAN.md](GAME-COMPLETENESS-PLAN.md)

This document is the **rejection test** for unnecessary systems. Completeness work (GC1–GC10) must pass it. Later economic expansions must pass it.

---

## Seal

> NOEMA should use a small number of deeply coupled primitives to produce complex economic, social, institutional, and historical outcomes. Complexity belongs in emergent relationships between systems, not in the number of systems themselves.

> **Model causes, not industries.**

Do not create a banking subsystem because banks exist. Model scarcity, ownership, trust, obligation, and collateral. If Players compose those into a bank-like institution, banking has emerged.

Do not create a shipping subsystem because shipping exists. Model distance, capacity, route state, cost, and risk. If Players specialize around those constraints, transportation has emerged.

---

## What completeness is not

Do not measure the world by:

```text
room count
NPC count
command count
quest count
number of independent subsystems
```

Measure it by whether a Player can acquire a role, develop specialization, build relationships, create something persistent, respond to disruption, influence institutions, leave evidence, and alter the environment later Players inherit.

Research observes that play. Research does not replace it.

---

## Seven primitives

Prefer these over a new entity class. An eighth primitive is legal only when the seven cannot express a required world transition without semantic distortion.

| Primitive | Meaning | Typical existing authority |
|-----------|---------|----------------------------|
| **RESOURCE** | Fungible or countable productive goods | [RESOURCE-ECONOMY.md](RESOURCE-ECONOMY.md) |
| **ASSET** | Persistent individually meaningful object (relay, workshop, artifact, route work) | [INFRASTRUCTURE.md](INFRASTRUCTURE.md), [CONSTRUCTION.md](CONSTRUCTION.md) |
| **LOCATION** | Spatial asymmetry: distance, routes, risk, local information | [GEOGRAPHY.md](GEOGRAPHY.md) |
| **PLAYER / ORGANIZATION** | Actors and membership containers. Companies, guilds, cartels, labs are organizations + roles + assets + contracts + practices — not new runtime species | [INSTITUTIONS.md](INSTITUTIONS.md), [AUTH-AND-IDENTITY.md](AUTH-AND-IDENTITY.md) |
| **TRADE** | General exchange of resources, assets, access, services, information, rights | [ACTION-CONTRACTS.md](ACTION-CONTRACTS.md) |
| **CONTRACT / AGREEMENT** | Future, conditional, recurring, or access obligations | [DIPLOMACY.md](DIPLOMACY.md) |
| **INFORMATION** | Observed, reported, purchased, inferred, historical, rumored — with provenance and partial observability | [EXPLORATION.md](EXPLORATION.md), [STRATEGIC-KNOWLEDGE.md](STRATEGIC-KNOWLEDGE.md), [PARTIAL-OBSERVABILITY.md](PARTIAL-OBSERVABILITY.md) |

World Services remain desks, not Players ([WORLD-SERVICES.md](WORLD-SERVICES.md)).

Do not add a new resource type unless it creates a materially distinct strategic constraint.

---

## Four world pressures

Most economic and social complexity MUST come from:

```text
SCARCITY     — no Player can have everything
DISTANCE     — useful things are not always where they are needed
DEPENDENCY   — no Player efficiently performs every function alone
UNCERTAINTY  — holdings, routes, capabilities, intentions, and history are not automatic knowledge
```

A mechanic that creates none of these, and does not respond to them, is a candidate for **DEFER**.

---

## Noun emergence, verb stability

The world may continuously acquire organizations, roles, assets, places, practices, customs, agreements, titles, and historical names.

It must not continuously acquire canonical Player verbs.

```text
stable action + target + parameters + authority + state
```

`The Eastern Watch`, `Grey Route Compact`, and `Cycle-81 Alloy` are nouns. They do not create `WATCH`, `COMPACT`, or `ALLOY` verbs.

Authority: [PLAYER-ACTION-MAP.md](PLAYER-ACTION-MAP.md), [ACTION-CONTRACTS.md](ACTION-CONTRACTS.md).

---

## Civilization ladder

```text
ACTION
  → REPEATED PATTERN
  → PRACTICE
  → CUSTOM
  → INSTITUTION
  → CULTURE
```

A **Practice** is a repeated, recognizable way Players or organizations use existing primitives. It is evidence-backed. It is **not** automatically an Institution.

Formalization requires Player agency:

```text
repeated behavior
  → candidate practice
  → Player recognition
  → optional formalization
  → resource / influence / authority cost
  → institution
```

Informal systems remain viable. Do not invent a `practice` schema unless a required transition cannot be derived from existing events and institution records. The **distinction** is normative even when the representation is derived.

Culture interprets history. It never rewrites the ledger ([LORE-BOUNDARY.md](LORE-BOUNDARY.md), [EMERGENT-CULTURE.md](EMERGENT-CULTURE.md)).

---

## Structural capability

Prefer concrete world mechanisms over abstract buffs.

| Avoid | Prefer |
|-------|--------|
| Market Level 4: +15% trade efficiency | A public board, known location, trade history, and social memory that make counterparties findable |
| Guild +20 logistics | Vehicles/routes/contracts/practiced members |
| Engineer Level 5: +25% repair | Repair history, prior difficulty, tools/assets, known procedures, institutional recognition |

Mastery ([MASTERY-SPECIALIZATION.md](MASTERY-SPECIALIZATION.md)) is an evidence-backed trajectory, not an RPG class tree. No universal XP. GC1-S2, if ever opened, MUST justify any `REPAIR` quality change as a world mechanism (tools, access, known procedure), not a level multiplier.

---

## Friction and density

Need **friction that creates decisions**, not chores.

Good: the alloy is far away; another Player has the expertise; the route is damaged; the stock is unknown.  
Bad: harvest twenty times; click through empty confirmations; low-information labor.

If twenty units are one commitment, that is **one** `HARVEST` with an amount, not twenty commands.

**Decision density** = meaningful strategic decisions / required Player actions. Prefer higher.

**Coupling density** = meaningfully affected systems / mechanic-specific complexity. Prefer higher. A relay that changes movement, communication, trade, territory, conflict, institutions, and history is high-value. A mechanic that only feeds its own progression tree is a defect ([GAME-BALANCE.md](GAME-BALANCE.md)).

---

## Removal / complexity test

For every proposed mechanic:

1. If deleted, is a product contract unmet or materially weaker?
2. Can existing primitives represent the same behavior without semantic distortion?
3. Does it create at least two meaningful cross-system interactions?

If not: **REJECT** or **DEFER**.

Do not add complexity because the mechanic is realistic, familiar, fashionable, or theoretically interesting.

---

## Design acceptance tests (A–J)

Every proposed game mechanic MUST be scored against:

| Test | Question |
|------|----------|
| **A. Primitive reuse** | Can existing primitives represent it? |
| **B. Pressure grounding** | Which of scarcity / distance / dependency / uncertainty does it create or answer? |
| **C. Decision density** | Meaningful decisions without busywork? |
| **D. Coupling density** | At least two other systems? |
| **E. Verb stability** | Existing canonical actions? |
| **F. Emergence** | Can an institution, business, custom, or specialization arise by composition? |
| **G. Deep Time** | If persistent, attributable and historically legible? |
| **H. Human/agent parity** | Equivalent world semantics for both Controllers? |
| **I. Research isolation** | Still meaningful if all research instrumentation is hidden? |
| **J. Removal test** | Does deleting it lose a real product contract? |

Failing several tests → **DEFER**, not “expand the active system.”

---

## Future-economy hard deferral

**Not authorized** in this campaign or any current first-world / completeness implementation:

```text
cryptocurrency
USDC
x402
NFTs
tokenized property
external asset title
external spend authority
Player wallets
settlement facilitators
blockchain contracts
NOEMA token
credit markets
bonds
insurance engines
real-money Player services
```

They may be named only as explicit future compatibility notes so a current primitive does not *block* later evolution.

Do **not** add dependencies, environment variables, schemas, APIs, wallet fields, token fields, blockchain libraries, or payment routes for them.

In-game mechanics MUST work fully without them.

Internal obligation, collateral, and trust remain in-world primitives (agreements, holdings, social memory). They are not banking, credit, or insurance engines.

---

## How this relates to other maps

Keep both levels:

```text
DOMAIN DEPENDENCY MAP     (geography → resources → … → history)
  +
EMERGENCE / COMPLEXITY MAP  (primitives → pressures → actions → consequences
                             → practices → institutions → culture)
```

The domain chain in [GAME-SYSTEM-MAP.md](GAME-SYSTEM-MAP.md) is not replaced. The emergence map is a higher-order complement.

Campaign sequencing remains [GAME-COMPLETENESS-PLAN.md](GAME-COMPLETENESS-PLAN.md). This doctrine **filters** that campaign. It does not delete GC1–GC10.
