# GC4-S1 — Named Institutional Offices

**Status:** Executable specification. Runtime authorized with RFC-0023.  
**Parent:** [GC4-FIRST-SLICE.md](GC4-FIRST-SLICE.md) · [INSTITUTIONAL-AUTHORITY.md](INSTITUTIONAL-AUTHORITY.md)  
**RFC:** [RFC-0023](../rfcs/RFC-0023-named-offices.md)  
**Does not open:** `ROLE_*` · `event-catalog/0.3` · elections · payroll · institution TRADE/REPAIR · Chamber help advertising

S1 is the smallest increment that still satisfies scenario D’s *office* shape: a named seat persists, a holder exercises a scoped act, vacancy removes that grant.

---

## Doctrine

```text
OFFICE ≠ PLAYER ≠ MEMBERSHIP ROLE ≠ EMPLOYMENT ≠ AUTHORITY ITSELF
```

| Temptation | Verdict |
|------------|---------|
| Freeze Treasurer as a class | **REJECT.** Name is display; profile is the grant |
| Merge into `officer` | **REJECT.** Separate concept |
| `ROLE_ASSIGNED` | **REJECT.** Reuse `ENTITY_CREATE` / `ENTITY_UPDATE` |
| New top-level verb | **REJECT.** `COMMIT.ORG_OFFICE_*` |
| Elections / parties | **REJECT** |
| Chat assignment | **REJECT** |

Pressures: **dependency** (ordinary members cannot create or assign seats) and **uncertainty** (a spoken title is not the grant).

---

## Model

Office lives on the owning organization (not a room entity, not a membership row).

| Field | Meaning |
|-------|---------|
| `office_id` | Stable `office.<slug>.<hex>` |
| `institution_id` | Owning `org_id` |
| `display_name` | Player-chosen label |
| `status` | `VACANT` \| `OCCUPIED` \| `RETIRED` |
| `holder_player_id` | Zero or one Player. Null when vacant/retired |
| `authority_profile` | Closed profile id |
| `created_cycle` | Create cycle |
| `retired_cycle` | Set only on retire |
| `history` | Prior holder refs. Not rewritten on replace |

Lifecycle:

```text
VACANT ⇄ OCCUPIED → RETIRED
```

Create starts `VACANT`. Resign / remove / leave-org / ineligible → `VACANT`. Retire is terminal. History kept.

Membership role remains the GC4-S0 grant. A Player MAY hold a membership role and zero or more offices.

---

## Profiles (closed)

Capability, not a `TREASURER_POWER` enum.

| Profile | May | Must not |
|---------|-----|----------|
| `PUBLISH_NOTICE` | Set that institution’s public notice | Read private DMs; bind third parties |
| `OPERATE_RESOURCE_ACCOUNT` | Later institution treasury | Personal appropriation |
| `ACCESS_RESTRICTED_ARCHIVE` | Later archive access | Create hidden rooms |
| `GRANT_ACCESS` | Later access-list mutate | Geography rewrite |
| `OPERATE_NAMED_ASSET` | Later named-asset operate | Ultra vires REPAIR everywhere |

Hosted S1 **exercises** only `PUBLISH_NOTICE`. Other profiles may be recorded; `OFFICE_ACT` on them is `FORBIDDEN` until a later RFC.

---

## Operations

Authorizers: `founder` or `officer` for create / assign / vacate-other / retire. Holder may resign (`OFFICE_VACATE` self). Holder may `OFFICE_ACT` when occupied.

| Operation | COMMIT | Evidence |
|-----------|--------|----------|
| Create | `ORG_OFFICE_CREATE` | `ENTITY_CREATE` (`DOCUMENT`, `location=null`, owner=`org_id`) |
| Assign / replace | `ORG_OFFICE_ASSIGN` | `ENTITY_UPDATE` |
| Vacate / resign | `ORG_OFFICE_VACATE` | `ENTITY_UPDATE` |
| Retire | `ORG_OFFICE_RETIRE` | `ENTITY_UPDATE` |
| Exercise | `ORG_OFFICE_ACT` | `ENTITY_UPDATE` |

`ORG_MEMBER_REMOVE` (leave or remove) vacates every office that Player holds in that org.

### Preconditions

| Check | Fail |
|-------|------|
| Org not `ACTIVE` | `NOT_FOUND` |
| Actor lacks grant | `FORBIDDEN` |
| Target Player missing / other world | `NOT_FOUND` / `FORBIDDEN` |
| Target not a member | `FORBIDDEN` |
| Office missing / retired | `NOT_FOUND` / `FORBIDDEN` |
| Assign onto `OCCUPIED` without `replace` | `FORBIDDEN` |
| Invalid profile | `FORBIDDEN` |
| Cosmetic title only | `FORBIDDEN` |
| Former holder or retired seat acts | `FORBIDDEN` |

Succession in S1 is **manual reassignment** only.

---

## Projection

Public / permissioned institution view:

```text
Offices:
- Treasurer — Nacre
- Archivist — vacant
```

Show name, vacant/occupied, current holder handle, public profile id. Do not leak private grant internals. Human and agent share this projection. Controller type does not change eligibility.

---

## A–J

| Test | Result |
|------|--------|
| A | Organization primitive + scoped grant. No eighth species |
| B | Dependency + uncertainty |
| C | COMMIT operations; no frozen new verb |
| D | Couples to later trade/repair/access without requiring them now |
| E | No new top-level verb |
| F | A notice desk habit can form around a named seat |
| G | `ENTITY_*` attributable |
| H | Human and agent identical |
| I | Meaningful with research hidden |
| J | Without this, “Treasurer” is only a word |

---

## Out of S1

```text
ROLE_* / event-catalog/0.3
elections / parties / legislation
salary / employment
institution TRADE / REPAIR
emergency scopes
designated succession
Chamber help advertising office commands
```
