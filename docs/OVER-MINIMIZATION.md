# Over-Minimization Guard

## Problem

```text
test still passes, but it is no longer the same behavior
```

## Rule

If uncertain, **retain context** rather than over-minimize.

Removal is authorized only when the oracle returns `PRESERVED` **and** the behavioral signature, dependency closure, observation conditions, required controls, target boundary, and equivalence boundary remain satisfied.

## Outcomes

- Superficially similar but signature-breaking proposal → `NOT_PRESERVED` → reject removal → restore required context.
- Simple UI: “This smaller test changed the behavior too much, so NOEMA restored the required context.”

Fixture: `examples/v05-compiler/over-minimization-proposal.json`.
