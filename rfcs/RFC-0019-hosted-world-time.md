# RFC-0019 — Hosted World-Time via WAIT Quorum

## Status

**Accepted**

Narrow architecture pin. No new Player verb. No `event-catalog/0.3`. No contest thaw. No WED. No Genesis reseed.

**Review-stage successor note.** [RFC-0128](RFC-0128-player-tempo-and-cycle-admission.md) proposes that worlds explicitly pinned to `player-tempo/1.0` use server-authoritative cycle admission instead of this WAIT-quorum-only trigger. RFC-0019 remains authoritative unless and until that proposal is Accepted, implemented, and pinned by the world. Existing ledgers are never reinterpreted.

## Problem

`WAIT` must not advance `World.cycle` alone ([ACTION-CONTRACTS.md](../docs/ACTION-CONTRACTS.md), reducer registry). After that pin, hosted Perihelion had no cycle-commit path. `wait_until_cycle` could never become current. GC7 expiry and GC10 schedule cycle 4 cannot fire. A cron tick must not be the clock ([SCHEDULER.md](../docs/SCHEDULER.md)).

## Proposed change

Hosted cycle commit (world-ops path; sole writer of `World.cycle`):

```text
present = entered AND last_seen within the existing 30m presence window
if present is empty → do not advance
if every present Player has wait_until_cycle > World.cycle
  → World.cycle += 1
```

`WAIT` still only sets `wait_until_cycle` and emits `WAIT`. The last present `WAIT` that completes the quorum is the commit trigger, not a second catalog event.

Idle (entered but not present) does not block. Not-entered Players do not block. Humans and agents both count. Wall clock is only the existing presence window, not the increment.

Does **not** run WED, contest resolve, production ticks, or reports. Those stay later authorized slices.

## Alternatives rejected

| Alternative | Why |
|-------------|-----|
| Cron / digest-tick advances cycle | Tick must not be world time |
| Every mutating command increments cycle | Invents a live-action clock; WAIT contract is wait-until |
| Solo WAIT never advances | One Player could never move world time |
| Idle entered Player blocks forever | Disconnect ≠ leave, but idle is not presence |
| `CYCLE_ADVANCED` event | Catalog expansion |

## Compatibility

Additive. Frozen catalogs unchanged. Existing `WAIT` event unchanged. First-world Genesis untouched.

## Data / security

No new entity fields. No hidden-room leak. No research scores.

## Validation

`check_rfc_0019`: Accepted; quorum; present; no Genesis pack; no new verbs; contest/WED not authorized here.

## Rollback

Stop calling commit. `WAIT` remains wait-until only; cycle stays put.

## Unresolved

Batched Chamber freeze-set (full [SCHEDULER.md](../docs/SCHEDULER.md) pipeline). Contest resolve hook on commit (GC7). WED schedule fire on commit (GC10).
