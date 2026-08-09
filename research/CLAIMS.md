# Claim and Evidence Register

Every study keeps one row per auditable proposition.

| Field | Requirement |
|---|---|
| Claim ID | Stable identifier such as `CLM-001` |
| Exact claim | One bounded, falsifiable sentence |
| Label | Label from `../docs/RESEARCH-METHOD.md` |
| Population | Systems, tasks, settings, and time covered |
| Evidence | Artifact IDs and direct results |
| Controls | Relevant passed and failed controls |
| Uncertainty | Interval, sensitivity, unresolved confounds |
| Provenance | Study version, commit, artifact hashes |
| Reviewer | Independent reviewer and date |
| Status | active, weakened, superseded, or retracted |

Claim promotion requires a new review and never occurs automatically. A failed critical control yields `[INCONCLUSIVE]` until resolved. Contradictory evidence is linked, not deleted. Wording must stay within the evaluated population.

Prefer “system S produced X in Y of N registered trials under condition C” over anthropomorphic interpretation. Separate output, inferred strategy, causal mechanism, and speculation. Do not use “understands,” “believes,” “wants,” “feels,” or “is aware” without an operational definition and claim label.