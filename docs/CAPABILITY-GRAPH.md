# Capability Graph

## Purpose

The Capability Graph translates demonstrated knowledge, resources, trust, and safety into explainable permissions to observe or intervene.

## Model

Nodes are capabilities with stable versioned IDs, presentation metadata, granted actions, parameters, costs, and revocation policy. Edges and requirement expressions reference prerequisite capabilities and evidence predicates. Requirement expressions use explicit `all`, `any`, and threshold operators and MUST be acyclic after expansion.

## Evidence predicates

A predicate may require phenomenon coverage, prediction outcome, quality status, independent replications, varied conditions, uncertainty bound, low-impact method, or contradiction resolution. Every satisfied predicate cites immutable evidence IDs and evaluator version. Raw playtime and opaque XP MUST NOT substitute for epistemic requirements.

## Evaluation

1. Load the pinned graph and eligible evidence snapshot.
2. Validate evidence integrity and compatibility.
3. Evaluate requirements in deterministic topological order.
4. Emit locked, eligible, granted, suspended, or revoked state.
5. Attach a player-safe explanation and machine-readable trace.
6. Apply grants atomically and idempotently.

A capability may require a deliberate player choice or resource cost after becoming eligible.

## Explainability

Locked nodes show known prerequisites without leaking undiscovered truth. Eligible and granted nodes show exactly which evidence satisfied each requirement. Near-miss guidance identifies missing evidence class, not the answer. Disputed or invalidated evidence updates the explanation.

## Revocation and migration

Capabilities earned under valid historical rules SHOULD remain grandfathered unless safety or integrity requires suspension. Revocation never deletes evidence. Graph migrations map node IDs, requirements, and player state and must be replayable.

## Graph quality

The graph MUST have a reachable root set, no cycles, no impossible requirements, and no mandatory single path where the game promises methodological plurality. Automated analysis checks reachability, bottlenecks, orphan nodes, privilege escalation, and content inventory coverage.

## Acceptance criteria

- Identical graph and evidence snapshots yield identical states and traces.
- Every grant is backed by cited eligible evidence.
- Removing an invalid citation recomputes affected state without deleting history.
- No node can grant an action outside its declared authority.
- Supported graph migrations preserve or explicitly explain player access.
