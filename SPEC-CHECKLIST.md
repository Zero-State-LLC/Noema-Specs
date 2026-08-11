# Specification Checklist

## Required structure

- [x] Root files, protocols, research, ADRs, validation entrypoint.
- [x] v0.1 Chamber: C01–C26, golden path, executable world contracts.
- [x] v0.2 Frontier: F01–F15, release package, genome/novelty/mutation contracts.
- [x] v0.3 Observatory: release package, trajectory/features/baselines/detectors/candidates, audit, fixtures, O01–O16.
- [x] v0.4 Lab: release package, experiment/intervention/fork/run/result schemas, catalogs, fixtures, L01–L34 (146 atomic cases), including deterministic intent compilation, simple result projection, and CAPTURE gating.
- [x] v0.5 Compiler: release package, capture intent/compilation/oracle/captured-test/receipt/audit/regression schemas, defaults + status catalogs, fixtures, P01–P30 (90 atomic cases), STUDY progressive disclosure.

## Core game design (player-facing)

- [x] Core game loop (primary + strategic overlay + timescales)
- [x] Realms as derived projections
- [x] Geography hierarchy and strategic room purpose
- [x] Emergent territory control
- [x] Crime as consequence layer; strategic contestation **executable** (RFC-0002 Accepted)
- [x] Loss/recovery, diplomacy, game cycle, world reports
- [x] Plural progression + ambitions (no single victory score)
- [x] Human play / agent play orientation
- [x] Balance principles, exploration, strategic knowledge, infrastructure progression
- [x] First-20-cycles pacing + Chamber map guidance + system dependency map
- [x] Event catalog audit notes for contestation RFC events (incl. AGREEMENT_*)
- [x] Expanded exploration, strategic knowledge, infrastructure progression
- [x] Spectator LIVE/WORLD REPORT/REALM/HISTORY surfaces + high-drama events
- [x] Starting conditions + system dependency chain
- [x] Canonical chamber-world 10-room map seed
- [x] GAME-DESIGN spine table for completed game design

## RFC-0002 / event-catalog/0.2 (strategic conflict)

- [x] RFC-0002 **Accepted**
- [x] `specs/event-types.0.2.json` (31 types = 24 + 7)
- [x] Seven event payload schemas (`$defs`, additionalProperties false)
- [x] `specs/contest-config.v02.json` + schema (integer millipoints)
- [x] `docs/CONTEST-RESOLUTION.md` deterministic algorithm
- [x] Defense model (passive + CONTEST_DEFEND reservation)
- [x] `docs/STRATEGIC-EVENT-COUPLING.md`
- [x] Action contracts v0.2 (`action-contracts.v02.json` + docs)
- [x] Positive fixtures + multi-agent trajectory
- [x] Negative fixtures (schema + catalog isolation)
- [x] Conformance S01–S18
- [x] Spectator / world-report / Observatory feature mappings
- [x] Migration 0.1 → 0.2
- [x] Catalog isolation: 0.1 rejects 0.2 types
- [x] Validator strategic gate PASS

## Contract quality

- [x] World truth isolation for Observatory.
- [x] Deterministic claim-bearing analysis path.
- [x] Unknown candidates need not map to existing primitives.
- [x] Research metrics redacted from ordinary spectators.
- [x] No consciousness / scalar intelligence scores.
- [x] RFC-0003 canonical action order is independent of network arrival.
- [x] Same-cycle message delivery commits before observation projection.
- [x] `noema-jcs/1` canonicalization and integer fixed-point canonical quantities.
- [x] Typed AgentAction IDs and monotonic `client_action_sequence` enforced.
- [x] Catalog-specific closed ledger-admission schemas with negative fixtures.
- [x] Canonical WorldState lineage and ledger-head fields enforced.
- [x] One fenced writer plus atomic `SERIALIZABLE` cycle transaction contract.
- [x] Scoped cumulative resume acknowledgements and bounded redelivery.
- [x] Signed evidence receipts required for research/evidence export profiles.

## v0.4 Lab

- [x] Experimental fork isolation (`mutates_production: false`)
- [x] Intervention taxonomy + perturbation/ablation catalogs
- [x] Controls including sham; failed/null results first-class
- [x] Lifecycle without PROVEN; claim labels separate
- [x] Lab → Compiler boundary (`compiler_readiness`)
- [x] Conformance L01–L22 + validator gate

## Validation

- [x] `python validation/validate_all.py` PASS.
- [x] C01–C26, F01–F15, O01–O16, S01–S18, L01–L34, P01–P30 present and linked.
- [x] RFC-0003 cross-document architecture hardening gate PASS.
- [x] Compiler v0.5 validator gate PASS.

## Notes

Product pins: Chamber 0.1.x (`event-catalog/0.1`), strategic conflict additive 0.2 catalog, Frontier 0.2.x, Observatory 0.3.0-draft, Lab 0.4.0-draft, Compiler 0.5.0-draft. Runtime Lab/Compiler engines outstanding in the Noema repo.

## v0.5 Compiler

- [x] Usability invariant: machine precision without ordinary conceptual burden
- [x] CAPTURE AS TEST → capture-intent → compilation-request (deterministic defaults)
- [x] Eligibility: `compiler_readiness == READY` + admission gates
- [x] Dependency-closed hierarchical ddmin pinned; over-minimization guard
- [x] Behavioral oracle + signature; minimality statuses bounded
- [x] Captured-test package; compile receipt; audit hash chain
- [x] Simple/advanced/reproducibility same artifact identity
- [x] Regression results without global ranking
- [x] RFC-0003 canonicalization/receipt reuse; no runtime implementation

## Experience simplification and progressive disclosure

- [x] Canonical PLAY → NOTICE → TEST → CAPTURE → LEARN model and internal mapping.
- [x] PLAY / WATCH / STUDY audience paths with text-first equivalents.
- [x] Ordinary flows do not require internal subsystem terminology.
- [x] Advanced and reproducibility detail remains accessible.
- [x] Versioned intent and error translations remain machine-authoritative.
- [x] Player and public WATCH views do not leak hidden research metadata.
- [x] Experience fixtures and validation coverage exist.
