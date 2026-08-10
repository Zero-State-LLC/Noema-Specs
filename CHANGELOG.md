# Changelog

## [Unreleased]

### Added

- Executable world/game contracts: `docs/MODULE-CONTRACTS.md`, `docs/RESOURCE-ECONOMY.md`, `docs/ACTION-CONTRACTS.md`, `docs/SCHEDULER.md`, `docs/SPECTATOR.md`.
- Machine-readable: `module-contracts.v01.json`, `resource-economy.v01.json`, `action-contracts.v01.json`, `id-rules.v01.json`, spectator-projection + module-contracts schemas.
- Strategic fixture package `examples/v01-strategic/` (4-agent coupled scenario).
- Conformance families **C18–C26** (resource, production, trade, org, infrastructure, scheduler, director, spectator, strategic persistence).
- Onboarding/deployment golden path docs: `docs/QUICKSTART.md`, `docs/OPERATIONS.md`, `docs/SPECTATOR-ONBOARDING.md`.
- Schemas: `runtime-manifest.schema.json`, `deployment-config.schema.json`.
- Fixtures: `examples/onboarding/`, `examples/deployment/`.
- Conformance families **C11–C17** (human/agent/spectator onboarding, reference deployment, restart persistence, backup/restore, version pinning).
- v0.1 Chamber **conformance suite** (`conformance/v0.1/`, docs/v0.1-CONFORMANCE.md) covering acceptance items C01–C17 (C01–C10 retained).
- Schemas: `world-state`, `world-seed`, `world-snapshot`, `equivalence-boundary`, `agent-protocol-message`, `conformance-case`.
- Protocol wire fixtures (`examples/protocol/`) and observation positives (`examples/observations/`).
- Genesis snapshot example for seed load (`examples/v01-seed/genesis-snapshot.json`).
- Expanded `protocols/agent-protocol-v1.md` with ACT→event mapping, error codes, resume, sandbox, and private cognition rules.
- Canonical NOEMA persistent MUD multi-agent specification baseline.
- Exact required protocol documents for MUD commands, agent protocol, event ledger, and replay.
- Ten requested Draft 2020-12 JSON Schema files and matching examples.
- Lowercase research ontology, controls, claims, and ethics files.
- RFC README and template for contract-changing decisions.
- `validation/` merge-gate suite (structure, JSON parse, link check, claim-label scan).
- `adr/` directory with five foundational ADRs (determinism, private cognition, claim labels, world-truth isolation, v0.1 equivalence boundary).
- `docs/SECURITY-SEQUENCES.md` — concrete containment, quarantine, revocation, incident, kill-switch, and undelivered-observation sequences.
- `docs/v0.1-ACCEPTANCE.md` — operational acceptance criteria and minimum conformance tests for The Chamber.
- `docs/CONTRACT-CARDS.md` — progressive-disclosure summaries of major contracts.
- `docs/INTEGRATION-SURFACE.md` — explicit extension points for Zero State / Abraxas ecosystem consumers.
- `research/phenomena-operational-definitions.md` — operational definitions, required data, confounds, and limits for the five high-signal constructs.
- `examples/negative/` — invalid fixtures for schema, catalog, and semantic rejection testing.
- `examples/v01-seed/` — concrete Chamber seed: world genesis, full 24-type trajectory, equivalence boundary, and expected digests.
- `.github/workflows/spec-validation.yml` — CI validation gate.

### Changed

- Expanded `docs/GAME-DESIGN.md`, `docs/DATA-MODEL.md`, `docs/WORLD-MODEL.md`, `docs/ENGINEERING.md` for Chamber strategic ecology and executable transitions.
- Extended acceptance/conformance/testing/roadmap to C01–C26; world-state schema optional infrastructure/resource_nodes fields.
- Clarified verb scope: v0.1 REQUIRED vs OPTIONAL vs LATER (GAME-DESIGN, ACTION-CONTRACTS, mud-command).
- Rewrote `docs/AGENT-ONBOARDING.md` for minimal HELLO→ACT path; advanced/research registration is secondary.
- Rewrote `docs/DEPLOYMENT.md` with normative modular-monolith reference architecture and explicit non-requirements.
- Reorganized `docs/ENVIRONMENT.md` and `.env.example` into Core / Advanced / Research / Providers / Optional scaling; local boot without Redis/Sentry/OTEL/external object storage/provider keys.
- Extended `docs/v0.1-ACCEPTANCE.md`, `docs/ROADMAP.md`, `docs/TESTING.md`, `README.md` for PLAY/WATCH/CONNECT AGENT and ops surface.
- Relaxed `agent-manifest.schema.json` required fields to minimal identity + protocol (compatible with full advanced manifests).
- Reframed all core docs from an agent-centered research-apparatus baseline to the requested autonomous-agent research apparatus.
- Reinforced claim-label and consciousness-score policy through ADR-003 and operational definitions.
- Made v0.1 equivalence boundary explicit and mandatory via ADR-005.
- Strengthened `validation/validate_all.py` to enforce structure, env docs, seed catalog coverage, digest chain, and negative corpus rejection.

### Removed

- Thought-centric protocol, schema, and example artifacts that were inconsistent with NOEMA.

### Notes

- Spec checklist structure, contract quality, tree validation, and CI on `main` are green.
- Specs release candidate tagged `v0.1.0-rc1`.
- Independent World Engine Chamber replay is implemented in `Zero-State-LLC/Noema` and matches `examples/v01-seed/` digests (`EQUIVALENT`).
