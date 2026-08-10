# Event Catalog Audit Notes (Game Design)

## Closed v0.1 catalog

The v0.1 Chamber closed catalog remains **24 types** ([EVENT-CATALOG.md](EVENT-CATALOG.md), `specs/event-types.json`). No casual additions.

## New events required only for v0.2 contestation and crime (RFC)

| Event type | Purpose |
|------------|---------|
| `CONTEST_DECLARED` | Formal contestation start |
| `CONTEST_RESOLVED` | Contestation outcome |
| `CRIME_DETECTED` | Crime detection record |
| `ACCESS_RESTRICTED` | Temporary access/route restriction |
| `INFRASTRUCTURE_DISRUPTED` | Sabotage/disruption outcome |

Exact schemas and reducers require an accepted RFC before implementation.

## Interim expressibility

Until RFC, soft effects may map to existing types where legitimate (`ENTITY_UPDATE`, `BUDGET_CONSUMED`, `ORG_MEMBER_REMOVE`, messages/documents). Do not overload types to invent unstated semantics.
