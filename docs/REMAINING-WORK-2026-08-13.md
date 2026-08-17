# Remaining work — 2026-08-13

**Status:** Analysis snapshot after S0 closeout. Not a thaw. Not a release.  
**Authority:** [GC-S0-CLOSEOUT-2026-08-13.md](GC-S0-CLOSEOUT-2026-08-13.md) · [GC-S1-ORDER.md](GC-S1-ORDER.md)  
**Hosted evidence:** Noema `docs/RUNTIME-READINESS-2026-08-13.md` · live Perihelion `ACTIVE` / `HEALTHY` / `genesis.ef578f4ffceeccd0` (cycle 0, seq 75 at last check).  
**Supersede (2026-08-17):** live `/ready` is still that genesis, seq **94**, HEALTHY. GC1-S2–S5, GC2 through S24, comms expiry, WR-S0, and first-world BUILD help (RFC-0090) shipped after this snapshot. Do not treat the SQL/bootstrap “blocked” lines below as current.  
**Does not open:** Genesis reseed, crypto, CONTEST / WED / ATTEST help.

Use this file to analyze what is left. Canonical-head Worker code is deployed (Noema #96 / `272a993`). Hosted SQL/RPC apply and isolated-world verification remain open. Perihelion canonical bootstrap remains blocked. GC1-S2 remains DEFERRED.

---

## Already on main (S0 — not remaining)

| Item | Specs | Hosted |
|------|--------|--------|
| GC1-S0 / S1 | RFC-0004 / 0005 | Yes (#68 / #69) |
| GC2-S0 BUILD | RFC-0006 | Yes (#79). Help omits BUILD |
| GC3-S0 | RFC-0007 | Yes (#70) |
| GC3-S1 betrayal | **RFC-0022** | Hosted this run. Danger from `CONTEST_RESOLVED`; no reputation scalar |
| GC4-S0 advisor pin | RFC-0008 | Yes (#71) |
| GC4-S1 named offices | **RFC-0023** | Hosted this run. Persistent vacant/occupied seats; `PUBLISH_NOTICE` only |
| GC4-S2 institution TRADE/REPAIR | **RFC-0029** | Hosted this run. Occupied office + treasury. No new verbs |
| GC4-S3 emergency scopes | **RFC-0030** | Hosted this run. Time-bounded grant overlay. No superuser |
| GC4-S4 designated succession | **RFC-0031** | Hosted this run. Explicit designation only. No implicit jump |
| GC5-S0 MESSAGE bands | RFC-0009 | Yes (#72) |
| GC6-S0 mapper + source | RFC-0010 / **0015** | Mapper yes; **Perihelion silent** until ATTEST |
| GC6-S1 reconstruction | **RFC-0024** | Hosted this run. Player-authored account from accessible archive/inspect |
| GC7-S0 contest | RFC-0011 | Yes (#81). Help omits CONTEST |
| GC7-S1 withdraw | **RFC-0026** | Hosted this run. `CONTEST_RESOLVED` ABORTED/SUCCESS. Help omits CONTEST |
| GC8-S0 costs | RFC-0012 | Already true |
| GC9-S0 custom | RFC-0013 | Yes (#71) |
| GC9-S1 tradition | **RFC-0025** | Hosted this run. CUSTOM plus persistence/transmission. No bonus |
| GC10-S0 pressure | RFC-0014 | Yes (#82). Silent if drop would go below 25 |
| GC10-S1 more classes | **RFC-0027** | Hosted this run. Resource stock + access restriction. S0 remains. No Admin spawn |
| World-time | **RFC-0019** | WAIT quorum (#80) |
| Head + fence | **RFC-0016 / 0017** | Worker shipped; **SQL / RPC apply unverified** |
| Atomic canonical settlement | runtime #96 | Deployed `272a993`. Isolated verification **blocked**. Perihelion bootstrap **blocked** |
| Archive writer pin | **RFC-0018** | INSPECT is not a writer |
| Attest spec | **RFC-0020** | Hosted `COMMIT.ATTEST`. Help omits ATTEST |
| GC5-S1 delay | **RFC-0021** | Hosted this run. 25–49 delays 1 cycle |
| GC5-S2 rumor | **RFC-0028** | Hosted this run. Claim + MESSAGE lineage. No score. Help omits rumor aliases |

Frozen catalogs `action-contracts.v01.json` and `event-types.0.2.json` are unchanged.

---

## Operator (blocks reconstructable heads)

Apply on hosted Postgres (project `dezykkherxlaysxyvgbs` unless Worker `SUPABASE_URL` says otherwise):

```text
Noema/supabase/migrations/20260813210000_noema_world_heads.sql
Noema/supabase/migrations/20260813223000_noema_world_head_fence.sql
Noema/supabase/migrations/20260813233000_noema_atomic_canonical_settlement.sql
```

Until that runs, the deployed #96 Worker fail-closes mutating ACK (`p_allow_bootstrap=false`). Do not fabricate a Perihelion canonical head. Production command routing has no isolated test world.

---

## Spec-ready, not authorized (explicit implementation pass)

Canonical-head infrastructure is implemented and deployed, not hosted-verified. Operator SQL + isolated world path remain. GC1-S2 remains DEFERRED.

---

## SPEC GAP (later RFC)

```text
GC1-S2 mechanical benefits (doctrine DEFER)
canonical-head SQL/RPC apply + isolated verification (operator)
Perihelion canonical bootstrap (blocked: no verified snapshot)
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

1. Operator: apply the three world-head / canonical-settlement SQL files.  
2. Do not bootstrap Perihelion from incomplete legacy events.  
3. Do not implement GC1-S2 benefits.
