# RFC 0000: RFC Process

- Status: Accepted
- Date: 2026-08-09
- Authors: Noema maintainers

## Summary

RFCs record durable decisions that affect more than one component or change a public contract.

## When required

An RFC is required for changes to save or replay compatibility, truth and belief boundaries, evidence semantics, progression rules, content admission, security or privacy posture, public schemas or protocols, and foundational product principles. Editorial and clearly additive compatible changes do not require one.

## Lifecycle

`Draft → Review → Accepted | Rejected | Withdrawn → Superseded`

Drafts receive the next zero-padded number and a descriptive filename. Review MUST include owners of affected domains. Accepted RFCs name implementation and migration work. Rejected and withdrawn RFCs remain for decision history. Accepted text is immutable except status metadata and errata; substantive revision uses a superseding RFC.

## Required sections

- metadata and summary;
- context and problem;
- decision with normative requirements;
- alternatives considered;
- consequences and risks;
- compatibility, migration, security, privacy, accessibility, and observability impacts as applicable;
- validation and rollout;
- unresolved questions.

## Decision criteria

Reviewers evaluate alignment with the product vision, player-observable benefit, determinism, provenance, explainability, bounded generation, compatibility, operational feasibility, safety, privacy, and accessibility. Consensus is preferred. The designated maintainer records the decision and dissent.

## Numbering and status

Numbers are never reused. RFC 0000 governs the process. Status changes update only the metadata and changelog. A superseding RFC links both directions.

## Implementation

Acceptance authorizes but does not prove implementation. Specifications, schemas, fixtures, migrations, and tests MUST be updated before a behavioral RFC is considered delivered.
