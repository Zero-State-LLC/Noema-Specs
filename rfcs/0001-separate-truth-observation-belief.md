# RFC 0001: Separate Truth, Observation, and Belief

- Status: Accepted
- Date: 2026-08-09

## Context

A discovery game becomes arbitrary if player labels can alter physical resolution or if measurements expose hidden state directly. Debug convenience can otherwise collapse distinct epistemic layers.

## Decision

Noema defines three mandatory domains:

1. canonical truth owned by the World Model;
2. observations produced only through versioned instruments;
3. beliefs and models authored in the Notebook.

Runtime laws MUST NOT read player beliefs. Player-facing services MUST NOT receive unrestricted canonical state. Beliefs cite observations but never mutate them. Canonical confirmation, where designed, is an explicit event rather than a property inferred from UI language.

## Consequences

Implementations need typed boundaries, disclosure-aware payloads, and dedicated debug authorization. Tests must detect truth leakage and belief-dependent simulation. The separation enables fair mystery, contradictory theories, and reproducible reasoning at the cost of additional data modeling.

## Alternatives

A unified flexible entity model was rejected because authorization conventions are too easy to violate. Designer-authored “correct answer” flags in the Notebook were rejected because they turn inquiry into answer matching.

## Validation

Conformance fixtures change beliefs while holding world inputs constant and require identical state digests. Public observation fixtures are scanned for canonical-only fields.
