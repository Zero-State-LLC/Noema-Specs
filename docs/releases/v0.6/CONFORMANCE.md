# v0.6 Deep Time: Conformance

Suite: `conformance/v0.6/` · **D01–D30** · 90 atomic cases · depends on v0.5.

| Family | Topic |
|---|---|
| D01 | Historical Identity |
| D02 | Institution Creation |
| D03 | Institution Persistence |
| D04 | Institution Lifecycle |
| D05 | Succession |
| D06 | Founder Departure |
| D07 | Dormancy |
| D08 | Dissolution |
| D09 | Revival / Successor Identity |
| D10 | Artifact Creation |
| D11 | Artifact Provenance |
| D12 | Artifact Integrity |
| D13 | Artifact Decay |
| D14 | Historical Claims |
| D15 | Conflicting Claims |
| D16 | Historical Reconstruction |
| D17 | Archaeological Observation |
| D18 | Hidden-History Protection |
| D19 | Institutional Memory |
| D20 | Cultural Transmission |
| D21 | Semantic Lineage |
| D22 | Stable Canonical IDs / Renaming |
| D23 | Historical Geography |
| D24 | World Scars |
| D25 | Inheritance |
| D26 | Historical Snapshot Separation |
| D27 | PLAY Projection |
| D28 | WATCH Timeline Projection |
| D29 | STUDY Longitudinal Questions |
| D30 | Lore Boundary / RFC-0003 Provenance |

### Genesis (minimal) G01–G09

| Family | Topic |
|---|---|
| G01 | Profile Validation |
| G02 | Story Seed Validation |
| G03 | Same-Seed Determinism |
| G04 | Different-Seed Validity |
| G05 | Cycle 0 World Validity |
| G06 | Starting Opportunity |
| G07 | Historical Evidence Boundary |
| G08 | PLAY Projection |
| G09 | Lore Separation / Admin Boundary |

Fixtures: `examples/v06-deep-time/`. Validator: `check_deep_time_v06` (+ Genesis checks).

## Extension Points

Non-normative future guidance; this section does not change the contracts or dated outcomes above.

**Seam.** Deep Time and Genesis coverage mapping can expand edge cases within D01–D30 and G01–G09, linking historical identity and projection cases to their fixtures.

**Preserved invariants.** Preserve stable IDs, original provenance, hidden-history protection, lore separation, and Admin-only Genesis; decay or reconstruction never rewrites what occurred.

**Compatibility and promotion.** Changed lifecycle, decay, reconstruction, or Genesis semantics require their owning versioned contracts and compatibility fixtures. Updating this conformance index does not activate deferred v0.6 breadth or authorize reseeding.

**Validation expectations.** Check same-seed determinism, renamed identities, conflicting claims, dormant/revived institutions, inaccessible artifacts, and PLAY/WATCH/STUDY partitioning; reconcile declared atomic-case counts with the actual suite and report v0.5 prerequisites independently.
