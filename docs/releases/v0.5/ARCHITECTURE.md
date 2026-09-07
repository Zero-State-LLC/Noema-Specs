# v0.5 Compiler: Architecture Delta

## Product flow (ordinary)

```text
STUDY → TEST RESULT → [CAPTURE AS TEST] → Capturing... → CAPTURED TEST
```

## Machine flow

```text
Lab Result → Eligibility → Phenomenon Candidate → Dependency Closure
  → Deterministic Minimization → Replay Oracle → Stability Validation
  → Captured Test → Behavioral Regression Surface
```

These are the same operation at different disclosure levels.

## Components

| Surface | Role |
|---|---|
| `capture-intent` | Experience-layer one-action request |
| `capture-defaults/0.5.0` | Versioned recommended defaults (inspectable, not hidden) |
| `compilation-request` | Canonical Compiler input ([PHENOMENON-COMPILER](../../PHENOMENON-COMPILER.md)) |
| dependency graph + unit manifest | Internal minimization inputs |
| behavioral oracle | PRESERVED / NOT_PRESERVED / INCONCLUSIVE / INVALID |
| compiler-result + receipt + audit | Status, promotion, provenance |
| captured-test package | Reusable regression artifact |
| experience views | SIMPLE → REPRODUCIBILITY projections |

## Progressive disclosure

| Level | Shows |
|---|---|
| 1 Simple | Captured title, required/removed, validation, limits, next action |
| 2 Researcher | Condition lists, validation counts, boundary language |
| 3 Advanced | Lab result, deps, minimality, oracle type, confounds, boundary enum |
| 4 Reproducibility | Digests, audit root, receipt, schema/version pins |

No separate simple truth model.

## RFC-0003 reuse

Canonicalization `noema-jcs/1`, content hashing, receipt identity, evidence export profiles—no Compiler-specific parallel provenance rules.

## Extension Points

Non-normative future guidance; this section grants no new behavioral authority and does not reopen accepted or deferred slices.

- **Seam:** Component documentation can expand adapter and failure-path examples between capture intent, dependency closure, minimization, oracle, and receipt.
- **Unchanged invariants:** Ordinary and machine flows remain one operation with one truth model; RFC-0003 canonicalization, hashing, receipts, and export rules are reused.
- **Compatibility, promotion, and verification:** Alternative minimizers or oracle integrations require pinned contracts and compatibility review before promotion. Verify every disclosure level describes the same captured test and preserves INCONCLUSIVE/INVALID outcomes and provenance.
