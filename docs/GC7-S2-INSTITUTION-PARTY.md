# GC7-S2 — Institution as Contest Party

**Status:** Executable specification. Runtime authorized with RFC-0041.  
**Parent:** [GC7-FIRST-SLICE.md](GC7-FIRST-SLICE.md) · [GC7-S1-WITHDRAW.md](GC7-S1-WITHDRAW.md) · [INSTITUTIONAL-AUTHORITY.md](INSTITUTIONAL-AUTHORITY.md)  
**RFC:** [RFC-0041](../rfcs/RFC-0041-institution-contest-party.md)  
**Does not open:** `event-catalog/0.3` · fifth form · HP · Chamber help advertising CONTEST

S2 lets an occupied office commit the institution to an existing v0.2 contest. The Player remains the actor. The treasury pays.

---

## Doctrine decisions

| Temptation | Verdict |
|------------|---------|
| Org id as declarer | **REJECT.** Actor stays a Player |
| Any member | **REJECT.** Occupied matching profile |
| New events / forms | **REJECT.** |
| Help lists contest | **REJECT.** |

---

## Slice contract

| Field | Value |
|-------|--------|
| Slice id | `gc7-s2` |
| Catalog | `conflict-catalog/gc7-s2` |
| Operations | existing `CONTEST_DECLARE`, `CONTEST_DEFEND`, `CONTEST_WITHDRAW` |
| Party fields | `acting_for` (declare) · `defender_acting_for` (defend) |
| Payer | Institution treasury |
| Actor | Occupied office holder, colocated |

### Profile map

| Form | Office profile |
|------|----------------|
| `RESOURCE_SEIZURE` | `OPERATE_RESOURCE_ACCOUNT` |
| `INFRASTRUCTURE_DISRUPTION` | `OPERATE_NAMED_ASSET` |
| `ACCESS_CONTEST` | `OPERATE_NAMED_ASSET` |
| `PRESENCE_PRESSURE` | `OPERATE_NAMED_ASSET` |

Office conflict-precedence still applies when two offices share a profile.

### Same-org rule

If declare `acting_for` is `org.X`, defend `acting_for` MUST NOT be `org.X`. Personal defend against your own org's contest is allowed only if you are **not** the `declarer_id` (another member). The declarer still cannot defend.

### Withdraw / resolve

Same Player who declared or defended. Stake release/consume hits the treasury that reserved it. Outcomes unchanged (S1).

---

## Out of S2

```text
fifth / information-target form
CONTEST_* catalog 0.3
declarer_id = org
Chamber help
idle withdraw
```

---

## Runtime rule

Hosted Chamber MUST accept `acting_for` on the three existing contest operations. Help still omits CONTEST. Isolated tests only.
