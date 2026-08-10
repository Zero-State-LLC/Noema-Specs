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
