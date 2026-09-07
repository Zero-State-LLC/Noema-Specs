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


## Extension Points

Non-normative guidance for future maintenance; this section changes no current behavior or promotion status.

- Evidence-set examples can expand mixed-source ordering, unresolved gaps, and mutually incompatible claims. Preserve the separation between supported facts, inferences, contradictions, and unknowns; reconstruction does not repair canonical history by narrative completion.

- Any added source class or changed ordering/interpretation rule needs a pinned reconstruction-rules version and schema review. Keep prior outputs reproducible under their original version and distinguish this compiler/research output from GC6-S1 Player-authored accounts.

- Validate permutation-invariant ordering by source_class, source_ref, and evidence_id, including ties and missing inputs. A contradictory set should retain CONTESTED claims, while absent signal yields unknowns or NOT_COMPUTABLE rather than a fabricated single story.
