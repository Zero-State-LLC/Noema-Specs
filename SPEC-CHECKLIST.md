# Specification Checklist

## Required structure

- [x] Root files, protocols, research, ADRs, validation entrypoint.
- [x] v0.1 Chamber: C01–C26, golden path, executable world contracts.
- [x] v0.2 Frontier: F01–F15, release package, genome/novelty/mutation contracts.
- [x] v0.3 Observatory: release package, trajectory/features/baselines/detectors/candidates, audit, fixtures, O01–O16.

## Core game design (player-facing)

- [x] Core game loop (primary + strategic overlay + timescales)
- [x] Realms as derived projections
- [x] Geography hierarchy and strategic room purpose
- [x] Emergent territory control
- [x] Crime as consequence layer; strategic contestation scoped as next milestone
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
- [x] RFC-0002 draft skeleton for contestation/crime/agreement events

## Contract quality

- [x] World truth isolation for Observatory.
- [x] Deterministic claim-bearing analysis path.
- [x] Unknown candidates need not map to existing primitives.
- [x] Research metrics redacted from ordinary spectators.
- [x] No consciousness / scalar intelligence scores.

## Validation

- [x] `python validation/validate_all.py` PASS.
- [x] C01–C26, F01–F15, O01–O16 present and linked.

## Notes

Product pins: Chamber 0.1.x, Frontier 0.2.x, Observatory 0.3.0-draft. Runtime implementation of O-suite outstanding.
