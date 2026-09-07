# Experience Errors

The machine reason code remains the authority. The user-facing message explains the next safe action without suppressing the code in advanced detail.

| Code | User-facing message |
|---|---|
| `CONTROL_REQUIRED` | This test needs a control run before the result can be interpreted. |
| `NOT_COMPARABLE` | These runs differ in too many important conditions to compare reliably. |
| `NOT_COMPUTABLE` | NOEMA cannot determine this with the available authorized evidence. |
| `UNAUTHORIZED_RESEARCH_DETAIL` | You do not have permission to view this research detail. |
| `LESION_UNSUPPORTED` | This agent does not declare a safe module-disable interface. |
| `BUDGET_EXHAUSTED` | This test reached its declared budget. Completed evidence is preserved. |

[`experience-error-catalog.json`](../specs/experience-error-catalog.json) is the machine-readable mapping. Error translation never turns an invalid, partial, or non-comparable record into a successful result.

## Extension Points (additive, i18n AX R3 Gate B handoff + MUD/PLAY craft per noema-specs-mud-craft)

- **i18n centralization (STRINGS + t() in ui.py/8765 Chamber)**: Keys for "experience_errors", "control_required", "not_comparable", "unauthorized_research_detail", "lesion_unsupported", "budget_exhausted", "experience_error_catalog". Use t() for error tables, codes, messages in Chamber experience/study/capture surfaces, PLAY projections.

- **R3 Chamber (RFC-0120 agent-only Player identity + human S0 withhold)**: Agent experience error handling in PLAY/WATCH/STUDY. Human S0 separate.

- **Gate B S0-S3 + version comparisons**: Error catalog conformance, translation rules, never-success for invalid records. Versioned with experience-error-catalog.json.

- **AX (semantic/ARIA/keyboard/contrast/live regions per omh patterns + CDP)**: Tables for error codes with aria-label, keyboard nav, live regions for messages.

- **Plugin atoms / graft / ops / maint-evolve (noema-specs-mud-craft)**: Atoms for error catalog packs. derive/validate for error types. Graft for catalog traceability.

- **MUD native interaction / PLAY craft / LCA2 handoff (per noema-specs-mud-craft + MUD-PLAY-CRAFT)**: Native i18n for error messages in MUD/PLAY experiences. Handoff to MUD-NATIVE-*, EXPERIENCE.md, PLAYER-*, AGENT-PLAY, LCA2. Cross to prior EPs.

- Cross-refs: EXPERIENCE.md, EVENT-CATALOG.md, MUD-PLAY-CRAFT.md, noema-specs-mud-craft, ui.py, elevation plan, graft, 8765, R3/Gate B, prior full list.
