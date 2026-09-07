# Integration Surface with Zero State / Abraxas Ecosystem

NOEMA is designed as an implementation-neutral persistent world that is also a research substrate. The following surfaces are intentional extension points for existing Zero State systems (Abraxas symbolic engines, signal foragers, Brier-calibrated forecasting, Capability Graph consumers, etc.). Player-facing presentation remains game-first ([PLAYER-BRAND.md](PLAYER-BRAND.md)).

## 1. Claim-label and provenance interop
All NOEMA evidence uses OBSERVED / INFERRED / SPECULATIVE / NOT_COMPUTABLE. External systems SHOULD consume these labels without remapping. Provenance digests and version lineages are content-addressed and can be referenced from Abraxas-style run envelopes.

## 2. Capability Graph export
Versioned Capability Graph snapshots (genesis, dependencies, transfer radius, architecture attribution) are Atlas artifacts. They can be ingested by external forecasting or symbolic reasoning layers as ground-truth capability boundaries under the declared conditions.

## 3. Frontier / Situation Genome pressure
The Frontier Director selects situations via Situation Genome and novelty vectors. External systems MAY propose genome mutations or score components through a future controlled injection API, but the World Engine remains the sole writer of truth. No external system may force outcomes.

## 4. Reproducibility Bundle consumption
Bundles are the preferred interchange format. They contain minimal fixtures, controls, claim labels, confounds, and digests. Downstream evaluation harnesses (including HollerSports-style calibration or Abraxas adversarial testing) can treat a bundle as a frozen experimental unit.

## 5. Observation and trajectory streams
Permissioned, research-eligible observation streams can be mirrored to external Observatory-style consumers provided consent, retention, and private/public partition rules are honored. Telemetry never becomes evidence silently.

## Non-goals
- NOEMA does not embed Abraxas runes or governance as world rules.
- Private cognition and provider keys remain isolated.
- Real-money or real-world destructive actions are out of scope.

This surface is informative for ecosystem planning and does not alter any normative contract.

## Extension Points

Non-normative maintenance and integration guidance; the contracts cited above remain authoritative.

### Document-specific seam

Extend external consumers at the reproducibility-bundle or permissioned observation boundary. An adapter can retain original claim labels, provenance digests, exclusions, and version lineage while adding its own explicitly downstream interpretation; symbolic analysis is not a new source of NOEMA world truth.

### Compatibility and promotion

The four claim labels are closed; no new label, hashing rule, injection API, or live economy hook is authorized by this planning surface. Frontier proposals require their existing governance and isolation boundaries. External Controllers integrate through protocols and cannot write canonical state or import framework governance into Core.

### Verification before adoption

Round-trip a permitted bundle and compare source digests/labels/lineage; reject unsupported versions and consent/export violations. Include downstream claims that exceed the source boundary and keep them separate. Check unauthorized stream subscription and direct mutation are denied, and do not claim hosted STUDY reopening from adapter readiness.
