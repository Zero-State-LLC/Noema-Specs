# Strategic Conflict

## Status

Authoritative design for conflict, crime, and contested action in NOEMA.
v0.1 Chamber remains free of **mandatory** combat. Strategic contestation and crime are introduced as **NEXT GAME MILESTONE (v0.2)** with a minimal viable subset.

v0.1 remains on the closed 24-type catalog. Strategic contestation is **Accepted** under [RFC-0002](../rfcs/RFC-0002-strategic-contestation-and-crime-events.md) as additive **`event-catalog/0.2`**. Implementations MUST NOT invent uncatalogued world events.

## Design principles

- Conflict must feel strategic, not twitchy.
- High cost and high risk.
- Persistent consequences and recovery paths are required.
- Crime is a consequence layer, not a separate minigame.
- No permanent character death or unwinnable spirals from a single event.
- World truth remains independent of agent belief.

## Conflict categories

### CURRENT REQUIRED (already possible in v0.1)

- Economic pressure (hoarding, refusal to trade, influence competition)
- Resource competition on shared nodes
- Infrastructure degradation races
- Organization rivalry through membership and messaging
- Information asymmetry and concealment

### NEXT GAME MILESTONE (v0.2)

- Formal strategic contestation actions
- Crime detection and graduated consequences
- Infrastructure sabotage / disruption
- Temporary access denial and route contest
- Resource seizure attempts under high risk

### LATER

- Complex multi-party wars
- Formal legal systems beyond organization policy
- Large-scale territorial campaigns

## Crime system

### Definition

A crime occurs when an agent performs an action that:

1. Violates a ledgered formal rule (organization policy or world contract), **or**
2. Attempts unauthorized extraction, sabotage, access, or seizure against assets the agent does not own or have explicit permission to affect.

### Detection

- Co-located witnesses (other agents who OBSERVE or are present)
- Infrastructure sensors (relays and production nodes with condition ≥ 50 can generate detection events)
- Later formal investigation actions

Detection produces a world-visible historical record and may trigger influence/reputation effects.

### Graduated consequences

| Severity | Effects |
|----------|---------|
| Minor | Influence loss, public historical note |
| Moderate | Larger influence loss, possible organization role demotion or expulsion, temporary access restriction |
| Major | Strong historical scar, possible multi-cycle restrictions, escalation into contested status |

Crime never permanently removes an agent from the world. Recovery and adaptation remain possible ([LOSS-RECOVERY.md](LOSS-RECOVERY.md)).

### Design intent

Crime creates risk/reward, drama, and story. It does not create a permanent underclass or automatic ban.

### Interim v0.1 mapping

Until dedicated crime events exist, products MAY represent soft consequences via:

- Influence / budget effects already expressible under authorized world rules
- `ORG_MEMBER_REMOVE` for expulsion
- Public history via messages, documents, and spectator projections

Hard crime semantics require versioned events via RFC.

## Strategic P2P contestation (v0.2)

Contestation is cycle-resolved or multi-cycle. It is **not** real-time combat.

### Supported contest forms (minimal set)

- **Resource seizure attempt**: high-cost action against a node or holding under contested conditions.
- **Infrastructure disruption**: attempt to lower condition of target infrastructure.
- **Access contest**: attempt to change exit state or room access rights temporarily.
- **Presence pressure**: attempt to force a temporary disable or forced movement of a co-located agent (high cost, high detection risk).

### Resolution principles

- Both parties commit resources.
- Outcome determined by committed resources, local infrastructure condition, organization support, and declared modifiers.
- Failure or partial success still generates history and possible crime flags.
- Success produces temporary advantage + persistent record, not permanent ownership transfer unless further actions follow.

### Required new events (RFC required)

- `CONTEST_DECLARED`
- `CONTEST_RESOLVED`
- `CRIME_DETECTED`
- `ACCESS_RESTRICTED` (temporary)
- `INFRASTRUCTURE_DISRUPTED`
- `AGREEMENT_FORMED` / `AGREEMENT_BROKEN` (formal diplomacy; see audit)

**Accepted:** [RFC-0002](../rfcs/RFC-0002-strategic-contestation-and-crime-events.md), catalog [`event-types.0.2.json`](../specs/event-types.0.2.json), config [`contest-config.v02.json`](../specs/contest-config.v02.json), algorithm [CONTEST-RESOLUTION.md](CONTEST-RESOLUTION.md), coupling [STRATEGIC-EVENT-COUPLING.md](STRATEGIC-EVENT-COUPLING.md), fixtures [`examples/v02-strategic-conflict/`](../examples/v02-strategic-conflict/).

## Defense

Defense is proactive investment, not a passive stat:

- Infrastructure condition and redundancy
- Distributed storage and alternate routes
- Early-warning via relays
- Organization mutual support
- Reserves of energy, storage, and influence
- Formal access agreements

Simple attack-stat vs defense-stat is avoided.

## Relation to existing systems

Conflict and crime consume the same five resources and produce standard `ENTITY_UPDATE`, `BUDGET_CONSUMED`, and historical records where expressible. They must not bypass existing action and event contracts ([ACTION-CONTRACTS.md](ACTION-CONTRACTS.md), [RESOURCE-ECONOMY.md](RESOURCE-ECONOMY.md), [TERRITORY-CONTROL.md](TERRITORY-CONTROL.md), [REALMS.md](REALMS.md)).

## Research boundary

Strategic conflict and crime are **world/game mechanics**. Observatory may later detect anomalies around them; research scores MUST NOT drive combat outcomes or crime detection as world truth.

The arXiv-informed conflict integration slice—culture and institutions affect
coordination, commitment, evidence, and recovery while the existing contest
rhythm remains authoritative—is recorded in
[RESEARCH-ASSIMILATION-2026-08-21.md](RESEARCH-ASSIMILATION-2026-08-21.md).

---

## Game Completeness v2 (GC7) — specification campaign

**Status:** Design extension for later strategic depth. P1. Phase GC-C.  
**Does not change** executable `event-catalog/0.2`, [RFC-0002](../rfcs/RFC-0002-strategic-contestation-and-crime-events.md), [CONTEST-RESOLUTION.md](CONTEST-RESOLUTION.md), or `action-contracts.v02.json`.  
**Campaign:** [GAME-COMPLETENESS-PLAN.md](GAME-COMPLETENESS-PLAN.md)  
**Doctrine:** operate through resources, assets, information, territory, relationships, agreements, and organizations. No hit-point combat subsystem ([COMPLEXITY-DOCTRINE.md](COMPLEXITY-DOCTRINE.md)).

v0.2 remains the implementation contract. v2 deepens **Player-facing rhythm and coupling** without converting NOEMA into hit-point combat and without a second conflict canon.

GC7-S0 machine pins: [GC7-FIRST-SLICE.md](GC7-FIRST-SLICE.md) · [RFC-0011](../rfcs/RFC-0011-contest-rhythm.md). Withdraw is [GC7-S1](GC7-S1-WITHDRAW.md). Institution-as-party is [GC7-S2](GC7-S2-INSTITUTION-PARTY.md). Information-target form is [GC7-S3](GC7-S3-INFORMATION-CONTEST.md).

### Target rhythm

```text
RECON → POSITION → PRESSURE → COUNTER → ESCALATE → COMMIT → RESOLVE → RECOVER
```

| Stage | Existing composition | Must not become |
|-------|----------------------|-----------------|
| RECON | `LOOK` / `INSPECT` / exploration / relays / rumors | A `SCAN` combat verb |
| POSITION | `MOVE`, access policy, presence, route control | Instant teleport / engage |
| PRESSURE | Trade refusal, hoarding, membership politics, degraded infrastructure | Auto-damage aura |
| COUNTER | `CONTEST_DEFEND`, repair, alternate routes, agreements | Perfect parry stat |
| ESCALATE | Larger reservations, additional contest forms, third parties | Unavoidable war flag |
| COMMIT | `CONTEST_DECLARE` with reserved resources | Irreversible character death |
| RESOLVE | Existing integer contest algorithm | Real-time HP |
| RECOVER | [LOSS-RECOVERY.md](LOSS-RECOVERY.md), repair, new agreements | Permanent underclass |

Prefer **composition of stable verbs** over command growth.

### Potential targets

```text
territory
trade routes
resource sites
institutions
information
reputation
infrastructure
agreements
authority / offices
```

Information warfare is bounded by [SOCIAL-MEMORY.md](SOCIAL-MEMORY.md) and [COMMUNICATION-ECOLOGY.md](COMMUNICATION-ECOLOGY.md): messages may deceive; the engine MUST NOT leak hidden facts through contest UI.

### Signals and counterplay

- Declaration, reservation, and public reports are the signals.
- Counterplay is defense investment, withdrawal before resolve (if the catalog later allows a versioned withdraw with cost), third-party `MUTUAL_DEFENSE`, and infrastructure repair.
- Cost escalation is larger reservations and wider crime/detection exposure — not an enrage timer.
- Alliances use existing formal agreements; informal help is social only.
- Third parties enter by their own actions, never by forced conscription.

### Effects and anti-snowball

| Effect | Rule |
|--------|------|
| Infrastructure | Disruption and condition loss already specified |
| Economic | Seizure attempts, route pressure, trade refusal |
| Reputation | Public contest/crime evidence feeds social memory; not a combat stat |
| Institution | Offices may authorize institutional participation ([INSTITUTIONAL-AUTHORITY.md](INSTITUTIONAL-AUTHORITY.md)); vacancy does not delete history |
| Recovery | Always a skillful path ([LOSS-RECOVERY.md](LOSS-RECOVERY.md)) |
| Anti-snowball | Expansion increases exposure and maintenance. No single dominant strategy. No irreversible dead end from one contest |

### SPEC GAP (v2 only)

```text
GC7-S0 closed: RECON→RECOVER stage table over existing verbs; four v0.2 forms only
GC7-S1 closed: versioned withdraw via CONTEST_RESOLVED
GC7-S2 closed: institution-as-party via occupied office + acting_for; treasury pays
GC7-S3 closed: INFORMATION_CONTEST on visible public ARTIFACT; INSPECT seal; no hidden leak
any later catalog increment — RFC required, no silent 0.3
```

Implement v0.2 first. Do not block Chamber play on GC7.

### Acceptance (scenario G)

Two groups reconnoiter, position, apply economic or infrastructural pressure, counter, escalate, commit via declared contest, resolve under the existing algorithm, and recover. No hit-point combat. No unwinnable spiral.

## Research assimilation 2026-08-27 — Crime producer completion (RFC-0002 PARTIAL)

**Status:** Design/research integration / bounded extension note. Inputs only. No contract, catalog, verb, or exposure change. Cites [CRIME-PRODUCER-RESEARCH-SEED.md](CRIME-PRODUCER-RESEARCH-SEED.md) and [RESEARCH-ASSIMILATION-2026-08-27-ARXIV-DISTILLATIONS-GC-GAPS.md](RESEARCH-ASSIMILATION-2026-08-27-ARXIV-DISTILLATIONS-GC-GAPS.md).

**Gap (per seed and RFC-0002):** RFC-0002 (Accepted) defines `CRIME_DETECTED` as a *detection* event (not automatic guilt). Detection requires witness, sensor (condition ≥ 50), investigation, or self-report. The **producer** side — how play generates these detections (witness flows, sensor mechanics, delayed revelation, self-report, investigation) — remains PARTIAL. No silent producer implementation.

**Signals (assimilation):**
- Crime hotspot dynamics (arXiv:2605.17709v1): coupled PDE/ODE with *delayed* crime signal + police/guardian deployment. Delays destabilize via Hopf bifurcations → oscillations, moving/splitting/merging hotspots. Timely crime data access > raw density for stabilization. Maps to delayed detection, attractiveness/condition dynamics (ties to REPAIR/infra), guardian response as third actor.
- Cops and Robbers path planning (arXiv:2503.11475): LTL + reactive synthesis for pursuit/evasion realizability. Formal angles for contest/crime resolution.

**Bounded producer extension (this authority):**
- Producer flows (design framing only):
  - Witness: nearby Players or sensors observe qualifying breach → public or authorized `CRIME_DETECTED`.
  - Sensor: infrastructure/condition-based (≥50) or dedicated guardian/sensor assets trigger on patterns.
  - Investigation: authorized office or Player action produces evidence leading to detection.
  - Self-report: offender or witness voluntary report.
- Delayed revelation: per arXiv, information lags create dynamic hotspots/oscillations; revelation not instantaneous.
- Interaction with existing: feeds SOCIAL-MEMORY (public breach descriptors), WATCH/public reports (coarse bands), CONTEST (crime as pressure/escalation layer), Deep Time (persistent attribution/scars). `CRIME_DETECTED` remains detection only; guilt/resolution via existing contest or institutional processes.
- No new events or catalog entries. Reuses `CRIME_DETECTED` + existing ENTITY_UPDATE / contest / agreement events where applicable.
- Graduated: high-cost/risk, partial observability, fail-closed.

**Explicit boundaries:**
- Extends [STRATEGIC-CONFLICT.md](STRATEGIC-CONFLICT.md) + RFC-0002 authority. Do not create second canon.
- Ties to GC3 social memory (public crime feeds relational edges/gossip) without duplication.
- Complexity doctrine: consequence layer, not industry or permanent death. Evidence trajectories.
- Research/game membrane: producer mechanics for world truth; projections redacted as needed.

This bounded note completes the producer framing for RFC-0002 without runtime or catalog changes. Future RFC may pin fixtures/conformance.

**Citations / provenance:** RFC-0002 (Accepted), [CRIME-PRODUCER-RESEARCH-SEED.md](CRIME-PRODUCER-RESEARCH-SEED.md), RESEARCH-ASSIMILATION-2026-08-27-ARXIV-DISTILLATIONS-GC-GAPS.md (crime hotspot section), arXiv:2605.17709v1 / 2503.11475, [STRATEGIC-CONFLICT.md](STRATEGIC-CONFLICT.md), [GAME-COMPLETENESS-PLAN.md](GAME-COMPLETENESS-PLAN.md) (GC7), [SOCIAL-MEMORY.md](SOCIAL-MEMORY.md), [DEEP-TIME.md](DEEP-TIME.md).

### Research assimilation 2026-08-25 — Crime detection evidence and enforcement (update)
**Signals:** Detailed review (RESEARCH-ASSIMILATION-2026-08-25-CRIME.md + supporting NOTES-CRIME-DETECTION-EVIDENCE.md).
- Per-incident source_event_ids and distinct detection records (no aggregation into one severe sanction).
- OCEAN/first-hand observation beats propagated rumor for detection.
- Enforcement cost, jurisdiction, second-order free riders, and monitoring cost for exclusion.
- Payload contradictions noted (influence_delta required in schema vs detection-only intent); fail-closed on insufficient evidence.
- Temporary scoped exclusion; rehabilitation; no stigma contagion; no retune of sanction ladder.

**Mapping to producer framing (this note):** Strengthens witness/sensor provenance requirements, per-event evidence paths, and the need for enforcement cost/jurisdiction in future producer mechanics. Aligns with existing bounded producer (witness/sensor/investigation/self-report + delays). No new events or verbs here.

**Boundaries:** Design input only. Extends prior 2026-08-27 bounded producer. See also SPEC-GAP-REGISTER-2026-08-25 and the new crime notes for open gaps (B7c etc.). Ties to GC3 social memory (public descriptors from detections).

Cites: RESEARCH-ASSIMILATION-2026-08-25-CRIME.md, NOTES-CRIME-DETECTION-EVIDENCE.md, SPEC-GAP-REGISTER-2026-08-25.md, prior arXiv hotspot models, CRIME-PRODUCER-RESEARCH-SEED.md, RFC-0002.

This incremental assimilation updates the crime producer context on main (PR #305 captured the 08-27 batch).
