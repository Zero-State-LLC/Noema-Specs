# Specification Checklist

## Required structure

- [ ] Root files exist: `README.md`, `CONTEXT.md`, `AGENTS.md`, `CONTRIBUTING.md`, `SECURITY.md`, `CHANGELOG.md`, `.env.example`.
- [ ] All required `docs/*.md` files exist.
- [ ] Required protocol files exist and define machine-readable semantics.
- [ ] Exactly requested JSON Schema filenames exist in `specs/`.
- [ ] Required lowercase research files exist.
- [ ] Required examples exist.
- [ ] `rfcs/README.md` and `rfcs/RFC-0000-template.md` exist.
- [x] ADR directory and index present (`adr/README.md` + ADR-001 through ADR-005).
- [x] Validation entrypoint present (`validation/validate_all.py`).
- [x] Security sequences documented (`docs/SECURITY-SEQUENCES.md`).
- [x] v0.1 acceptance criteria documented (`docs/v0.1-ACCEPTANCE.md`).
- [x] Contract cards for progressive disclosure (`docs/CONTRACT-CARDS.md`).
- [x] Operational definitions for key phenomena constructs (`research/phenomena-operational-definitions.md`).
- [x] Integration surface note for ecosystem consumers (`docs/INTEGRATION-SURFACE.md`).
- [x] Negative example fixtures started (`examples/negative/`).

## Contract quality

- [ ] Persistent MUD, BBS strategy, multi-agent, and Deep Time concepts are represented.
- [ ] Unknown Ontology remains valid.
- [ ] Agent-generated institutions and external cognition are specified.
- [ ] Situation Genome and novelty vector are machine-readable.
- [ ] Emergent capability labeling requires replication, perturbation, transfer, and counterfactual evidence.
- [ ] No scalar consciousness score is introduced.
- [ ] Claim labels are consistently OBSERVED, INFERRED, SPECULATIVE, and NOT_COMPUTABLE.
- [x] Determinism and seeded nondeterminism decision recorded (ADR-001).
- [x] Private cognition boundary decision recorded (ADR-002).
- [x] Claim-label discipline decision recorded (ADR-003).
- [x] World-truth isolation decision recorded (ADR-004).
- [x] v0.1 equivalence boundary profile fixed (ADR-005).

## Validation

- [ ] JSON schemas parse as JSON.
- [ ] JSON examples parse as JSON or JSONL.
- [ ] Internal Markdown links resolve.
- [ ] Environment variables in `.env.example` are documented in `docs/ENVIRONMENT.md`.
- [ ] `git diff --check` passes.
- [ ] Full validation suite green on CI.
- [ ] Minimum seed world + sample trajectory that exercises the closed event catalog.
- [ ] Expanded negative test corpus.
