# v0.3 Observatory — Migration

```text
v0.1/v0.2 canonical history
    ↓
derived v0.3 Observatory records
```

## Rules

1. Do not rewrite historical world events as Observatory artifacts.
2. Retrospective analysis allowed only if source versions, required fields, and consent permit; declare limitations.
3. Derived records live in research partition only.
4. Feature/detector/baseline versions pin each analysis run.
5. Feature flag: enable Observatory modules without changing world rules version unless observation semantics change.

## Fail-closed

Incomplete catalog/config/versions ⇒ analysis status `NOT_COMPUTABLE` or `PARTIAL` with unprocessed range declared.

## Extension Points

Non-normative future guidance; this section grants no new behavioral authority and does not reopen accepted or deferred slices.

- **Seam:** Retrospective-analysis guidance can document additional incomplete-input and consent-limited migration cases.
- **Unchanged invariants:** Observatory records remain derived research-partition data; historical canonical events are never rewritten, and analysis runs retain detector, feature, and baseline versions.
- **Compatibility, promotion, and verification:** Observation-semantic changes need separately reviewed versioning rather than a feature flag alone. Verify missing pins fail closed and PARTIAL outputs declare unprocessed ranges without manufacturing evidence.
