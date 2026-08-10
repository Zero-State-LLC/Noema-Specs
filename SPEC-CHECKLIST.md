# Specification Checklist

## Required structure

- [x] Root files, protocols, research, ADRs, validation entrypoint.
- [x] v0.1 onboarding/deployment docs and C01–C26.
- [x] v0.1 executable world contracts (modules, resources, actions, scheduler, spectator, strategic fixtures).
- [x] v0.2 release package under `docs/releases/v0.2/`.
- [x] Frontier executable docs: Situation Genome, Novelty, Mutations, Partial Observability, Noise, Contradiction, Attention, Information-Gain, Controls, Capability Primitives.
- [x] Frontier schemas/config catalogs and `examples/v02-frontier/`.
- [x] Conformance `conformance/v0.2/` families F01–F15 (≥75 atomic cases).

## Contract quality

- [x] World truth / research separation; no consciousness score.
- [x] Deterministic replay; fixed-point Frontier scores; no opaque claim-bearing selector.
- [x] Frontier cannot directly mutate WorldState; injection via `SITUATION_INJECTED`.
- [x] Player/spectator research-target redaction.
- [x] v0.1 behavior preserved.

## Validation

- [x] `python validation/validate_all.py` PASS.
- [x] Markdown links resolve; negatives reject; fixtures validate.

## Notes

Product pins: Chamber `0.1.x`, Frontier `0.2.0-draft`. Runtime implementation of F-suite remains outstanding.
