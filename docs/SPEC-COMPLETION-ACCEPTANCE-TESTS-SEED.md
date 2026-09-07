# Spec Completion Contract Micro-Note (Acceptance Tests) — Design Note

**Status:** Micro-note per GAME-COMPLETENESS-PLAN section 11. Inputs only. No contract, catalog, verb, or exposure change.

**Element:** Acceptance tests.

**Coverage notes:**
- Per GC seeds: positive/negative fixtures exist for core cases (e.g., mastery recognition, construction attempts, contest resolution, crime detection).
- Higher GCs: tests via seeds (e.g., pressure divergence, culture inheritance).
- Full suites to be expanded in later slices.

**Boundaries:** Notes only. Cites GAME-COMPLETENESS-PLAN.md section 11 + matrix + prior seeds + main.

Smallest unit for acceptance tests element.

## Extension Points

Non-normative guidance for future maintenance; no new behavior is authorized here.

- **Coverage seam:** Extend this acceptance inventory with concrete fixture paths, positive/negative cases, and the GC matrix row each exercises. Distinguish schema validation, behavioral evaluation, and hosted execution instead of calling the existence of a seed a passing test.
- **Compatibility boundary:** Later coverage follows accepted slice/catalog versions and preserves their prior expectations. New acceptance criteria that change semantics need promotion through the owning authority; this micro-note does not reopen closed mastery, construction, contest, crime, culture, or pressure slices.
- **Validation expectations:** Resolve each cited test to inputs, expected result, tested pin, and actual runner output where available. Include permission denial, boundary, and replay cases appropriate to that row, with missing or deferred coverage explicitly marked rather than inferred from a full-suite label.
