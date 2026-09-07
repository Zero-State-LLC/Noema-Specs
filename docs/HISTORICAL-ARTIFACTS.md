# Historical Artifacts

## Classes (closed set)

`RECORD` · `MAP` · `MARKER` · `CONTRACT_COPY` · `LEDGER` · `ARCHIVE` · `MEMORIAL` · `STRUCTURE`

## Required fields

`artifact_id`, `artifact_class`, `creator_ref`, `creation_cycle`, `integrity`, `visibility`, `content_ref`, `claims_are_not_world_truth: true`, provenance, digest.

## Truth boundary

Separate:

```text
artifact exists
```

from:

```text
artifact claims X happened
```

Artifacts may be accurate, incomplete, misleading, forged, corrupted, or misunderstood. Canonical event history remains independent.

GC6-S0 hosted source ([RFC-0015](../rfcs/RFC-0015-archive-record-source.md)): Chamber reads only explicit `archive_subject_entity_id` + `archive_claim` ∈ {`DESTROYED`, `OPERATING`} on an `ARTIFACT`. It does not parse `content_ref` or presentation text.

## Integrity

`INTACT` → `DEGRADED` → `FRAGMENTARY` → `CORRUPTED` → `DESTROYED`

If destroyed: preserve the canonical fact that it **existed** (`existed_fact_preserved`). Do not rewrite prior history.

## Extension Points

Non-normative guidance; the existing slice and its authority remain unchanged.

### Artifact readers and integrity views

Future readers can present additional provenance or integrity explanations while separating artifact existence from the truth of its claims. Destruction preserves the fact of prior existence; corrupted content does not rewrite canonical events.

New artifact classes or machine-interpreted claim values require an accepted schema/catalog change. Preserve RFC-0015 explicit archive_subject_entity_id and DESTROYED/OPERATING parsing rather than interpreting prose. Validate forged or contradictory claims, unsupported claim values, visibility denial and destroyed-artifact provenance continuity.
