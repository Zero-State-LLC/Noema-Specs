# RFC 0131: Invitation-scoped study preparation access

**Status: Draft — proposed security contract; not accepted or implemented.**

**Date:** 2026-11-13

**Intent:** [invitation-scoped study administration](../intent/2026-11-13-study-admin-surfaces.md)

**Design:** [study administration UI](../specify/study-admin-ui/spec.md)

**Tracking:** [Specs issue396](https://github.com/Zero-State-LLC/Noema-Specs/issues/396)

This document proposes requirements for review. MUST/SHOULD below describe the proposed contract, not present runtime behavior or adoption. Merging this Draft would publish a proposal only. Acceptance is blocked on the machine contracts, durable-adapter qualification, identity integration and recorded security review listed below. No production, resource, invitation, role, enrollment, study, migration or implementation work is authorized here. This is not the separate hosted-research-routes/isolation RFC.

## Problem

The operator needs Admin-invited access to redacted study setup/readiness, scoped to one study/world, with later Admin-interface steward assignment. Existing public Study observation, global Admin admission and Agent Player Controller enrollment do not establish that boundary. Reusing the Admin allowlist would grant the wrong authority. A visible role badge, accepted link or successful email delivery is not a current authorization grant.

The operator explicitly selected read-only redacted setup/readiness and mounted Worker authorization tests plus controlled browser workflows with injected identity/persistence on 2026-11-13 UTC. Those design inputs are settled; credential, storage and lifetime proposals below still need security review. Earlier design prose attributed selection to a bare continuation; the later explicit response, not continuation alone, supplies that confirmation.

## Context

- [CONTEXT](../CONTEXT.md) and [RFC-0120](RFC-0120-agent-only-player-identity.md): HumanPrincipals are not Players. No proposed study credential can mint Controller authority, carry Player mutation scope or write world truth.
- [AUTH-AND-IDENTITY](../docs/AUTH-AND-IDENTITY.md), [SECURITY](../docs/SECURITY.md) and [Admin Live](../docs/ADMIN-LIVE-OPERATIONS.md): authentication, explicit capabilities, world isolation, redaction and research authorization remain distinct.
- [Source notes](../specify/study-admin-ui/SOURCE-NOTES.md): inspected runtime `3267d4267ea3e62be7d6342763065d4b67a0deda` has global Admin bearer verification and public observational Study. No mounted study invitation/grant handler was established by that bounded audit; this is not a claim about every branch or deployment.
- [PSR-2](../docs/PSR-2-STUDY-READINESS-SCENARIO.md), [STUDY](../docs/STUDY.md) and [research ethics](../research/research-ethics.md): designation, explicit duty acceptance, participant consent, research eligibility, operational approval, release authority and hosting remain separate gates.
- [RFC lifecycle](README.md) and `SKILL.RFC` in [SKILLS](../SKILLS.md): a Draft does not override accepted contracts. Acceptance needs machine-readable contracts and validation evidence.

Names of records, claims, actions and version domains in this Draft are **proposed**, not additions to the existing schema or accepted vocabulary. No schema, event catalog, dataset, world, Player protocol or runtime version changes in this publication.

## Proposed change

### 1. Authority and phase-one capability

The proposed initial capability set is closed: `study.setup.read` only. It permits only an explicitly allowlisted redacted setup/readiness projection for an assigned study/world. It does not permit arbitrary metadata, evidence bodies, member contact details, raw audit records, collection, draft edits, invitations, stewardship actions, research, runs, exports, world operations or Player actions. No future capability is inferred from the role name.

Effective permission is the intersection of verified HumanPrincipal identity, a current active study/world grant, the exact action and current projection policy. Missing, expired, withdrawn or unverifiable applicable consent suppresses protected research-derived content and fails closed for any processing or release that requires it. An already-authorized allowlisted prerequisite indicator may say missing or unverified without revealing participant identities, protected content or hidden existence; it is not collection, consent proof or an evidence export. A readiness label never authorizes the activity it describes. The projection must exclude secrets, private cognition, casual private-message bodies, protected contact details and hidden-study existence. A schema-defined allowlist is required before acceptance; there is no generic serialized-record response.

Admin management is a separate boundary. New study-management operations require both existing valid Admin admission and an explicit server-controlled management authorization for the exact world/study and operation. A generic ADMIN label alone is not this new authorization. Configuration cannot be supplied by an untrusted request, wildcard request scope, invitee, ordinary grant or the study record being modified. The initial authority registry, who can configure it and recovery procedure must be specified and reviewed before acceptance. This Draft grants nobody the ability to bootstrap that registry.

Study membership neither creates nor removes independently legitimate Admin authority. A HumanPrincipal who independently qualifies as Admin may exercise that separate path, including later steward designation; no invented two-Admin or mandatory second-person approval rule is added. Read-only study membership itself never permits self-designation or delegation.

### 2. Issuer identity and invitee binding

Invitation creation, reissue, revocation, management-authorization changes and steward designation require an attributable authenticated **account** issuer. Individual attribution means a verified account identity, not proof of a unique natural person. The server derives issuer identity and authentication method from verified credentials; request bodies cannot choose either.

A shared operator credential must not be relabeled as an individual merely because a caller supplied a name or email. Proposed default: deny new study-management writes when only an unattributable shared credential is available. Existing operator operations outside this new contract are unchanged. Any alternative authenticated delegation or recovery mechanism requires an explicit reviewed binding from the shared authority to an attributable account, not an unaudited impersonation parameter.

**Source constraint:** the inspected shared-token mint passes the fixed `op.token` operator identity; older mailbox claims may resolve to `op.legacy`. The mailbox path derives an opaque mailbox hash, not the provider subject or a demonstrated Noema Account link. A fresh session identifier does not improve individual attribution. Require an explicitly verified mapping to the attributable Account for new management writes; do not accept a mailbox-derived operator label as proof of that mapping. See [issuer trace](../specify/study-admin-ui/SOURCE-NOTES.md#issuer-and-persistence-audit-for-the-draft-rfc).

An invitation targets an existing stable HumanPrincipal identifier or a protected verified-contact binding pending account resolution. In the latter case, acceptance must prove the intended contact through the reviewed identity flow, then atomically bind exactly one stable principal. Email possession is not global Admin authority or participant consent. Subsequent changes to contact do not transfer the accepted grant to another account. Contact normalization, reassignment/recovery risks and the provider-to-principal mapping must be specified before acceptance; no new identity provider is selected or provisioned here.

### 3. Logical records and partitioning

The following are logical requirements, not SQL migrations or published JSON schemas. Exact field types, limits, enums and serialization belong in the acceptance packet.

| Proposed record | Required meaning and constraints |
|---|---|
| Study scope | Immutable study identifier, exact world identifier, status and policy version. No implicit default world, wildcard scope, cross-world alias or reassignment in place. |
| Management authorization | Attributable Admin account, exact scope, closed operations, validity, issuer/configuration authority and version. Independent of ordinary study grants. |
| Invitation | Opaque identifier, exact study/world, intended identity binding, fixed read-only capability, attributable issuer, issue/expiry times, state/version and credential digest. Never a raw reusable credential. |
| Grant | Opaque identifier, immutable principal/study/world, originating invitation, closed capability, finite expiry, active/revoked state and monotonically changing authorization version. |
| Audit transition | Bounded operation identity, attributable actor or verified refusal category, exact protected scope, target identifier, prior/new version, time and outcome. No secret credential or protected content body. |
| Steward designation | Study/world, designated principal, designating Admin and pending/accepted/withdrawn responsibility state. Duty acceptance and consent sign-offs remain separate governed records. |

Every record key, query, cache entry, uniqueness rule, pagination cursor, background item and audit lookup must include verified scope. Identical local identifiers in different worlds must not alias. Authenticate and authorize before revealing protected existence or looking up another partition. Caller-supplied world/study values are requests to validate, never authority. No cross-study roster or aggregate is available to the read-only role.

### 4. Invitation and grant transitions

Proposed invitation states: pending, accepted, declined, expired, revoked, superseded. Only pending may accept or decline. Admin revocation of a pending invitation leaves no grant; reissue creates a new invitation and atomically supersedes the old one. Resending the same pending invitation does not extend its validity or widen its capability. Mail delivery status is separate from invitation state and never proves delivery or activation.

Acceptance requires current verified invitee identity, exact immutable scope/capability, unexpired pending invitation, still-valid issuer management authorization and an available authoritative store. Acceptance is a conditional atomic transition: consume the invitation, bind its principal if necessary, create at most one grant and append the transition witness. Failure before commit leaves no access; ambiguous commit is recovered through the operation record, not by blindly creating another grant.

An accepted-invitation retry by the same authorized principal returns the existing result only after checking the grant's current state and scope. It never creates a duplicate or widens authority. If the grant is revoked or expired, the retry reports an inactive result without reactivation. A wrong principal or other-scope request gets a non-enumerating refusal. Revoked, declined, expired or superseded invitations cannot be redeemed.

Grant revocation is independent of the consumed invitation history. All subsequent protected requests and output boundaries must deny the revoked version. Expiry cannot be extended by replay, email resend, stale credentials, browser reload or steward designation. New authority requires a new authorized invitation and explicit acceptance, not resurrection of a terminal record.

### 5. Lifetime and session proposal

All deadlines use an authoritative server clock, explicit UTC instants and fail-closed clock handling. Proposed upper bounds for review are: invitation lifetime 24 hours, active grant lifetime 30 days, study access credential lifetime 15 minutes. Admins may choose shorter bounds, never unbounded values. Grant expiry is explicitly displayed before acceptance; accepting late cannot silently extend it. Any adopted limits must be copied into machine constraints and adversarial boundary fixtures before acceptance. These values are proposals, not operator-adopted settings.

Proposed transport reuses the Worker's bearer-request pattern without reusing Admin scopes: a short-lived, separately typed and audience-bound study access credential held in browser memory, not persistent browser storage. Proposed audience is `noema.study.setup`. Verified claims must bind issuer, stable HumanPrincipal subject, study/world, grant identifier, grant version, issue/expiry and the single capability. No refresh token or cookie-session fallback is implied. Reauthentication must traverse the reviewed identity flow and current grant check; it cannot mint access from an invitation link alone.

A signed credential is only an authenticated claim, not offline permission. Each protected request checks current authoritative grant, scope, version, expiry and policy. Unavailable, stale or ambiguous authorization state denies access; positive authorization cannot rely on an eventually consistent cache. Admin credentials and Player Controller credentials fail the study-access verifier unless a separately authorized conversion flow validates the actual human study grant; no broad token-type coercion is allowed.

### 6. Persistence, concurrency and output fence

A future durable adapter must provide atomic conditional transitions or equivalent transactions, uniqueness of the invitation-to-grant relation, monotonic authorization versions, attributable audit linkage and read-after-write recovery by operation identity. Acceptance/revocation/reissue races must have one verifiable outcome. A client-generated idempotency key is scoped to the authenticated actor, operation and exact request semantics; reuse with different scope/payload is refused without exposing another operation's result.

Preserve the existing [identity/authority split](../docs/AUTH-AND-IDENTITY.md#planned-compatibility): Supabase Auth supplies human identity proof; Noema Account/session/scopes belong to its Postgres control plane; World DO handles live game transitions. This Draft selects no new provider, infrastructure or concrete adapter/migration. New durable access records must honor that ownership; a separately coordinated DO is not a substitute for durable identity/scope authority. Existing DO serialization does not by itself prove durable recoverability; existing Postgres durability does not prove a particular transaction, policy or partition implementation. The adapter's consistency, crash/retry and recovery behavior must be qualified before acceptance. No resource creation, schema installation, provider call or migration is authorized to obtain that evidence by this proposal.

Before returning protected output, recheck effective authorization and complete a defined output fence against revocation. A future adapter/handler must specify the linearization point and demonstrate races, including revocation between lookup and response commitment. Do not claim an unqualified network/transaction gap is solved by a second check. Already delivered information cannot be recalled; stop future delivery and honor governed retention/deletion obligations. Phase one exposes no streaming protected research feed or downloadable dataset.

### 7. Proposed interface boundary

Concrete endpoint paths are deliberately not reserved by this Draft. The acceptance packet must define route/method, authentication class, request/response schema, bounded error contract, idempotency behavior and rate limits for these operations:

| Operation | Required authority | Effect |
|---|---|---|
| Read assigned setup/readiness | Current study access grant and projection policy | Allowlisted redacted projection only |
| Create/reissue/revoke invitation | Attributable Admin plus exact management authorization | Conditional scoped invitation transition |
| Accept/decline invitation | Verified intended HumanPrincipal plus valid pending invitation | Conditional consume; at most one read-only grant |
| Revoke grant | Attributable Admin plus exact management authorization | Authoritative version/state transition |
| Designate later steward | Attributable Admin plus exact management authorization | Pending designation only; no duty acceptance on their behalf |
| Read management audit | Separately authorized attributable Admin | Bounded protected audit projection; never an ordinary study capability |

No generic study-role configuration-write, invite-delegation, run, collect or export operation exists in the phase-one proposal. Admin configuration writes must be separately enumerated and constrained, not a generic object patch.

### 8. Browser, delivery and abuse controls

Use HTTPS, same-origin API policy, explicit allowed origins and least-privileged credential audiences. Do not accept a bearer in a query string or authorize state-changing GET requests. No cookie authentication is proposed; introducing it requires an explicit CSRF, SameSite, Secure/HttpOnly, origin and redirect design, not a silent fallback. Browser storage choice is not an XSS defense: require an appropriate CSP, safe text rendering, dependency review and no untrusted HTML interpolation.

Invitation credentials must be cryptographically unpredictable, stored only as a verified digest at rest and redacted from logs, audit prose, analytics, error pages and lists. Delivery/redeem design must define referrer suppression, landing-page URL cleanup, redirect allowlists, mail-scanner prefetch safety and explicit human confirmation before consumption. No third-party asset or analytics request may receive invitation material. A mail-provider acknowledgment is not recipient receipt. Delivery failure leaves a truthful pending/failed-delivery state, not an active grant.

Rate limits must bound unauthenticated identity challenges, redemption attempts, invitation sends, reissues and management writes by appropriate principal/scope/client signals. Uniform unauthenticated and wrong-scope responses must not disclose contact membership, study existence, counts or hidden failure reasons. Exact limits and response/timing policy remain acceptance prerequisites, not runtime-defined defaults. Audit recording must also be bounded and resistant to unauthenticated log amplification.

### 9. Stewardship, consent and hosting

An unassigned steward is a valid preparation state. Admin can designate a steward later; invitation acceptance, designation and explicit duty acceptance must be displayed separately. No UI click signs participant consent or accepts duties for someone else. Existing consent/opt-in sign-offs and Danny human-yes are unchanged.

Read-only readiness may show only authorized redacted prerequisite status, never manufacture evidence, erase exclusions, promote PSR gates or open blocked operations. Capture, retention, analysis, publication and export remain independently consent-checked and most-restrictive-policy governed. Hosted NOTICE/TEST/COMPARE/CAPTURE and data release are not authorized by this preparatory metadata contract; the separate hosting/isolation RFC and PSR prerequisites remain required.

## Alternatives

- **Add invitees to the Admin allowlist:** rejected; creates global authority rather than a study grant.
- **Treat a generic STUDY role, Controller enrollment or forwarded link as membership:** rejected; wrong identity/scope and no current grant.
- **Grant draft edits or onward invitations in phase one:** rejected for this design by the explicit read-only choice; any later expansion needs its own reviewed capability contract.
- **Attribute shared bearer calls to a client-supplied person:** rejected; unverified impersonation, not issuer accountability.
- **Trust self-contained study credentials until expiry:** rejected; stale credentials bypass revocation.
- **Choose a new provider/store to finish this Draft:** deferred; no resource authority or qualified adapter evidence. Logical obligations must not pretend infrastructure was created.
- **Cookie-only session:** not selected; would require an explicit browser/CSRF contract. Existing Admin login behavior is not changed.

## Compatibility

Existing public observational `/study`, Admin login/operations and Agent Player admission remain unchanged. No automatic backfill from Admin allowlists, generic roles, existing research contacts, Controller enrollment or steward names. Default deployment state remains no new study grants and no new route enablement.

Proposed control-plane version domain is `study-access/0.1`, separate from world rules, event catalog, Agent Protocol, dataset and replay versions. It is not registered or negotiated by this publication. Acceptance must specify schema identifiers, strict unknown-field handling and version negotiation/refusal; incompatible claims, scopes or versions fail closed. Do not retag existing tokens or mutate historical world records.

## Data impact

Potential new protected control-plane data includes principal bindings, invitation digests, grants, authorization versions, management authorization and minimal transition audit. It is not canonical world state, research observations, participant consent or a Player action ledger. No data is created by this Draft beyond its text.

Before acceptance, define data classification, encryption/access policy, per-record retention/deletion and backup recovery. Credential-bearing pending material must not remain redeemable in backup restore. Recovery must preserve terminal/revoked state and uniqueness; if freshness cannot be established, deny rather than restore authority. Audit retention is not permission to retain secret credentials or private evidence bodies. No arbitrary retention duration is adopted here.

## Research impact

No study is run, no observation becomes eligible, no consent changes and no claim label, exclusion, metric, floor, reproducibility bundle or release changes. Control-plane audit is not automatically research evidence. If later cited, preserve its scope, provenance and eligibility under the existing research contracts. PSR-1, named/accepting steward, signed consent basis and separate hosted STUDY gates remain unchanged.

## Security impact

Threat model includes forged/wrong-audience credentials, human-to-Player escalation, shared-issuer ambiguity, invitation forwarding, contact takeover, enumeration, replay, stale authorization, cross-world identifiers, cache/cursor confusion, unsafe redirects, mail scanning, XSS, log leakage, transactional ambiguity and revocation/output races. Proposed mitigations are explicit above; none is claimed implemented or qualified.

An accountable security reviewer must verify the issuer chain, authority-registry bootstrap, identity recovery, closed projection, durable adapter, concurrency fence, browser flow and abuse bounds before acceptance. A generic docs approval, CI success or admin review bypass does not supply that security decision.

## Migration

This publication has no migration. After an accepted contract and separately authorized implementation work order: add inert adapters and machine contracts, qualify isolated mounted tests, then controlled browser workflows; verify no new grants/routes enabled by default. Any actual schema/data migration, provider change, deployment, production test or real invitation requires its own applicable permission and rollback evidence. Existing Admin authority is neither silently broadened nor removed.

## Validation

These are required future cases, not tests executed by this document:

| Case | Required externally visible outcome |
|---|---|
| SA-01 | Anonymous, ordinary WATCH, generic STUDY, Admin-only or Controller credential cannot access a protected study projection without the required grant. |
| SA-02 | Correct principal sees only the allowlisted redacted setup/readiness for the assigned study/world; private content and roster/contact/audit data are absent. |
| SA-03 | Identical local identifiers in another study/world do not collide or disclose existence through data, count, cursor, error or timing contract. |
| SA-04 | Wrong identity, forwarded, expired, declined, revoked and superseded invitation produces no active grant. |
| SA-05 | Duplicate acceptance creates at most one grant; later replay cannot widen capability, extend validity or reactivate a revoked grant. |
| SA-06 | Issuer authority revoked before acceptance denies it; unattributable shared-bearer writes cannot masquerade as a named account. |
| SA-07 | Accept/reissue/revoke concurrency, crash and ambiguous commit recover one authoritative result without duplicate grant or unlinked success audit. |
| SA-08 | Revocation after lookup, stale credential/version/cache and queued-output races are denied at the qualified output fence; unavailable store fails closed. |
| SA-09 | Exact expiry boundaries, clock failure and mismatched credential audience/type/version are refused without fallback. |
| SA-10 | Read-only principal cannot edit drafts, invite, self-designate, accept another's duties, run, export, mutate world or gain Admin. Independently held Admin authority still uses its separate gate. |
| SA-11 | Later designation remains pending until explicit duty acceptance; readiness does not satisfy consent or PSR/hosting gates. |
| SA-12 | Missing/withdrawn/contradictory applicable consent and policy changes suppress protected projection/output rather than cache stale eligibility. |
| SA-13 | Delivery failure, repeated send, scanner GET, redirect and referrer/browser-history paths do not activate authority or disclose credentials. |
| SA-14 | Wrong-scope refusal, rate limits, bounded audit and sanitized logs avoid enumeration, secret leakage and unbounded amplification. |
| SA-15 | Keyboard/accessibility, expired/revoked sessions, reload/re-authentication and duplicate submissions show truthful state without a route around the server gate. |
| SA-16 | Backup restore and rollback preserve revocation/terminal states; no implicit Admin/contact/enrollment backfill grants access. |

Use the explicitly confirmed mounted Worker request/auth seam with injected identity and durable-adapter dependencies, then controlled real-browser workflows against that boundary. Existing [test seams](../specify/study-admin-ui/SOURCE-NOTES.md#testing-seams--discovered-not-executed) guide the harness; helper/HTML tests are supplemental. No live provider or production service is required or authorized by the test proposal. Backend-specific isolated qualification needs its own applicable scope.

### Acceptance blockers and next work

1. Machine-readable identity, management authorization, invitation/grant/session and redacted projection contracts, exact strict bounds/enums/error/idempotency semantics, version registration and linked positive/negative fixtures. No new schema is installed by this Draft.
2. Attributable identity-provider integration and account/contact-recovery binding, plus explicit registry configuration/bootstrap authority and issuer-chain review. A shared token alone is insufficient.
3. Durable adapter selection and isolated evidence of atomicity, recovery, revocation/output linearization and backup freshness; resource permissions remain separate.
4. Reviewed lifetime values, retention, rate/response/timing limits, delivery method and browser/redirect security. Proposed values are not adopted defaults.
5. Recorded compatibility, data, research, security, migration, validation and rollback reviews; eligible code-owner review and required current-head checks for publication are separate from formal contract acceptance.

Keep this RFC Draft until those obligations have evidence. Do not mark the runtime feature ready or add acceptance checkmarks based on text validation.

## Rollback

This Draft changes no live state. A future implementation must support disabling the new study-access surface without altering public Study, existing Admin authority, Player operation or world history. Disable issuance/admission, invalidate affected study credentials and deny grants; preserve attributable audit and terminal states. Do not erase revocation history, reactivate records through restore or recall already delivered information. Any data deletion, schema reversal or production rollback requires its own authorized procedure and evidence.
