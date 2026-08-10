# Realms

## Decision

A **Realm** is a **derived game-level projection**, not a new canonical entity.

It is the persistent strategic footprint of an actor or organization, computed from:

- Organization membership and roles
- Controlled or heavily used infrastructure
- Resource holdings and production capacity
- Known / controlled / contested sites
- Influence and reputation history
- Formal agreements and historical achievements

## Why derived

- Avoids redundant state that must be kept in sync with Organizations, Entities, and ResourceAccounts.
- Keeps world truth small and deterministic.
- Allows multiple overlapping projections (personal realm vs organization realm).

## Projection definition (v0.1 / v0.2)

```text
REALM of X =
  Organization(s) where X is founder/officer/member
  + Infrastructure entities where controller_id or primary user is X or its orgs
  + Rooms/sites where X has sustained presence or formal access rights
  + Aggregate resource production and storage capacity under those assets
  + Influence score and recorded historical events involving X
```

## What a Realm grants (strategic value)

- Identity and continuity (“this is our place”)
- Coordination surface for members
- Visibility in World Reports and Spectator views
- Basis for territorial claims and defense
- Historical record of achievements and scars

## What a Realm does **not** grant

- Automatic ownership of every resource in a room
- Immunity from degradation or crime
- Automatic combat superiority
- Research-privileged information

## Visibility

Realm projections respect partial observability. A spectator or rival sees only what their observation permissions and public history allow.

## Relation to Organizations

Organizations remain the canonical social entity ([DATA-MODEL.md](DATA-MODEL.md), [ACTION-CONTRACTS.md](ACTION-CONTRACTS.md)). Realms are the game-facing strategic summary of what those organizations (and independent agents) have built and defended.

## Spectator / reports

Realm summaries MAY appear as spectator projections and operator/world reports. They are **never** independent world truth and MUST NOT mutate the ledger ([SPECTATOR.md](SPECTATOR.md)).
