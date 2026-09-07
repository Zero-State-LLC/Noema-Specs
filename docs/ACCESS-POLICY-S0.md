# ACCESS_POLICY S0 — GRANT_ACCESS exit deny / clear

**Status:** Executable specification. Runtime authorized with RFC-0101.  
**Parent:** [ACTION-CONTRACTS.md](ACTION-CONTRACTS.md) · [PLAYER-ACTION-MAP.md](PLAYER-ACTION-MAP.md) · [GC4-S1-OFFICES.md](GC4-S1-OFFICES.md)  
**RFC:** [RFC-0101](../rfcs/RFC-0101-access-policy.md)  
**Does not open:** ALLOW_ONLY · ROOM scope · ACCESS_POLICY help · WED/ATTEST help · YOUR POSITION · event-catalog/0.3  
**Next:** [ACCESS-POLICY-S1.md](ACCESS-POLICY-S1.md)

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

## Extension Points

Non-normative conformance seams for the closed RFC-0101 slice.

- Extend isolated fixtures around EXIT DENY/CLEAR matching, expiry and treasury charges using the existing restriction store and ACCESS_RESTRICTED event. Preserve current-public-room scope, occupied GRANT_ACCESS office and acting_for checks.
- Controller enrollment confers no office, policy-registry or administrative privilege. Only authenticated Agent Player actions with the required in-world authority reach enforcement; human WATCH/CONNECT/STUDY/ADMIN permissions remain separate. S0 here is a slice identifier, not a human access tier.
- Compatibility/promotion: keep this slice's DENY/CLEAR and help omission pinned; later accepted slices supply their own changes. Do not import ROOM, ALLOW_ONLY or access help into an S0 conformance fixture. Any new behavior requires governing contract approval, not an EP plugin.
- Verification proposal: test authorized deny then MOVE block, matching clear then restored access, default expiry, missing office, wrong organization and absent exit. Compare event and treasury deltas on success and rejection. Restriction notices may be localized and keyboard-readable without exposing hidden policy state or enabling human Player actions.
