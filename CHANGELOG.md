# Changelog

## [Unreleased]

### Added

- **v0.4 Lab executable package:** `docs/releases/v0.4/*`, experiment/intervention/plan/run/fork/lab-result/audit schemas, perturbation + ablation catalogs, variable registry, full Lab docs (identity, lifecycle, design, controls, fork, counterfactual, outcomes, replication, isolation, audit, lesions, determinism), fixtures `examples/v04-lab/`, conformance **L01–L16**.
- Validator Lab gate: schema fixtures, production isolation negatives, null results retained.

### Changed

- ROADMAP/README/VERSIONING/SPEC-CHECKLIST/EXPERIMENT-LAB for executable Lab scope.

### Added

- **RFC-0002 Accepted** — strategic conflict executable contracts (`event-catalog/0.2`).
- `specs/event-types.0.2.json` (31 types), `contest-config.v02.json` + schema, `action-contracts.v02.json`.
- Docs: CONTEST-RESOLUTION, STRATEGIC-EVENT-COUPLING, strategic conflict acceptance/conformance/migration.
- Fixtures: `examples/v02-strategic-conflict/` (trajectory, resolution, spectator, report, Observatory features, negatives).
- Conformance: `conformance/v0.2-strategic/` families **S01–S18**.
- Validator gate for catalog isolation, resolution arithmetic, S-suite.

### Changed

- EVENT-CATALOG documents 0.1 vs 0.2; ACTION-CONTRACTS, SPECTATOR, DIPLOMACY, BEHAVIOR-FEATURES, VERSIONING, SPEC-CHECKLIST, README.

### Added

- RFC-0002 expanded to full Draft: payload sketches, reducer preconditions, coupling, observability, worked sequence for seven contestation/crime/agreement events.
- `examples/chamber-world/start-distributions.json` — ENTER_WORLD assignment profiles.
- Chamber seed route pressure: `traversal_cost` on edge/vault routes, edge condition tags; richer `map_design` (starts, chokepoints, scarcity).

### Changed

- SPEC-CHECKLIST / README / EVENT-CATALOG-AUDIT / STRATEGIC-CONFLICT / rfcs index for RFC-0002 payload-draft status and chamber-world depth.

### Added

- `examples/chamber-world/` — canonical 10-room Chamber starting map + `world-seed.json`.
- `rfcs/RFC-0002-strategic-contestation-and-crime-events.md` (Draft skeleton).
- GAME-DESIGN completed spine table linking all player-facing game docs.

### Changed

- CHAMBER-MAP / STARTING-CONDITIONS point at chamber-world product map (v01-seed remains ADR-005 fixture).

### Added

- `docs/STARTING-CONDITIONS.md`, `docs/GAME-SYSTEM-DEPENDENCY.md`.
- Expanded EXPLORATION, STRATEGIC-KNOWLEDGE, INFRASTRUCTURE, SPECTATOR (primary surfaces + high-drama events).
- EVENT-CATALOG-AUDIT: `AGREEMENT_FORMED` / `AGREEMENT_BROKEN` as v0.2 RFC candidates.

### Changed

- GAME-SYSTEM-MAP cross-links and indexes for completed core game design.

### Added

- **Core game design completion package:** LOSS-RECOVERY, DIPLOMACY, GAME-CYCLE, WORLD-REPORTS, PROGRESSION, AMBITIONS, HUMAN-PLAY, AGENT-PLAY, GAME-BALANCE, EXPLORATION, STRATEGIC-KNOWLEDGE, INFRASTRUCTURE (progression), FIRST-20-CYCLES, CHAMBER-MAP, GAME-SYSTEM-MAP, EVENT-CATALOG-AUDIT.
- Expanded STRATEGIC-CONFLICT with full crime + contestation forms, defense, RFC event list.

### Changed

- GAME-DESIGN contracts map, TERMINOLOGY, ROADMAP, README, SPEC-CHECKLIST for full player-facing design index.

### Added

- **Core game design foundation:** `docs/CORE-GAME-LOOP.md`, `docs/REALMS.md`, `docs/GEOGRAPHY.md`, `docs/TERRITORY-CONTROL.md`, `docs/STRATEGIC-CONFLICT.md` (crime consequence layer; strategic P2P contestation as next milestone; no closed-catalog event expansion without RFC).

### Changed

- Linked GAME-DESIGN, TERMINOLOGY, SPECTATOR, ROADMAP, README to core game design docs.

### Added

- **v0.3 Observatory executable package:** `docs/releases/v0.3/*`, trajectory/0.3, behavior features, context normalization, baselines, anomaly/shift/capability/unknown candidates, agent-version comparison, external cognition & coordination signals, analysis-run + audit schemas, `examples/v03-observatory/`, conformance **O01–O16** (96 cases).
- Docs: TRAJECTORY, BEHAVIOR-FEATURES, CONTEXT-NORMALIZATION, BASELINES, ANOMALY-DETECTION, BEHAVIOR-SHIFT, AGENT-VERSION-COMPARISON, CAPABILITY-CANDIDATES, CONTRADICTION-ANALYSIS, EXTERNAL-COGNITION, COORDINATION-SIGNALS, EMERGENCE-CANDIDATES, OBSERVATORY-AUDIT; expanded OBSERVATORY.md.

### Changed

- Roadmap/README/VERSIONING/MODULE-CONTRACTS/SPECTATOR/TESTING for Observatory executable scope.

### Added

- **v0.2 Frontier executable package:** `docs/releases/v0.2/*`, Situation Genome 0.2, novelty axes, mutation catalog, noise/attention/info-gain configs, capability primitives, Frontier request/plan/candidate/audit/replay schemas.
- Docs: SITUATION-GENOME, NOVELTY-VECTOR, CAPABILITY-PRIMITIVES, SITUATION-MUTATION, PARTIAL-OBSERVABILITY, NOISE-MODEL, CONTRADICTORY-EVIDENCE, ATTENTION-PROJECTION, INFORMATION-GAIN, FRONTIER-CONTROLS.
- Fixtures: `examples/v02-frontier/` end-to-end deterministic Frontier scenario.
- Conformance: `conformance/v0.2/` families **F01–F15** (76 atomic cases).
- Hardened `FRONTIER-DIRECTOR.md` cross-links to versioned configs; spectator Frontier projections; migration/version domains.

### Changed

- Roadmap/README/VERSIONING/MODULE-CONTRACTS/SPECTATOR updated for v0.2 Frontier executable scope.
- Conformance-case schema: acceptance_items max 200; family_id; frontier-director actor.

### Added (prior)

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

## Unreleased

- Expanded v0.4 Lab into a machine-checkable experimental contract: immutable identity, isolated forks, explicit intervention/control/replication rules, audit chain, catalogs, fixtures, and L01–L22 conformance.

## Unreleased

- Added the PLAY / WATCH / STUDY experience layer, progressive disclosure contracts, deterministic experiment-intent templates, error translations, and audience fixtures.
