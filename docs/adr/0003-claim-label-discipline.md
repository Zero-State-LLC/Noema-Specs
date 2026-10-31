# ADR-003: Claim-label discipline

## Status
Accepted

## Context
Ambiguous language about what was observed versus inferred produces non-reproducible science and over-claiming.

## Decision
Every Observation, Trajectory claim, and Reproducibility Bundle interpretation MUST carry exactly one of: OBSERVED, INFERRED, SPECULATIVE, NOT_COMPUTABLE. No scalar consciousness score is permitted. Mixed payloads must either split or adopt the least-direct label.

## Consequences
- Atlas releases remain scientifically usable.
- Downstream systems (including Capability Graph and Phenomena Lab) inherit the same vocabulary.
- Editorial pressure to upgrade labels is constrained by evidence requirements.
