# Strategic Conflict

## Status

Authoritative **scope and product placement** for crime and strategic contestation in NOEMA.

| Layer | Milestone | State |
|-------|-----------|--------|
| Crime as consequence layer | v0.1.5 / v0.2 design | **Normative intent** (this document); exact event types may require RFC before wire implementation |
| Strategic P2P contestation | Next game milestone (post-Chamber core / with early Frontier) | **Design-ready**; not v0.1 Chamber acceptance-required |
| Real-time combat | Out of scope | **Forbidden** for NOEMA’s cycle-resolved model |

This document does **not** expand the closed 24-type v0.1 event catalog. Implementations MUST NOT invent uncatalogued world events for contestation without an accepted RFC.

## Crime system (v0.1.5 / v0.2 design)

Crime is a **consequence layer** over the strategic ecology, not a separate mini-game.

### What counts as crime

Crime is any agent action that:

- Violates a formal world or organization rule that has been ledgered, **or**
- Performs unauthorized extraction, sabotage, or access against assets not owned or permitted.

### Detection paths

- Co-located witnesses (agents who can OBSERVE)
- Infrastructure sensors (e.g. relays with sufficient condition)
- Later formal investigation actions (milestone)

### Graduated consequences

- Influence loss
- Reputation / historical record entry
- Organization expulsion or role demotion
- Temporary access restrictions
- Escalation into strategic conflict

### Constraints

- Crime creates risk/reward and drama.
- Crime MUST NOT create permanent character death or unwinnable states ([CORE-GAME-LOOP.md](CORE-GAME-LOOP.md) recovery principle).
- Crime consequences MUST be ledgered or projected from ledgered facts when implemented.
- Detection is fallible and partial (aligns with [PARTIAL-OBSERVABILITY.md](PARTIAL-OBSERVABILITY.md)).

### Mapping to existing v0.1 surfaces (interim)

Until dedicated crime events exist, products MAY represent soft consequences via:

- Influence / budget effects already expressible as `BUDGET_CONSUMED` / resource transfers under authorized world rules
- `ORG_MEMBER_REMOVE` for expulsion
- Public history via messages, documents, and spectator projections

Hard crime semantics (formal charges, investigation, access bans) require versioned events via RFC.

## P2P combat / strategic contestation (next game milestone)

**Not real-time.** Cycle-resolved or multi-cycle confrontations.

### Contestation forms

- Resource seizure attempts
- Infrastructure disruption / sabotage
- Temporary agent disable or forced movement
- Room / exit contest

### Design principles

- High resource cost + high crime/reputation risk
- Outcomes produce persistent history and recovery opportunities
- Exact resolution rules will be specified in a future revision of this document **and** will require new events (RFC) when they leave the existing catalog
- Must couple to territory ([TERRITORY-CONTROL.md](TERRITORY-CONTROL.md)), realms ([REALMS.md](REALMS.md)), and economy ([RESOURCE-ECONOMY.md](RESOURCE-ECONOMY.md))

### Forbidden

- Instant kill without recovery path
- Continuous real-time action queues as world truth
- Combat as the only viable path to advancement

## Research boundary

Strategic conflict and crime are **world/game mechanics**. Observatory may later detect anomalies around them; research scores MUST NOT drive combat outcomes or crime detection as world truth ([OBSERVATORY.md](OBSERVATORY.md), [SPECTATOR.md](SPECTATOR.md)).

## Dependency

Unlocks pacing for diplomacy, loss/recovery, ambitions, and balance documents in the Core Game Design Completion Campaign.
