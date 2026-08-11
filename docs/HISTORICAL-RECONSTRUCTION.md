# Historical Reconstruction

## Input

```text
evidence set · time window · subject · reconstruction rules version
```

## Output

```text
supported_facts · inferences · contradictions · unknowns
```

Schema: [`historical-reconstruction.schema.json`](../specs/historical-reconstruction.schema.json).

## Rules

- Deterministic ordering of evidence by `(source_class, source_ref, evidence_id)`.
- Never fill gaps with narrative invention (`no_narrative_invention: true`).
- Missing signal → `NOT_COMPUTABLE` / `unknowns[]`.
- Conflicting sources remain as `contradictions[]` with `evidence_status: CONTESTED` on claims.
- Do not force a single narrative when evidence does not resolve.
