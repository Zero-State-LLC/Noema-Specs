# Confound Registry

The closed v0.4 registry is `WORLD_STATE_DRIFT`, `AGENT_VERSION_DRIFT`, `PROMPT_DRIFT`, `MEMORY_DRIFT`, `TOOL_VERSION_DRIFT`, `SEED_DIVERGENCE`, `OBSERVATION_MISMATCH`, `PARTICIPANT_MISMATCH`, `RESOURCE_MISMATCH`, `TIMING_MISMATCH`, `PROVIDER_NONDETERMINISM`, and `EXTERNAL_SERVICE_DRIFT`. Each experiment/run records IDs, severity, evidence, boundary dimensions, and disposition. `INFO` preserves context, `MATERIAL` downgrades the named claim, and `SEVERE` is `NOT_COMPARABLE` unless the declared analysis rule requires `INVALID`. Confounds are retained evidence.

## Extension Points

Non-normative extension guidance; accepted authority controls.

- **Registry seam:** Extend experiment/run fixtures for each closed v0.4 confound ID with severity, evidence, boundary dimensions, and disposition. A reviewer can link the confound directly to the claim it limits.
- **Invariants:** Retain confounds as evidence. INFO preserves context, MATERIAL downgrades the named claim, and SEVERE yields NOT_COMPARABLE unless the declared analysis rule requires INVALID. No clean-looking summary may erase those distinctions.
- **Compatibility:** New IDs or severity semantics require registry/version authority; do not silently reinterpret old experiment records. Controller access is not research authorization, and experiments with confounds do not run inside production PLAY by virtue of this EP.
- **Verification:** Exercise each severity with an explicitly declared analysis rule, including the SEVERE/INVALID branch; verify retained evidence survives export and comparison. Test an unauthorized viewer and a missing disposition without inventing a benign default.
- **Presentation:** Authorized research tables can localize descriptions while preserving canonical IDs and show severity in text, not color alone. WATCH gets no automatic confound projection or private evidence.
