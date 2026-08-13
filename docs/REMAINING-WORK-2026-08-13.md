# Remaining work — 2026-08-13

**Status:** Analysis snapshot. Not a thaw. Not a release.  
**Hosted evidence:** Noema `docs/RUNTIME-READINESS-2026-08-13.md` · live Perihelion `ACTIVE` / `HEALTHY` / `genesis.ef578f4ffceeccd0` (seq 75 at last check).  
**Does not open:** BUILD, contest, WED, Genesis reseed, crypto, SERIALIZABLE cycle fence.

Use this file to analyze what is left. Do not treat it as authorization.

---

## Already on main (not remaining)

| Item | Specs | Hosted |
|------|--------|--------|
| GC1-S0 / S1 | RFC-0004 / 0005 | Yes (Noema #68 / #69) |
| GC3-S0 | RFC-0007 | Yes (#70) |
| GC4-S0 advisor pin | RFC-0008 | Yes (#71) |
| GC5-S0 MESSAGE bands | RFC-0009 | Yes (#72) |
| GC6-S0 mapper + source pin | RFC-0010 / **0015** | Mapper yes; **Perihelion silent** (no claim fields) |
| GC8-S0 costs | RFC-0012 | Already true |
| GC9-S0 custom | RFC-0013 | Yes (#71) |
| Reducer registry | `REDUCER-REGISTRY.md` | Spec only (index) |
| Durable world head | **RFC-0016** | Worker shipped (#76 / #77); **SQL may be unapplied** |

Frozen catalogs `action-contracts.v01.json` and `event-types.0.2.json` are unchanged.

---

## Operator (blocks reconstructable heads)

Apply on hosted Postgres:

```text
Noema/supabase/migrations/20260813210000_noema_world_heads.sql
```

Until that runs, the Worker skips a missing `noema_world_heads` table (404) so PLAY does not fail-close. Events still settle to `noema_settled_events`. Heads are not stored.

---

## Spec-ready, not authorized (explicit thaw required)

| Item | Authority | Why blocked |
|------|-----------|-------------|
| GC2-S0 BUILD | RFC-0006 | Chamber `BUILD` unsupported until implementation pass |
| GC7-S0 contest | RFC-0011 | Contest not thawed in first-world verbs |
| GC10-S0 WED | RFC-0014 | No production schedule; do not reseed Genesis |

---

## SPEC GAP (needs a later RFC)

```text
who may write archive_subject_entity_id + archive_claim (no Genesis pack)
SERIALIZABLE cycle fence + writer-fence token + replay after a stale head
GC1-S2 mechanical benefits
GC3-S1 betrayal / GC4-S1 named offices / GC5-S1 delay-rumor
GC6-S1 reconstruction / GC9-S1 tradition
WAIT must not increment World.cycle (hosted still does)
presence idle without AGENT_LEFT_WORLD
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

1. Confirm the world-heads SQL is applied (or not) on hosted Postgres.  
2. Decide a thaw: GC2 BUILD, GC7 contest, or GC10 WED.  
3. Or write the archive-claim *writer* RFC if GC6 should appear on Perihelion without a content pack.
