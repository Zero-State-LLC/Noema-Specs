# RFC-0096 — WR-S5 public discovery report lines

## Status

**Accepted**

Specification-only until hosted. No NEWS verb. No `REPORT_*`. WATCH silent. No QUEST help. YOUR POSITION / diplomacy stay out. AGREEMENT_FORM stays unthawed.

## Problem

[WR-S4-CRIME-REPORT.md](../docs/WR-S4-CRIME-REPORT.md) lists infra, orgs, contests, access, and public crime. Public reconstructions already sit on the world and never appear on the world report. An implementer would copy claim text, name authors, or treat open trades as public.

## Proposed change

Accept WR-S5. The same 5-cycle last-1 rebuild adds one line per **public** `RECORDED` reconstruction whose subject is public:

- `{label} is reconstructed.`
- Label is the public entity or room name for `subject_ref`
- `PUBLIC` + `RECORDED` only. PRIVATE / INSTITUTIONAL / SUPERSEDED omitted
- Hidden rooms and hidden entities omitted
- No claim text. No author. No evidence list
- Sorted by `reconstruction_id`
- None public → no discovery lines
- Projection only. Help unchanged (still no NEWS / QUEST)

Catalog: [`world-report-catalog.wr-s5.json`](../specs/world-report-catalog.wr-s5.json).  
Slice: [WR-S5-DISCOVERY-REPORT.md](../docs/WR-S5-DISCOVERY-REPORT.md).

## Alternatives rejected

| Alternative | Why |
|-------------|-----|
| NEWS verb | Extra command |
| QUEST help | Closed pin |
| Claim / author / evidence | Leak |
| Open TRADE rows | Dyadic, not public |
| Diplomacy | No agreement store |
| WATCH ticker | Spectator leak |

## Compatibility

Additive discovery lines. Worlds ignoring S5 keep S4 reports.

## Data / security

Public recorded reconstructions only. No claim text. WATCH silent.

## Validation

`check_wr_s5`: after 5 cycles a public reconstruction line is kept; hidden/private omitted; no new verbs.

## Rollback

Omit discovery lines (S4 infra+org+contest+access+crime only).

## Unresolved

Diplomacy S0 is [RFC-0097](RFC-0097-diplomacy-trade.md). YOUR POSITION. WED / ATTEST help.
