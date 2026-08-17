# ACCESS_POLICY S1 — ROOM deny / clear

**Status:** Executable specification. Runtime authorized with RFC-0102.  
**Parent:** [ACCESS-POLICY-S0.md](ACCESS-POLICY-S0.md) · [ACTION-CONTRACTS.md](ACTION-CONTRACTS.md)  
**RFC:** [RFC-0102](../rfcs/RFC-0102-access-policy-room.md)  
**Does not open:** ALLOW_ONLY · ACCESS_POLICY help · WED/ATTEST help · YOUR POSITION · event-catalog/0.3  
**Next:** [ACCESS-POLICY-S2.md](ACCESS-POLICY-S2.md)

S1 adds **ROOM** scope to the existing `COMMIT.ACCESS_POLICY` verb. EXIT DENY/CLEAR from S0 stay. Authority, cost, and event stay S0.

---

## Doctrine decisions

| Temptation | Verdict |
|------------|---------|
| ALLOW_ONLY | **REJECT.** MOVE still only checks DENY. |
| Inbound lock | **REJECT.** ROOM DENY blocks leaving the room, same as contest. |
| Help ACCESS_POLICY | **REJECT.** |
| New events | **REJECT.** |
| Hidden rooms | **REJECT.** Public rooms only. |

---

## Slice contract

| Field | Value |
|-------|--------|
| Slice id | `access-policy-s1` |
| Catalog | `access-policy-catalog/s1` |
| Verb | existing `COMMIT.ACCESS_POLICY` |
| Scopes | `EXIT` (S0) · `ROOM` (this slice) |
| Modes | `DENY` · `CLEAR` |
| Authority | occupied `GRANT_ACCESS` via `acting_for` |
| Cost | compute 1, influence 2 (treasury) |
| Events | `ACCESS_RESTRICTED` |
| Help | still omits ACCESS_POLICY |
| WATCH | existing restriction projection; no ticker |

---

## Runtime rule

Hosted Chamber MUST accept `access here deny for <org>` and `access here clear for <org>` (alias `room`) under the same GRANT_ACCESS rule as S0. ROOM DENY writes a live restriction on the actor’s current public room. MOVE from that room is rejected while the restriction is live. CLEAR removes a matching ROOM restriction. Isolated tests only. Help unchanged. No Genesis change.
