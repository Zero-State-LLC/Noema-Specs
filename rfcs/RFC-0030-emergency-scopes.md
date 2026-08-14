# RFC-0030 — Institutional Emergency Authority Scopes

## Status

**Accepted**

Closes the emergency-scope SPEC GAP. An emergency scope is a temporary, explicit, narrowly bounded AuthorityGrant overlay. It expires on world-time. It is not admin power, a permanent role upgrade, or a crisis engine. No new top-level verb. No `event-catalog/0.3`.

## Problem

[INSTITUTIONAL-AUTHORITY.md](../docs/INSTITUTIONAL-AUTHORITY.md) allows a versioned emergency rule but left activation, duration, and containment unspecified. An implementer would add `EMERGENCY_*` events, a superuser office, or let any Player self-declare power.

## Proposed change

Accept emergency scopes as time-bounded grants:

```text
EMERGENCY SCOPE ≠ ADMIN POWER ≠ UNIVERSAL BYPASS ≠ PERMANENT ROLE UPGRADE ≠ OWNER PRIVILEGE
```

```text
AuthorityGrant
+ predeclared template
+ deterministic condition
+ [start_cycle, end_cycle)
+ explicit source office
```

- Predeclared templates live on the institution. Activation does not invent capabilities.
- Source authority is founder/officer or an occupied office whose profile is listed on the template.
- Ordinary TRADE / REPAIR run under `acting_for` + `emergency_scope_id`.
- Expiry is world-time. A late scheduler does not extend power.
- Revocation ends future acts; settled acts stand.
- Vacant office cannot activate or use a scope bound to that seat.
- No implicit successor.

Catalog: [`authority-catalog.gc4-s3.json`](../specs/authority-catalog.gc4-s3.json).  
Slice: [GC4-S3-EMERGENCY-SCOPES.md](../docs/GC4-S3-EMERGENCY-SCOPES.md).

## Alternatives rejected

| Alternative | Why |
|-------------|-----|
| `EMERGENCY_STARTED` family | Catalog 0.3 |
| Self-declare “emergency” | Natural language is not a grant |
| ALL_ACTIONS / SUPERUSER | Escalation |
| Wall-clock duration | World-time is the clock |
| Implicit successor | Designated succession is the next slice |
| Operator routed through grants | Control plane stays separate |

## Compatibility

Additive on GC4-S1/S2. Personal and ordinary institutional TRADE/REPAIR unchanged when no scope is cited. Frozen catalogs unchanged.

## Data / security

Scopes live on the organization (world head). Not a new table. Cross-world refs are `NOT_FOUND`. Emergency does not override `ACCESS_RESTRICTED`.

## Validation

`check_gc4_s3`: activate / expire / revoke; containment; vacancy; no self-grant; no new verbs.

## Rollback

Ignore emergency templates and `ORG_EMERGENCY_*`. Ordinary office TRADE/REPAIR remain.

## Unresolved

Designated succession when the only emergency holder becomes unavailable. Delegation of emergency templates. Operator-visible-only recovery remains control-plane.
