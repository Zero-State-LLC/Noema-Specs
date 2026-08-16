# GC3-S3 — Institution→Player Edges

**Status:** Executable specification. Runtime authorized with RFC-0035.  
**Parent:** [SOCIAL-MEMORY.md](SOCIAL-MEMORY.md) · [INSTITUTIONAL-AUTHORITY.md](INSTITUTIONAL-AUTHORITY.md) · [GC4-S1-OFFICES.md](GC4-S1-OFFICES.md)  
**RFC:** [RFC-0035](../rfcs/RFC-0035-institution-edges.md)  
**Does not open:** `ROLE_*` · Player private edges copied onto the org · WATCH titles

S3 is institutional memory of Players from records that org is authorized to hold. It closes scenario B's institutional-expectation half.

---

## Doctrine decisions

| Temptation | Verdict |
|------------|---------|
| Copy A→B private S0/S1 onto the org | **REJECT.** Unauthorized |
| `ROLE_*` events | **REJECT.** RFC-0008 / RFC-0023 |
| WATCH “org enemy” | **REJECT.** Institutional, not public |
| Player opinion of an org as WorldState | **REJECT.** Private interpretation |

---

## Slice contract

| Field | Value |
|-------|--------|
| Slice id | `gc3-s3` |
| Catalog | `social-memory-catalog/gc3-s3` |
| Edge | Directed `org_id` → `player_id` |
| Evidence (closed) | That org's TRADE, membership, contest, breach |
| State | Derived. Not WorldState |
| WATCH | Empty |

### Evidence rules

| Event | Credits when | Family |
|-------|--------------|--------|
| `TRADE_ACCEPTED` | `acting_for` is this org; object is `counterparty_id` | trade (same 1 / 3 thresholds as S0) |
| `ORG_MEMBER_ADD` | `org_id` matches | membership |
| `ORG_MEMBER_REMOVE` | `org_id` matches | membership |
| `CONTEST_RESOLVED` | org is `defender_id` or `acting_for` | danger → `declarer_id` |
| `AGREEMENT_BROKEN` | org in `party_ids` | danger + deceptive → `broken_by` |
| Personal `TRADE_ACCEPTED` without `acting_for` | never | — |

### Thresholds (officers)

| Family | Line |
|--------|------|
| 1–2 org trades | `{org} has traded with {name}.` |
| ≥ 3 org trades | `{org} has found {name} reliable in trade.` |
| current member (last ADD after any REMOVE) | `{org} records {name} as a member.` |
| last event is REMOVE | `{org} records {name} as removed.` |
| ≥ 1 danger evidence | `{org} records {name} as dangerous.` |

`{org}` is the org's public name. `{name}` is the Player handle.

### Visibility

| Audience | S3 |
|----------|----|
| Founder / officer of that org | All of that org's edges |
| Member | Only the edge about **self** |
| Other Players | Nothing |
| WATCH | Nothing |
| Successor of an office | Inherits **this org's** edges, not the prior holder's private S0/S1 |

---

## A–J

| Test | Result |
|------|--------|
| A | Institution + authorized record |
| B | Uncertainty: C does not see the org's private book |
| C | No extra command |
| D | Trade / membership / contest already exist |
| E | No new verb |
| F | Org can refuse later via existing officer choice, not auto-filter |
| G | Evidence refs are that org's event ids |
| H | Same rebuild for human and agent officers |
| I | Meaningful with STUDY hidden |
| J | Without this, scenario B has no institutional scar |

---

## Out of S3

```text
ROLE_*
WATCH titles
copying private Player edges
Player→Institution WorldState opinion
```

---

## Runtime rule

Hosted Chamber MAY project S3 on PLAY for officers of the acting org. WATCH empty. Help unchanged. Occupied office still required to act (RFC-0029).
