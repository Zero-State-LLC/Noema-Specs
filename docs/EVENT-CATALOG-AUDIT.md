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

### One type is emitted and catalogued nowhere

`TRADE_CANCELLED`. It is in neither `event-types.json` (24 types) nor
`event-types.0.2.json` (31), carries no payload `$def` in either, and is **publicly
projected** — the WATCH feed renders `<who> withdrew a trade`. It has been in the Worker
since 2026-08-12 and has never existed in the offline Python runtime.

This reads as a catalog omission rather than an unauthorized addition:
[GC4-S2-INSTITUTION-ACTIONS.md](GC4-S2-INSTITUTION-ACTIONS.md) §Events already lists
`TRADE_CANCELLED` among *"existing"* types beside the three that are catalogued, so the
specification has been treating it as present for some time. Nothing else in this repository
mentions it — one line, in one slice document.

**Not fixed here.** Adding a type to a closed catalog is what the closure rule exists to make
deliberate: it is `event-catalog/0.3`, or an amendment to 0.2, and either way an RFC decides
it. Dozens of accepted RFCs carry `No event-catalog/0.3` in their scope lines, so this is
not a line to add quietly. Recorded for a maintainer with the evidence attached.

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
