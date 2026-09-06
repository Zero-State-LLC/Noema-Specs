# Confound Registry

The closed v0.4 registry is `WORLD_STATE_DRIFT`, `AGENT_VERSION_DRIFT`, `PROMPT_DRIFT`, `MEMORY_DRIFT`, `TOOL_VERSION_DRIFT`, `SEED_DIVERGENCE`, `OBSERVATION_MISMATCH`, `PARTICIPANT_MISMATCH`, `RESOURCE_MISMATCH`, `TIMING_MISMATCH`, `PROVIDER_NONDETERMINISM`, and `EXTERNAL_SERVICE_DRIFT`. Each experiment/run records IDs, severity, evidence, boundary dimensions, and disposition. `INFO` preserves context, `MATERIAL` downgrades the named claim, and `SEVERE` is `NOT_COMPARABLE` unless the declared analysis rule requires `INVALID`. Confounds are retained evidence.

## Extension Points

- i18n centralization (STRINGS + t()) for confound registry terms (drift types e.g. WORLD_STATE_DRIFT, severity INFO/MATERIAL/SEVERE, evidence, disposition, boundary dimensions) in Chamber /study /watch UI (evidence tables, anomaly/confound displays).
- R3 Chamber: evidence in STUDY (confounds as retained), projection in WATCH, actions in PLAY (experiment with confounds).
- Gate B: controller access to confound evidence (S0-S3), agent-only analysis, human S0 (read-only WATCH), version comparisons for drift fixtures.
- AX: role="table" / "row" for registry, aria-label for drift types, keyboard nav for lists, live regions for new confounds, contrast on severity badges.
- ui.py / 8765: centralize confound labels, severity via STRINGS.get + t() in templates/JS; dynamic evidence rendering.
- Handoff LCA2 / R3+: agent-only packets include confound registry, plugin atoms for Gate B evidence UI, ties to LCA-2 MUD handoff.
- 9222 CDP: AX tree for evidence lists, focus on confound items, live monitoring for updates, contrast samples.
- Cross-refs: ANOMALY-DETECTION, BEHAVIORAL-ORACLE, DEEPER-ACCEPTANCE-MATRIX, CONTRACT-CARDS (Observation), ARCHAEOLOGY.
- Elevation: UX (clear evidence presentation), DX (modular confound handling), AX (semantic tables + keyboard). Additive only.
