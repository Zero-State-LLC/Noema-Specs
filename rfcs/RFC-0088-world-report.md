# RFC-0088 — WR-S0 public world report

## Status

**Accepted**

No `NEWS` / `REPORT` verb. No `event-catalog/0.3`. No `REPORT_*` events. WATCH silent. Help unchanged. Operator Digests stay Admin wall-clock. YOUR POSITION, diplomacy, conflict, and crime sections stay out.

## Problem

[WORLD-REPORTS.md](../docs/WORLD-REPORTS.md) and [GAME-CYCLE.md](../docs/GAME-CYCLE.md) require a periodic public projection so the primary loop’s “news arrive” beat exists. [PLAY.md](../docs/PLAY.md) already sketches a `WORLD` line. Hosted Chamber has none. An implementer would reuse Operator Digests or invent a ticker.

## Proposed change

Accept WR-S0. After **5** committed cycles (`cycle % 5 === 0` and `cycle ≥ 5`), rebuild last **1** public report from current public-room live infrastructure:

- Each line: `{label} condition {n}.`
- Hidden rooms omitted. In-progress shells omitted. Private holdings omitted
- Projection only. No new event. WATCH silent
- PLAY `report_lines`. Absent before the first interval
- No new verb. Chamber help unchanged
- Interval other than 5 is out of slice

Catalog: [`world-report-catalog.wr-s0.json`](../specs/world-report-catalog.wr-s0.json).  
Slice: [WR-S0-WORLD-REPORT.md](../docs/WR-S0-WORLD-REPORT.md).

## Alternatives rejected

| Alternative | Why |
|-------------|-----|
| Operator Digest reuse | Admin wall-clock, not world-time |
| NEWS / REPORT verb | Extra command |
| `REPORT_*` event | Extra catalog |
| WATCH ticker | Spectator leak before play exists |
| YOUR POSITION | Already budgets / status |
| Diplomacy / conflict / crime sections | Later slices |
| Interval ≠ 5 | Extra machinery |
| Help news | S0 pin family |

## Compatibility

Additive projection. Worlds ignoring S0 keep no `report_lines`.

## Data / security

Public live infrastructure condition only. Hidden rooms store none. WATCH silent.

## Validation

`check_wr_s0`: after 5 committed cycles a public infra line is kept; before interval none; hidden infra omitted; no new verbs.

## Rollback

Ignore report rebuild (no `report_lines`).

## Unresolved

YOUR POSITION block. Diplomacy / conflict / crime / access sections. SHARE family closeout is [RFC-0089](RFC-0089-share-closeout.md).
