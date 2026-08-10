# Specification Checklist

## Required structure

- [x] Root files exist: `README.md`, `CONTEXT.md`, `AGENTS.md`, `CONTRIBUTING.md`, `SECURITY.md`, `CHANGELOG.md`, `.env.example`.
- [x] Required docs including QUICKSTART, OPERATIONS, SPECTATOR-ONBOARDING, MODULE-CONTRACTS, RESOURCE-ECONOMY, ACTION-CONTRACTS, SCHEDULER, SPECTATOR.
- [x] Required protocol files exist and define machine-readable semantics.
- [x] JSON Schemas in `specs/` including runtime-manifest, deployment-config, module-contracts, spectator-projection, resource/action/id contracts.
- [x] Required research files, examples (v01-seed, v01-strategic, onboarding, deployment, negative, protocol).
- [x] RFCs, ADRs, validation entrypoint, v0.1 acceptance/conformance.

## Contract quality

- [x] Persistent MUD/BBS/multi-agent/Deep Time represented.
- [x] Unknown Ontology, institutions, external cognition, Situation Genome.
- [x] Claim labels OBSERVED/INFERRED/SPECULATIVE/NOT_COMPUTABLE; no scalar consciousness score.
- [x] ADRs 001–005 present.
- [x] PLAY/CONNECT AGENT/WATCH entry model; modular-monolith deployment; persistence invariant.
- [x] Executable Chamber economy, actions, scheduler, infrastructure, orgs, trade, spectator projections.
- [x] C01–C26 conformance families.

## Validation

- [x] `python validation/validate_all.py` PASS.
- [x] Markdown links resolve; env vars documented; seed 24-type catalog.
- [x] Conformance 26 cases linked; strategic package schema-valid.
- [x] C01–C17 not removed.

## Notes

Specs pin: `v0.1.0-rc2+`. Runtime must still implement protocol/onboarding/economy cases for full product Chamber claims. Seed reducer C04 green in `Zero-State-LLC/Noema`.
