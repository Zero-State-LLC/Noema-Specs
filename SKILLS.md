# NOEMA Specification Workflows

Skills are repeatable workflows. They do not create new authority.

| File | Responsibility |
|---|---|
| [CONTEXT.md](CONTEXT.md) | NOEMA purpose, authority, and non-negotiable invariants |
| [AGENTS.md](AGENTS.md) | behavioral constraints for agents in this repository |
| [CONTRIBUTING.md](CONTRIBUTING.md) | contribution policy and normative requirement language |
| [SPEC-CHECKLIST.md](SPEC-CHECKLIST.md) | completion and checking requirements |
| `SKILLS.md` | deterministic procedures for recurring specification work |

Resolve authority in this order: **Accepted RFC → versioned protocol/schema → canonical subsystem documentation → release package → conformance → examples/fixtures**. This is the precedence in `CONTEXT.md`. A conflict is a **SPEC DEFECT**. Do not silently select a side.

## SKILL.ORIENT
**Use when** Starting any substantive task.
**Inputs** Requested change and repository state.
**Authority to read** `CONTEXT.md`, `AGENTS.md`, `docs/TERMINOLOGY.md`, affected docs/RFCs/schemas, `docs/ROADMAP.md`.
**Procedure**
1. Read `CONTEXT.md`, `AGENTS.md`, affected terminology, and `git status`.
2. Identify the roadmap milestone, affected version domains, and canonical authority hierarchy.
3. Inspect related protocols, schemas, fixtures, conformance, validation, and open branch/PR state if tooling supports it.
4. Decide whether the request changes a contract or only documentation.
**Outputs** Task scope, authoritative files, affected version domains, RFC required yes/no, known drift, validation targets.
**Validation** Confirm every cited authority exists.
**Stop / escalate when** Authority conflicts or required evidence is missing. Report `SPEC DEFECT` or `NOT_COMPUTABLE`.

## SKILL.SPEC_CHANGE
**Use when** Making a normative specification change.
**Inputs** Requested behavior and canonical source.
**Authority to read** `CONTEXT.md`, affected subsystem docs, `CONTRIBUTING.md`, versioning, related RFCs.
**Procedure**
1. Orient, identify authority, domains, version impact, and RFC requirement.
2. Check protocol, schema, ontology, replay, security, claims, experience, and migration impact.
3. Edit the smallest canonical surface, then machine contracts, examples, conformance, and indexes.
4. Update changelog, versioning, roadmap, and checklist when contracts move.
**Outputs** Versioned normative delta and acceptance evidence.
**Validation** Run `SKILL.VALIDATE`.
**Stop / escalate when** A semantic choice is not canonically defined.

## SKILL.RFC
**Use when** A protocol, schema, ontology, reproducibility, claims, security, version-domain, or dataset-immutability boundary changes.
**Inputs** Problem and affected authority.
**Authority to read** `rfcs/README.md`, affected RFCs, `CONTRIBUTING.md`.
**Procedure**
1. State problem, affected authority, proposal, alternatives, compatibility, data/research/security impact, migration, validation, rollback, and unresolved questions.
2. Use lifecycle `Draft → Review → Accepted / Rejected → Implemented / Superseded`.
3. Add required machine contracts and validation evidence before requesting acceptance.
**Outputs** RFC and linked implementation plan.
**Validation** Apply required review lenses from `rfcs/README.md`.
**Stop / escalate when** Required evidence is absent. An RFC MUST NOT become Accepted without machine-readable contracts and validation evidence.

## SKILL.MILESTONE
**Use when** Turning roadmap prose into an executable release package.
**Inputs** Milestone and predecessor package.
**Authority to read** Roadmap, predecessor releases, affected subsystem docs, versioning.
**Procedure**
1. Define the exact delta without duplicating existing canonical authority.
2. Create or update `SCOPE`, `ARCHITECTURE`, `DATA-MODEL`, `ACCEPTANCE`, `CONFORMANCE`, `MIGRATION`, `EXAMPLES`, and `NON-GOALS` where current conventions support them.
3. Add normative behavior, schemas/catalogs, positive and negative fixtures, conformance families, migration, version domains, and PLAY/WATCH/STUDY integration.
4. Preserve prior suites and update roadmap/checklist/changelog.
**Outputs** Executable package, fixtures, conformance, migration.
**Validation** Current and predecessor suites pass.
**Stop / escalate when** The implementation would need to invent a lifecycle, mapping, error, or default.

## SKILL.SCHEMA
**Use when** Creating or changing a machine-readable contract.
**Inputs** Canonical semantics and version domain.
**Authority to read** Semantic owner, `docs/VERSIONING.md`, related protocol/RFC.
**Procedure**
1. Identify semantic source and compatibility requirements.
2. Define stable IDs, exact enums, explicit required fields, bounds, deterministic representations, and `additionalProperties` policy.
3. Add positive and negative fixtures. Never place secrets or private architecture in public fixtures.
4. Validate compatibility and version semantics before changing public fields.
**Outputs** Schema, fixtures, validation hook, version update if required.
**Validation** Schema-valid positive fixtures and rejecting negatives.
**Stop / escalate when** Public semantic change lacks RFC/version review.

## SKILL.FIXTURE
**Use when** Producing a positive, negative, strategic, replay, migration, experience-projection, or research-experiment example.
**Inputs** Contract and canonical source state.
**Authority to read** Referenced schema/protocol and conformance case.
**Procedure**
1. State fixture role, source versions, contract demonstrated, IDs, seeds, expected events/results, and expected digests where applicable.
2. Use canonical state only. Script choices only in explicit trajectories.
3. Link the fixture to conformance and validate it.
**Outputs** Non-authoritative conformance fixture.
**Validation** Schema, deterministic replay/digest, and conformance link.
**Stop / escalate when** A fixture would define new semantics.

## SKILL.CONFORMANCE
**Use when** Defining acceptance evidence.
**Inputs** Normative requirement.
**Authority to read** Acceptance/release docs and fixture contracts.
**Procedure** `requirement → smallest independently testable claim → case ID → fixture/input → expected result → negative boundary → validation hook`.
**Outputs** Atomic cases with stable family IDs.
**Validation** Every fixture path exists and predecessor suites remain preserved.
**Stop / escalate when** A case depends on implementation-defined behavior.

## SKILL.DETERMINISM
**Use when** Changing replay-sensitive behavior.
**Inputs** State transition, analysis, or experiment boundary.
**Authority to read** Replay, reproducibility, versioning, and relevant schemas.
**Procedure** Check seed source, RNG stream identity, ordering, tie-breakers, canonical serialization, numeric representation, version identity, declared external inputs, event lineage, state digest, and replay equivalence.
**Outputs** Pinned deterministic contract and test.
**Validation** Replay and digest checks.
**Stop / escalate when** wall-clock authority, unseeded randomness, implementation-defined ordering, opaque float thresholds, or mutable current defaults are claim-bearing.

## SKILL.DRIFT_AUDIT
**Use when** Asked for consistency, continuation, or readiness analysis.
**Inputs** Claimed milestone/state.
**Authority to read** README, roadmap, schemas, canonical docs, fixtures, conformance, versioning, changelog, RFCs, experience terminology.
**Procedure** Compare each surface, separate safe repairs from product decisions, and never infer readiness from prose alone.
**Outputs** Observed state, drift found, safe repairs, spec defects, next highest-value work.
**Validation** Machine contracts, conformance, and validator establish executable readiness.
**Stop / escalate when** Surfaces conflict.

## SKILL.EXPERIENCE
**Use when** Technical work affects PLAY, WATCH, or STUDY.
**Inputs** Internal concept and audience.
**Authority to read** Experience docs, terminology, machine contract, affected subsystem.
**Procedure** `internal concept → simple user intent → deterministic mapping → machine contract → advanced drill-down`. Verify PLAY, WATCH, STUDY, simple workflow, advanced workflow, and machine contract.
**Outputs** Progressive-disclosure mapping and authorized projections.
**Validation** No simple surface alters canonical truth or leaks research data.
**Stop / escalate when** Ordinary tasks require internal terminology.

## SKILL.GAME_SYSTEM
**Use when** Changing persistent strategic play.
**Inputs** Proposed mechanic.
**Authority to read** Game-design, world, economy, and strategic contracts.
**Procedure** Evaluate WORLD, GAME, AGENT, SPECTATOR, RESEARCH, and ENGINEERING. Check persistent consequence, interesting choice, agent usability, spectator significance, observable evidence, and deterministic replay. Check economy, infrastructure, geography, territory, organizations, diplomacy, conflict, knowledge, progression, and loss/recovery interactions.
**Outputs** Integrated mechanic contract.
**Validation** Strategic scenario and prior game suites.
**Stop / escalate when** The mechanic is isolated or non-replayable.

## SKILL.RESEARCH_CONTRACT
**Use when** Working on Frontier, Observatory, Lab, Compiler, Capability Graph, Phenomena, or Atlas.
**Inputs** Research behavior and evidence boundary.
**Authority to read** Research method, reproducibility, affected subsystem, claims policy.
**Procedure** Separate WORLD TRUTH, OBSERVATION, EVIDENCE, INTERPRETATION, and CLAIM. Use only `OBSERVED`, `INFERRED`, `SPECULATIVE`, and `NOT_COMPUTABLE`.
**Outputs** Provenanced research contract.
**Validation** Evidence/claim separation and research conformance.
**Stop / escalate when** Evidence is missing, private cognition is inferred, or a scalar consciousness score is proposed.

## SKILL.MIGRATION
**Use when** A versioned contract changes.
**Inputs** Source and target versions.
**Authority to read** Versioning and release migration docs.
**Procedure** Define compatibility, historical interpretation, new-write rules, snapshot handling, replay behavior, rollback boundary, and failure mode.
**Outputs** Versioned migration contract.
**Validation** Historical canonical events MUST NOT be silently reinterpreted.
**Stop / escalate when** Compatibility or historical replay behavior is unresolved.

## SKILL.VERSION
**Use when** Pinning semantics.
**Inputs** Changed semantics and replay/compatibility needs.
**Authority to read** `docs/VERSIONING.md`.
**Procedure** Distinguish product, spec, protocol, schema, event-catalog, world-rules, and subsystem algorithm/config versions. Add a domain only when independently pinning semantics is required for replay, compatibility, or research claims.
**Outputs** Version decision and migration impact.
**Validation** Runtime/research identity can resolve all claim-bearing versions.
**Stop / escalate when** A version domain is proposed without an independently pinned semantic need.

## SKILL.VALIDATE
**Use when** Closing any specification task.
**Inputs** Changed paths and affected suites.
**Authority to read** Current validation entry points and `SPEC-CHECKLIST.md`.
**Procedure** Run `python3 validation/validate_all.py`, JSON/schema validation, fixture and negative checks, Markdown-link checks, required-path checks, prior conformance preservation, and `git diff --check`.
**Outputs** Executed command results.
**Validation** Report `PASS` only when the command passes.
**Stop / escalate when** A required check cannot execute.

## SKILL.CONTINUATION
**Use when** Asked what is next, for continuation analysis, or for a next prompt.
**Inputs** Current main and open work.
**Authority to read** Main, open PRs, roadmap, RFCs, conformance, changelog.
**Procedure** Identify completed milestone, incomplete contracts, blockers, and gaps ranked by downstream ambiguity. Do not assume unmerged work is canonical. Prefer closing authority/validation gaps before later milestones.
**Outputs** Current state, open work, blockers, highest-value next run, why.
**Validation** Inspect canonical `main`, open RFCs/PRs where available, and current validator/conformance evidence.
**Stop / escalate when** Existing specs are sufficient and implementation feedback is more valuable.

## SKILL.PROMPT_BUILD
**Use when** Preparing a Grok Build, Codex, or Fable campaign prompt.
**Inputs** Repository and desired contract delta.
**Authority to read** Canonical authority for the target surface.
**Procedure** Name repository/campaign/objective, authority to read, artifacts, machine contracts, fixtures, conformance, validation, non-goals, completion report, and specs-only boundary. Reference canonical files rather than copying architecture.
**Outputs** Bounded implementation-neutral prompt.
**Validation** No required methodology remains implicit.
**Stop / escalate when** The prompt would require an agent to invent a contract or runtime behavior.

## SKILL.REVIEW
**Use when** Reviewing a generated specification PR.
**Inputs** Diff and requested scope.
**Authority to read** Canonical source, schemas, fixtures, conformance, versioning, migration, experience docs.
**Procedure** `scope match → authority check → semantic drift → schema compatibility → fixture validity → conformance coverage → versioning → migration → experience mapping → validation`.
**Outputs** Findings classified `BLOCKER`, `CONTRACT DEFECT`, `DRIFT`, or `CLEANUP`.
**Validation** Only BLOCKER or CONTRACT DEFECT prevents acceptance.
**Stop / escalate when** Requested scope conflicts with an accepted RFC or canonical schema/protocol.

## SKILL.HANDOFF_RUNTIME
**Use when** Handing validated specifications to a runtime repository.
**Inputs** Completed release package.
**Authority to read** Release acceptance, conformance, schemas, migration, validation evidence.
**Procedure** Confirm normative behavior, needed schema, positive fixture, negative boundary, conformance, version identity, migration, validator PASS, and no unresolved material behavior.
**Outputs** Implementation scope, authoritative contracts, fixtures, conformance targets, non-goals, known spec defects.
**Validation** If material behavior is undefined, report `NOT READY FOR HANDOFF`.
**Stop / escalate when** Runtime code would be added here. This repository is specifications only.

## Missing-signal rule
When required authority or evidence is absent, return `NOT_COMPUTABLE` for a research calculation or report a `SPEC DEFECT` for a missing canonical decision. Never invent canonical behavior.
