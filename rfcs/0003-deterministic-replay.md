# RFC 0003: Deterministic Replay Contract

- Status: Accepted
- Date: 2026-08-09

## Context

Scientific comparison, debugging, save migration, compiler validation, and shared investigations require the same inputs to produce the same outcomes.

## Decision

Canonical resolution is deterministic for runtime version, artifact digests, seed, initial snapshot, and total ordered action log. Randomness uses named, versioned streams. Floating-point, iteration, scheduling, and event-order semantics that affect state are specified by the runtime contract. Presentation-only nondeterminism is permitted when it cannot affect state or evidence.

Saves pin required versions and replay cursor. A runtime MUST refuse or migrate incompatible replay. It MUST NOT silently approximate and label the result reproducible.

## Consequences

Implementations constrain concurrency and numeric behavior and maintain golden vectors across platforms. This adds engineering cost but provides strong diagnosis, portable fixtures, and trustworthy replication.

## Alternatives

Best-effort replay was rejected because near matches are insufficient for evidence. Recording every random result without named streams was rejected because unrelated feature changes destabilize logs.

## Validation

Golden sessions execute on every supported runtime target and compare event, state, observation, and evidence digests. Stream-isolation tests add unrelated random consumers and require unchanged outcomes.
