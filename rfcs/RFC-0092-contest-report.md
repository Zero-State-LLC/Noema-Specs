# RFC-0092 — WR-S2 public contest report lines

## Status

**Accepted**

No NEWS verb. No `REPORT_*`. WATCH silent. Chamber help still omits CONTEST. YOUR POSITION / diplomacy / crime / access stay out.

## Problem

[WR-S1-ORG-REPORT.md](../docs/WR-S1-ORG-REPORT.md) lists infrastructure and ACTIVE orgs. Open public contests are already projected on PLAY and never appear on the world report. An implementer would invent a ticker or list hidden rooms.

## Proposed change

Accept WR-S2. The same 5-cycle last-1 rebuild adds one line per **OPEN** contest in a **public** room:

- `{form} is contested.` where `form` is `contest_form` with `_` → space, lowercased
- Hidden-room contests omitted
- Sorted by `contest_id`
- No open public contests → no contest lines
- Projection only. No new event. Help still omits CONTEST

Catalog: [`world-report-catalog.wr-s2.json`](../specs/world-report-catalog.wr-s2.json).  
Slice: [WR-S2-CONTEST-REPORT.md](../docs/WR-S2-CONTEST-REPORT.md).

## Alternatives rejected

| Alternative | Why |
|-------------|-----|
| NEWS verb | Extra command |
| Help CONTEST | Separate pin |
| WATCH ticker | Spectator leak |
| Crime / access / diplomacy | Later |
| Hidden-room contest | Leak |

## Compatibility

Additive contest lines. Worlds ignoring S2 keep S1 infra+org reports.

## Data / security

Public OPEN contests only. No stakes, ids, or parties. WATCH silent.

## Validation

`check_wr_s2`: after 5 cycles a public OPEN contest line is kept; hidden-room contest omitted; no new verbs.

## Rollback

Omit contest lines (S1 infra+org only).

## Unresolved

Access report lines are [RFC-0093](RFC-0093-access-report.md). YOUR POSITION. Diplomacy / crime. CONTEST help.
