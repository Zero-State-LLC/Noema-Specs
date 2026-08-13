# Institutional Authority (GC4)

**Status:** Product authority for playable institutional offices. P1. Phase GC-B.  
**Campaign:** [GAME-COMPLETENESS-PLAN.md](GAME-COMPLETENESS-PLAN.md)  
**Does not replace:** [INSTITUTIONS.md](INSTITUTIONS.md) · [SUCCESSION.md](SUCCESSION.md) · [WORLD-SERVICES.md](WORLD-SERVICES.md)  
**v0.1 org roles** (founder/officer/member/advisor) remain the coarse Chamber set until this package is executable.

Core rule:

> A title with no world authority is presentation, not an institutional mechanic.

No free-form LLM authority.

**Doctrine:** offices are authority configurations over existing primitives, not a new codebase per title ([COMPLEXITY-DOCTRINE.md](COMPLEXITY-DOCTRINE.md)).

GC4-S0 machine pins: [GC4-FIRST-SLICE.md](GC4-FIRST-SLICE.md) · [RFC-0008](../rfcs/RFC-0008-office-authority-pins.md). Named offices, emergency scopes, and `ROLE_*` events remain **SPEC GAP**.

---

## Thesis

v0.6 institutions already persist beyond founders. Completeness makes them **positions a Player can hold**, with bounded, auditable powers.

World Services remain **not Players**. A Relay Keeper desk is not an office. A Player **Custodian** of a maintenance order is an office.

---

## Role definition

A **role** (office) is a versioned capability grant bound to one institution.

| Field | Meaning |
|-------|---------|
| `role_id` | Stable identity within the institution or a shared catalog |
| `institution_id` | Owning institution |
| `authority_scopes` | Closed set of granted powers |
| `assignment_rule` | How the seat is filled |
| `term` | Open, fixed cycles, or until vacancy rule |
| `delegation_allowed` | Whether the holder may grant a strictly smaller subset |
| `requires_recognition` | Optional mastery/social-memory gates |

Candidate names (examples, **not** frozen unless a catalog later requires them):

```text
Steward
Treasurer
Archivist
Envoy
Quartermaster
Surveyor
Auditor
Marshal
Speaker
Custodian
```

An implementation MAY use institution-specific display names. Capability is defined by `authority_scopes`, not by the string “Marshal”.

v0.1 `founder` / `officer` / `member` / `advisor` map as coarse scopes. This package **refines** them; it does not delete membership.

---

## Authority scopes (closed families)

Anything not listed is denied.

| Scope family | May include | Must not include |
|--------------|-------------|------------------|
| Resource | Spend or reserve institution-held lots within a cap | Silent personal appropriation |
| Access | Grant/revoke institution access lists already expressible | Create hidden rooms |
| Contract | Propose/accept institution-side `TRADE` or `AGREEMENT_*` after institution rules | Bind third parties who never consented |
| Communication | Post to institution channels / notices ([COMMUNICATION-ECOLOGY.md](COMMUNICATION-ECOLOGY.md)) | Read private Player DMs |
| Territorial | Assert institution claims already legal under territory rules | Rewrite geography |
| Conflict | Authorize institution participation in a contest form | Personal HP combat |
| Audit | Read institution records; emit audit notes | Delete ledger history |
| Emergency | Temporary extra scope under a declared institution emergency rule | Permanent undefined power |

Conflicting grants: if two offices claim exclusive control of the same object, the institution’s versioned rule names precedence. If the rule is missing, the action **fails closed**.

---

## Lifecycle

```text
DEFINED → ASSIGNED ⇄ VACANT → REMOVED
                ↓
            SUCCEEDED
```

| Operation | Rule |
|-----------|------|
| Creation | Institution with role-definition authority (or founder bootstrap) adds a role with explicit scopes |
| Assignment | Closed mechanism: designation, rule-based, consensus, or vacant-fill ([SUCCESSION.md](SUCCESSION.md)) |
| Removal | Holder resigns, is removed by authorized office, term ends, or crime/expulsion rule fires |
| Vacancy | Role remains; institution does not dissolve; actions requiring the office fail with `ROLE_VACANT` |
| Succession | Existing succession mechanisms; failed succession leaves `VACANT` unless `institution_continues` says otherwise |
| Term / tenure | Versioned; expiry produces `VACANT` or automatic successor if designated |
| Delegation | Optional; must be a **strict subset** of the delegator’s scopes; expires with the delegator or sooner |
| Abuse / failure | Ultra vires action is `FORBIDDEN`. Repeated abuse may be institutional crime if ledgered rules say so |
| Transformation | Institution `TRANSFORMED` may remap roles via successor edges; unmapped roles become `REMOVED` with history kept |

[SUCCESSION.md](SUCCESSION.md) already flags candidate events `ROLE_ASSIGNED`, `ROLE_VACATED`, `SUCCESSION_RECORDED`, `INSTITUTION_TRANSFORMED` as requiring RFC. This package **does not** silently add `event-catalog/0.3`.

---

## Audit log

Every successful office action MUST be attributable:

```text
actor_player_id
role_id
institution_id
action_id / event_id
scope_invoked
cycle
```

Audit records are institutional memory ([INSTITUTIONAL-MEMORY.md](INSTITUTIONAL-MEMORY.md)). They MAY be incomplete to unauthorized readers. They MUST NOT be secretly deleted.

---

## Emergency authority

An institution MAY define one versioned emergency rule:

- trigger is a ledgered condition (not an LLM judgment);
- extra scopes are listed;
- duration in cycles is finite;
- cooldown or ratification is required to repeat;
- expiry returns scopes to the ordinary set.

Undefined emergency power does not exist.

---

## Human / agent parity and presentation

Humans and agents hold offices identically. A natural-language “I am the Steward” message is not an assignment.

Cosmetic titles in messages or culture ([EMERGENT-CULTURE.md](EMERGENT-CULTURE.md)) have **zero** authority unless bound to a role record.

---

## Coupling

| System | Link |
|--------|------|
| Mastery | Eligibility MAY require recognition |
| Social memory | Institution edges MAY block assignment |
| Construction | Institution-owned structures acted on only by scoped offices |
| Communication | Envoy/Speaker scopes post notices |
| Conflict | Marshal-like scopes authorize institutional contest participation |
| World Services | Offices may operate service desks as Players confirming actions; they do not become services |

---

## SPEC GAP

```text
GC4-S0 closed: v0.1 founder/officer/member/advisor grants on ORG_*
named-office scope catalog (Steward / Treasurer / …)
assignment/removal beyond ORG_MEMBER_* (likely later COMMIT operations)
event types ROLE_* (no silent catalog expansion)
conflict-precedence rules
emergency rule schema
fixtures: vacancy, succession, institution TRADE/REPAIR
conformance
PLAY/WATCH office projections
```

Until GC4-S1, only the four v0.1 membership roles are executable authority.

---

## Acceptance (scenario D)

A Player is assigned a bounded office, performs a permitted institution `TRADE` or `REPAIR` under that scope, is `FORBIDDEN` from an unscoped action, leaves office, and the successor (or vacancy) is the only remaining holder of that scope.
