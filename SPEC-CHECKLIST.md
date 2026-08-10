# Specification Checklist

## Required structure

- [x] Root files, protocols, research, ADRs, validation entrypoint.
- [x] v0.1 Chamber: C01–C26, golden path, executable world contracts.
- [x] v0.2 Frontier: F01–F15, release package, genome/novelty/mutation contracts.
- [x] v0.3 Observatory: release package, trajectory/features/baselines/detectors/candidates, audit, fixtures, O01–O16.
- [x] v0.4 Lab: release package, experiment/intervention/fork/run/result schemas, catalogs, fixtures, L01–L16.

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

## v0.4 Lab

- [x] Experimental fork isolation (`mutates_production: false`)
- [x] Intervention taxonomy + perturbation/ablation catalogs
- [x] Controls including sham; failed/null results first-class
- [x] Lifecycle without PROVEN; claim labels separate
- [x] Lab → Compiler boundary (`compiler_readiness`)
- [x] Conformance L01–L16 + validator gate

## Validation

- [x] `python validation/validate_all.py` PASS.
- [x] C01–C26, F01–F15, O01–O16, S01–S18, L01–L16 present and linked.

## Notes

Product pins: Chamber 0.1.x (`event-catalog/0.1`), strategic conflict additive 0.2 catalog, Frontier 0.2.x, Observatory 0.3.0-draft, Lab 0.4.0-draft. Runtime Lab engine outstanding in the Noema repo.
