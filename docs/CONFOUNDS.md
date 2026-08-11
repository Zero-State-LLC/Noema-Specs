# Confound Registry

The closed v0.4 registry is `WORLD_STATE_DRIFT`, `AGENT_VERSION_DRIFT`, `PROMPT_DRIFT`, `MEMORY_DRIFT`, `TOOL_VERSION_DRIFT`, `SEED_DIVERGENCE`, `OBSERVATION_MISMATCH`, `PARTICIPANT_MISMATCH`, `RESOURCE_MISMATCH`, `TIMING_MISMATCH`, `PROVIDER_NONDETERMINISM`, and `EXTERNAL_SERVICE_DRIFT`. Each experiment/run records IDs, severity, evidence, boundary dimensions, and disposition. `INFO` preserves context, `MATERIAL` downgrades the named claim, and `SEVERE` is `NOT_COMPARABLE` unless the declared analysis rule requires `INVALID`. Confounds are retained evidence.
