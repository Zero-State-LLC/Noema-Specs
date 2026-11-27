# ADR-013: Offline Spark Research Chamber Scope (Spec 014 Writer Authority)

## Status

Accepted

Date: 2026-11-27

Authority: operator approval, 2026-11-27 ("approval is granted where needed to move forward"; "you can handle all of this"), given to resolve the open spec 014 defect recorded in Noema-Orin `G-001` and blocking Noema-Orin #6.

Related docs: [CONTEXT.md](../../CONTEXT.md) (Platform), [specs/014-spark-orin-nvidia-stack/spec.md](../../specs/014-spark-orin-nvidia-stack/spec.md), [ADR-003](0003-claim-label-discipline.md), [ADR-004](0004-world-truth-isolation.md), [ADR-009](0009-psr1-and-study-promotion-evidence.md).

This ADR does not change the hosted Platform, open verbs or event types, or promote spec 014 beyond SPECULATIVE.

## Context

Spec 014 says "Spark runs the Noema chamber as the sole writer of WorldState". CONTEXT.md says the hosted Platform's live serialization belongs to `NoemaWorldDO` and its durable canonical record to Supabase Postgres. Read literally, both cannot be true of the same world. The spec carries an open SPEC DEFECT, and Noema-Orin cannot build its offline-Spark Controller path (#6) until a canonical decision scopes the chamber.

## Decision

### A. The chamber is a separate, non-canonical world

An offline Spark chamber is a distinct world with its own identity. It is not NOEMA's hosted world, a replica of it, or a fork that can rejoin it.

- World ids MUST start with `offline.spark.` and MUST NOT equal or start with any hosted world id (`world-01`, `world.perihelion*`, `test.hosted-canonical.*`).
- Spec 014's "sole writer of WorldState" is read as **sole writer of that chamber's WorldState only**. CONTEXT.md's Platform authority over the hosted world is unchanged and absolute.
- No component may write chamber state into hosted Durable Objects or Postgres, or write hosted state into the chamber. There is no sync, import, replay-into, or merge path in either direction.

### B. Interfaces

- Controllers reach the chamber only at an explicitly configured LAN or loopback origin. A Controller profile is either `hosted` or `offline-spark`, never both. Hosted credentials (controller tokens, Admin JWTs) MUST be refused by the chamber profile, and chamber credentials MUST be refused by the hosted profile. Both directions fail closed.
- There is no fallback across profiles. A chamber outage never routes to hosted, and a hosted outage never routes to the chamber.

### C. Evidence boundary

- Every chamber output (receipts, logs, ledgers, metrics) MUST carry `evidence_scope=OFFLINE_SPARK_RESEARCH` and a claim label no stronger than `OBSERVED` for chamber-local facts. Cosmos and Omniverse outputs stay `INFERRED` (spec 014 requirement 6).
- Chamber evidence MUST NOT be promoted as a hosted-world fact, a hosted STUDY result, or PSR-1 evidence ([ADR-009](0009-psr1-and-study-promotion-evidence.md)). It may be cited as research about offline behaviour, labelled as such.
- [ADR-004](0004-world-truth-isolation.md) applies inside the chamber: research layers read projections and never mutate chamber WorldState.

## Consequences

- The spec 014 SPEC DEFECT is resolved by scoping and is marked resolved in the spec, with a link here. Spec 014 itself stays SPECULATIVE.
- Noema-Orin #6 may build the `offline-spark` Controller path against this ADR. Running it still requires a reachable Spark chamber.
- A hosted-world cutover to Spark would need a new ADR that supersedes CONTEXT.md's Platform section. This ADR does not authorize one.
