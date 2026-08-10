# Strategic Conflict

## Status

Authoritative design for conflict, crime, and contested action in NOEMA.
v0.1 Chamber remains free of **mandatory** combat. Strategic contestation and crime are introduced as **NEXT GAME MILESTONE (v0.2)** with a minimal viable subset.

This document does **not** expand the closed 24-type v0.1 event catalog. Implementations MUST NOT invent uncatalogued world events for contestation without an accepted RFC.

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

Exact schemas and reducers will be specified in the v0.2 RFC. No casual additions to the closed v0.1 24-type catalog.

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
