# GC4-S3 — Institutional Emergency Authority Scopes

**Status:** Executable specification. Runtime authorized with RFC-0030.  
**Parent:** [GC4-S2-INSTITUTION-ACTIONS.md](GC4-S2-INSTITUTION-ACTIONS.md) · [INSTITUTIONAL-AUTHORITY.md](INSTITUTIONAL-AUTHORITY.md)  
**RFC:** [RFC-0030](../rfcs/RFC-0030-emergency-scopes.md)  
**Does not open:** designated succession · martial law / crisis director · `event-catalog/0.3` · admin-as-Player · GC1-S2 benefits

S3 adds a temporary, predeclared grant overlay. It is not a second permission system.

---

## Doctrine

```text
emergency capability ⊆ template ⊆ source office/profile
validity = world.cycle ∈ [start_cycle, end_cycle)
expired even if the expiry job has not run
```

| Temptation | Verdict |
|------------|---------|
| Self-declare emergency | **REJECT** |
| ALL_ACTIONS | **REJECT** |
| Permanent emergency office | **REJECT** |
| Wall-clock extension | **REJECT** |
| Emergency beats ACCESS_RESTRICTED | **REJECT.** Fail closed |
| Implicit successor | **REJECT** |
| Operator uses institution grants | **REJECT** |

Pressures: **dependency** (someone must still hold the source seat) and **uncertainty** (the clock will end the grant).

---

## Representation

Not a new world object family. A scope is an AuthorityGrant overlay on the organization.

### Template (predeclared)

| Field | Meaning |
|-------|---------|
| `template_id` | Stable `emrule.<slug>` |
| `source_profiles` | Offices that may activate (`GRANT_ACCESS`, `OPERATE_NAMED_ASSET`, `OPERATE_RESOURCE_ACCOUNT`) plus founder/officer |
| `capability` | `REPAIR` or `TRADE` |
| `condition` | `ASSET_CONDITION_LT` + threshold, or `TREASURY_LT` + resource + threshold |
| `duration_cycles` | Finite integer, hosted default **3** |
| `max_spend` | Optional treasury cap for TRADE |

Default templates are installed at `ORG_CREATE`. Founder/officer may add more via `COMMIT.ORG_EMERGENCY_DEFINE`.

### Scope (activated)

| Field | Meaning |
|-------|---------|
| `scope_id` | `emscope.<hex>` |
| `template_id` | Source template |
| `institution_id` | Owning org |
| `holder_player_id` | Member who may act |
| `source_office_id` | Occupied office used to activate, if any |
| `capability` | Copied from template |
| `target_ref` | One entity id or `treasury` |
| `start_cycle` / `end_cycle` | Half-open world-time interval |
| `status` | `ACTIVE` \| `EXPIRED` \| `REVOKED` |
| `spent` | TRADE lots already used under the cap |
| `reason` | Declaration text (not authority) |

Lifecycle: `ACTIVE → EXPIRED | REVOKED`. No PROPOSED in hosted S3.

---

## Activation

`COMMIT.ORG_EMERGENCY_ACTIVATE`

Requires:

```text
org ACTIVE, same world
actor is founder/officer OR holds an occupied source_profile office
holder is a current member
template exists
condition is true now
no duplicate ACTIVE scope for same template+holder+target
```

Natural-language “emergency” does nothing.

Human alias (org help only):

```text
emergency activate <org> <template> <target>
emergency revoke <scope>
```

---

## Conditions (deterministic)

| Kind | True when |
|------|-----------|
| `ASSET_CONDITION_LT` | Named live entity `condition < threshold` (hosted default 25) |
| `TREASURY_LT` | Institution treasury `resource < threshold` (hosted default energy 5) |

No LLM predicates.

---

## Use

Ordinary TRADE / REPAIR with:

```text
acting_for = org_id
emergency_scope_id = scope_id
```

If a standing office grant already authorizes the act, that path remains. Emergency is an additional context, not a bonus.

Authorization when citing a scope:

```text
scope ACTIVE
world.cycle < end_cycle
holder == actor
actor still a member
if source_office_id set: that office still OCCUPIED by actor (or founder/officer source)
capability matches the verb
target_ref matches the asset / treasury
TRADE remaining max_spend covers the offered lots
ACCESS_RESTRICTED still applies
```

If the bound office is vacant, the scope cannot authorize.

No implicit jump to another Player.

---

## Expiry and revocation

- Expiry: `world.cycle >= end_cycle` → ineffective. Cycle commit marks `EXPIRED`.
- Worker delay / wall clock do not extend `end_cycle`.
- Revoke: `COMMIT.ORG_EMERGENCY_REVOKE` by founder/officer or the still-valid source office holder.
- Revocation / expiry do not unwind settled TRADE or completed REPAIR.
- TRADE/REPAIR are `ENTRY_ONLY` for this overlay: authorization is captured at COMMIT.

---

## Events

`ENTITY_CREATE` (`DOCUMENT`, `location=null`) on activate. `ENTITY_UPDATE` on revoke / expire. No `EMERGENCY_*` types.

---

## Visibility

| Surface | Sees |
|---------|------|
| PLAY (holder) | `Emergency authority active: {capability} on {target} until cycle N.` |
| PLAY (other members) | That a public declaration exists, not private target if restricted |
| WATCH | `An institution declared a temporary repair authority.` only for REPAIR/TRADE scopes (public consequence, no balances, no operator rationale) |
| Admin | Full scope record |

---

## Out of S3

```text
designated succession
martial law / crisis director
permanent emergency role
operator-as-institution
emergency cost discount
event-catalog/0.3
```

---

## Runtime rule

Hosted Chamber evaluates `[start, end)` on every authorize. Cycle commit expires due scopes. Do not reseed Genesis.

## Acceptance

1. Authorized activation when the condition holds.
2. Bounded emergency REPAIR / TRADE use ordinary verbs.
3. Expired and revoked scopes cannot authorize.
4. Self-declare and vacant office fail.
5. Emergency does not override ACCESS_RESTRICTED.
6. Human and agent holders have the same interval and capability.
