# Experiment Variables

The closed classes are `WORLD`, `AGENT`, `INFORMATION`, `RESOURCE`, `TOOL`, `SOCIAL`, `TEMPORAL`, `PROTOCOL`, and `OBSERVATION`. All claim-bearing independent, dependent, controlled, held-constant, or confound-relevant variables must appear in `specs/experiment-variable-registry.v04.json` with `variable_id`, `version`, `domain`, `measurement`, `mutable`, `allowed_interventions`, `visibility`, and `provenance`.

Plans pin registry-entry versions and may use only allowed intervention types. A nonregistered claim-bearing variable is `INVALID`; unavailable authorized measurement is `NOT_COMPUTABLE`. A supposedly held constant failing boundary verification is recorded as a confound, never silently treated as constant.
