# World Model

## Purpose

The World Model is the authoritative simulation of entities, environments, processes, and hidden laws. It answers what happened, not what the player believes happened.

## State

A world contains a stable ID, seed, simulation time, runtime version, artifact digests, entities, fields, processes, ordered event ledger, and named random streams. Quantities MUST include unit and precision semantics. Unknown, absent, below-detection, and not-applicable are distinct states.

## Resolution cycle

1. Validate actions against capabilities and safety constraints.
2. Gather process inputs from an immutable pre-step view.
3. Compute proposed effects in defined system order.
4. Resolve conflicts using explicit priority and conservation rules.
5. Commit next state atomically.
6. Append events and state digest.
7. Expose eligible signals to the Observatory.

Content MUST NOT depend on filesystem order, map iteration, locale, or wall-clock timing.

## Laws and phenomena

A **law** is a reusable causal rule. A **phenomenon** is an encounterable manifestation produced by laws, entities, conditions, and observability constraints. Phenomena reference laws by stable versioned ID. Local exceptions are explicit conditions or modifiers, never undocumented overrides.

## Uncertainty

Canonical stochastic outcomes are deterministic given a named random stream. Epistemic uncertainty belongs to observations and beliefs, not replay ambiguity. Aleatoric and measurement uncertainty MUST be distinguishable.

## Intervention

An intervention declares target, operation, magnitude, duration, cost, and capability authority. Rejected actions return a reason code without side effects. Consequences, including ecological impact, become canonical events.

## Truth disclosure

The World Model never returns unrestricted internal state to player-facing systems. Observatory adapters map signals through response, calibration, noise, sampling, and detection limits. Debug truth views require privileged tooling and MUST be excluded from production evidence exports.

## Replay and invariants

Snapshots contain a canonical digest and replay cursor. Unsupported exact replay is marked non-reproducible rather than approximated. Entity IDs are never reused, events are immutable and ordered, domain constraints hold after commits, player interpretations are unreadable to resolution, and presentation cannot affect state digests.

## Acceptance criteria

- Same inputs produce identical event and state digests across supported platforms.
- Invalid interventions cause no state change.
- Removing an instrument changes observations, not underlying behavior.
- A stochastic fixture replays identically using named streams.
- Artifact changes are detected before replay.
