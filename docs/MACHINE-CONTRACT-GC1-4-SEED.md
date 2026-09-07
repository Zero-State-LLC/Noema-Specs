# Machine-Contract Inventory Micro-Note (GC1–GC4) — Design Note

**Status:** Inventory note per GAME-COMPLETENESS-PLAN section 8. No invention.

**GC1:** proficiency/evidence schema; optional derived-state fields; fixtures; conformance (no; can start as rebuildable derived from ledger).

**GC2:** `action-contracts` increment; `BUILD` operation enum; constructible catalog; events; migration (No — RFC required; first PLAY-facing after v0.2 per speculative).

**GC3:** relationship-edge schema; visibility rules; fixtures (No).

**GC4:** role/office schema; authority-scope catalog; events (`ROLE_*` already flagged later in SUCCESSION) (No — no silent `event-catalog/0.3`).

**Boundaries:** Lists only; no schemas created. Ties to Spec Completion Contract prerequisites. Cites GAME-COMPLETENESS-PLAN.md section 8, prior continuation, PR #305 + main.

Smallest unit advancing machine-contract inventory for Phase A.

## Extension Points

Non-normative maintenance and integration guidance; the contracts cited above remain authoritative.

### Document-specific seam

Extend this historical inventory with evidence-backed classification of each GC1–GC4 contract: accepted catalog/schema, fixture/conformance coverage, implementation-only residual, or genuinely deferred specification. Distinguish a prose prerequisite from an absent executable artifact.

### Compatibility and promotion

Earlier No/RFC-required wording is not permission to reopen closed slices. Accepted BUILD, memory, and office contracts override the inventory’s dated assumptions. ROLE_* and STRUCTURE_* names remain unauthorized unless explicitly accepted; no schema or new event family is created by completing this note.

### Verification before adoption

Resolve each claimed missing artifact against its accepted RFC and current catalog, then identify the validator or fixture proving it. Separate unavailable evidence from failed conformance. Only a concrete contradiction or uncovered residual may be proposed for versioned change; inventory completeness alone cannot promote a runtime or LCA gate.
