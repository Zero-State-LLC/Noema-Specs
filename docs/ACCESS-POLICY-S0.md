# ACCESS_POLICY S0 — GRANT_ACCESS exit deny / clear

**Status:** Executable specification. Runtime authorized with RFC-0101.  
**Parent:** [ACTION-CONTRACTS.md](ACTION-CONTRACTS.md) · [PLAYER-ACTION-MAP.md](PLAYER-ACTION-MAP.md) · [GC4-S1-OFFICES.md](GC4-S1-OFFICES.md)  
**RFC:** [RFC-0101](../rfcs/RFC-0101-access-policy.md)  
**Does not open:** ALLOW_ONLY · ROOM scope · ACCESS_POLICY help · WED/ATTEST help · YOUR POSITION · event-catalog/0.3  
**Next:** ALLOW_ONLY / ROOM stay later pins

S0 hosts the existing `COMMIT.ACCESS_POLICY` verb for **EXIT DENY and CLEAR** only. Authority is an occupied `GRANT_ACCESS` office. Restrictions reuse the live `access_restrictions` store and `ACCESS_RESTRICTED` event.

---

## Doctrine decisions

| Temptation | Verdict |
|------------|---------|
| Anyone may lock an exit | **REJECT.** Authority is `GRANT_ACCESS`. |
| New events | **REJECT.** |
| ALLOW_ONLY | **REJECT.** MOVE only understands DENY today. |
| ROOM scope | **REJECT.** EXIT only. |
| Help ACCESS_POLICY | **REJECT.** |
| Geography rewrite / hidden rooms | **REJECT.** Public rooms only. |
| Personal (no `acting_for`) | **REJECT.** |

---

## Slice contract

| Field | Value |
|-------|--------|
| Slice id | `access-policy-s0` |
| Catalog | `access-policy-catalog/s0` |
| Verb | existing `COMMIT.ACCESS_POLICY` |
| Scope | `EXIT` in the actor’s current public room |
| Modes | `DENY` · `CLEAR` |
| Authority | occupied office `GRANT_ACCESS` via `acting_for` |
| Cost | compute 1, influence 2 (treasury) |
| Events | `ACCESS_RESTRICTED` |
| Default expiry | `cycle + 4` (DENY) |
| Help | still omits ACCESS_POLICY |
| WATCH | existing `access_changed` / restriction projection; no ticker |

---

## Runtime rule

Hosted Chamber MUST accept `access <dir> deny for <org>` and `access <dir> clear for <org>` when the actor holds an occupied `GRANT_ACCESS` office on that org, is entered, and stands in a public room that has that exit. DENY appends a live restriction and `ACCESS_RESTRICTED`. CLEAR removes a matching live restriction and emits `ACCESS_RESTRICTED` (`mode=CLEAR`). Isolated tests only. Help unchanged. No Genesis change.
