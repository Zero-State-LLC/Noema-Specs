# Contributing to Noema Specifications

## Requirement language

The words **MUST**, **MUST NOT**, **SHOULD**, **SHOULD NOT**, and **MAY** are normative. Plain present-tense descriptions are normative when they define a contract. Sections marked “non-normative” provide rationale or examples.

## Change classes

| Class | Examples | Required path |
| --- | --- | --- |
| Editorial | clarity, spelling, link repair | pull request |
| Compatible | additive optional field, new example | pull request plus validation |
| Behavioral | scoring, director, unlock, or compiler semantics | RFC plus tests/fixtures |
| Breaking | required field, identifier, meaning, or replay change | RFC, migration, version boundary |

## Workflow

1. Open an issue or RFC describing the player or operator problem.
2. Identify affected contracts and acceptance criteria.
3. Update specifications, schemas, fixtures, terminology, and changelog together.
4. Run the validation matrix in `SPEC-CHECKLIST.md`.
5. Request review from design and engineering. Add research, safety, accessibility, or content review when relevant.

## Specification style

A subsystem document SHOULD contain: purpose, responsibilities, boundaries, inputs, outputs, state model, algorithms or policy, invariants, failure behavior, observability, versioning, and acceptance criteria. Prefer tables and small examples. Avoid binding the contract to a particular framework.

## RFCs

Use `rfcs/0000-rfc-process.md`. An RFC is required when a decision changes save compatibility, replay, evidence semantics, progression, trust boundaries, content admission, or a public protocol. Accepted RFCs are immutable except for status metadata and obvious errata. Supersede them with a new RFC.

## Review checklist

Reviewers ask:

- Can a player distinguish observation from interpretation?
- Can an implementation reproduce and explain the outcome?
- Does failure preserve actionable evidence?
- Can old data be read or migrated?
- Are safety, privacy, accessibility, and provenance explicit?
- Is generated content bounded and testable?

## Conduct and security

Be respectful, critique artifacts rather than people, and do not include sensitive personal data. Report vulnerabilities privately according to `SECURITY.md` when that file is present.
