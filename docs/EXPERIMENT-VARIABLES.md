# Experiment Variables

The closed classes are `WORLD`, `AGENT`, `INFORMATION`, `RESOURCE`, `TOOL`, `SOCIAL`, `TEMPORAL`, `PROTOCOL`, and `OBSERVATION`. All claim-bearing independent, dependent, controlled, held-constant, or confound-relevant variables must appear in `specs/experiment-variable-registry.v04.json` with `variable_id`, `version`, `domain`, `measurement`, `mutable`, `allowed_interventions`, `visibility`, and `provenance`.

Plans pin registry-entry versions and may use only allowed intervention types. A nonregistered claim-bearing variable is `INVALID`; unavailable authorized measurement is `NOT_COMPUTABLE`. A supposedly held constant failing boundary verification is recorded as a confound, never silently treated as constant.

## Extension Points

Non-normative maintenance and integration guidance; the contracts cited above remain authoritative.

### Document-specific seam

Extend plan review with a join from each independent, dependent, controlled, or confound-relevant variable to its pinned registry entry. Show measurement availability and held-constant verification separately from whether intervention is permitted.

### Compatibility and promotion

The nine variable classes, registry versions, allowed_interventions, visibility, and provenance remain authoritative. An unregistered variable is INVALID, not merely missing data; unavailable authorized measurement is NOT_COMPUTABLE. A research registry browser is not a PLAY affordance or Controller privilege.

### Verification before adoption

Test unknown variable_id, incompatible entry version, prohibited intervention, and inaccessible measurement. Include a supposedly held constant that changes at the boundary and require a recorded confound. Validate that translated descriptions retain exact IDs and that revised variable definitions create new claim-bearing experiment identity.
