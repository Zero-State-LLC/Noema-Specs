# RFC-0095 — GC7 first-world CONTEST help

## Status

**Accepted**

Specification-only until hosted. No new contest forms. No HP. No `SCAN` / `ATTACK`. WED / ATTEST stay omitted from Chamber help.

## Problem

[GC7-FIRST-SLICE.md](../docs/GC7-FIRST-SLICE.md) through [GC7-S3-INFORMATION-CONTEST.md](../docs/GC7-S3-INFORMATION-CONTEST.md) are hosted, and PLAY already parses `contest` / `defend` / `withdraw`. Chamber help still hides them. An implementer would keep the verb secret or invent a second command language.

## Proposed change

Accept first-world PLAY advertising of **existing** CONTEST aliases:

- `help` KNOWN COMMANDS names CONTEST
- `help contest` lists contest / defend / withdraw
- Five closed forms already hosted
- No new verb, form, cost, or event
- WED / ATTEST remain unlisted
- No HP. No scan or attack

Catalog: [`conflict-catalog.gc7-thaw-play.json`](../specs/conflict-catalog.gc7-thaw-play.json).  
Slice: [GC7-THAW-PLAY.md](../docs/GC7-THAW-PLAY.md).

## Alternatives rejected

| Alternative | Why |
|-------------|-----|
| New CONTEST verb | Extra command |
| Help WED / ATTEST | Separate pins |
| HP / SCAN / ATTACK | Combat subsystem |
| WATCH contest ticker | Spectator leak |
| Diplomacy help | No AGREEMENT_FORM |

## Compatibility

Help-only. Worlds ignoring S0 keep CONTEST parsed and unlisted.

## Data / security

No new fields. Hidden rooms unchanged.

## Validation

`check_gc7_thaw_play`: help_contest true; WED/ATTEST still false; no new verbs; no HP.

## Rollback

Omit CONTEST from Chamber help again.

## Unresolved

WED / ATTEST help. Diplomacy. YOUR POSITION.
