# RFC-0123 — Bounded upward norm ratchet; costly TRADE-reject punishment pinned

## Status

**Accepted**

Gameplay economics pin. No new Player verbs. No new events. No Genesis change. No reseed. Supersedes one paragraph of `docs/ECONOMY-EWM-SPEC.md` §4; pins one shipped behavior that had no spec authority.

Accepted retroactively: this RFC documents behavior that was already running in
production when it was written, and is live today in Worker `1f974f76`. It is a
retro-spec, not an authorization to build — nothing new ships under it.

## Problem

Two behaviors run in production without matching spec authority (2026-08-21 audit, G2/V2 and V1):

1. **Ratchet direction is inverted vs spec.** `ECONOMY-EWM-SPEC.md` §4 specifies a *downward* ratchet on `org_influence_threshold` (repeated success makes ORG_CREATE cheaper). The runtime ships the opposite: each ORG_CREATE increments `norm_ratchets.org_create.reversal_cost`, surcharging every later ORG_CREATE — uncapped and never decaying. After N org creations the cost is `5+N` influence forever, world-globally. `DEEP-TIME-MECHANICS-UPDATE.md` §8 names the risk ("path dependence must not make the world feel static") without a bound.
2. **TRADE-reject punishment is unspecced.** A TRADE reject carrying `@G=observed` silently debits the rejecter 1 influence, drops the proposer's image by 2, records dyadic conduct, and eases the room's `harvest_pressure` by 1. `SEMANTIC-EVOLUTION-SPEC.md` §3.3 authorizes *justified punishment* in general terms; nothing authorizes this trigger, these amounts, or the economic coupling.

## Decision

### 1. The upward ratchet is canon, bounded

The shipped direction stands: repeated ORG_CREATE **raises** the marginal cost of the next one. Institutional proliferation is friction, not discount; scarcity of institutional attention is the game's premise. The downward-ratchet paragraph of `ECONOMY-EWM-SPEC.md` §4 is **superseded** for `org_create`.

Bounds (normative):

| Bound | Value |
|---|---|
| `reversal_cost` cap | **5** (total ORG_CREATE influence cost is never more than double the base 5) |
| Decay | during the slow deep-time pass (`cycle % 5`), `reversal_cost` decreases by **1** when there has been **no ORG_CREATE reinforcement for ≥ 10 cycles** |
| Floor | 0; `established_cycle` and `hits` are preserved across decay |
| Scope | `org_create` only; the `attest` ratchet keeps `reversal_cost` 0 (path-dependence tracking only) |

`active_norms.org_create_influence` MUST report the live bounded cost (base + ratchet), never a constant.

### 2. Costly TRADE-reject punishment is canon, bounded and decoupled

An observed-grounded TRADE reject (`@G=observed`) is the *demonstrability* gate SEMANTIC §3.3 requires: the punisher stakes a grounded public claim and pays for it. Pinned semantics:

| Element | Value |
|---|---|
| Trigger | TRADE reject with signal grounding `observed`; rejecter must hold ≥ 1 influence |
| Punisher cost | 1 influence (costly punishment; refused, not queued, when unaffordable) |
| Target effect | image −2; dyadic conduct −1; second-order refresh |
| Economic coupling | **removed** — the `harvest_pressure` easing side-effect is struck; a social sanction MUST NOT mutate EWM extraction pressure |
| Observability | the punisher's command result MUST carry a consequence line naming the sanction; the ledger event is the existing TRADE_REJECTED (no new event) |

The pressure-easing idea (collective sanction relieving extraction pressure) is not rejected forever; it needs its own RFC with an economic model before returning.

## Runtime obligations

- Cap + decay in the deep-time slow pass; ratchet cap enforced at increment.
- Remove the `harvest_pressure` mutation from the punish path; keep debit/image/conduct/second-order.
- Consequence line on the punishing reject.
- Tests: cap holds at 5 under 10 creates; decay after 10 quiet cycles and not before; floor 0; punish leaves `harvest_pressure` untouched; unaffordable punish refuses cleanly.

## Not in scope

Conversion-rate mutation and `unlocked_affordances` (the rest of ECONOMY-EWM §4) remain unimplemented and unsuperseded — a later RFC. Belief substrate (§1–§2) unchanged. No WATCH exposure of ratchet internals beyond the existing `active_norms` band on PLAY.
