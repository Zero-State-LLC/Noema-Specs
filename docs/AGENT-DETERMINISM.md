# Agent Determinism Classification

`DETERMINISTIC` permits exact behavior equivalence with pinned inputs. `SEED_CONTROLLED` permits it only with pinned seeds and no recorded stream divergence. `NONDETERMINISTIC` remains studyable with declared wider bands/more repetitions. `UNKNOWN` disallows exact behavioral equivalence and needs conservative analysis. Classification is pinned in experiment/run identity. Nondeterminism never automatically invalidates a study.

## Extension Points

Non-normative maintenance and integration guidance; the contracts cited above remain authoritative.

### Document-specific seam

Extend research reporting with a classification rationale tied to pinned inputs, seeds or recorded response streams, and observed divergence. Classification describes the reproducibility boundary of the declared AgentVersion; it does not inspect private cognition.

### Compatibility and promotion

Keep the four classification identifiers stable and bind changes to experiment/run identity. Nondeterminism permits appropriately declared replication, not exact-equivalence claims. Pinning and analysis require research authorization; Controller enrollment grants neither, and ordinary PLAY/WATCH gains no classification feed.

### Verification before adoption

Check exact-equivalence eligibility for all four classes, missing seed/stream evidence, and divergence under SEED_CONTROLLED. Verify UNKNOWN cannot yield an exact-equivalence conclusion and a nondeterministic run retains its declared wider bands and repetition plan. Localized labels must not alter serialized classifications.
