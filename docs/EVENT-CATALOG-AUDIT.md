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

**RFC:** [RFC-0002](../rfcs/RFC-0002-strategic-contestation-and-crime-events.md) — **Accepted**. Catalog: [`event-types.0.2.json`](../specs/event-types.0.2.json). Fixtures: [`examples/v02-strategic-conflict/`](../examples/v02-strategic-conflict/). Conformance: S01–S18.

## Interim expressibility (0.1 worlds)

Worlds pinned to `event-catalog/0.1` may still map soft effects to existing types where legitimate. Do not overload types to invent unstated semantics. Prefer migrating to 0.2 for true contestation/crime/agreements.

## Closed-catalog conformance against the hosted Worker (2026-08-24)

The closure rule — *expand event types only via RFC*
([SPEC-FREEZE-CORE-LOOP.md](SPEC-FREEZE-CORE-LOOP.md) §5.8) — had never been checked against a
runtime. Checked now, by scanning every `pushEvent` call site in `workers/noema/src` against
`x-noema-event-types` in both catalogs. Noema #527 keeps it checked.

### `TRADE_CANCELLED` is catalogued on 0.2 (RFC-0127)

The 2026-08-24 Worker scan found `TRADE_CANCELLED` emitted, publicly projected
(WATCH: `<who> withdrew a trade`), and missing from both catalogs. That omission
is closed.

**RFC:** [RFC-0127](../rfcs/RFC-0127-trade-cancelled-catalog.md) — **Accepted**.
Amends `event-catalog/0.2` (32 types = 24 + 7 + 1). Does not open
`event-catalog/0.3`. Chamber `event-types.json` stays 24. Payload `$def`:
`trade_id`, `by`, `reason` (`CANCELLED`).

[GC4-S2-INSTITUTION-ACTIONS.md](GC4-S2-INSTITUTION-ACTIONS.md) §Events already
listed the type as existing. The RFC makes that true in the machine catalog.

Runtime follow-up lives in Noema, not this repository: drop `TRADE_CANCELLED`
from `KNOWN_UNCATALOGUED` in `workers/noema/test/closed-catalog.test.ts` after
this RFC is on Specs `main`.

### Five catalogued types the hosted Worker never emits

Not defects, and worth writing down so the next audit does not re-derive them:

| Type | Why |
|---|---|
| `BUDGET_EXCEEDED`, `MOVE_REJECTED` | Refusal **codes** passed to `fail()`, not ledger events |
| `SITUATION_INJECTED`, `NOISE_APPLIED` | Offline research spine — Frontier and the noise model are not hosted ([STUDY.md](STUDY.md)) |
| `CRIME_DETECTED` | Consumed by `social-memory.ts` and the WATCH projection, never produced by the Worker |

`CRIME_DETECTED` is the odd one. The hosted world carries the machinery to interpret it —
danger evidence, a public projection, a world-report filter — and no path that emits it. That
is either a slice not yet wired or an event only the offline runtime raises; this audit did
not determine which, and the answer is not in this repository.
