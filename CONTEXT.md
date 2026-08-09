# Repository Context

## Purpose
This repository defines NOEMA, a persistent text-based multi-agent world and research apparatus for discovering, reproducing, and measuring emergent capabilities in autonomous agents. The durable world, not an agent-centric puzzle, is the experimental substrate.

## Authority
Accepted RFCs override versioned protocols and schemas for their stated scope. Protocols and schemas override subsystem documentation. Examples are conformance fixtures, not independent authority. Conflicts are defects.

## Canonical domains
- **World truth:** authoritative state, rules, resources, institutions, and ordered transitions.
- **Observation:** partial, permissioned signals delivered to an agent or researcher.
- **Agent state:** externally declared identity and capabilities plus observable behavior. Private cognition is out of scope.
- **Evidence:** immutable observations and interventions with provenance.
- **Claims:** versioned interpretations with stated confidence and citations.

## Non-negotiable invariants
World state MUST NOT depend on an agent's belief. A genesis state, seeds, versioned rules, ordered event ledger, and declared external inputs MUST support deterministic replay. Agent actions MUST be authenticated, authorized, budgeted, and containable. Research exports MUST preserve consent, provenance, exclusions, and version lineage. Telemetry MUST NOT silently become evidence.
