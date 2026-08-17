# ACCESS_POLICY S2 — ALLOW_ONLY

**Status:** Executable specification. Runtime authorized with RFC-0103.  
**Parent:** [ACCESS-POLICY-S1.md](ACCESS-POLICY-S1.md) · [ACTION-CONTRACTS.md](ACTION-CONTRACTS.md)  
**RFC:** [RFC-0103](../rfcs/RFC-0103-access-policy-allow-only.md)  
**Does not open:** ACCESS_POLICY help · WED/ATTEST help · YOUR POSITION · event-catalog/0.3 · inbound-only locks  
**Next:** ACCESS_POLICY help stays a later pin

S2 adds **ALLOW_ONLY** to the existing `COMMIT.ACCESS_POLICY` verb. EXIT/ROOM DENY and CLEAR from S0/S1 stay. Authority, cost, and `ACCESS_RESTRICTED` stay.

---

## Doctrine decisions

| Temptation | Verdict |
|------------|---------|
| New events | **REJECT.** |
| ALLOW_ONLY `applies_to=*` | **REJECT.** A list is required. |
| ALLOW_ONLY punches through DENY | **REJECT.** DENY still wins. |
| Help ACCESS_POLICY | **REJECT.** |
| Inbound lock | **REJECT.** Same outbound MOVE check as DENY. |

---

## Slice contract

| Field | Value |
|-------|--------|
| Slice id | `access-policy-s2` |
| Catalog | `access-policy-catalog/s2` |
| Verb | existing `COMMIT.ACCESS_POLICY` |
| Scopes | `EXIT` · `ROOM` |
| Modes | `DENY` · `CLEAR` · `ALLOW_ONLY` |
| Authority | occupied `GRANT_ACCESS` via `acting_for` |
| Cost | compute 1, influence 2 (treasury) |
| Events | `ACCESS_RESTRICTED` |
| ALLOW_ONLY list | named Player; not `*` |
| MOVE | listed party may take the route; anyone else is rejected |
| Help | still omits ACCESS_POLICY |
| WATCH | existing restriction projection; no ticker |

---

## Runtime rule

Hosted Chamber MUST accept `access <dir|here> allow for <org> applies_to=<player>` under the same GRANT_ACCESS rule as S0/S1. ALLOW_ONLY writes a live restriction. MOVE on a matching route succeeds only for the listed player. Other live DENY restrictions still reject. CLEAR removes a matching ALLOW_ONLY restriction. Isolated tests only. Help unchanged. No Genesis change.
