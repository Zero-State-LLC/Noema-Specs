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

## Extension Points

Non-normative guidance for future maintenance; no new behavior is authorized here.

- **Guard seam:** Extend over-minimization-proposal.json-style cases that keep a superficial test outcome while losing a required control, dependency, observation condition, or target boundary. Use them to explain why restored context matters rather than weakening the preservation oracle.
- **Compatibility boundary:** A changed signature, equivalence boundary, or oracle method is a new versioned comparison, not permission to relabel an old rejected removal PRESERVED. Only the existing full preservation decision authorizes removal; uncertainty continues to favor retaining context.
- **Validation expectations:** Pair one genuinely preserved reduction with signature-breaking and missing-control proposals. Verify NOT_PRESERVED rejects removal and restores required context, evidence links survive restoration, and the simple explanation agrees with the detailed decision instead of reporting success because the smaller test still passes.
