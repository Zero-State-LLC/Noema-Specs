# Specification Checklist

## Required structure

- [ ] Root files exist: `README.md`, `CONTEXT.md`, `AGENTS.md`, `CONTRIBUTING.md`, `SECURITY.md`, `CHANGELOG.md`, `.env.example`.
- [ ] All required `docs/*.md` files exist.
- [ ] Required protocol files exist and define machine-readable semantics.
- [ ] Exactly requested JSON Schema filenames exist in `specs/`.
- [ ] Required lowercase research files exist.
- [ ] Required examples exist.
- [ ] `rfcs/README.md` and `rfcs/RFC-0000-template.md` exist.

## Contract quality

- [ ] Persistent MUD, BBS strategy, multi-agent, and Deep Time concepts are represented.
- [ ] Unknown Ontology remains valid.
- [ ] Agent-generated institutions and external cognition are specified.
- [ ] Situation Genome and novelty vector are machine-readable.
- [ ] Emergent capability labeling requires replication, perturbation, transfer, and counterfactual evidence.
- [ ] No scalar consciousness score is introduced.
- [ ] Claim labels are consistently OBSERVED, INFERRED, SPECULATIVE, and NOT_COMPUTABLE.

## Validation

- [ ] JSON schemas parse as JSON.
- [ ] JSON examples parse as JSON or JSONL.
- [ ] Internal Markdown links resolve.
- [ ] Environment variables in `.env.example` are documented in `docs/ENVIRONMENT.md`.
- [ ] `git diff --check` passes.
