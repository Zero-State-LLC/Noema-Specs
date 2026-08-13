# Completeness S1 order

**Status:** Recommended specification order after S0. **Not** a runtime thaw.  
**Parent:** [GAME-COMPLETENESS-PLAN.md](GAME-COMPLETENESS-PLAN.md) · [GC-S0-CLOSEOUT-2026-08-13.md](GC-S0-CLOSEOUT-2026-08-13.md)  
**Doctrine:** [COMPLEXITY-DOCTRINE.md](COMPLEXITY-DOCTRINE.md)

S1 slices remain SPEC GAP until each has an Accepted RFC, fixtures, and an explicit implementation pass. This file only ranks them.

## Order

| Rank | Slice | Why this position | Hard deferral |
|------|-------|-------------------|---------------|
| 1 | Archive-claim attestation | Unblocks already-shipped GC6 on Perihelion without a Genesis pack. [RFC-0020](../rfcs/RFC-0020-archive-claim-attest.md) | Not `INSPECT`. Not a content pack |
| 2 | GC5-S1 delay / rumor | Uses existing `MESSAGE` + world-time; no new combat | Not `SHOUT` / `BOARD` as verbs |
| 3 | GC3-S1 betrayal | Needs `AGREEMENT_BROKEN` / `CRIME_DETECTED` already in 0.2 | Not a reputation integer |
| 4 | GC4-S1 named offices | Extends existing org roles | Not `ROLE_*` events |
| 5 | GC6-S1 reconstruction | Compile after claims exist | Not `QUEST` |
| 6 | GC9-S1 tradition | After custom + time | Lore cannot override ledger |
| 7 | GC7-S1 withdraw / GC10-S1 more classes | After isolated contest and one schedule exist | No HP; no Admin spawn |

## Do not start

```text
GC1-S2 mechanical benefits
crypto / wallets / x402
v0.8 Phenomena
production Genesis activate / force-supersede / reseed
Chamber help advertising BUILD / CONTEST / WED / ATTEST
```

GC1-S2 stays deferred: S0/S1 recognition is self-only lines. A cheaper-build or XP-like benefit is an isolated progression tree.

## Runtime rule

Implementing rank 1 still requires a later authorized pass. This document does not ship `COMMIT.ATTEST`.
