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

## Extension Points

Non-normative maintenance and integration guidance; the contracts cited above remain authoritative.

### Document-specific seam

Extend the research error presentation with safe recovery guidance for missing controls, incomparable runs, unavailable evidence, unsupported lesions, and exhausted budgets. Keep the machine code available in advanced detail and retain completed evidence when a budget stops work.

### Compatibility and promotion

The experience-error catalog owns the mapping; this is not the ordinary PLAY command-error catalog. Translation must preserve invalid/partial/incomparable outcomes and cannot disclose unauthorized research detail. New codes or semantics require catalog/version review, not an ad-hoc localized string.

### Verification before adoption

Check every listed code against the machine catalog, including missing translation fallback and unauthorized-detail redaction. Verify a budget-exhausted result remains incomplete rather than successful. In a future UI audit, test keyboard recovery controls and announced errors without moving focus or leaking hidden diagnostic content.
