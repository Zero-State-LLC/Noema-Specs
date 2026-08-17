# RFC-0093 — WR-S3 public access report lines

## Status

**Accepted**

Specification-only until hosted. No NEWS verb. No `REPORT_*`. WATCH silent. No ACCESS_POLICY help. YOUR POSITION / diplomacy / crime stay out.

## Problem

[WR-S2-CONTEST-REPORT.md](../docs/WR-S2-CONTEST-REPORT.md) lists infra, orgs, and public contests. Live `access_restrictions` already change movement and never appear on the world report. An implementer would name hidden rooms or copy Operator Digests.

## Proposed change

Accept WR-S3. The same 5-cycle last-1 rebuild adds one line per **live** access restriction on a **public** room:

- EXIT: `{room name} {direction} is restricted.`
- ROOM: `{room name} is restricted.`
- Live means `cycle <= expires_cycle`
- Hidden rooms omitted. Expired omitted
- Sorted by `restriction_id`
- None live → no access lines
- Projection only. Help unchanged (still no NEWS / ACCESS_POLICY)

Catalog: [`world-report-catalog.wr-s3.json`](../specs/world-report-catalog.wr-s3.json).  
Slice: [WR-S3-ACCESS-REPORT.md](../docs/WR-S3-ACCESS-REPORT.md).

## Alternatives rejected

| Alternative | Why |
|-------------|-----|
| NEWS verb | Extra command |
| ACCESS_POLICY help | Separate pin |
| Hidden room | Leak |
| Party / applies_to names | Leak |
| Diplomacy / crime | Later |
| WATCH ticker | Spectator leak |

## Compatibility

Additive access lines. Worlds ignoring S3 keep S2 reports.

## Data / security

Public live restrictions only. No member lists. WATCH silent.

## Validation

`check_wr_s3`: after 5 cycles a live public restriction line is kept; hidden/expired omitted; no new verbs.

## Rollback

Omit access lines (S2 infra+org+contest only).

## Unresolved

Crime report lines are [RFC-0094](RFC-0094-crime-report.md). YOUR POSITION. Diplomacy. CONTEST help.
