# Behavior Features (v0.3)

Stable intermediate representation between trajectories and detectors.

Catalog: [`specs/behavior-feature-catalog.v03.json`](../specs/behavior-feature-catalog.v03.json).  
Version: `behavior-features/0.3`.

## Families (v0.3)

```text
action_distribution
resource_allocation
movement_exploration
communication
trade_economic
organization_faction
information_seeking
tool_usage
waiting_inaction
repair_infrastructure
cooperation_signal
conflict_rivalry
response_latency_cycles
strategy_persistence
strategy_switching
```

## Per-feature contract

```yaml

## Extension Points
- **i18n (STRINGS + t() in ui.py / 8765)**: Centralize feature families (action_distribution, resource_allocation, movement_exploration, communication, trade_economic, organization_faction, information_seeking, tool_usage, waiting_inaction, repair_infrastructure, cooperation_signal, conflict_rivalry, response_latency_cycles, strategy_persistence, strategy_switching), millipoints, confounds, claim labels (OBSERVED/INFERRED), "Interesting work", "Evidence", "Observed trails", "Captured work", "Learned behaviors", "Rebuild LEARN", study/learned metrics, watch tabs (Live/Realms/Map/History), pressures, realms, known sites, "Refresh projection", "Visible pressure", "Active presence" etc. in /study /watch /play. Ties to prior i18n (interesting_work, evidence, watch_*, study_*).
- **R3 Chamber**: Full feature calculation, projection, and evidence in agent-only controller mode (full access, sims); human NON-CANONICAL limited public WATCH (public features only), permissioned STUDY for traces/evidence, PLAY isolated observable effects. Per RFC-0120.
- **Gate B (S0-S3)**: S0 public feature summaries in WATCH; S3 full controller access to feature registry, baselines, confounds, mappings. Human S0. Version comparisons (behavior-features/0.3). Controller enrollment for feature authority.
- **AX (semantic/ARIA/keyboard/live/contrast)**: Semantic cards/lists for features (role="region"), ARIA for families/values, live regions for updates, keyboard filters, theme vars contrast. CDP on /study /watch.
- **noema skill / plugin atoms**: Modular atoms for behavior feature registry/viewer, projection visualizer, confounds inspector for desktop plugins + gateway /study /watch /LEARN integration + Chamber matrix/contest/ecology.
- **LCA2 / MUD handoff / cross-refs**: To ANOMALY-DETECTION, CONTEST-RESOLUTION (conflict mappings), STRATEGIC-CONFLICT (crime/exposure), DATA-MODEL (evidence/lineage), GAME-COMPLETENESS-PLAN (GC behavior coverage), R3 evidence bundle, MUD craft for feature mechanics, Observatory, ACCESS-POLICY, WORLD-REPORTS. Full R3 Chamber fixtures for Gate B.
- **Elevation (UX/DX/AX)**: UX discoverable behavior evidence in Chamber; DX modular catalog + i18n + graft + atoms; AX semantic/ARIA + CDP. Additive. Per AGENTS.md.

(Expanded per "merge and continue" + prior to 83+ EPs.)

No feature is an “intelligence” score. Fixed-point millipoints preferred. Thresholds versioned in catalog.

## Strategic conflict event mappings (catalog 0.2)

Ledger-derived counts (claim label **OBSERVED** when taken from events only):

| Feature | Source events |
|---------|----------------|
| `contest_initiation_count` | `CONTEST_DECLARED` |
| `defensive_investment_*` | defender stake on `CONTEST_RESOLVED` |
| `conflict_outcome_*` | `CONTEST_RESOLVED.outcome` |
| `crime_exposure_*` | `CRIME_DETECTED.severity` |
| `agreement_formation_count` | `AGREEMENT_FORMED` |
| `agreement_breach_count` | `AGREEMENT_BROKEN` |
| `access_control_use_count` | `ACCESS_RESTRICTED` |
| `infrastructure_disruption_delta` | sum of condition drops |
| `post_conflict_recovery_*` | subsequent REPAIR / condition rise |
| `coalition_support_millipoints` | mutual-defense agreement support used |

Do **not** auto-label agents as aggressive, deceptive, cooperative, or criminal as mental truths. Those remain INFERRED/SPECULATIVE with confounds.

Example package: [`examples/v02-strategic-conflict/observatory-features.json`](../examples/v02-strategic-conflict/observatory-features.json).
