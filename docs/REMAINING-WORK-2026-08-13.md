# Remaining work — 2026-08-13

**Status:** Analysis snapshot after S0 closeout. Not a thaw. Not a release.  
**Authority:** [GC-S0-CLOSEOUT-2026-08-13.md](GC-S0-CLOSEOUT-2026-08-13.md) · [GC-S1-ORDER.md](GC-S1-ORDER.md)  
**Hosted evidence:** Noema `docs/RUNTIME-READINESS-2026-08-13.md` · live Perihelion `ACTIVE` / `HEALTHY` / `genesis.ef578f4ffceeccd0` (cycle 0, seq 75 at last check).  
**Does not open:** Genesis reseed, crypto, SERIALIZABLE cycle fence, GC1-S2 benefits, Chamber help for BUILD / CONTEST / WED / ATTEST.

Use this file to analyze what is left. GC3-S1 (RFC-0022) is authorized and hosted. Later S1s are still SPEC GAP.

---

## Already on main (S0 — not remaining)

| Item | Specs | Hosted |
|------|--------|--------|
| GC1-S0 / S1 | RFC-0004 / 0005 | Yes (#68 / #69) |
| GC2-S0 BUILD | RFC-0006 | Yes (#79). Help omits BUILD |
| GC3-S0 | RFC-0007 | Yes (#70) |
| GC3-S1 betrayal | **RFC-0022** | Hosted this run. Danger from `CONTEST_RESOLVED`; no reputation scalar |
| GC4-S0 advisor pin | RFC-0008 | Yes (#71) |
| GC5-S0 MESSAGE bands | RFC-0009 | Yes (#72) |
| GC6-S0 mapper + source | RFC-0010 / **0015** | Mapper yes; **Perihelion silent** |
| GC7-S0 contest | RFC-0011 | Yes (#81). Help omits CONTEST |
| GC8-S0 costs | RFC-0012 | Already true |
| GC9-S0 custom | RFC-0013 | Yes (#71) |
| GC10-S0 pressure | RFC-0014 | Yes (#82). Silent if drop would go below 25 |
| World-time | **RFC-0019** | WAIT quorum (#80) |
| Head + fence | **RFC-0016 / 0017** | Worker shipped; **SQL may be unapplied** |
| Archive writer pin | **RFC-0018** | INSPECT is not a writer |
| Attest spec | **RFC-0020** | Hosted `COMMIT.ATTEST`. Help omits ATTEST |
| GC5-S1 delay | **RFC-0021** | Hosted this run. 25–49 delays 1 cycle; rumor still out |

Frozen catalogs `action-contracts.v01.json` and `event-types.0.2.json` are unchanged.

---

## Operator (blocks reconstructable heads)

Apply on hosted Postgres:

```text
Noema/supabase/migrations/20260813210000_noema_world_heads.sql
Noema/supabase/migrations/20260813223000_noema_world_head_fence.sql
```

Until that runs, the Worker skips a missing `noema_world_heads` table (404) so PLAY does not fail-close. Events still settle to `noema_settled_events`.

---

## Spec-ready, not authorized (explicit implementation pass)

None remaining from RFC-0022. Later S1 slices still need their own RFCs ([GC-S1-ORDER.md](GC-S1-ORDER.md)).

---

## SPEC GAP (later RFC)

```text
GC5-S2 rumor provenance
GC4-S1 named offices
GC6-S1 reconstruction / GC9-S1 tradition
GC7-S1 withdraw / GC10-S1 more pressure classes
GC1-S2 mechanical benefits (doctrine DEFER)
```

---

## Out unless doctrine changes

```text
crypto / wallets / x402
v0.6B / v0.6C
v0.8 Phenomena
production Genesis activate / force-supersede / reseed
```

---

## Suggested analysis order

1. Operator: confirm or apply the two world-heads SQL files.  
2. Next S1 RFC from [GC-S1-ORDER.md](GC-S1-ORDER.md) (GC4-S1 named offices). Leave unnamed slices as SPEC GAP.  
3. Do not implement GC1-S2 benefits.
