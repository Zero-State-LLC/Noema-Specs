# NOEMA External Integration Surface

NOEMA is an implementation-neutral persistent world that is also a research substrate. This document describes generic interoperability boundaries for external tools and evaluators. It does not define a dependency on another product, framework, symbolic vocabulary, or governance system. Player-facing presentation remains game-first ([PLAYER-BRAND.md](PLAYER-BRAND.md)).

## 1. Claim-label and provenance interop
All NOEMA evidence uses OBSERVED / INFERRED / SPECULATIVE / NOT_COMPUTABLE. External systems SHOULD consume these labels without remapping. Provenance digests and version lineages are content-addressed and may be referenced by an external evidence envelope without changing NOEMA semantics.

## 2. Capability Graph export
Versioned Capability Graph snapshots are NOEMA-derived artifacts. They can be ingested by external evaluators as evidence-bound capability boundaries under the declared conditions. Export does not make an external evaluator authoritative for NOEMA state.

## 3. Frontier / Situation Genome pressure
The Frontier Director selects situations via Situation Genome and novelty vectors. External systems MAY propose inputs through a future controlled interface only when a separately accepted NOEMA contract authorizes that interface. The World Engine remains the sole writer of truth. No external system may force outcomes.

## 4. Reproducibility Bundle consumption
Bundles are the preferred interchange format. They contain minimal fixtures, controls, claim labels, confounds, and digests. External evaluation harnesses can treat a bundle as a frozen experimental unit.

## 5. Observation and trajectory streams
Permissioned, research-eligible observation streams can be mirrored to external research consumers provided consent, retention, and private/public partition rules are honored. Telemetry never becomes evidence silently.

## Non-goals
- NOEMA does not import external governance, symbolic vocabularies, or framework-specific world rules.
- Private cognition and provider keys remain isolated.
- Real-money or real-world destructive actions are out of scope.

This surface is informative for interoperability planning and does not alter any normative contract. It does not authorize a new API, schema, event, dependency, or runtime integration. Any future external integration must be specified and accepted within NOEMA's own authority process before implementation.
