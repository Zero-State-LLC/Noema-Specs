# World Model

## Scope

The World Engine is a persistent MUD-style simulation of rooms, geography, movement, economy, resources, infrastructure, organizations, markets, communication, institutions, local state, persistent history, and Deep Time.

## State domains

- Canonical state: authoritative private truth used for resolution.
- Observable state: mediated room, entity, resource, message, and event descriptions.
- Agent state: connection, budgets, capabilities, permissions, and declared metadata.
- Research state: trajectories, observations, events, predictions, self-reports, and provenance.

## Resolution

State transitions MUST be deterministic under world version, seed, deterministic config, prior state, and ordered event ledger. Seeded nondeterminism MUST name the stream and decision point.

## Deep Time objects

The world retains old treaties, dead agents, previous organizations, abandoned infrastructure, obsolete currencies, agent-written documents, historical misinformation, cultural conventions, ruins, artifacts, and institutional memory.

## Unknown Ontology

World content and research records MUST support unknown identifiers such as `UNKNOWN_CAPABILITY_<id>` and `UNKNOWN_PHENOMENON_<id>` without requiring immediate taxonomy.
