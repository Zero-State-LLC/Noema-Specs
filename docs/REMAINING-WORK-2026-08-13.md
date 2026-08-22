# Remaining work — 2026-08-13

**Status:** Analysis snapshot after S0 closeout. Not a thaw. Not a release.  
**Authority:** [GC-S0-CLOSEOUT-2026-08-13.md](GC-S0-CLOSEOUT-2026-08-13.md) · [GC-S1-ORDER.md](GC-S1-ORDER.md)  
**Hosted evidence:** Noema `docs/RUNTIME-READINESS-2026-08-13.md` · live Perihelion `ACTIVE` / `HEALTHY` / `genesis.ef578f4ffceeccd0` (cycle 0, seq 75 at last check).  
**Supersede (2026-08-17):** live `/ready` is still that genesis, seq **94**, HEALTHY. GC1-S2–S5, GC2 through S24, comms expiry, WR-S0, and first-world BUILD help (RFC-0090) shipped after this snapshot. Do not treat the SQL/bootstrap “blocked” lines below as current.  
**Supersede (2026-08-18 OBSERVED):** `GET https://noema.guru/ready` is `ACTIVE` / `HEALTHY`, cycle 105, sequence **303**, same genesis. Production head + RPCs are present (Noema `docs/DATA-STORES.md`). Residual is isolated `test.hosted-canonical.*` re-runnable proof — not “production head missing.” Do not Recover again. Do not reseed.  
**Supersede (2026-08-19 OBSERVED):** Isolated Worker/DO/SQL proof shipped (Noema #318 INSPECT 200 on `inspect-s0`; #320 SQL-head inspect). Perihelion SQL head matches `/ready` (105/307/rev 176). Do **not** apply the world-head SQL files — hosted objects already exist. Do not Recover. Do not reseed.  
**Supersede (2026-08-20):** MUD Play Craft companion is **specs-complete** (C1–C9; C2 sketch-only). Runtime work is phased R0–R5 in [MUD-PLAY-CRAFT-CLOSEOUT.md](MUD-PLAY-CRAFT-CLOSEOUT.md) — presentation/client first; optional C2 wire RFC only if needed. Native Interaction S0–S7 remain the implementation task list. Do not treat craft as open Specs backlog. Do not reseed for craft.  
**Supersede (2026-08-20 thaw):** hosted-alpha + first-world operational freeze **thawed**. Ranked remaining work: [REMAINING-WORK-2026-08-20.md](REMAINING-WORK-2026-08-20.md). RFC-0120 stays law. Do not reseed in the thaw PR.  
**Does not open:** Genesis reseed, crypto, CONTEST / WED / ATTEST help.

Use this file to analyze what is left. Canonical-head Worker code is deployed (Noema #96 / `272a993`). Production SQL/RPC apply is OBSERVED done. Isolated-world verification is shipped. Perihelion canonical bootstrap is **not** the residual (head adopted). GC1-S2 same-asset Engineer quality is hosted (RFC-0040). Later GC1 (parameter-access) stays later. Host STUDY stays stub.

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
| Head + fence | **RFC-0016 / 0017** | Worker shipped; hosted SQL/RPC **present** (2026-08-17 SQL + 2026-08-18 `/ready`) |
| Atomic canonical settlement | runtime #96 | Deployed. Isolated `test.hosted-canonical.*` proof is the residual. Perihelion head **present** — do not bootstrap |
| Archive writer pin | **RFC-0018** | INSPECT is not a writer |
| Attest spec | **RFC-0020** | Hosted `COMMIT.ATTEST`. Help omits ATTEST |
| GC5-S1 delay | **RFC-0021** | Hosted this run. 25–49 delays 1 cycle |
| GC5-S2 rumor | **RFC-0028** | Hosted this run. Claim + MESSAGE lineage. No score. Help omits rumor aliases |

Frozen catalogs `action-contracts.v01.json` and `event-types.0.2.json` are unchanged.

---

## Operator (historical — do not apply)

The three world-head / canonical-settlement SQL files are on disk. Hosted objects (tables + both RPCs + Perihelion head) were read 2026-08-17 and again 2026-08-19. **Do not re-apply.** Do not fabricate a Perihelion canonical head. Isolated `test.hosted-canonical.*` is the operator test-world path; production PLAY stays Perihelion.

---

## Spec-ready, not authorized (explicit implementation pass)

Canonical-head infrastructure is implemented, deployed, and SQL-verified. Isolated ENTER/INSPECT/SQL-head proof shipped. GC1-S2 is hosted (RFC-0040). Host STUDY stays stub.

---

## SPEC GAP (later RFC)

```text
GC1 parameter-access and later unshipped mastery slices
```

---

## Out unless doctrine changes

```text
crypto / wallets / x402
v0.6B / v0.6C
v0.8 Phenomena
production Genesis activate / force-supersede / reseed
host STUDY unstub
```

---

## Suggested analysis order

1. Do not re-apply hosted world-head SQL.  
2. Do not Recover or bootstrap Perihelion from incomplete legacy events.  
3. Do not implement unshipped GC1 slices (parameter-access). GC1-S2 is already hosted.
