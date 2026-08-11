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

## Integrity

`INTACT` → `DEGRADED` → `FRAGMENTARY` → `CORRUPTED` → `DESTROYED`

If destroyed: preserve the canonical fact that it **existed** (`existed_fact_preserved`). Do not rewrite prior history.
