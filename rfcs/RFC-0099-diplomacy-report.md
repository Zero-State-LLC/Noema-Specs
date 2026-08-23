# RFC-0099 — WR-S6 public diplomacy report lines

## Status

**Accepted**

No NEWS verb. No `REPORT_*`. WATCH silent. No AGREEMENT help. Other agreement types stay out. YOUR POSITION stays out.

## Problem

[DIPLOMACY-S1.md](../docs/DIPLOMACY-S1.md) can form and break TRADE agreements. Those ACTIVE public records never appear on the world report. An implementer would name parties or list unaccepted offers.

## Proposed change

Accept WR-S6. The same 5-cycle last-1 rebuild adds one line per **ACTIVE** **PUBLIC** agreement:

- `{type} is agreed.`
- Type is the catalog enum, lowercased, underscores as spaces
- `OFFERED` and `BROKEN` omitted
- No party names. No terms
- Sorted by `agreement_id`
- None active → no diplomacy lines
- Projection only. Help unchanged (still no NEWS / AGREEMENT)

Catalog: [`world-report-catalog.wr-s6.json`](../specs/world-report-catalog.wr-s6.json).  
Slice: [WR-S6-DIPLOMACY-REPORT.md](../docs/WR-S6-DIPLOMACY-REPORT.md).

## Alternatives rejected

| Alternative | Why |
|-------------|-----|
| NEWS verb | Extra command |
| AGREEMENT help | Separate pin |
| Party names / terms | Leak |
| Offered / broken | Not live |
| Other types | Later |
| WATCH ticker | Spectator leak |

## Compatibility

Additive diplomacy lines. Worlds ignoring S6 keep S5 reports.

## Data / security

Active public agreements only. No member lists. WATCH silent.

## Validation

`check_wr_s6`: after 5 cycles an active public agreement line is kept; offered/broken omitted; no new verbs.

## Rollback

Omit diplomacy lines (S5 report only).

## Unresolved

Remaining types and AGREEMENT help are [RFC-0100](RFC-0100-diplomacy-closeout.md). YOUR POSITION. WED / ATTEST help.
