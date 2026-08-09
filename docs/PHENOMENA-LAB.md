# Phenomena Lab

## Purpose

Phenomena Lab is the internal workspace for authoring, generating, simulating, reviewing, and promoting phenomena. It makes content decisions auditable and keeps unreleased truth out of player-facing systems.

## Roles

Authors edit sources. Researchers review inference and scientific framing. Designers review playability. Safety and accessibility reviewers enforce constraints. Engineers own compiler and runtime compatibility. Release managers promote or revoke artifacts. Separation of duties MUST prevent a candidate or automated generator from approving itself.

## Workspace flow

`draft → generated candidate → linted → simulated → reviewed → approved → compiled → staged → promoted | quarantined | revoked`

Every transition records actor, timestamp, source revision, reason, and validation report. Branches and comparisons preserve lineage.

## Tools

The Lab SHOULD provide structured editors, dependency and capability graphs, unit checking, seed explorer, batch simulation, evidence-path solver, truth-leak preview, player-safe preview, difficulty distributions, accessibility emulation, performance budgets, provenance and license inspection, and side-by-side artifact diff.

## Truth safety

Canonical parameters and answer keys are restricted by role. Screenshots, exports, logs, and collaboration links inherit disclosure classification. Production telemetry cannot reveal canonical truth back into authoring views unless explicitly authorized and aggregated.

## Evaluation

Review covers coherence, multiple viable inquiry paths, calibration opportunities, failure recovery, evidence validity, capability fit, narrative framing, ecological and sensory safety, cultural sensitivity, accessibility, performance, replay, duplication, and rights. Automated scores support but never replace accountable approval.

## Promotion and incident response

Promotion requires passing compiler gates, required human approvals, staging replay, and signed manifest. Emergency revocation stops new distribution, preserves affected IDs, identifies save impact, and initiates migration or safe replay policy. Quarantined artifacts cannot be copied into release packs.

## Acceptance criteria

- Every promoted artifact has complete source-to-review-to-build lineage.
- A user cannot approve their own generated candidate when two-person review is required.
- Player-safe preview detects a seeded truth leak fixture.
- Re-running a saved simulation uses pinned dependencies and seed.
- Revocation is visible to registry, director, save compatibility, and incident tooling.
