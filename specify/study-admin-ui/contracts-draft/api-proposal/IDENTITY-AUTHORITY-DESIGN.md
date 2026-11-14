# D02 — Account binding and management configuration (Draft design)

**Status: Draft design only; unaccepted, unregistered and unimplemented.** The operator explicitly selected **owner-authorized out-of-band configuration only; no registry-configuration UI yet**, for this Draft. This chooses the initial proposed authority boundary, not a real owner/Account, installed registry, accepted policy, runtime mechanism or implementation/deployment grant. D02 and all D01–D10 remain UNRESOLVED for full contract and qualification.

## Problem Statement

The [owning Draft RFC](../../../../rfcs/RFC-0131-study-access-control-plane.md), §§1–2 and acceptance blocker2, requires an attributable Account plus existing Admin admission and exact management authorization. A signed Admin bearer, mailbox-derived operator label, fresh session or optional Account-shaped field is not by itself that complete chain. The bootstrap/configuration path MUST NOT derive its own initial authority from the registry it is creating.

At Specs source `afd1b07d3b76fb021b880674c303fd877d414f18` and runtime source `5ed9635f7fbd73bbab6dbc5bd3fad6ffbe51d627`, the bounded source audit revalidated the maintained issuer chain and neighboring human-principal seam. It is not a global absence claim, live provider inspection, executed behavior test or recorded security acceptance.

## Solution and selected Draft model

Use a separately owner-authorized **out-of-band configuration process** for the initial registry seed, later changes and recovery. Do not add a registry-configuration UI capability in this phase. Its attributable acting Account, authorization source, exact subjects/study/world/operations, validity/version and recovery procedure still need a complete reviewed contract before application. No concrete process, file format, policy values, named actor, signing method or adapter is selected here.

A reviewed configuration artifact is an input and provenance witness, not an alternative identity/scopes authority. Preserve [canonical ownership](../../../../docs/AUTH-AND-IDENTITY.md#planned-compatibility): Supabase Auth supplies human proof; Noema Account/session/scopes belong to its Postgres control plane; World DO handles live game transitions. No new provider or infrastructure, live control-plane write, schema, migration or environment change follows from this selection.

## User Stories

1. As an invited study user, I want the read-only study/world grant to remain separate from global Admin and management configuration.
2. As an independently qualified Admin, I want legitimate existing powers preserved while new management writes require their own exact authorization.
3. As an owner, I want initial authority, changes and recovery to come from a separately authorized process rather than a first-login or self-grant rule.
4. As an accountable issuer, I want the recorded Account to be the actual verified actor, not an email/name supplied with a shared credential.
5. As a reviewer, I want two valid credentials for different actors to fail the same-actor requirement rather than be combined into authority.
6. As an operator, I want missing or unavailable binding/configuration state to refuse truthfully, not fabricate a registry or owner.
7. As an invitee, I want later contact changes/recovery not to transfer an accepted grant or confer configuration power.
8. As a future implementer, I want selected Draft boundaries separated from unselected Account-link, wire, durable and security mechanisms.

## Source-grounded identity distinctions

| Inspected boundary | What the pinned source establishes | Remaining qualification |
|---|---|---|
| [Admin mint and verifier](https://github.com/Zero-State-LLC/Noema/blob/5ed9635f7fbd73bbab6dbc5bd3fad6ffbe51d627/workers/noema/src/admin-auth.ts#L40-L148) | Existing signed Admin type/scope, authentication context, shared/legacy or mailbox-derived operator label and session | An attributable stable Noema Account and its relation to the admitted Admin actor; opacity/session freshness is not that binding |
| [Mailbox consumer](https://github.com/Zero-State-LLC/Noema/blob/5ed9635f7fbd73bbab6dbc5bd3fad6ffbe51d627/workers/noema/src/admin-auth.ts#L298-L354) | Provider verification response, normalized email, existing Admin allowlist and mailbox-labelled Admin mint | The inspected producer does not establish a provider-subject-to-Account join; do not reuse the allowlist for ordinary study invitees |
| [Human principal](https://github.com/Zero-State-LLC/Noema/blob/5ed9635f7fbd73bbab6dbc5bd3fad6ffbe51d627/workers/noema/src/auth.ts#L54-L167) and [types](https://github.com/Zero-State-LLC/Noema/blob/5ed9635f7fbd73bbab6dbc5bd3fad6ffbe51d627/workers/noema/src/types.ts#L48-L75) | Distinct human/Player types, human-provider verification path, subject-based human identity and optional Account claim | Current authoritative Account linkage, correct recovery and same-actor relation to the Admin admission; a carried string is not store qualification |
| Existing world admission | A separate existing world resolver, not a study registry | Exact verified study/world/operation; no inherited default-world/wildcard authority |

The source audit verified exact Git-blob and byte identity of current `admin-auth.ts`, `genesis.ts` and `ops.ts` against the earlier audited source cohort at `3267d4267ea3e62be7d6342763065d4b67a0deda`. That is source-identity carryforward, not deployed evidence or a new runtime execution. Neighboring identity code was inspected separately; this note does not claim that the whole runtime lacks Account functionality.

## Producer, authority and consumer obligations

| Proposed boundary | Required obligation | Refused substitute |
|---|---|---|
| Verified human proof → Account | Resolve exactly one stable authoritative Noema Account in the proper provider/issuer/audience context, under reviewed linkage and recovery rules | Caller-selected Account/name/email, mailbox hash, fresh session, optional claim alone |
| Account → Admin admission | Establish that the Account is the same attributable actor satisfying existing valid Admin admission | Unrelated valid Admin and human credentials combined; ordinary role text or Player/Controller coercion |
| Owner-approved configuration → initial/changed/recovered registry | Require independently established configuration authority and attributable actor; validate exact subject/scope/operations/current validity/version before qualified control-plane application | Registry self-authorization, first user, ordinary Admin request, edited study record, wildcard/default, invitation acceptance |
| Current registry → management operation | Intersect attributable Account, valid Admin admission and explicit live exact world/study/operation authorization before protected target disclosure or mutation | Signed token alone, stale positive cache, ordinary study membership, steward/readiness badge |
| Transition → audit/retry/output | Preserve actual actor, exact scope, current configuration decision/version and qualified transition/recovery/output witness | Shape-valid reference as authority, ambiguous write labelled success, old backup resurrecting rights, second read advertised as a solved fence |

Necessary authorization-store reads remain distinct from protected study-content lookup. Unavailable, ambiguous, stale or missing Account/authority/configuration state is not permission to create it implicitly or return successful default state. Current Admin operations outside the new contract remain unchanged.

## Configuration is not ordinary study administration

The selected out-of-band model concerns **management-authority registry configuration**, not a grant of study-configuration editing and not removal of the proposed Admin invitation/access or later steward interfaces. Ordinary study membership stays `study.setup.read` only. Study-configuration writes, if later authorized, remain separately enumerated exact operations; this note adds no endpoint or generic object patch.

A generic Admin label does not configure management authority. The same independently qualified Admin may hold separately authorized configuration responsibility if the adopted policy permits it; no mandatory two-Admin/second-person rule is introduced. No shared credential is silently upgraded into individual Account attribution. A future recovery path MUST preserve revocations/terminal states and cannot treat old registry contents as fresh authority.

The [record packet](../README.md) remains hypothetical structure. Its `configuration_decision_ref` and `configuration.update` vocabulary neither select an actor nor install a registry/UI/API. Existing schemas, operation catalogue and fixtures remain unchanged. This design selects an initial governance boundary, not a live bootstrap power or a complete configuration contract.

## Testing Decisions — future observations, not executed

Use the selected mounted Worker request/auth boundary with injected identity/persistence, then controlled browser workflows. A separately qualified out-of-band configuration producer MUST supply controlled authoritative inputs; no new HTTP configuration route is implied. These document-local D02 labels are future observations, not registered conformance IDs, complete SA coverage or child/native test results.

- **D02-01 — Qualified positive**: Current verified provider subject joins one authoritative Noema Account, the same acting Account satisfies existing Admin admission and exact world/study/operation authorization; retain attributable transition and current version.
- **D02-02 — Shared credential is not an individual**: A shared Admin bearer plus caller-supplied name/account cannot authorize new management writes; preserve unrelated existing operator behavior.
- **D02-03 — Opaque labels do not establish Account linkage**: Mailbox-derived operator label, legacy fallback and a fresh session identifier cannot substitute for a qualified Account binding.
- **D02-04 — Human proof is not the Account join**: Valid HumanPrincipal/provider subject with absent, stale, ambiguous or mismatched Account linkage fails the new boundary; a shaped account_id claim alone is not store qualification.
- **D02-05 — Same-actor binding**: Independently valid Admin material for actor A and HumanPrincipal/Account material for actor B cannot be combined into management authority.
- **D02-06 — Exact management authorization**: A legitimate Admin without the new exact operation/study/world authorization is refused; preserve legitimate positive and wrong-partition controls without protected existence disclosure.
- **D02-07 — Unavailable authority is not a default registry**: Missing, stale or unavailable binding/configuration source denies the new operation; no implicit registry, first-user owner or global-Admin fallback.
- **D02-08 — No request-driven bootstrap**: Client request fields, the edited study record, invitation acceptance and ordinary study grants cannot install or widen configuration authority; owner selection is not a deployment grant.
- **D02-09 — Configuration retry and revocation**: Replay/conflict/current-authority changes cannot duplicate, widen or resurrect configuration or management rights; require qualified durable recovery/output boundaries.
- **D02-10 — Recovery retains terminal truth**: Rollback/restore/recovery cannot reinstate revoked authority or accept an older version as current; recovery actor and scope require their own reviewed authority.
- **D02-11 — Intended contact remains separate**: Verified-contact acceptance and later reassignment/recovery cannot transfer an accepted grant to another Account or mint Admin/configuration authority.
- **D02-12 — Privacy and evidence tier**: No operator label, Account/contact linkage or audit detail is exposed merely because the binding is valid; positive/refusal outputs and browser display obey their actual disclosure policy. Design assertions are not runtime passes.

Positive, refusal and retained-state observations MUST link to the same qualified actor/scope/version and preserve complete response/audit privacy. Helper/HTML/shape checks are supplemental. No new mounted, browser, provider or production probe is authorized by this note.

## Out of Scope and remaining gates

No real person/Account/role appointment, registry installation/change/recovery, provider call, resource/data/auth mutation, schema/migration/deployment, enrollment, research/export/hosting or coding-partner assignment. No new identity provider, Account/contact-link/recovery protocol, Admin-to-Account binding mechanism, configuration encoding/distribution/signing format, credential transport, route/method/DTO/status/error, lifetime/retention/rate/timing policy, adapter/RLS/transaction, output fence or version registration is selected. Steward designation remains later Admin-interface work with separate duty acceptance and consent.

D02 still needs full identity/Account/contact recovery, same-actor issuer/configuration-chain review, exact trusted configuration contract and recovery qualification. D01/D03–D10 remain unresolved for their own complete contracts/qualification. RFC-0131 stays Draft/unaccepted/unimplemented; issue #396 remains OPEN / not runtime-ready. Existing D03/D10 designs, record packets, catalogue, canonical identifiers/registries, version domains, RFC status, native tooling/workflows and acceptance checklists remain unchanged. Preserve #882/Q6, #851, frozen #777/source0, #733 OPEN, RFC-0128, PSR, consent, steward, hosting and protected scratch holds.

Independent technical review and this publication's own CI/code-owner gate are distinct from formal security acceptance. PR #405 and all earlier merge exceptions are consumed and do not authorize this publication's merge. Refs #396.
