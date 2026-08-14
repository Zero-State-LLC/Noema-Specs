# RFC-0031 — Designated Institutional Succession

## Status

**Accepted**

Closes the designated-succession SPEC GAP, including the emergency-holder handoff. Succession is an explicit predeclared rule. No implicit jump. No elections, dynasties, or `event-catalog/0.3`.

## Problem

[SUCCESSION.md](../docs/SUCCESSION.md) names `DESIGNATED` but left PLAY office/emergency handoff unspecified. [RFC-0030](RFC-0030-emergency-scopes.md) asked: when the only emergency-authorized holder becomes unavailable, who—if anyone—receives a predeclared successor authority? An implementer would pick the nearest member or reset the emergency clock.

## Proposed change

Accept designated succession:

```text
SUCCESSION ≠ PLAYER IDENTITY TRANSFER ≠ OWNERSHIP TRANSFER ≠ CONTROLLER TRANSFER ≠ AUTOMATIC INHERITANCE
NO IMPLICIT JUMP
```

- A founder/officer may designate an ordered successor list (primary, optional secondary) on an office or an active emergency scope.
- Triggers are resign / vacate / leave-institution / office vacancy. Disconnect, idle, controller change, and DORMANT alone do not trigger.
- At activation, revalidate eligibility. First eligible candidate becomes holder. None eligible → vacancy / unstaffed scope.
- Office identity persists. Old grant ends; new holder instantiates the same profile.
- Emergency successor inherits the **remaining** `[now, end_cycle)` interval. Duration does not reset.
- Institution treasury and assets stay institution-owned. Personal reputation and private knowledge do not transfer.

Catalog: [`authority-catalog.gc4-s4.json`](../specs/authority-catalog.gc4-s4.json).  
Slice: [GC4-S4-SUCCESSION.md](../docs/GC4-S4-SUCCESSION.md).

## Alternatives rejected

| Alternative | Why |
|-------------|-----|
| Implicit nearest/oldest/most-active | No implicit jump |
| Elections / dynasty | Out of slice |
| Disconnect / controller change | Not world-identity unavailability |
| Reset emergency duration | Would extend temporary power |
| `SUCCESSION_*` event family | Catalog 0.3 |
| Holder self-designates without grant | Designation is founder/officer |

## Compatibility

Additive on GC4-S1–S3. Vacate without a designation still leaves `VACANT`. Frozen catalogs unchanged.

## Data / security

Rules live on the office / emergency scope (world head). Not a new table. Cross-world successors are `NOT_FOUND`. Dissolved orgs do not activate.

## Validation

`check_gc4_s4`: designate / resign-activate / no-designation vacancy / emergency remaining duration / ineligible / disconnect.

## Rollback

Ignore `succession` fields. Vacate remains vacant.

## Unresolved

Consensus and rule-based mechanisms from SUCCESSION.md. Dormancy-threshold rules. Institution-to-institution successor orgs.
