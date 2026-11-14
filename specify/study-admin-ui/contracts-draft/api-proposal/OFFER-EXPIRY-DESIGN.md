# D10 — offered grant deadline (Draft design)

**Status: A selected for the Draft proposal only; unaccepted, unregistered and unimplemented.**

The operator's later “continue as recommended” selected the previously recommended representation A: a fixed, server-owned offered grant deadline on the invitation. The earlier confirmation form was unanswered; this selection is not attributed to that timeout, the earlier bare continuation or the PR401 merge exception. It selects a proposal representation, not lifetime values, wire field adoption, RFC acceptance, implementation or live access authority. The [operation catalogue](operations.json) correctly retains D10 as UNRESOLVED until the complete contract and qualification gates are satisfied.

## Problem Statement

An invitee must know when offered access ends before accepting. Acceptance later in time must not silently produce a later access deadline. The [owning Draft RFC](../../../../rfcs/RFC-0131-study-access-control-plane.md), sections 4–6, requires explicit pre-acceptance grant expiry, non-extending replay and qualified authoritative transitions; none is implemented by this note.

At source baseline `4f57011e910c3f24727d3f8ba8aea4c1ad470eb1`, the [record-shape packet](../README.md) has an `Invitation.expires_at` redemption deadline and a `Grant.expires_at` access deadline, but no invitation field binding the offered grant deadline. Exact [schema](../records.schema.json) locations are `/$defs/Invitation/properties` and `/$defs/Grant/properties/expires_at`. The existing create/accept capsules explicitly leave that binding incomplete. This is a missing proposed producer→record→consumer contract, not an observed runtime bypass.

## Solution

Propose carrying one immutable absolute offered access deadline on the server-owned invitation. A candidate name is `offered_grant_expires_at`; it is not an existing, accepted or registered field. Fix it when issuing that offer after the required authority and finite-policy checks. The initial grant preserves this offered deadline instead of starting a fresh full lifetime when acceptance happens.

Keep invitation redemption expiry and offered access expiry distinct. If the invitation is still redeemable but the offered access deadline has passed, acceptance must not create active access. This proposal introduces no ordering requirement between the two deadlines, numerical lifetime, equality-boundary rule or error/status code. Those require their existing policy/clock/wire review.

## User Stories

1. As an invitee, I want to see both redemption and offered access deadlines after identity verification so that I can distinguish when I may accept from when access ends.
2. As an invitee, I want the first grant to preserve the deadline I was shown so that accepting later does not silently change the offer.
3. As an attributable Admin with exact management authorization, I want the server to issue only a policy-qualified finite offer so that an invalid configuration cannot create unlimited access.
4. As an access reviewer, I want acceptance to validate the authoritative offer, intended identity, exact scope, capability and current issuer authority together so that display copy or client fields cannot manufacture permission.
5. As an invitee retrying after an interrupted request, I want the existing authoritative outcome so that retries cannot create another grant or extend access.
6. As an Admin handling reissue, I want duplicate recovery of the same operation to reuse its one result so that replay does not rotate credentials or recalculate deadlines again.
7. As an auditor, I want the qualified operation witness linked to the consumed invitation and resulting grant so that an apparent success cannot hide a different deadline or ambiguous commit.
8. As a research operator, I want access expiry to remain separate from consent, stewardship and study-run authorization so that a valid grant does not imply research readiness.

## Implementation Decisions — proposal boundaries

### Representation and authority

A is the selected Draft representation; a second offer entity is not proposed in this bounded follow-up. The candidate deadline is server-owned offer data, not an authoritative client input. A request expressing a shorter preference would need its own bounded DTO and policy review; ordinary acceptance cannot set the grant deadline.

Existing valid Admin admission, an attributable authenticated Account and current server-controlled exact study/world/operation management authorization remain necessary for issuance/reissue. An ordinary study-role grant, shared operator label, mailbox-derived identity, client-selected issuer or plain link possession supplies none of that authority. Independently held legitimate Admin authority remains separate; no second-Admin rule is added.

### Producer, record and consumer binding

| Stage | Proposed binding obligation | Still unqualified |
|---|---|---|
| Issuance | Validate management authority and finite policy, then persist the invitation's fixed offered deadline with the intended identity, exact scope/capability and authoritative offer/version context. | Account/registry binding, configured values, timestamp encoding and durable creation. |
| Identity-verified display | Obtain the authorized authoritative offer and show redemption and offered access deadlines distinctly; do not disclose protected invitation/study details before the required identity and disclosure checks. | Exact display/read contract, privacy/error policy and browser workflow. |
| Acceptance | Validate the authoritative pending offer and current identity/scope/issuer/policy/deadlines at the qualified transition. The initial grant deadline equals that offer's deadline. | Compare/version carrier, transaction API, clock/equality boundaries and durable acknowledgement. |
| Retry and recovery | Reconcile the existing operation with current grant/state/scope; preserve its deadline and inactive outcomes without another grant or resurrection. | Idempotency representation/retention, recovery and backup freshness. |
| Reissue | Atomically supersede the prior invitation; duplicate recovery of the same reissue operation returns its one new invitation/result without recalculating again. | Whether a genuinely new authorized reissue may propose changed terms; no automatic extension is selected. |
| Protected output | Enforce current authoritative grant/policy and the separately qualified revocation/output fence; an offered deadline or signed claim alone is not permission. | Actual adapter/handler linearization and delivery races. |

The binding is semantic and server-validated; metadata equality, an opaque reference, an unverified version field or a second lookup alone proves none of it. Exact request carriers and offer-bearing stale-version handling remain D03/D05 decisions, not a new mandatory HTTP field. A policy/issuer/clock problem must deny rather than silently substitute another offer; this note authorizes no policy changes.

### Lifecycle and privacy preservation

Resend of the same invitation, browser refresh, duplicate acceptance and operation replay do not extend validity. A retry after revocation or expiry reports the current inactive result without reactivation. Reissue remains distinct from resend, and invitation revocation remains distinct from grant revocation. Decline never creates a grant; only an otherwise valid pending invitation may transition. No invalid decline gains a state change through this note.

Return only separately reviewed, authorized projections, never a raw invitation/grant record, reusable credential, digest or protected content. Schema-valid strings and references are not privacy proof. Ordinary setup access does not gain invitation, audit, configuration, export or global Admin powers. Steward designation, scope-qualified eligibility, personal duty acceptance, consent and hosting/research gates remain independent and unmodified.

## Testing Decisions — future qualification, not executed

Use the already-confirmed mounted Worker request/authorization boundary with injected identity and persistence, then controlled browser workflows. That seam is retained, not newly approved or replaced by static document checks. The following are candidate observations, not passing tests, complete SA acceptance or evidence of a working API.

| Candidate | Required observation |
|---|---|
| OF-01 | Issue, display and accept at different server times; the initial grant retains the offered deadline rather than shifting to acceptance time. |
| OF-02 | Redemption remains pending but offered access expiry has passed; no active grant is created or reported. Exact equality/status rules still need review. |
| OF-03 | Wrong identity/scope and client-altered deadline/display cannot change the offer, create access or reveal a protected target. |
| OF-04 | Same-operation replay/resend creates no duplicate or later deadline; revoked/expired grants remain inactive. |
| OF-05 | Policy/issuer/offer-version changes between display and commit fail closed without an unreviewed replacement offer or success before durable acknowledgement. |
| OF-06 | Reissue/race/crash/backup recovery preserve one authoritative offer/result and terminal/revoked history. |

Future schema fixtures may check proposed representation only. They must not claim cross-record equality, trusted clock, verified identity, atomicity, replay, recovery or output fencing from JSON Schema. The existing 56 record expectations and eight checker CLI tests do not validate this new field or these future cases. Native CI validates specification tooling/links, not this design's behavioral truth.

## Alternatives

A separate immutable offer record could carry the same terms and bind invitation/acceptance to it. It adds record/reference, lookup/version/linkage, privacy and transaction/recovery obligations not demanded by the inspected source. It is not selected for this Draft follow-up. A future concrete offer-versioning requirement may justify reviewing it separately.

Recomputing a fresh full lifetime only at acceptance without a bound pre-acceptance offer is incompatible with the proposed no-silent-extension requirement. A calculation may inform issuance, but its resulting offered deadline must already be fixed and bound before acceptance.

## Out of Scope

No change to existing record schemas, examples/case roster, operation catalogue, canonical identifiers/registries, RFC status, lifetime values, wire contracts, native validators, workflows or acceptance checklists. No clock implementation, provider, persistence adapter, transaction mechanism, credential carrier, encryption/signature scheme, route or error code is selected. The existing draft timestamp format and proposed RFC upper bounds are not adopted here.

No live invitation/account/role/auth/resource/data/migration/deployment/enrollment/research/export/hosting action, coding partner assignment or named steward. Preserve #882 hold, #851 draft, #777 frozen/source0, #733 OPEN, RFC-0128 unchecked acceptance and Q6/PSR/consent/steward/hosting gates.

## Further Notes — remaining gates

All D01–D10 remain unresolved at the acceptance/qualification level. The operator selected A for Draft preparation only. Separately scope actual machine schemas, field/version registration, clock/policy/expiry boundaries, identity/bootstrap and durable/output-fence qualification before implementation or acceptance. Issue #396 stays OPEN/not runtime-ready; RFC-0131 stays Draft, unaccepted and unimplemented.

This is a design/RFC-preparation continuation, not a new accepted RFC or implemented endpoint. Independent technical review and current-head CI for any publication are separate from formal security review and RFC adoption. All prior PR-specific merge exceptions, including #401, are consumed; none applies to a new PR. Refs #396.
