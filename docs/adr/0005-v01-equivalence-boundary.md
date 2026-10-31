# ADR-005: v0.1 equivalence boundary profile

## Status
Accepted

## Context
v0.1 acceptance requires recorded sessions to replay to a defined equivalence boundary.

## Decision
The mandatory v0.1 profile requires:
1. identical ordered event digests;
2. identical final canonical WorldState digest;
3. identical observation digests at every declared focal-agent observation point.

The boundary object follows the structure defined in docs/REPLAY.md. Implementations MAY add stricter comparisons but MUST NOT weaken this profile while claiming v0.1 conformance.

## Consequences
- Clear acceptance test for The Chamber.
- Later behavioral-equivalence modes can layer on top without invalidating early evidence.
