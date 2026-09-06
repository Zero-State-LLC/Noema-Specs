# Capability Candidates (v0.3)

Hypothesis generated from evidence patterns. **Not** Capability Graph. **Not** proof.

Schema: [`specs/capability-candidate.schema.json`](../specs/capability-candidate.schema.json).

## Fields

```text
candidate_capability_id
capability_primitive_id?          # if matched known primitive
novel_unknown_marker?              # UNKNOWN_CAPABILITY_<id>
supporting_anomaly_refs[]
behavior_shift_refs[]
trajectory_refs[]
observed_conditions
counterexamples[]
confounds[]
generalization_unknowns[]
replication_required: true
status
claim_label                         # typically SPECULATIVE or INFERRED
```

## Classes

* `KNOWN_PRIMITIVE_CANDIDATE` — maps to CAPABILITY-PRIMITIVES id  
* `UNKNOWN_CAPABILITY_<id>` — must not force ontology mapping  

Status remains unvalidated until later Lab evidence. Observatory does not emit world-truth capability labels.

## Extension Points

- **i18n (STRINGS + t() in ui.py / 8765)**: Centralize any capability candidate labels, status (SPECULATIVE/INFERRED), claim_label, UNKNOWN_CAPABILITY_*, supporting_anomaly etc. for Chamber /watch /study surfaces and admin. Add keys for "capability_candidate", "supporting_anomaly", "replication_required", "status_speculative" etc. Cross to existing players_label/world_label etc.
- **R3 Chamber**: Capability candidates feed STUDY evidence, WATCH public projection (agent-only per RFC-0120), PLAY discovery of novel capabilities. Agents discover/observe candidates in behavior; humans watch only (NON-CANONICAL for Chamber).
- **Gate B controller independence / access S0-S3**: Controller enrollment can surface candidate capabilities for operators (S2/S3 ALLOW_ONLY); human S0 limited to WATCH public view of known capabilities. Version comparison for evidence.
- **AX (browser_exec / CDP 9222 / proxy)**: Use semantic (table, list, dl for fields/classes), aria-label on candidates, keyboard navigation, live regions for status updates, contrast via theme vars. Screen-reader friendly lists.
- **noema skill / plugin atoms for Gate B**: Modular atoms for capability registry UI (desktop plugin pane or gateway /admin view): list candidates, filter by status, link to anomalies. Reusable for controller status, evidence.
- **handoff / LCA2-MUD**: Tie to R3 handoff map; candidates in runtime fixtures for STUDY/PLAY. Elevation: UX (discoverable evidence), DX (modular schema + EPs), AX (semantic).
- Cross-refs: ANOMALY-DETECTION.md, BEHAVIORAL-*, ARCHITECTURE.md, CHAMBER-MAP.md, COMMAND-DISCOVERY.md, CONTRACT-CARDS.md, ui.py, 8765, chrome-profiles 9222, graft savings. Additive per AGENTS.md.
