# STUDY

STUDY is the authorized research interface. Its ordinary workflow is:

```text
NOTICE → TEST → COMPARE → CAPTURE
```

NOTICE presents evidence-grounded Interesting Behavior cards. TEST begins with a plain-language intent, not an experimental schema. COMPARE presents evidence, limits, and next choices. CAPTURE AS TEST is enabled only when an immutable Lab result has `compiler_readiness: READY`; it is a v0.5 handoff, not a v0.4 fixture mutation.

Simple mode selects deterministic, versioned templates from [`experiment-intent-catalog.json`](../specs/experiment-intent-catalog.json). It never creates an opaque AI-designed experiment. Advanced users may inspect or override fork point, seed policy, intervention, controls, run count, equivalence boundary, and dependent measures, subject to normal validation, consent, containment, and Lab rules. Agent research actions, when enabled, are structured NOTICE/TEST/COMPARE/CAPTURE proposals only and never bypass research policy or expose private data.

Exact labels remain authoritative. Simple displays are Observed, Evidence suggests, Possible, and Cannot determine for `OBSERVED`, `INFERRED`, `SPECULATIVE`, and `NOT_COMPUTABLE`; advanced detail shows the canonical label.

