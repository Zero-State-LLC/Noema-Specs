# Completeness S1 order

**Status:** Recommended specification order after S0. **Not** a runtime thaw.  
**Parent:** [GAME-COMPLETENESS-PLAN.md](GAME-COMPLETENESS-PLAN.md) · [GC-S0-CLOSEOUT-2026-08-13.md](GC-S0-CLOSEOUT-2026-08-13.md)  
**Doctrine:** [COMPLEXITY-DOCTRINE.md](COMPLEXITY-DOCTRINE.md)

S1 slices remain SPEC GAP until each has an Accepted RFC, fixtures, and an explicit implementation pass. This file only ranks them.

## Order

| Rank | Slice | Why this position | Hard deferral |
|------|-------|-------------------|---------------|
| 1 | Archive-claim attestation | Hosted (RFC-0020). Unblocks GC6 after a Player attests. | Not `INSPECT`. Not a content pack |
| 2 | GC5-S1 delay | [RFC-0021](../rfcs/RFC-0021-relay-message-delay.md). Existing `MESSAGE` + world-time. Rumor is GC5-S2 | Not `SHOUT` / `BOARD` / `RUMOR` |
| 3 | GC3-S1 betrayal | [RFC-0022](../rfcs/RFC-0022-betrayal-dangerous.md). Hosted from `CONTEST_RESOLVED`. Agreement/crime rebuild when those events exist | Not a reputation integer |
| 4 | GC4-S1 named offices | [RFC-0023](../rfcs/RFC-0023-named-offices.md). Persistent vacant/occupied seats on the org. Not membership | Not `ROLE_*` events |
| 5 | GC6-S1 reconstruction | [RFC-0024](../rfcs/RFC-0024-historical-reconstruction.md). Player-authored account from accessible evidence | Not `QUEST` |
| 6 | GC9-S1 tradition | [RFC-0025](../rfcs/RFC-0025-tradition.md). CUSTOM plus persistence/transmission. Lore cannot override ledger | Not a culture score |
| 7 | GC7-S1 withdraw | [RFC-0026](../rfcs/RFC-0026-contest-withdraw.md). Open contest, own participation, `CONTEST_RESOLVED` | No HP; no teleport |
| 8 | GC10-S1 more classes | After isolated contest and one schedule exist | No Admin spawn |

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

Ranks 1–7 are hosted. Later ranks still need their own RFC and an explicit implementation pass. Help still omits ATTEST / BUILD / CONTEST / WED.
