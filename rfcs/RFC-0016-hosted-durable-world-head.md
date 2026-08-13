# RFC-0016 — Hosted Durable World Head

## Status

**Accepted**

First architecture-resume slice after the reducer registry. No new verbs. No `event-catalog` expansion. No Genesis activate/reseed. No platform migration.

## Problem

Reconciled authority says Durable Object = live ordering and Postgres = durable canonical record ([NOTION-RECONCILIATION-2026-08-13.md](../docs/NOTION-RECONCILIATION-2026-08-13.md), [REDUCER-REGISTRY.md](../docs/REDUCER-REGISTRY.md)). Hosted Stage 0 only copied events into `noema_settled_events`. WorldState lived solely in DO storage. After DO loss, reconstruction was **NOT_COMPUTABLE**.

## Proposed change

Persist one **world head** row per `world_id` in existing Supabase Postgres:

```text
noema_world_heads
  world_id            PK
  sequence            integer
  cycle               integer
  genesis_id          text null
  status              text
  settlement_health   text
  state_json          jsonb   # WorldRuntime snapshot
  updated_at          timestamptz
```

Rules:

1. After a mutating command, the Worker upserts the head (same service-role REST path as events).
2. Events continue to settle into `noema_settled_events` (idempotent on `event_id`).
3. If DO storage has no world and a head exists, restore from the head. If DO storage has a world, that live copy remains the ordering authority — do not clobber it with an older head.
4. Failed event settles stay on `unsettled[]` with enough fields to retry. Retry is idempotent.
5. Missing table or secrets: treat as settle failure (existing DEGRADED → BLOCKING bound). Do not invent a second database.

Full `SERIALIZABLE` cycle-fence rewrite of WORLD-ENGINE remains later. This slice makes the world reconstructable from Postgres.

## Alternatives rejected

| Alternative | Why |
|-------------|-----|
| New database / queue product | Stack freeze |
| Event log only, no head | Replay of full WorldRuntime from Stage 0 event payloads is incomplete |
| Clobber live DO from head on every boot | Breaks live ordering |
| Genesis reseed to “fix” durability | First-world freeze |
| New event types | Catalog expansion |

## Compatibility

Additive persistence. Frozen `action-contracts.v01.json` and `event-types.0.2.json` unchanged. DO remains the live writer fence.

## Data / security

Service role stays in the Worker. Agents never receive it. Head JSON is WorldRuntime (rooms, players, trades, derived caches) — no controller secrets.

## Validation

`check_rfc_0016`: RFC Accepted; table `noema_world_heads`; restore-if-missing; no Genesis pack; no new verbs/events.

## Rollback

Stop upserting heads. Existing event sink remains. DO storage still works.

## Unresolved

SERIALIZABLE multi-statement cycle transaction; writer-fence token in Postgres; replay of events *after* a stale head.
