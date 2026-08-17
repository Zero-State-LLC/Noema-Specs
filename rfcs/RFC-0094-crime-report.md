# RFC-0094 — WR-S4 public crime report lines

## Status

**Accepted**

Specification-only until hosted. No NEWS verb. No `REPORT_*`. WATCH silent. No CRIME help. YOUR POSITION / diplomacy stay out. AGREEMENT_FORM stays unthawed.

## Problem

[WR-S3-ACCESS-REPORT.md](../docs/WR-S3-ACCESS-REPORT.md) lists infra, orgs, public contests, and live public access. Public `CRIME_DETECTED` already sits on the hosted social-event cache and never appears on the world report. An implementer would name subjects, methods, or hidden rooms.

## Proposed change

Accept WR-S4. The same 5-cycle last-1 rebuild adds one line per **public** `CRIME_DETECTED` whose room is public:

- `{category} is detected.`
- Category is the catalog enum, lowercased, underscores as spaces
- Public means `flags` includes `PUBLIC_HISTORY` or host `visibility` is `PUBLIC`
- Hidden rooms omitted. Private detections omitted
- Sorted by `detection_id`
- None public → no crime lines
- Projection only. Help unchanged (still no NEWS / CRIME)

Catalog: [`world-report-catalog.wr-s4.json`](../specs/world-report-catalog.wr-s4.json).  
Slice: [WR-S4-CRIME-REPORT.md](../docs/WR-S4-CRIME-REPORT.md).

## Alternatives rejected

| Alternative | Why |
|-------------|-----|
| NEWS verb | Extra command |
| CRIME help | Separate pin; no writer |
| Subject / method / severity | Leak |
| Hidden room | Leak |
| Diplomacy | No agreement store or writer |
| WATCH ticker | Spectator leak |

## Compatibility

Additive crime lines. Worlds ignoring S4 keep S3 reports.

## Data / security

Public detections only. No subject handles. No method. No influence. WATCH silent.

## Validation

`check_wr_s4`: after 5 cycles a public crime line is kept; hidden/private omitted; no new verbs.

## Rollback

Omit crime lines (S3 infra+org+contest+access only).

## Unresolved

Discovery report lines are [RFC-0096](RFC-0096-discovery-report.md). CONTEST help is [RFC-0095](RFC-0095-contest-play-thaw.md). YOUR POSITION. Diplomacy. WED / ATTEST help.
