# D02 — existing Account resolution for study management (Draft design)

**Status: Draft design only; unaccepted, unregistered and unimplemented.** The operator explicitly selected **existing uniquely qualified Account link only; missing or ambiguous linkage refuses** for the initial **study-management issuer path**. Unavailable required identity/link state also fails closed under the owning Draft RFC. This selects a proposed boundary, not an Account record, lookup implementation, onboarding flow, accepted policy or runtime permission. Full D02 and D01–D10 remain UNRESOLVED for qualification.

## Problem Statement

The [Account/configuration design](IDENTITY-AUTHORITY-DESIGN.md) separates Account attribution, same-actor Admin admission, exact management authorization and owner-approved out-of-band registry configuration. It does not establish the actual Account join. An optional claim, one fetched row or a reusable function name is not evidence of a current uniquely qualified authoritative Account.

Source baseline: Specs `7ce5d5e56e35ed4e944623a76a981b8c0b4fde4a`, runtime `5ed9635f7fbd73bbab6dbc5bd3fad6ffbe51d627`. The runtimes are [independent](https://github.com/Zero-State-LLC/Noema/blob/5ed9635f7fbd73bbab6dbc5bd3fad6ffbe51d627/AGENTS.md#L1-L39); bounded offline-source findings below are not a hosted production failure, executed exploit or global absence claim.

## Solution and selected Draft boundary

For this initial management issuer path, a future resolver MUST use an already established, uniquely qualified eligible Noema Account link. Missing, ambiguous, unavailable, stale or unverifiable linkage MUST refuse rather than provision an Account, choose the first candidate, trust an optional JWT Account field, or invoke a combined legacy identity binder. The exact current-eligibility, provider-context, recovery and durable uniqueness predicates still need review and qualification.

This boundary MUST NOT create or relink an Account implicitly through a management request, create/bind a Player or Controller, open a PlayerSession, mint agent/play credentials, seed a registry or confer a new role. It does not prohibit separately authorized canonical Account-only human onboarding; that flow is not built or selected by this note. Intended-invitee/contact acceptance and recovery remain separate D02 obligations. Legitimate existing Admin operations outside the new contract remain unchanged.

[Canonical ownership](../../../../docs/AUTH-AND-IDENTITY.md#planned-compatibility) stays Supabase Auth for human proof, Noema Postgres control plane for Account/session/scopes, and World DO for live game transitions. Provider subjects remain links rather than Noema domain identifiers; global Account resolution and exact study/world operation permission are separate layers. No new identity provider, database, authoritative file/env registry, migration or adapter is selected.

## User Stories

1. As a qualified Admin, I want a uniquely established Account link before new study-management actions can be attributed to me.
2. As a person with a verified provider identity but no qualified link, I want truthful refusal rather than an implicit Account or unexpected Player/Controller.
3. As a reviewer, I want ambiguity detected rather than a first-row result being treated as uniqueness proof.
4. As an owner, I want management admission unable to create its own Account, registry authority or onboarding exception.
5. As a platform user, I want this initial issuer restriction not to rewrite unrelated human login or invitation-contact flows.
6. As an operator, I want source reuse separated from qualified current storage, issuer, recovery and same-actor evidence.

## Maintained prior art and reuse limits

| Pinned source | Observed behavior in the inspected spans | Proposed reuse limit |
|---|---|---|
| [Python human binding](https://github.com/Zero-State-LLC/Noema/blob/5ed9635f7fbd73bbab6dbc5bd3fad6ffbe51d627/src/noema/auth/identity.py#L104-L196) | Subject-based Account lookup can upsert Account and Player, then ensure a browser Controller and call token issuance. Token verification also has an inspected retry without the first audience argument. | This combined producer is not an Account-only resolver or the new strict issuer/audience contract; do not call it wholesale for this feature. |
| [Controller/token production](https://github.com/Zero-State-LLC/Noema/blob/5ed9635f7fbd73bbab6dbc5bd3fad6ffbe51d627/src/noema/auth/identity.py#L206-L282) | Controller and credential writes plus access/refresh material are produced. | Do not inherit these effects from Account resolution; no such function was executed by this audit. |
| [Subject getter](https://github.com/Zero-State-LLC/Noema/blob/5ed9635f7fbd73bbab6dbc5bd3fad6ffbe51d627/src/noema/persistence/store.py#L592-L613) and [DDL/index](https://github.com/Zero-State-LLC/Noema/blob/5ed9635f7fbd73bbab6dbc5bd3fad6ffbe51d627/src/noema/persistence/store.py#L303-L373) | Getter uses `fetchone()`; inspected Account DDL has Account-ID primary key and an ordinary subject index, not a declared unique subject constraint in those spans. | One returned row is not proof of exactly one authoritative link. Do not claim actual duplicate data, all-migration coverage or hosted schema qualification. |
| [Hosted human resolver](https://github.com/Zero-State-LLC/Noema/blob/5ed9635f7fbd73bbab6dbc5bd3fad6ffbe51d627/workers/noema/src/auth.ts#L54-L167) | Separate verified human-provider path and optional carried Account claim. | Useful maintained boundary, not itself qualified current Account linkage or a same-actor relation to a separate Admin bearer. |
| [Hosted Admin admission](https://github.com/Zero-State-LLC/Noema/blob/5ed9635f7fbd73bbab6dbc5bd3fad6ffbe51d627/workers/noema/src/admin-auth.ts#L40-L148) | Separate Admin credential type/scope, authentication context and shared/mailbox/legacy operator labels. | Existing Account plus a generic label or unrelated valid credential is not the complete new management chain. |

No offline runtime behavior is changed or qualified for hosted use by this document. The inspected persistence methods are prior art, not a selected Worker/control-plane adapter. The canonical human-login prohibition on Player/Controller/PlayerSession effects remains independently binding.

## Proposed admission and refusal obligations

| Boundary | Proposed obligation |
|---|---|
| Human proof → link lookup | Verify the proper provider/issuer/audience context before resolving a canonical subject link; no caller-selected actor or domain-ID conversion. |
| Link cardinality/eligibility | Establish exactly one eligible current authoritative Account under reviewed linkage/recovery rules; zero, multiple or unqualified outcomes refuse. A first-row query or optional claim cannot prove that predicate. |
| Account → Admin | Demonstrate the same attributable actor satisfies existing valid Admin admission; two unrelated valid credentials cannot be composed into authority. The mechanism remains unselected. |
| Admin → management | Require independent current exact study/world/operation authorization from the separately owner-authorized registry model. No first-user, wildcard/default scope or generic-Admin bootstrap fallback. |
| Transition/audit/output | Preserve qualified actor, link/configuration/version and exact operation scope through the separately qualified durable and output boundaries; unavailable or stale state is not successful default state. |

Necessary identity/authorization-store reads do not permit protected study content or another partition's disclosure. The no-provisioning/refusal boundary concerns domain authority and identity effects; it does not claim every separately reviewed audit/idempotency path performs zero writes. Such bookkeeping cannot create or widen authority and needs its own privacy/durability contract.

Preserve the selected [out-of-band registry model](IDENTITY-AUTHORITY-DESIGN.md), with no registry-configuration UI capability yet. Registry configuration differs from study-configuration editing and the proposed Admin invite/access/later-steward interfaces. No real owner/Account is appointed. Preserve independently legitimate Admin power and no invented two-Admin rule.

## Testing Decisions — future observations, not executed

Use the already selected mounted Worker request/auth boundary with injected identity/persistence, then controlled browser workflows. These document-local AR labels are unregistered future observations, not executed SA cases, offline test passes or hosted qualification. Do not call a legacy binder or live provider merely to obtain a qualification claim.

- **AR-01 — Existing unique Account**: Properly verified provider identity resolves exactly one eligible existing Noema Account under the qualified issuer/provider linkage; preserve legitimate positive and actual internal Account identity.
- **AR-02 — No implicit provisioning**: No matching Account refuses the new study-management issuer path without creating Account, Player, Controller, PlayerSession, credentials or registry authority.
- **AR-03 — Ambiguity is not fetch-first success**: Two competing subject/link matches or unverifiable uniqueness refuse; one fetched row cannot prove exactly one authoritative match.
- **AR-04 — Provider scope and identifiers**: Verify the intended issuer/audience/provider context; equal subject strings in another identity context do not substitute for the reviewed link. Provider subjects remain links, not invented Noema IDs.
- **AR-05 — Account current eligibility**: Apply the reviewed current Account status/link/recovery policy; stale, replaced, ambiguous or unavailable linkage cannot be accepted from an optional JWT field or old result.
- **AR-06 — No Player side effects**: Provider proof and Account resolution remain human-platform operations and cannot create/bind Player or Controller, open a PlayerSession or issue agent/play credentials.
- **AR-07 — Same-actor Admin boundary**: A resolved Account still needs demonstrated same-actor existing Admin admission; unrelated valid human/Admin credentials cannot be combined.
- **AR-08 — Separate exact management permission**: Existing Account plus Admin alone does not grant registry configuration or study management; require independent owner-approved configuration and exact current study/world/operation authorization.
- **AR-09 — Refusal privacy**: Missing and ambiguous Account/link states do not expose protected contact, Account existence or hidden scopes in complete responses/logs/audit/browser output; qualify actual refusal policy separately.
- **AR-10 — Legacy reuse boundaries**: A query/mapping name or passing offline legacy test is not qualified hosted integration; any later reuse excludes combined Player/Controller/token producers and proves current unique-link/durable/issuer predicates.

## Out of Scope and remaining gates

No Account creation/relinking/onboarding, invitee-contact recovery policy, new credential/claim/schema/DTO/route/error/timing/retention/rate/lifetime/version, concrete lookup/query/index/migration, provider/adapter/RLS/transaction or output-fence implementation is selected. Existing schemas/catalogue/fixtures and D02/D03/D10 proposals remain unchanged. No native validator/workflow, canonical identifier, RFC status, acceptance checklist or runtime file changes.

Qualified Account uniqueness/eligibility/recovery, same-actor Admin binding, complete trusted configuration, machine/wire/policy/durable/output/security review and eventual mounted/browser evidence remain D02/D01–D10 prerequisites. RFC-0131 remains Draft/unaccepted/unimplemented; issue #396 remains OPEN/not runtime-ready. Publication/CI/static review or a one-time review exception is not formal security acceptance. PR #406 and earlier exceptions are consumed and cannot authorize this PR's merge.

No live accounts/roles/auth/registry configuration/provider/resources/data/migration/deployment/enrollment/research/export/hosting or coding-partner assignment. Preserve #882/Q6, #851, frozen #777/source0, #733 OPEN, RFC-0128, PSR, consent, steward, hosting and protected scratch holds. Refs #396.
