# v0.5 Compiler: Scope Delta

v0.5 closes the Phenomenon Compiler as an **executable specification package** around the canonical [Phenomenon Compiler](../../PHENOMENON-COMPILER.md).

It adds machine schemas, versioned capture defaults, STUDY/CAPTURE progressive disclosure, fixtures, negatives, and conformance **P01–P30** so a researcher can move from a READY Lab Result to a reusable captured behavioral test with one ordinary action: **CAPTURE AS TEST**.

## In scope

- Capture intent → canonical compilation request (deterministic, no hidden LLM planning)
- Eligibility gated on `compiler_readiness == READY` plus Compiler admission gates
- Dependency-closed hierarchical `ddmin` pinned ordering and records
- Behavioral oracle, over-minimization guard, captured-test package
- Compile receipt + append-only audit chain (RFC-0003 canonicalization/receipts reused)
- Simple/researcher/advanced/reproducibility projections of the **same** captured test
- Behavioral regression results without scalar ranking

## Preserves

C01–C26, F01–F15, O01–O16, S01–S18, L01–L34, RFC-0003 architecture hardening, PLAY/WATCH/STUDY, claims discipline, research isolation, no production mutation of Lab/world history.

## Usability invariant

> v0.5 MUST reduce implementation ambiguity without increasing ordinary-user conceptual burden.

Authority: [Phenomenon Compiler](../../PHENOMENON-COMPILER.md), [Capture Intent Compilation](../../CAPTURE-INTENT-COMPILATION.md), [Experience](../../EXPERIENCE.md), [Study](../../STUDY.md).

## Extension Points

Non-normative future guidance; this section grants no new behavioral authority and does not reopen accepted or deferred slices.

- **Seam:** Scope maintenance can map additional implementation evidence to the existing P01–P30 capture pipeline without expanding release claims.
- **Unchanged invariants:** READY admission, deterministic dependency-closed minimization, append-only audit, research isolation, and the earlier conformance suites remain intact; no scalar ranking.
- **Compatibility, promotion, and verification:** A new Compiler capability requires separate accepted scope and machine contracts, not an addition to this release summary. Verify scope claims against conformance evidence and keep ordinary CAPTURE AS TEST free of extra conceptual requirements.
