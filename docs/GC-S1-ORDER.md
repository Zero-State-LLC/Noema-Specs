# Completeness S1 order

**Status:** Recommended specification order after S0. **Not** a runtime thaw.  
**Parent:** [GAME-COMPLETENESS-PLAN.md](GAME-COMPLETENESS-PLAN.md) · [GC-S0-CLOSEOUT-2026-08-13.md](GC-S0-CLOSEOUT-2026-08-13.md)  
**Doctrine:** [COMPLEXITY-DOCTRINE.md](COMPLEXITY-DOCTRINE.md)

S1 slices remain SPEC GAP until each has an Accepted RFC, fixtures, and an explicit implementation pass. This file only ranks them.

## Order

| Rank | Slice | Why this position | Hard deferral |
|------|-------|-------------------|---------------|
| 1 | Archive-claim attestation | Hosted (RFC-0020). Unblocks GC6 after a Player attests. | Not `INSPECT`. Not a content pack |
| 2 | GC5-S1 delay | [RFC-0021](../rfcs/RFC-0021-relay-message-delay.md). Existing `MESSAGE` + world-time. | Not `SHOUT` / `BOARD` / `RUMOR` |
| 2b | GC5-S2 rumor | [RFC-0028](../rfcs/RFC-0028-rumor-provenance.md). Claim + MESSAGE lineage. Not truth | Not `RUMOR` verb / score |
| 3 | GC3-S1 betrayal | [RFC-0022](../rfcs/RFC-0022-betrayal-dangerous.md). Hosted from `CONTEST_RESOLVED`. Agreement/crime rebuild when those events exist | Not a reputation integer |
| 4 | GC4-S1 named offices | [RFC-0023](../rfcs/RFC-0023-named-offices.md). Persistent vacant/occupied seats on the org. Not membership | Not `ROLE_*` events |
| 5 | GC6-S1 reconstruction | [RFC-0024](../rfcs/RFC-0024-historical-reconstruction.md). Player-authored account from accessible evidence | Not `QUEST` |
| 6 | GC9-S1 tradition | [RFC-0025](../rfcs/RFC-0025-tradition.md). CUSTOM plus persistence/transmission. Lore cannot override ledger | Not a culture score |
| 7 | GC7-S1 withdraw | [RFC-0026](../rfcs/RFC-0026-contest-withdraw.md). Open contest, own participation, `CONTEST_RESOLVED` | No HP; no teleport |
| 8 | GC10-S1 more classes | [RFC-0027](../rfcs/RFC-0027-additional-world-pressure.md). Existing events; S0 remains valid | No Admin spawn |

## Do not start

```text
crypto / wallets / x402
v0.8 Phenomena
production Genesis activate / force-supersede / reseed
Chamber help advertising WED / ATTEST
```

GC1-S2 same-asset Engineer quality is hosted (RFC-0040). GC1-S3 decay is [RFC-0043](../rfcs/RFC-0043-mastery-decay.md). GC1-S4 prior-work Explorer/Surveyor/Broker benefits are [RFC-0044](../rfcs/RFC-0044-prior-work-benefits.md). GC1-S5 office eligibility is [RFC-0055](../rfcs/RFC-0055-office-eligibility.md). GC1-S6 public titles is [RFC-0105](../rfcs/RFC-0105-public-titles.md). Remaining GC1 (focus) stays later.

## Runtime rule

Ranks 1–8 plus GC5-S2 are hosted. GC1-S2 / GC1-S3 are specified (S3 hosted with RFC-0043). GC3-S2–S6 (RFC-0034–0038) are specified. ACCESS_POLICY S0–S3 is hosted (RFC-0101–0104). Chamber help names BUILD, CONTEST, AGREEMENT, and ACCESS. WED / ATTEST stay omitted.
