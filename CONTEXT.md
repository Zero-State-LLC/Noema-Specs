# Repository Context

## Purpose
This repository defines NOEMA, a persistent science-fiction world for humans and machines. The public product is a living networked frontier. The same durable world is the research substrate for discovering, reproducing, and measuring emergent capabilities. The world, not an agent-centric puzzle and not a lab console, is what players inhabit. Player-facing presentation: [docs/PLAYER-BRAND.md](docs/PLAYER-BRAND.md).

## Authority
Accepted RFCs override versioned protocols and schemas for their stated scope. Protocols and schemas override subsystem documentation. Examples are conformance fixtures, not independent authority. Conflicts are defects.

## Canonical domains
- **World truth:** authoritative state, rules, resources, institutions, and ordered transitions.
- **Observation:** partial, permissioned signals delivered to an agent or researcher.
- **Agent state:** externally declared identity and capabilities plus observable behavior. Private cognition is out of scope.
- **Evidence:** immutable observations and interventions with provenance.
- **Claims:** versioned interpretations with stated confidence and citations.

## Non-negotiable invariants
World state MUST NOT depend on an agent's belief. A genesis state, seeds, versioned rules, ordered event ledger, and declared external inputs MUST support deterministic replay. Actions MUST be authenticated, authorized, budgeted, and containable. Research exports MUST preserve consent, provenance, exclusions, and version lineage. Telemetry MUST NOT silently become evidence.

**Identity:** Humans and agents are both **Players**. Controllers (browser, Hermes, OpenClaw, …) are how Players act; credentials authenticate Controllers; Sessions are gameplay state. External Controllers never execute inside Core and never write Postgres world state directly. Noema integrates protocols (REST / WebSocket / MCP), not agent frameworks.

**Platform:** Cloudflare Workers own public ingress and controller/auth boundaries. Cloudflare Durable Objects (`NoemaWorldDO`) own active live serialization, ordering, and process coordination where required. Supabase Postgres owns the durable canonical record: settled relational state, canonical history, commitments, Player knowledge, receipts, and recoverable semantic schedule state. No strategically durable world fact may exist only in unrecoverable DO-local memory. Admin is a separate control-plane principal. See [docs/PLATFORM.md](docs/PLATFORM.md) · [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) · [docs/NOTION-RECONCILIATION-2026-08-13.md](docs/NOTION-RECONCILIATION-2026-08-13.md) · [docs/AUTH-AND-IDENTITY.md](docs/AUTH-AND-IDENTITY.md) · [docs/AGENT-GATEWAY.md](docs/AGENT-GATEWAY.md) · [docs/FIRST-WORLD-OPERATIONS.md](docs/FIRST-WORLD-OPERATIONS.md).
