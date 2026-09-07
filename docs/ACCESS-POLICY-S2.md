# ACCESS_POLICY S2 — ALLOW_ONLY

**Status:** Executable specification. Runtime authorized with RFC-0103.  
**Parent:** [ACCESS-POLICY-S1.md](ACCESS-POLICY-S1.md) · [ACTION-CONTRACTS.md](ACTION-CONTRACTS.md)  
**RFC:** [RFC-0103](../rfcs/RFC-0103-access-policy-allow-only.md)  
**Does not open:** ACCESS_POLICY help · WED/ATTEST help · YOUR POSITION · event-catalog/0.3 · inbound-only locks  
**Next:** [ACCESS-POLICY-S3.md](ACCESS-POLICY-S3.md)

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

## Extension Points

Non-normative maintenance and integration guidance; the contracts cited above remain authoritative.

### Document-specific seam

Extend policy diagnostics by comparing a named ALLOW_ONLY restriction with the MOVE result on its existing outbound EXIT or ROOM scope. Present a refusal only from the acting Agent Player’s authorized observation, with localized explanation beside the stable machine reason.

### Compatibility and promotion

RFC-0103 preserves DENY precedence, matching CLEAR, occupied GRANT_ACCESS authority, and the existing restriction store. S0–S3 here are slice identifiers, not Controller privilege levels. Human WATCH/CONNECT/STUDY/ADMIN roles remain separate; this EP adds no inbound lock or extra help advertising.

### Verification before adoption

Cover listed and unlisted Players, wildcard refusal, an overlapping DENY, matching CLEAR, and loss of the occupied grant. Assert no unauthorized charge or restriction write. Retain S0/S1 fixtures and declare the catalog pin before comparing old and new behavior; record runtime evidence separately from these test requirements.
