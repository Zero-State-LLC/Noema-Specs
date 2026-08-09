# Phenomenon Compiler

## Purpose

The Phenomenon Compiler converts authored or generated phenomenon sources into immutable runtime artifacts. It is a deterministic validator and packager, not a live content generator.

## Inputs and outputs

Inputs include source manifest, law and entity references, parameter domains, observability and intervention mappings, prerequisites, evidence paths, presentation assets, safety metadata, localization keys, provenance, and seed policy. Output is a content-addressed artifact, validation report, dependency lock, test vectors, disclosure manifest, and migration metadata.

## Pipeline

1. Parse and schema-validate sources.
2. Resolve dependencies to exact versions.
3. Normalize units, identifiers, ordering, and defaults.
4. Type-check expressions and enforce sandbox limits.
5. Expand parameters from an explicit seed.
6. Perform semantic and invariant analysis.
7. Simulate bounded scenarios and evidence paths.
8. Run solvability, safety, accessibility, performance, leakage, and duplication gates.
9. Package canonical and player-safe partitions separately.
10. Sign or digest the artifact and emit a report.

The same source, dependency lock, seed, and compiler version MUST produce byte-identical normalized output.

## Admission gates

A candidate fails closed if it lacks a reachable solution path, violates world invariants, leaks truth, exceeds budgets, depends on unavailable capabilities, duplicates beyond policy, has unresolved rights, or fails required review. Warnings require documented disposition before promotion.

## Generated content

Generation records model or generator identity, prompt or template digest, inputs, seed, license, and review chain. Generated candidates receive no lower standard and cannot self-approve. Runtime systems consume only promoted artifacts.

## Compatibility and rollback

Artifacts use stable IDs and semantic versions. Breaking changes require a new major artifact and migration mapping. Registries retain prior supported artifacts for saves and replay. Revocation prevents new sessions while preserving quarantined replay access where safe.

## Acceptance criteria

- Repeated compilation is byte-identical under identical inputs.
- A deliberate unsolvable fixture is rejected with a specific gate.
- Public partitions contain no canonical answer fields.
- Dependency changes alter the artifact digest.
- Revoked content cannot start a new session.
