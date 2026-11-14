# D03 — setup/readiness projection disclosure (Draft design)

**Status: Draft design only; unaccepted, unregistered and unimplemented.** This note clarifies value-source and disclosure obligations for the existing `setup.read` candidates. It selects no wire schema, route, error, numeric policy, identity/registry owner, persistence adapter or runtime implementation. All D01–D10 remain UNRESOLVED for full contract and qualification.

## Problem Statement

The [operation catalogue](operations.json) lists seven candidate response fields. The [records-only schema](../records.schema.json), at `/$defs/ReadinessProjection`, additionally requires the internal `record_type` discriminator. Neither that closed shape nor a matching field list proves that a value came from the authorized study/world or is safe to disclose. A valid `criterion_ref` can still encode private information; a `recorded` marker is not acceptance evidence.

At source baseline `c3cca9dd0a862f6c7feed00c3ef7fe75d4848d6e`, the [owning Draft RFC](../../../../rfcs/RFC-0131-study-access-control-plane.md), sections 1, 3, 5–9 and acceptance blockers, already requires an allowlisted redacted projection, current authority, scoped reads, consent restrictions and a qualified output fence. This follow-up makes those obligations reviewable per field without changing the record packet or catalogue.

## Solution

Propose constructing a fresh, minimal projection from separately qualified server sources after audience and scope checks. Every selected field needs both a permitted source and a permitted disclosure rule; source truth alone is not permission to publish it. Preserve the agreed read-only setup/readiness baseline and the eventual mounted Worker plus controlled-browser injected-dependency seam.

The seven names below remain catalogue candidates, not an accepted DTO. The existing record-only `record_type` is not silently added to that candidate inventory, removed from its record shape or reserved for an API. Whether a wire discriminator is required belongs to D03/D08 review.

## User Stories

1. As a scoped human platform principal, I want only the setup/readiness information I am entitled to see, without receiving roster, contact, audit or research content.
2. As an invitee, I want the displayed scope and capability to reflect current verified authority, not my request or a stale credential.
3. As a reviewer, I want to trace each output field to its scoped source and disclosure rule rather than accepting a schema-valid serialized record as redaction proof.
4. As a research operator, I want an already-authorized missing or unverified prerequisite indicator to remain distinct from consent, accepted evidence, gate promotion and run authority.
5. As an Admin who independently holds legitimate authority, I want this study-role view neither to manufacture nor erase that separate authority.
6. As an operator handling a dependency failure, I want truthful refusal rather than a fabricated unassigned steward, recorded criterion or healthy default view.

## Proposed value-source and disclosure obligations

| Existing response candidate | Required source obligation | Disclosure and refusal boundary |
|---|---|---|
| `view` | A server-selected, reviewed projection class for this admitted operation; not a client-selected record serializer. | The existing record constant is hypothetical representation, not negotiated wire adoption. A view label grants no access and cannot select a broader view. |
| `scope` | The exact study/world validated against current identity, grant and projection policy; request scope is only an input to validation. | No default world, wildcard, cross-partition alias or reflected unauthorized target. Authorization-store reads needed to establish the grant are distinct from fetching protected study content or another partition. |
| `as_of` | A truthful, qualified server observation context for the projected sources. | A UTC-shaped string is not a trusted clock, common snapshot or linearization witness. Do not replace unavailable provenance with client time or claim a stronger consistency interval; timestamp encoding, precision and clock policy remain D03/D06/D07/D08 work. |
| `capabilities` | The current effective baseline permission for this operation, constrained by verified identity, active exact-scope grant and current policy. | Ordinary access remains only `study.setup.read`; never union in Admin, management, Player/Controller, export, research or run authority. Do not relabel a cached signed claim as current permission. Independently held Admin authority uses its separate gate. |
| `steward_status` | Authoritative scoped designation and separately governed personal duty-acceptance state, interpreted under its reviewed lifecycle. | Existing unassigned/pending/accepted/withdrawn strings remain proposals. No name, contact, principal, duty receipt or roster is exposed merely to display status. Assignment, invitation acceptance, duty acceptance and consent remain different facts. Lookup failure is not evidence of unassigned status. |
| `prerequisites` | Only individually authorized, allowlisted non-sensitive criterion/status projections from qualified scoped sources and current applicable disclosure/consent policy. | A row's `criterion_ref` and status both require disclosure permission. Never copy arbitrary criterion names, private evidence references, explanations, contacts, payloads, hidden counts or forbidden existence. `recorded` is a display marker, not acceptance or research authority; an authorized missing/not-verified indicator is not permission to expose protected content. |
| `operational_authority` | The proposed baseline's explicit non-conferral marker, not an authorization grant or an evaluation of every independent authority a principal may hold. | Preserve `not_conferred` as a candidate representation only. Readiness does not enable runs, exports, hosting, consent, stewardship duties, world mutations or canonical acceptance. |

The record packet's row bound and other string/numeric representations remain proposals. This note does not adopt the value 32, define overflow behavior, authorize truncation or reserve a cursor/count field. Exact fields, vocabulary, bounds, ordering and completeness/error policy require D03/D04/D06/D08 review. No criterion catalogue, registry owner, bootstrap/configuration power, retention duration or new privileged writer is selected.

## Admission, construction and output obligations

The following is a proposed dependency sequence, not implemented code or proof that a second check closes a race:

```text
verified HumanPrincipal + current exact-scope grant + projection policy
  -> establish audience and permitted scoped sources
  -> obtain only the authorized source projections
  -> construct fresh reviewed fields; apply value/content disclosure policy
  -> recheck applicable current authority, consent and provenance
  -> complete the separately qualified revocation/output fence
  -> emit only the authorized projection
```

A generic Admin token, Controller credential, role label, opaque reference or existing study record does not supply a study grant. Authenticate and establish authority before revealing protected existence or reading another partition. Necessary authorization-store lookups do not authorize a study-wide roster or protected-content fetch.

Do not serialize a full grant, study, invitation, audit, designation, evidence or policy record and then rely on field removal as proof of safe output. Construct only the reviewed projection and apply content policy to every admitted reference and string. Shape closure alone cannot detect encoded secrets, identity details or hidden existence.

Missing, expired, withdrawn, contradictory or unverifiable applicable consent suppresses protected research-derived content and fails closed for dependent processing or release. Preserve the RFC's narrower exception for an already-authorized non-sensitive missing/unverified indicator; do not invent a blanket claim that all preparatory status is research data, or use that exception to expose protected reasons.

Unavailable, stale, mismatched or ambiguous authority/provenance is not success. No fabricated empty, healthy, unassigned or recorded result may hide a failed required dependency. Exact refusal/status/timing and any separately reviewed partial-projection policy remain undecided, as do policy version carriers, cache/cursor keys and snapshot guarantees. Protected caches, pagination, retries and queued work must retain the verified study/world/audience boundary and may not outlive current permission.

A second authorization read is not a qualified output fence. D07 must establish the actual linearization/delivery boundary and revocation races; already delivered information cannot be recalled. This design claims no mechanism for persistence, transactions, clocks, encryption, credentials or browser enforcement.

## Testing Decisions — future observations, not executed

Use the already-selected mounted Worker request/auth boundary with injected identity and persistence, then controlled browser workflows. These document-local SP labels are candidate observations only, not registered conformance IDs or executed SA acceptance. Keep per-field assertions, complete response privacy and source provenance visible together; a schema pass or a field-name snapshot is supplemental.

| Local candidate | Required future observation | Owning SA relationships |
|---|---|---|
| SP-01 | Admit an authorized exact-scope positive and assert all seven reviewed field meanings, minimal visible content and no inferred operational authority. Distinguish the record discriminator from the chosen wire contract. | SA-02, SA-10 |
| SP-02 | Anonymous/wrong-credential/no-grant controls receive no protected projection; forged requested scope/capability cannot select an authorized source. Preserve the legitimate admitted control. | SA-01, SA-09 |
| SP-03 | Identical local IDs in another study/world, cache and cursor variants cannot substitute another source or reveal its existence; qualify the eventual complete refusal contract. | SA-03, SA-14 |
| SP-04 | Feed prohibited content through each potentially admitted criterion/reference/string source and require its absence from the complete serialized response and rendered consumer, with a permitted populated positive. A marker alone is not permission. | SA-02, SA-14 |
| SP-05 | Missing/withdrawn/contradictory or unverifiable applicable consent blocks protected content while a separately authorized non-sensitive missing indicator remains possible under its actual policy. | SA-12 |
| SP-06 | Revoke or change effective authority/policy between admitted lookup and output; the qualified fence prevents stale delivery. Test unavailable/stale provenance without fabricating a successful default. | SA-08 |
| SP-07 | Authoritative unassigned and pending designation remain distinct from explicit duty acceptance; lookup failure cannot imitate either. No status implies participant consent or PSR/hosting readiness. | SA-11, SA-15 |
| SP-08 | Reload, retry and re-authentication use current qualified sources and audience/scope rather than a retained claim or cached success; browser display does not claim an unverified snapshot or current grant. | SA-08, SA-09, SA-15 |

These rows do not complete any entire SA criterion. Future source records, privacy assertions, transition effects, durable receipts and browser observations must be linked to the same admitted scope; independent green examples are not one end-to-end proof. No new mounted, browser, provider or production probe is authorized by this note.

## Out of Scope

No change to existing JSON schemas, examples/case rosters, checkers, operation catalogue, canonical identifiers/registries, version domains, RFC status, native validators/workflows or acceptance checklists. No adoption of the inherited row bound, timestamps, vocabularies or any lifetime/rate/retention/timing/error policy. No DTO/route/header/credential/cookie/redirect/cache implementation, criterion registry/configuration authority, provider, storage adapter, transaction or output-fence mechanism is selected.

No live invitations/accounts/roles/auth/providers/resources/data/migration/deployment/enrollment/research/export/hosting, coding partner or named steward. Preserve #882 hold, #851 draft, #777 frozen/source0, #733 OPEN, RFC-0128 unchecked acceptance and Q6/PSR/consent/steward/hosting gates. The D10 selected-A design and isolated shape packet remain unchanged; their local fixture results are not this design's disclosure evidence.

## Further Notes — remaining gates

D03 remains UNRESOLVED: this is value-source/disclosure design preparation, not an accepted response allowlist or implemented projector. All D01–D10 remain unresolved at full qualification. D02 identity/Account/bootstrap, D04 refusal/abuse/bounds, D06 policy/browser and D07 durable output fencing remain dependencies; D08 wire/version/discriminator decisions and D09 recorded security/compatibility/data/research/migration/rollback reviews remain independent.

Issue #396 stays OPEN/not runtime-ready; RFC-0131 stays Draft, unaccepted and unimplemented. Independent technical review and this publication's own CI/code-owner gate are separate from formal security acceptance. All prior PR-specific admin exceptions, including #403, are consumed; none applies to this new work. Refs #396.
