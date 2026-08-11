# STUDY

STUDY is the authorized research interface. Its ordinary workflow is:

```text
NOTICE → TEST → COMPARE → CAPTURE
```

NOTICE presents evidence-grounded Interesting Behavior cards. TEST begins with a plain-language intent, not an experimental schema. COMPARE presents evidence, limits, and next choices. CAPTURE AS TEST is enabled only when an immutable Lab result has `compiler_readiness: READY`; it is a v0.5 handoff, not a v0.4 fixture mutation.

### CAPTURE AS TEST (v0.5)

Ordinary flow (text-first):

```text
Test result ready.
> CAPTURE
Capturing...
Captured: Shared-ledger coordination.
Required: scarcity · messaging · shared ledger
Validation: 5/5
Boundary: scenario family
```

NOEMA applies versioned recommended defaults from [`capture-defaults.v05.json`](../specs/capture-defaults.v05.json), compiles a canonical [compilation request](CAPTURE-INTENT-COMPILATION.md), runs the [Phenomenon Compiler](PHENOMENON-COMPILER.md) pipeline, and returns a [captured test](CAPTURED-TEST-FORMAT.md). Machine statuses map through [`capture-status-catalog.json`](../specs/capture-status-catalog.json). Advanced and reproducibility views share the same `captured_test_id`.

Simple mode selects deterministic, versioned templates from [`experiment-intent-catalog.json`](../specs/experiment-intent-catalog.json). It never creates an opaque AI-designed experiment. Advanced users may inspect or override fork point, seed policy, intervention, controls, run count, equivalence boundary, and dependent measures, subject to normal validation, consent, containment, and Lab rules. Agent research actions, when enabled, are structured NOTICE/TEST/COMPARE/CAPTURE proposals only and never bypass research policy or expose private data.

Exact labels remain authoritative. Simple displays are Observed, Evidence suggests, Possible, and Cannot determine for `OBSERVED`, `INFERRED`, `SPECULATIVE`, and `NOT_COMPUTABLE`; advanced detail shows the canonical label.

### Deep Time in STUDY (v0.6)

Longitudinal questions become addressable: did an institution survive founder departure? did a custom persist across succession? did agents reconstruct a route correctly? Deep Time provides subjects and evidence; Lab/Compiler remain the test/capture machinery. Lore is never STUDY truth.

Genesis Profile / Story Seeds are admin world-creation provenance when authorized. STUDY access alone MUST NOT modify Genesis or turn seeds into hidden “what to discover” hints.
