# Closed Event Catalog Fixtures

These fixtures exercise catalog-specific composed schemas for ledger admission.

| Fixture | Schema |
|---|---|
| `valid-event-catalog-0.1-move.json` | `specs/event-catalog-0.1.schema.json` |
| `valid-event-catalog-0.2-contest-declared.json` | `specs/event-catalog-0.2.schema.json` |
| `valid-event-catalog-0.2-trade-cancelled.json` | `specs/event-catalog-0.2.schema.json` |
| `valid-event-catalog-0.2-crime-detected-public.json` | `specs/event-catalog-0.2.schema.json` (RFC-0129: `victim_id` + `visibility` `PUBLIC` + `PUBLIC_HISTORY`) |
| `valid-event-catalog-0.2-crime-detected-neither.json` | `specs/event-catalog-0.2.schema.json` (RFC-0129: neither `victim_id` nor `visibility`) |

Negative catalog and payload-binding fixtures live under `examples/negative/`.
