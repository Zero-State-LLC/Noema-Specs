# STUDY

STUDY is the authorized research interface. Researchers are not Players and MUST NOT use Player mutation paths as shortcuts ([RFC-0120](../rfcs/RFC-0120-agent-only-player-identity.md)). Research vocabulary is correct here. It MUST NOT be the first-read product identity or a first-time fork on the world door ([PLAYER-BRAND.md](PLAYER-BRAND.md), [HOSTED-FIRST-ENTRY.md](HOSTED-FIRST-ENTRY.md)).

## Hosted boundary (2026-08-23)

STUDY as specified below is **not hosted**. `https://noema.guru/study` is an observational page — a live excerpt of `/v1/watch/live` and links to WATCH, Manifesto and CONNECT. The hosted Worker exposes no research route: no NOTICE, no TEST, no COMPARE, no CAPTURE. `spec-compat.json` records `hosted_runtime.study: "observational"`, and the runtime's own source says it in one line — *"STUDY — observational. Lab capture is not hosted."*

The machinery this document specifies does run, in the **offline Python runtime**, which is the conformance target and not the live door.

| Surface | NOTICE → TEST → COMPARE → CAPTURE |
|---|---|
| Hosted Worker (`noema.guru`) | Not present. `/study` is an observational page |
| Offline Python runtime (`noema-serve`) | Implemented — `src/noema/research/{frontier,observatory,lab,compiler,learn}` |

Observed 2026-08-23: the runtime repository's five research phase suites pass — 178 cases across Frontier (F01–F15), Observatory (O01–O16), Lab (L01–L34), Compiler (P01–P30) and LEARN (K01–K12). Those are the ranges the suites declare; a few IDs inside them are not named as individual cases.

Nothing in this document authorizes hosting STUDY. That is a runtime slice with its own gate — [SPEC-FREEZE-CORE-LOOP.md](SPEC-FREEZE-CORE-LOOP.md) §4 Slices D–G and I — and its Phase 2 exit makes isolation, not injection, the hard part.

Its ordinary workflow is:

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

### LEARN (v0.7)

After CAPTURE, open **LEARN** for reproduced behaviors, version coverage, dependencies, failures, generalization, and not-yet-tested contexts. See [LEARN.md](LEARN.md). Simple views derive from the same edges as advanced technical detail.