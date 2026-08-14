# GC4-S2 — Institutional TRADE and REPAIR Authority

**Status:** Executable specification. Runtime authorized with RFC-0029.  
**Parent:** [GC4-S1-OFFICES.md](GC4-S1-OFFICES.md) · [INSTITUTIONAL-AUTHORITY.md](INSTITUTIONAL-AUTHORITY.md)  
**RFC:** [RFC-0029](../rfcs/RFC-0029-institution-trade-repair.md)  
**Does not open:** emergency scopes · designated succession · banking/market/payroll · `event-catalog/0.3` · Chamber help advertising BUILD / CONTEST / WED / ATTEST

S2 lets an occupied office spend **institution** resources through ordinary TRADE and REPAIR. The institution is not a Player.

---

## Doctrine

```text
Player
+ valid institutional authority
+ institutional target/resource scope
→ ordinary canonical action
```

```text
INSTITUTION RESOURCES ≠ OFFICER RESOURCES ≠ FOUNDER RESOURCES
OFFICE EXISTS + NO HOLDER → NO AUTHORITY
```

| Temptation | Verdict |
|------------|---------|
| `INSTITUTION_TRADE` / `INSTITUTION_REPAIR` | **REJECT** |
| `TREASURER_POWER` / `ENGINEER_POWER` | **REJECT.** Profile is the grant |
| Founder may spend treasury | **REJECT** unless they hold the office |
| Vacant office acts | **REJECT** |
| Silent account pick | **REJECT** |
| Institution autopilot | **REJECT** |

Pressures: **dependency** (someone must hold the seat) and **scarcity** (treasury is real).

---

## Acting-for

Institutional action requires explicit context:

| Field | Meaning |
|-------|---------|
| `acting_for` | `org_id` |
| `office_id` | Occupied office on that org (optional if exactly one valid grant) |

If `acting_for` is omitted, the action is **personal**.

If `office_id` is omitted and the actor holds more than one matching occupied office on that org, fail `FORBIDDEN` (ambiguous). Zero matching offices → `FORBIDDEN`. One → use it.

Human aliases (org help only, not KNOWN COMMANDS):

```text
trade for <org> <player> offer=energy:3 want=storage:1
accept <trade> for <org>
repair <infrastructure> for <org>
```

---

## Profiles exercised

| Profile | May | Must not |
|---------|-----|----------|
| `OPERATE_RESOURCE_ACCOUNT` | Propose / accept / cancel / reject TRADE using that org’s treasury | Spend personal lots as treasury; accept the other side without that org’s grant |
| `OPERATE_NAMED_ASSET` | REPAIR an in-scope asset using that org’s treasury | Repair another institution’s owned asset; invent an asset |

`PUBLISH_NOTICE` remains as S1. Display names (Treasurer, Custodian) are labels.

---

## Treasury

Each ACTIVE organization has `treasury` (`Budgets`). Created at `ORG_CREATE` as zeros.

- Reservations and transfers mutate `treasury`, not the holder’s personal `budgets`, when `acting_for` is set.
- Actor still pays the personal compute fee for TRADE (`compute 1`).
- Vacate / resign / remove / retire: treasury unchanged; former holder loses the grant.

---

## Institutional TRADE

Ordinary `TRADE` + context.

| Side | Account |
|------|---------|
| Proposer `acting_for=org` | Reserve `offered` from that treasury |
| Proposer personal | Existing personal reserve |
| Accept `acting_for=org` | Pay `requested` from that treasury; receive `offered` into that treasury |
| Accept personal | Existing personal pay/receive |
| Reject / cancel / expire | Release the reserved account |

Counterparty MAY be a Player id or an `org_id`.

If counterparty is an org, only a Player with `OPERATE_RESOURCE_ACCOUNT` on **that** org may accept.

One Player must not authorize both sides in this slice (`FORBIDDEN`). Broader conflict-of-interest remains SPEC GAP.

Events: existing `TRADE_PROPOSED` / `TRADE_ACCEPTED` / `TRADE_REJECTED` / `TRADE_CANCELLED` / `RESOURCE_TRANSFER`. Payload MAY include `acting_for` and `office_id` (additive metadata, not a new type).

---

## Institutional REPAIR

Ordinary `COMMIT.REPAIR` + context.

Cost (`energy 3`, `compute 2`, `storage 1`) is debited from the named institution treasury. Not from personal lots. Not from “whichever account has funds.”

### Asset scope

A target is in scope for `org` when all of:

```text
entity is repairable INFRASTRUCTURE or RUIN
entity is in the actor's current room
entity.owner_id is null, the actor, or org
entity.owner_id is not a different organization
```

Another institution’s owned asset is out of scope.

Condition change is the existing +15 cap 100 `ENTITY_UPDATE`.

---

## Authorization

Every institutional TRADE/REPAIR checks:

```text
Player entered and active
org exists, same world, ACTIVE
office exists on that org, OCCUPIED, holder = actor
office.authority_profile matches the operation
scope includes the account or asset
resources available and unreserved
```

Membership role, advisor title, and office display name grant nothing by themselves.

Revocation (vacate/retire/leave) fails **future** acts. Settled trades and completed repairs stand.

---

## Visibility

| Surface | Sees |
|---------|------|
| PLAY (grant holder) | That org’s treasury amounts; “You may trade/repair for {org}.” |
| PLAY (other members) | Office names/holders. No treasury amounts |
| WATCH | Public consequence only, no balances: `An institution traded from its treasury.` / `Institution infrastructure was repaired.` |

---

## A–J

| Test | Result |
|------|--------|
| A | Institution + resource + asset. No finance primitive |
| B | Scarcity + dependency |
| C | No new top-level verb |
| D | Couples to offices, TRADE, REPAIR |
| E | Verb-stable |
| F | Treasurer / custodian habits can form |
| G | Events remain attributable |
| H | Human and agent same grants |
| I | Meaningful with STUDY hidden |
| J | Without this, recorded profiles never spend |

---

## Out of S2

```text
emergency scopes
designated succession
delegation machine
banking / market / payroll
institution XP / office buffs
autonomous institution NPC
INSTITUTION_* event family
GC1-S2 benefits
```

---

## Runtime rule

Hosted Chamber applies `acting_for` on existing TRADE and REPAIR. Help org topic may name the aliases. Do not reseed Genesis.

## Acceptance

1. Occupied `OPERATE_RESOURCE_ACCOUNT` proposes from treasury; accept transfers atomically.
2. Occupied `OPERATE_NAMED_ASSET` repairs an in-scope asset from treasury.
3. Member, advisor, vacant office, and former holder cannot act.
4. Personal lots and treasury stay separate through turnover.
5. No new verbs or event types.
