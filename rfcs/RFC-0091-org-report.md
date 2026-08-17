# RFC-0091 — WR-S1 organization report lines

## Status

**Accepted**

Specification-only until hosted. No NEWS verb. No `REPORT_*`. WATCH silent. YOUR POSITION / diplomacy / conflict / crime / access stay out. BUILD help stays [RFC-0090](RFC-0090-build-play-thaw.md).

## Problem

[WR-S0-WORLD-REPORT.md](../docs/WR-S0-WORLD-REPORT.md) reports public infrastructure only. Organizations exist and are public identity. An implementer would invent a ticker or Operator Digest line.

## Proposed change

Accept WR-S1. The same 5-cycle last-1 rebuild adds one line per `ACTIVE` organization:

- `{name} stands.`
- Sorted by `org_id`
- Infra lines unchanged
- No orgs → no org lines
- Projection only. WATCH silent. No NEWS verb

Catalog: [`world-report-catalog.wr-s1.json`](../specs/world-report-catalog.wr-s1.json).  
Slice: [WR-S1-ORG-REPORT.md](../docs/WR-S1-ORG-REPORT.md).

## Alternatives rejected

| Alternative | Why |
|-------------|-----|
| NEWS verb | Extra command |
| WATCH ticker | Spectator leak |
| Diplomacy / conflict sections | Later |
| YOUR POSITION | Already status |

## Compatibility

Additive org lines on the existing report. Worlds ignoring S1 keep infra-only reports.

## Data / security

Public ACTIVE org names only. No member lists. WATCH silent.

## Validation

`check_wr_s1`: after 5 cycles a public org line is kept with infra; hidden infra omitted; no new verbs.

## Rollback

Omit org lines (S0 infra only).

## Unresolved

YOUR POSITION. Diplomacy / conflict / crime / access. CONTEST help.
