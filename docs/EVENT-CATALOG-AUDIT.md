# Event Catalog Audit Notes (Game Design)

## Closed v0.1 catalog

The v0.1 Chamber closed catalog remains **24 types** ([EVENT-CATALOG.md](EVENT-CATALOG.md), `specs/event-types.json`). No casual additions.

## v0.2 RFC candidates required by completed design

| Event | Purpose |
|-------|---------|
| `CONTEST_DECLARED` | Begin strategic contestation |
| `CONTEST_RESOLVED` | Record outcome and resource commitments |
| `CRIME_DETECTED` | Ledger detection of unauthorized action |
| `ACCESS_RESTRICTED` | Temporary or policy-based access change |
| `INFRASTRUCTURE_DISRUPTED` | Explicit sabotage/contest result on condition |
| `AGREEMENT_FORMED` | Formal diplomatic contract |
| `AGREEMENT_BROKEN` | Formal breach with consequences |

These will be introduced only through the normal RFC process and will not silently expand Chamber acceptance criteria.

**RFC:** [RFC-0002](../rfcs/RFC-0002-strategic-contestation-and-crime-events.md) — **Draft** with full payload sketches, reducer preconditions, coupling rules, and worked sequence. Target catalog pin: `event-catalog/0.2`. Machine-readable schemas and fixtures are still required before **Accepted**.

## Interim expressibility

Until RFC-0002 is Accepted and schemas land, soft effects may map to existing types where legitimate (`ENTITY_UPDATE`, `BUDGET_CONSUMED`, `ORG_MEMBER_REMOVE`, messages/documents). Do not overload types to invent unstated semantics.
