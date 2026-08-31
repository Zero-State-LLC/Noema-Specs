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

**2026-08-24.** The runtime follow-up landed in Noema #534: `TRADE_CANCELLED`
is no longer in `KNOWN_UNCATALOGUED`. `CRIME_DETECTED` stays unproduced /
PARTIAL. This audit does not wire Detection.

### `CRIME_DETECTED` payload fields (RFC-0129)

**RFC:** [RFC-0129](../rfcs/RFC-0129-crime-detected-payload-reconciliation.md) — **Accepted**.
Amends `CRIME_DETECTED_payload` on `event-catalog/0.2` with optional `victim_id`
and `visibility` (`PARTIES` \| `PUBLIC`). `visibility` has no default. A producer
that sets `PUBLIC_HISTORY` or `visibility` `PUBLIC` MUST set both. Catalog stays
32 types. Chamber 0.1 stays 24. No producer, verb, Genesis, or sanction retune.
Closes `B7a`. Detection remains unwired; `B7b`–`B7e` stay open.

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

**2026-08-25 — answered: a slice not yet wired.** The second branch is eliminated.
`CRIME_DETECTED` appears nowhere in the offline Python runtime (`src/noema/`) and is not among
the 24 types of `event-catalog/0.1` ([event-types.json](../specs/event-types.json)). It exists
only in `event-catalog/0.2`, consumed by the hosted Worker and produced by nothing, in either
plane. The `visibility` / `victim_id` payload gap is closed by RFC-0129 on
`event-catalog/0.2`. Detection remains unwired; see
[Research Assimilation — Crime](RESEARCH-ASSIMILATION-2026-08-25-CRIME.md)
and `B7b`–`B7e` in [SPEC-GAP-REGISTER-2026-08-25.md](SPEC-GAP-REGISTER-2026-08-25.md).
