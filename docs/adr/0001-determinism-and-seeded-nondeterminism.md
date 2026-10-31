# ADR-001: Determinism and seeded nondeterminism

## Status
Accepted

## Context
NOEMA must support exact replay of world state and observation digests for research evidence. Uncontrolled wall-clock, network, or entropy sources destroy attribution.

## Decision
All world reducers are pure with respect to (world_version, seeds, deterministic_config, prior_state, ordered accepted inputs). Any nondeterminism MUST use a named, recorded random stream whose draws are derived via HMAC-SHA-256(world_seed, stream_name || decision_point || draw_index). Wall-clock and undeclared external inputs are forbidden in the reducer context.

## Consequences
- Replay becomes a first-class evidence mechanism.
- Provider model outputs must be recorded as external inputs when stochastic-agent mode is used.
- Implementations that inject unseeded randomness are non-conformant.
