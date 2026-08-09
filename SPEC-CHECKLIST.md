# Specification Checklist

Use this checklist for every release candidate. Mark an item not applicable only with a written reason.

## Repository integrity

- [ ] All links resolve and all referenced files exist.
- [ ] Terms match `docs/TERMINOLOGY.md`.
- [ ] Normative statements do not conflict with accepted RFCs.
- [ ] Changelog and version metadata are current.
- [ ] Examples identify whether they are illustrative or conformant.

## Contract completeness

- [ ] Each subsystem names its owner, inputs, outputs, boundaries, and invariants.
- [ ] Stable identifiers, timestamps, units, ordering, and null semantics are defined.
- [ ] Errors are typed, actionable, and non-destructive.
- [ ] Compatibility and migration behavior are defined.
- [ ] Acceptance criteria are observable through public behavior.

## Scientific integrity

- [ ] World truth is isolated from player belief.
- [ ] Observations retain instrument, calibration, conditions, units, uncertainty, and provenance.
- [ ] Hypotheses make falsifiable predictions before results are revealed.
- [ ] Negative, null, and ambiguous results remain representable.
- [ ] Unlocks cite reproducible evidence and can be explained.

## Generation and content

- [ ] Compiled phenomena pass schema, determinism, solvability, safety, performance, and duplication checks.
- [ ] Every generated artifact records source template, parameters, seed, compiler version, and review status.
- [ ] Content licenses and attribution are known.
- [ ] Quarantine and rollback paths are tested.

## Player experience

- [ ] The next useful action is legible without revealing hidden truth.
- [ ] Failure yields feedback rather than a dead end.
- [ ] Difficulty changes opportunity and support, not canonical truth.
- [ ] Required interactions have accessible alternatives.
- [ ] Sensitive themes and intense sensory effects respect safety settings.

## Verification

- [ ] Golden replay tests are deterministic.
- [ ] Schema and protocol conformance suites pass.
- [ ] Save migration fixtures cover supported versions.
- [ ] Property tests cover invariants and boundary values.
- [ ] End-to-end fixtures cover encounter through capability unlock.
