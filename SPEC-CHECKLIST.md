# Specification Checklist

## Required structure

- [x] Root files exist: `README.md`, `CONTEXT.md`, `AGENTS.md`, `CONTRIBUTING.md`, `SECURITY.md`, `CHANGELOG.md`, `.env.example`.
- [x] All required `docs/*.md` files exist.
- [x] Required protocol files exist and define machine-readable semantics.
- [x] Exactly requested JSON Schema filenames exist in `specs/`.
- [x] Required lowercase research files exist.
- [x] Required examples exist.
- [x] `rfcs/README.md` and `rfcs/RFC-0000-template.md` exist.
- [x] ADR directory and index present (`adr/README.md` + ADR-001 through ADR-005).
- [x] Validation entrypoint present (`validation/validate_all.py`).
- [x] Security sequences documented (`docs/SECURITY-SEQUENCES.md`).
- [x] v0.1 acceptance criteria documented (`docs/v0.1-ACCEPTANCE.md`).
- [x] Contract cards for progressive disclosure (`docs/CONTRACT-CARDS.md`).
- [x] Operational definitions for key phenomena constructs (`research/phenomena-operational-definitions.md`).
- [x] Integration surface note for ecosystem consumers (`docs/INTEGRATION-SURFACE.md`).
- [x] Negative example fixtures started (`examples/negative/`).

## Contract quality

- [x] Persistent MUD, BBS strategy, multi-agent, and Deep Time concepts are represented.
- [x] Unknown Ontology remains valid.
- [x] Agent-generated institutions and external cognition are specified.
- [x] Situation Genome and novelty vector are machine-readable.
- [x] Emergent capability labeling requires replication, perturbation, transfer, and counterfactual evidence.
- [x] No scalar consciousness score is introduced.
- [x] Claim labels are consistently OBSERVED, INFERRED, SPECULATIVE, and NOT_COMPUTABLE.
- [x] Determinism and seeded nondeterminism decision recorded (ADR-001).
- [x] Private cognition boundary decision recorded (ADR-002).
- [x] Claim-label discipline decision recorded (ADR-003).
- [x] World-truth isolation decision recorded (ADR-004).
- [x] v0.1 equivalence boundary profile fixed (ADR-005).

## Validation

- [x] JSON schemas parse as JSON.
- [x] JSON examples parse as JSON or JSONL.
- [x] Internal Markdown links resolve.
- [x] Environment variables in `.env.example` are documented in `docs/ENVIRONMENT.md`.
- [x] `git diff --check` passes (enforced at commit time).
- [x] Full validation suite green locally (`python validation/validate_all.py`).
- [x] Minimum seed world + sample trajectory that exercises the closed event catalog (`examples/v01-seed/`).
- [x] Expanded negative test corpus (`examples/negative/`, ≥6 fixtures).
- [x] CI gate green on `main` after push (`.github/workflows/spec-validation.yml`).
- [x] Independent World Engine implementation replay matches fixture digests ([Zero-State-LLC/Noema](https://github.com/Zero-State-LLC/Noema) `noema-replay`, specs pin `v0.1.0-rc1`).

## Notes

Checked items are enforced by `validation/validate_all.py`, GitHub Actions, the Noema runtime Chamber replay, and/or inspection of the committed tree. Specs release candidate: `v0.1.0-rc1`. Final `0.1.0` may follow after broader operator/protocol surface coverage beyond seed replay.
