# RFC-0090 — GC2 first-world BUILD help

## Status

**Accepted**

No new BUILD operations. No `STRUCTURE_*`. No `event-catalog/0.3`. CONTEST / WED / ATTEST stay omitted from Chamber help.

## Problem

[CONSTRUCTION.md](../docs/CONSTRUCTION.md) and [PLAYER-ACTION-MAP.md](../docs/PLAYER-ACTION-MAP.md) still call first-world BUILD **UNSUPPORTED** while GC2-S0–S24 are hosted. An implementer would keep the verb secret or invent a second command language.

## Proposed change

Accept first-world PLAY advertising of **existing** BUILD aliases:

- `help` KNOWN COMMANDS names BUILD
- `help build` lists construct / dismantle / upgrade / repurpose / restore / vest / share / connect
- Eight constructible classes already in the catalog
- No new verb, cost, or event
- CONTEST / WED / ATTEST remain unlisted

Catalog: [`construction-catalog.gc2-thaw-play.json`](../specs/construction-catalog.gc2-thaw-play.json).  
Slice: [GC2-THAW-PLAY.md](../docs/GC2-THAW-PLAY.md).

## Alternatives rejected

| Alternative | Why |
|-------------|-----|
| New BUILD verb | Extra command |
| Help CONTEST / WED / ATTEST | Separate pins |
| WATCH construction ticker | Spectator leak |
| Sixth SHARE | Family closed |

## Compatibility

Help-only. Worlds ignoring S0 keep BUILD parsed and unlisted.

## Data / security

No new fields. Hidden rooms unchanged.

## Validation

`check_gc2_thaw_play`: help_build true; CONTEST/WED/ATTEST still false; no new verbs.

## Rollback

Omit BUILD from Chamber help again.

## Unresolved

CONTEST help is [RFC-0095](RFC-0095-contest-play-thaw.md). WED / ATTEST help.
