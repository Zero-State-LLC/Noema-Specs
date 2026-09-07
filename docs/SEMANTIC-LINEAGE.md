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


## Extension Points

Non-normative guidance for future maintenance; this section changes no current behavior or promotion status.

- Lineage examples can document reuse of a term, name, warning, or custom with cited origin and later evidence. Preserve auto_interpreted: false and distinguish a documented change of usage from a machine claim that its meaning has been inferred.

- New lineage fields or interpretation rules require schema/version review and retain the original evidence chain. Cultural renaming never mutates canonical machine IDs; the v0.6 foundation does not activate the deferred v0.6C semantic-evolution engine.

- Validate renamed entities retain stable identifiers, every proposed meaning-change entry points to its source evidence, and missing or contradictory sources remain explicit. Replay or regeneration under the same pinned inputs should retain ordering and lineage without silently filling gaps through automatic interpretation.
