# RFC-0024 — GC6-S1 Historical Reconstruction

## Status

**Accepted**

Closes the GC6-S0 reconstruction SPEC GAP. A reconstruction is a Player-authored interpretation of accessible evidence. It is not canonical history. No `QUEST`. No oracle. No `event-catalog/0.3`.

## Problem

[SYSTEMIC-DISCOVERY.md](../docs/SYSTEMIC-DISCOVERY.md) and [RFC-0010](RFC-0010-discovery-contradiction.md) left Player-compiled reconstruction as SPEC GAP. An implementer would add `RECONSTRUCT` as a quest closer, resolve archive vs live automatically, or leak `known_truth_relationship`.

## Proposed change

Accept GC6-S1:

```text
CANONICAL HISTORY ≠ ACCESSIBLE EVIDENCE ≠ PLAYER RECONSTRUCTION ≠ RESEARCH INTERPRETATION
```

- Player record on WorldRuntime (Information-shaped). Not the v0.6 compiler schema (`historical-reconstruction/0.6` remains research/compiler output).
- Evidence must already be accessible to the author (`ARCHIVE_CLAIM` from attested artifact `INSPECT`, `LIVE_INSPECT` of the subject). Hidden ledger, research, admin, and cross-world refs are rejected.
- Contradiction is a valid recorded state (`CONTESTED`), not a validation failure.
- Lifecycle: `RECORDED` → `SUPERSEDED`. Visibility: `PRIVATE` | `INSTITUTIONAL` | `PUBLIC`.
- Publication does not grant others the underlying archive/inspect access.
- Wire: `COMMIT.RECONSTRUCT` / `COMMIT.RECONSTRUCT_SUPERSEDE` / `COMMIT.RECONSTRUCT_PUBLISH`. No new top-level verb in frozen `action-contracts.v01.json`.
- Evidence events: `ENTITY_CREATE` (`DOCUMENT`, `location=null`) and `ENTITY_UPDATE`. Not `QUEST_*` / `DISCOVERY_*`.

Catalog: [`reconstruction-catalog.gc6-s1.json`](../specs/reconstruction-catalog.gc6-s1.json).  
Slice: [GC6-S1-RECONSTRUCTION.md](../docs/GC6-S1-RECONSTRUCTION.md).

## Alternatives rejected

| Alternative | Why |
|-------------|-----|
| `QUEST` / `SOLVE_MYSTERY` | Doctrine: no quest engine |
| Engine names the true past | `known_truth` is research-only |
| Reuse `historical-reconstruction/0.6` as PLAY record | Compiler output; required digest / no-narrative-invention |
| New catalog 0.3 events | Silent expansion |
| Confidence = 0.87 | Scoring as truth |
| Tradition / rumor | GC9-S1 / GC5-S2 |

## Compatibility

Additive. GC6-S0 contradiction line unchanged. ATTEST remains the archive-claim writer. Frozen catalogs unchanged.

## Data / security

Rebuildable map on WorldRuntime / world head. Not a new database. Citing an inaccessible id is `FORBIDDEN`. Public summary does not include private source text unless the author wrote it into the claim. Reconstruction grants no authority and does not mutate the ledger.

## Validation

`check_gc6_s1`: accessible compile accepted; hidden/cross-world/research refs rejected; contradiction may be recorded; supersede is append; no quest/oracle tokens.

## Rollback

Omit `COMMIT.RECONSTRUCT*`. GC6-S0 contradiction projection remains.

## Unresolved

WATCH public contradiction pulse. Additional evidence kinds (messages, maps) beyond hosted archive/inspect. GC9-S1 tradition citation.
