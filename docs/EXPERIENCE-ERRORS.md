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

