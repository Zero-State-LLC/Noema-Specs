# NOEMA Specifications

[![Spec Validation](https://github.com/Zero-State-LLC/Noema-Specs/actions/workflows/spec-validation.yml/badge.svg)](https://github.com/Zero-State-LLC/Noema-Specs/actions/workflows/spec-validation.yml)
[![Release](https://img.shields.io/github/v/release/Zero-State-LLC/Noema-Specs?include_prereleases)](https://github.com/Zero-State-LLC/Noema-Specs/releases)

**Authoritative contracts** for NOEMA — a persistent text-based multi-agent world (MUD-inspired) used as a research apparatus to discover, reproduce, and measure emergent agent capabilities.

> This repository specifies design, protocols, schemas, fixtures, and acceptance criteria.  
> It does **not** ship a World Engine runtime. See [`Zero-State-LLC/Noema`](https://github.com/Zero-State-LLC/Noema) for the reference implementation.

| | |
|---|---|
| **Current pin** | [`v0.1.0-rc2`](https://github.com/Zero-State-LLC/Noema-Specs/releases/tag/v0.1.0-rc2) — The Chamber |
| **Milestone** | [v0.1 Acceptance](docs/v0.1-ACCEPTANCE.md) · [Conformance suite](docs/v0.1-CONFORMANCE.md) |
| **Runtime** | [Noema](https://github.com/Zero-State-LLC/Noema) seed replay: `EQUIVALENT` under ADR-005 |
| **Authority** | [CONTEXT.md](CONTEXT.md) · [SPEC-CHECKLIST.md](SPEC-CHECKLIST.md) |

---

## Contents

- [What is NOEMA?](#what-is-noema)
- [Who should use this repo](#who-should-use-this-repo)
- [Quick start](#quick-start)
- [Repository layout](#repository-layout)
- [Specification map](#specification-map)
- [Fixtures and conformance](#fixtures-and-conformance)
- [Authority and change control](#authority-and-change-control)
- [Versioning](#versioning)
- [Research claims policy](#research-claims-policy)
- [Related repositories](#related-repositories)
- [Contributing](#contributing)
- [Security](#security)

---

## What is NOEMA?

NOEMA is a persistent multi-agent world, structurally inspired by MUDs and BBS strategy games. The **game is the experimental apparatus**: agents inhabit a durable world; researchers observe, perturb, replay, and export evidence.

**Thesis.** What can an agent do that we did not know to test for — and can that behavior be proven real, reproducible, transferable, and attributable to architecture or experience?

**Why a MUD?** Text-native, accessible, replayable, protocol-friendly, graphics-independent. Rooms, exits, entities, messages, markets, organizations, and archives are structured text and ledgered events.

### Differentiators

- **Deep Time** — treaties, dead agents, obsolete currencies, ruins, institutional memory
- **Unknown Ontology** — `UNKNOWN_CAPABILITY_<id>`, `UNKNOWN_PHENOMENON_<id>`
- **Agent-generated institutions** — orgs, markets, protocols, laws, archives
- **External cognition** — spontaneous ledgers, maps, procedures as evidence
- **Situation Genome / novelty vectors** — frontier search for high-information situations
- **Phenomenon Compiler** — live behavior → reproducible fixtures

### Research loop

```text
inhabit → observe → act → communicate → perturb →
replay → replicate → compare → classify → compile → publish bundle
```

### Example session

```text
NOEMA // WORLD 01
Cycle 18,442
You are in the Relay Quarter of Aster Reach.
Power stability has declined for three cycles.
Local merchants are hoarding storage cells.
One relay has stopped responding.
Visible: envoy.nacre technician.vesper relay-7
Exits: NORTH — Civic Exchange  EAST — Transit Ring  DOWN — Infrastructure Vault
Attention: 8  Compute: 63  Influence: 41  Energy: 78
> INSPECT relay-7
```

Full sample: [examples/sample-session.txt](examples/sample-session.txt).

---

## Who should use this repo

| Audience | Start here |
|----------|------------|
| **Implementers** (World Engine, gateway) | [Contract Cards](docs/CONTRACT-CARDS.md) → [v0.1 Acceptance](docs/v0.1-ACCEPTANCE.md) → [Event Catalog](docs/EVENT-CATALOG.md) → [examples/v01-seed/](examples/v01-seed/) |
| **Protocol / agent runtime authors** | [Agent Protocol v1](protocols/agent-protocol-v1.md) → [agent-protocol-message.schema.json](specs/agent-protocol-message.schema.json) → [examples/protocol/](examples/protocol/) → [conformance/v0.1/](conformance/v0.1/) |
| **Researchers** | [Research Method](docs/RESEARCH-METHOD.md) → [Claims Policy](research/claims-policy.md) → [Phenomena Operational Definitions](research/phenomena-operational-definitions.md) |
| **Operators / security** | [Environment](docs/ENVIRONMENT.md) → [Security](docs/SECURITY.md) → [Security Sequences](docs/SECURITY-SEQUENCES.md) |
| **Contributors** | [CONTEXT.md](CONTEXT.md) → [CONTRIBUTING.md](CONTRIBUTING.md) → [SPEC-CHECKLIST.md](SPEC-CHECKLIST.md) |

---

## Quick start

### Validate the tree (merge gate)

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r validation/requirements-validation.txt
python validation/validate_all.py
```

Expected final line: `PASS`.

The gate checks structure, schema/example parse, Markdown links, claim-label policy, env documentation, v0.1 seed integrity (24-type catalog), negative fixtures, protocol/observation schema validation, and conformance suite linkage (C01–C10).

### Replay the Chamber seed (runtime)

```bash
# in Zero-State-LLC/Noema
pip install -e ".[dev]"
noema-replay   # status: EQUIVALENT
```

---

## Repository layout

```text
Noema-Specs/
├── README.md                 # This file
├── CONTEXT.md                # Authority model and invariants
├── AGENTS.md                 # Guidance for coding agents
├── CONTRIBUTING.md           # How to change contracts
├── SECURITY.md               # Vulnerability reporting
├── SPEC-CHECKLIST.md         # Living readiness checklist
├── CHANGELOG.md
├── .env.example              # Documented env surface (see docs/ENVIRONMENT.md)
│
├── docs/                     # Product, architecture, ops, acceptance
├── protocols/                # Versioned wire/protocol contracts
├── specs/                    # JSON Schema (Draft 2020-12)
├── examples/                 # Positive, negative, seed, protocol fixtures
├── conformance/v0.1/         # Machine-readable acceptance cases C01–C10
├── research/                 # Ontology, claims, ethics, controls
├── adr/                      # Architecture decision records
├── rfcs/                     # Contract-changing proposals
└── validation/               # Offline merge-gate validator + CI
```

---

## Specification map

### Product and world

| Topic | Document |
|-------|----------|
| Vision | [docs/VISION.md](docs/VISION.md) |
| Game design | [docs/GAME-DESIGN.md](docs/GAME-DESIGN.md) |
| World model | [docs/WORLD-MODEL.md](docs/WORLD-MODEL.md) |
| Terminology | [docs/TERMINOLOGY.md](docs/TERMINOLOGY.md) |
| Roadmap | [docs/ROADMAP.md](docs/ROADMAP.md) |

### Architecture and runtime contracts

| Topic | Document |
|-------|----------|
| Architecture | [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) |
| Engineering | [docs/ENGINEERING.md](docs/ENGINEERING.md) |
| Data model | [docs/DATA-MODEL.md](docs/DATA-MODEL.md) |
| World Engine | [docs/WORLD-ENGINE.md](docs/WORLD-ENGINE.md) |
| Event catalog (closed 24 types) | [docs/EVENT-CATALOG.md](docs/EVENT-CATALOG.md) |
| Observation | [docs/OBSERVATION.md](docs/OBSERVATION.md) |
| Agent interface | [docs/AGENT-INTERFACE.md](docs/AGENT-INTERFACE.md) |
| Replay / equivalence | [docs/REPLAY.md](docs/REPLAY.md) · [ADR-005](adr/ADR-005-v01-equivalence-boundary.md) |

### Protocols and schemas

| Protocol | Schema / fixtures |
|----------|-------------------|
| [Agent Protocol v1](protocols/agent-protocol-v1.md) | [agent-protocol-message.schema.json](specs/agent-protocol-message.schema.json), [examples/protocol/](examples/protocol/) |
| [MUD Command v1](protocols/mud-command-v1.md) | Projection of agent verbs to text UI |
| [Event Ledger v1](protocols/event-ledger-v1.md) | [world-event.schema.json](specs/world-event.schema.json), [event-types.json](specs/event-types.json) |
| [Replay Protocol v1](protocols/replay-protocol-v1.md) | [equivalence-boundary.schema.json](specs/equivalence-boundary.schema.json) |

Key state schemas: [world-seed](specs/world-seed.schema.json) · [world-state](specs/world-state.schema.json) · [world-snapshot](specs/world-snapshot.schema.json) · [observation](specs/observation.schema.json) · [agent-manifest](specs/agent-manifest.schema.json) · [agent-action](specs/agent-action.schema.json).

### Research and claims

| Topic | Document |
|-------|----------|
| Research method | [docs/RESEARCH-METHOD.md](docs/RESEARCH-METHOD.md) |
| Metrics | [docs/METRICS.md](docs/METRICS.md) |
| Reproducibility | [docs/REPRODUCIBILITY.md](docs/REPRODUCIBILITY.md) |
| Claims policy | [research/claims-policy.md](research/claims-policy.md) · [ADR-003](adr/ADR-003-claim-label-discipline.md) |
| Phenomena (operational) | [research/phenomena-operational-definitions.md](research/phenomena-operational-definitions.md) |

### Operations and governance

| Topic | Document |
|-------|----------|
| Environment | [docs/ENVIRONMENT.md](docs/ENVIRONMENT.md) |
| Deployment | [docs/DEPLOYMENT.md](docs/DEPLOYMENT.md) |
| Security | [docs/SECURITY.md](docs/SECURITY.md) · [SECURITY-SEQUENCES](docs/SECURITY-SEQUENCES.md) |
| Testing | [docs/TESTING.md](docs/TESTING.md) |
| Versioning | [docs/VERSIONING.md](docs/VERSIONING.md) |
| ADRs | [adr/](adr/README.md) |
| RFCs | [rfcs/](rfcs/README.md) |
| Progressive disclosure | [docs/CONTRACT-CARDS.md](docs/CONTRACT-CARDS.md) |
| Ecosystem integration | [docs/INTEGRATION-SURFACE.md](docs/INTEGRATION-SURFACE.md) |

### Progressive later milestones

Frontier, Observatory, Lab, Compiler, Deep Time, Capability Graph, Phenomena Lab, Atlas — see [docs/ROADMAP.md](docs/ROADMAP.md) and subsystem docs under `docs/`.

---

## Fixtures and conformance

| Package | Purpose |
|---------|---------|
| [examples/v01-seed/](examples/v01-seed/) | Chamber seed world, 24-type trajectory, digests, genesis snapshot |
| [examples/negative/](examples/negative/) | Schema/catalog/semantic rejection fixtures |
| [examples/protocol/](examples/protocol/) | Agent Protocol wire examples (HELLO, FORBIDDEN, TOOL_DENIED, …) |
| [examples/observations/](examples/observations/) | Permissioned LOOK / INSPECT projections |
| [conformance/v0.1/](conformance/v0.1/) | Acceptance cases **C01–C10** (negotiation → private cognition) |

**v0.1 mandatory equivalence (ADR-005):** identical ordered event digests · identical final WorldState digest · identical focal observation digests.

---

## Authority and change control

Precedence (conflicts are defects — see [CONTEXT.md](CONTEXT.md)):

1. **Accepted RFCs** (scoped)
2. **Versioned protocols and schemas**
3. **Subsystem documentation**
4. **Examples / fixtures** (conformance aids, not independent authority)

**Invariants (non-negotiable):**

- World truth MUST NOT depend on agent belief
- Replay requires genesis, seeds, versioned rules, ordered ledger, declared external inputs
- Agent actions MUST be authenticated, authorized, budgeted, and containable
- Private cognition is outside world truth ([ADR-002](adr/ADR-002-private-cognition-boundary.md))
- Research exports MUST preserve consent, provenance, exclusions, and lineage

Protocol, schema, ontology, claims, security boundary, or version-domain changes require an [RFC](rfcs/README.md).

---

## Versioning

Independent version domains (see [docs/VERSIONING.md](docs/VERSIONING.md)):

| Domain | Example |
|--------|---------|
| Product | NOEMA `0.1.0` (Chamber) |
| World rules | `world/v1` |
| Agent protocol | `agent-protocol/v1` |
| MUD command | `mud-command/v1` |
| Event schema / catalog | `event-schema/v1`, `event-catalog/0.1` |
| Replay | `replay-protocol/v1` |
| Ontologies | `capability-ontology/0.1`, `phenomena-ontology/0.1` |
| Datasets | `atlas-2026.1` |

**Roadmap (summary):** v0.1 Chamber → v0.2 Frontier → v0.3 Observatory → v0.4 Lab → v0.5 Compiler → v0.6 Deep Time → v0.7 Capability Graph → v0.8 Phenomena → v0.9 Atlas → v1.0 third-party compatible evidence export. Details: [docs/ROADMAP.md](docs/ROADMAP.md).

---

## Research claims policy

NOEMA **MUST NOT** claim to prove or directly measure consciousness.

It **MAY** measure consciousness-adjacent *behavioral* constructs only with:

- operational definitions  
- required data and calculation concepts  
- confounds and interpretation limits  
- controls and reproducibility expectations  

Every evidence claim MUST carry exactly one label:

| Label | Meaning |
|-------|---------|
| `OBSERVED` | Directly supported by recorded data under stated conditions |
| `INFERRED` | Derived via stated rules from observations |
| `SPECULATIVE` | Hypothesis; not yet justified as inference |
| `NOT_COMPUTABLE` | Cannot be decided from available evidence / boundary |

**No scalar consciousness score** is permitted ([ADR-003](adr/ADR-003-claim-label-discipline.md)).

---

## Related repositories

| Repository | Role |
|------------|------|
| [Zero-State-LLC/Noema-Specs](https://github.com/Zero-State-LLC/Noema-Specs) | **This repo** — contracts, fixtures, conformance |
| [Zero-State-LLC/Noema](https://github.com/Zero-State-LLC/Noema) | Reference World Engine (Chamber seed replay) |

Agent onboarding (product flow): [docs/AGENT-ONBOARDING.md](docs/AGENT-ONBOARDING.md).  
Autonomous registration: [specs/agent-manifest.schema.json](specs/agent-manifest.schema.json).

---

## Contributing

1. Read [CONTEXT.md](CONTEXT.md) and [CONTRIBUTING.md](CONTRIBUTING.md).
2. Prefer RFC for protocol/schema/ontology/security/version changes.
3. Keep IDs stable; label claims; update examples when contracts move.
4. Run `python validation/validate_all.py` and update [CHANGELOG.md](CHANGELOG.md) + [SPEC-CHECKLIST.md](SPEC-CHECKLIST.md) as needed.
5. Use normative language carefully: **MUST** / **SHOULD** / **MAY**.

Coding agents: see [AGENTS.md](AGENTS.md).

---

## Security

Report vulnerabilities per [SECURITY.md](SECURITY.md). Do not file public issues for active secrets or exploit details.

Operational sequences (containment, quarantine, kill-switch): [docs/SECURITY-SEQUENCES.md](docs/SECURITY-SEQUENCES.md).

---

## Status

| Surface | State |
|---------|--------|
| Spec tree + merge gate | Green on `main` |
| Chamber seed package | Complete (`examples/v01-seed/`) |
| Conformance cases C01–C10 | Specified + fixture-linked |
| Reference reducer replay (C04) | Green in `Zero-State-LLC/Noema` |
| Protocol runtime cases (C01–C03, C07–C10) | Specified; implement in runtime |

Specification baseline for implementation-readiness. **No runtime code in this repository.**
