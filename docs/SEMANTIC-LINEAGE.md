# Semantic Lineage (v0.6 foundation)

Track terms, symbols, practices, names, warnings, stories, customs:

```text
origin → meaning at origin → later use → changed meaning → source evidence
```

Schema: [`semantic-lineage.schema.json`](../specs/semantic-lineage.schema.json).

## Boundaries

- `auto_interpreted: false` — do not automatically interpret meaning shifts.
- Canonical machine IDs never mutate when cultural names change ([historical-name](../specs/historical-name.schema.json)).
- Full semantic-evolution engine is **out of scope** for v0.6 foundation (see roadmap handoff v0.6C).
