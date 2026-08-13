# GC4 First Slice — Existing Roles as Bounded Authority

**Status:** Executable specification. Not a runtime implementation.  
**Parent:** [INSTITUTIONAL-AUTHORITY.md](INSTITUTIONAL-AUTHORITY.md) · [COMPLEXITY-DOCTRINE.md](COMPLEXITY-DOCTRINE.md)  
**RFC:** [RFC-0008](../rfcs/RFC-0008-office-authority-pins.md)  
**Does not open:** Steward / Treasurer / Marshal name freeze · `ROLE_*` events · `event-catalog/0.3` · LLM authority · institution-owned TRADE/REPAIR

S0 is the smallest institutional-authority increment that still satisfies scenario D’s *shape* (a bounded grant, a permitted act, a forbidden act, a leave) using the v0.1 membership roles already on `COMMIT.ORG_*`. Named offices, vacancy events, and emergency scopes wait for GC4-S1.

---

## Doctrine decisions

| Temptation | Verdict |
|------------|---------|
| Freeze Steward / Treasurer / Archivist as new engines | **REJECT.** Those strings are presentation until a later catalog binds them to scopes |
| `ROLE_ASSIGNED` / `ROLE_VACATED` in S0 | **REJECT.** Reuse `ORG_CREATE`, `ORG_MEMBER_ADD`, `ORG_MEMBER_REMOVE` |
| New `APPOINT` / `GRANT` verb | **REJECT.** Verb inflation |
| LLM or chat “I am the Steward” | **REJECT.** Not an assignment |
| Cosmetic title grants invite power | **REJECT.** Title without a role record is presentation |
| Institution-side TRADE / REPAIR scopes | **DEFER** (needs later authority families) |
| Emergency extra-scope rule | **DEFER** |
| Delegation / succession / vacancy state machine | **DEFER** (SUCCESSION already flags `ROLE_*` as RFC-gated) |

Pressures: **dependency** (ordinary members cannot mutate membership) and **uncertainty** (a displayed title is not proof of grant).

---

## Slice contract

| Field | Value |
|-------|--------|
| Slice id | `gc4-s0` |
| Catalog | `authority-catalog/gc4-s0` |
| Offices | Existing v0.1 roles only: `founder`, `officer`, `member`, `advisor` |
| Wire verbs | Unchanged `COMMIT` operations `ORG_CREATE`, `ORG_MEMBER_ADD`, `ORG_MEMBER_REMOVE` |
| Events | Existing `event-catalog/0.1` org types only |
| Display names | Not frozen. Zero authority |

A **role** in this slice is an authority configuration over those operations. It is not a new institution species and not a class tree.

### Grants (closed)

| Role | May `ORG_MEMBER_ADD` | May remove another member | May self-leave |
|------|----------------------|---------------------------|----------------|
| `founder` | yes, assigned role ∈ {`officer`, `member`, `advisor`} | yes, subject to last-founder guard | yes, subject to last-founder guard |
| `officer` | yes, same assignable set | yes, subject to last-founder guard | yes |
| `member` | no | no | yes |
| `advisor` | no | no | yes |
| none (non-member) | no | no | no |

`ORG_CREATE` remains founder bootstrap. It is the only S0 path that may create a `founder` seat.

### Pins that ACTION-CONTRACTS left open

| Gap | S0 pin |
|-----|--------|
| “authorizer permitted” on `ORG_MEMBER_REMOVE` | Authorizer role ∈ {`founder`, `officer`}, or self-leave |
| Whether `ORG_MEMBER_ADD` may assign `founder` | **No.** Founder is create-time only |
| Last founder while others remain | **FORBIDDEN.** Prevents silent founderless orgs; dissolution stays LATER |
| Cosmetic / culture titles | Ignored. Only `actor_role` authorizes |

`advisor` is a distinct role with the same membership-mutation grant as `member` (self-leave only). A later runtime MUST NOT treat the string `advisor` as `officer`.

### Events

| Operation | Success events |
|-----------|----------------|
| `ORG_CREATE` | `BUDGET_CONSUMED`×, `ORG_CREATE` |
| `ORG_MEMBER_ADD` | `ORG_MEMBER_ADD` |
| `ORG_MEMBER_REMOVE` | `ORG_MEMBER_REMOVE` |

No `ROLE_*`. No `event-catalog/0.3`.

### Failure codes

| Code | When |
|------|------|
| `FORBIDDEN` | Actor lacks the grant; assigned role is `founder`; last-founder guard |
| `NOT_FOUND` | Org not `ACTIVE`; target is not a member on remove |

Budget and activity preconditions stay with [ACTION-CONTRACTS.md](ACTION-CONTRACTS.md). This slice does not retune costs.

---

## A–J

| Test | Result |
|------|--------|
| A | Player / Organization primitive. No eighth species and no office engine |
| B | Dependency + uncertainty |
| C | No extra commands; grants fall out of ordinary `ORG_*` |
| D | Membership couples to later trade, construction, and communication scopes |
| E | No new verb |
| F | A compact or desk habit can form around who may invite, without a Steward class |
| G | `ORG_*` events remain attributable |
| H | Human and agent Players use the same role table |
| I | Meaningful with research hidden |
| J | Without this, “office” is only a displayed word |

---

## Out of S0

```text
Steward Treasurer Archivist Envoy Quartermaster Surveyor Auditor Marshal Speaker Custodian
ROLE_ASSIGNED ROLE_VACATED SUCCESSION_RECORDED INSTITUTION_TRANSFORMED
emergency scopes
delegation subsets
institution-owned TRADE / REPAIR / ACCESS
vacancy as ROLE_VACANT
WATCH office titles
LLM assignment
```

---

## Runtime rule

This document does not change Chamber PLAY. Hosted membership already uses founder/officer grants; S0 is the specification pin those checks must not drift past. Advisor must remain non-authorizing for invite/remove. Displayed titles must not authorize.

## Acceptance (narrower than scenario D)

1. An `officer` `ORG_MEMBER_ADD` of a `member` is accepted.
2. A `member` `ORG_MEMBER_ADD` is `FORBIDDEN`.
3. A `member` self-leave is accepted.
4. An `advisor` `ORG_MEMBER_ADD` is `FORBIDDEN`.
5. Assigning `founder` via `ORG_MEMBER_ADD` is `FORBIDDEN`.
6. Removing the only founder while other members remain is `FORBIDDEN`.
7. A Player whose displayed title is “Steward” but whose role is `member` cannot invite.

Full scenario D (named office, institution TRADE/REPAIR, succession of that scope) is **GC4-S1**.
