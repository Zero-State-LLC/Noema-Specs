# Study administration UI — invitation-scoped access

**Status: proposed design for review.** The operator selected the recommended read-only study-role baseline and mounted-request plus controlled-browser test seams by directing continuation after those recommendations. This records the design to review, not an Accepted RFC, existing API/schema, implemented UI, deployment, invitation or study-run authority. New identity, role, persistence and security contracts require the applicable RFC/security process before implementation. Requirements below describe the proposed future feature; they do not amend current protocols or authorize acceptance promotion.

**Intent:** [Invitation-scoped study administration](../../intent/2026-11-13-study-admin-surfaces.md)  
**Source baseline:** runtime `3267d4267ea3e62be7d6342763065d4b67a0deda`; Specs `d84264c7f416989fe4148bcbbbe294dacda2dce9`.  
**Evidence:** [source notes](SOURCE-NOTES.md) · [proposed security-RFC scope](SECURITY-RFC-OUTLINE.md).

## Problem Statement

An Admin needs preparatory study-management surfaces and a way to assign a research-and-ethics steward later. Invited study users need access to their assigned study, not unrestricted Admin access. Setup must be possible without prematurely starting research, satisfying consent by implication, promoting a readiness gate or opening hosted STUDY.

The user's settled requirements are:

1. A steward may be assigned later by an Admin through the interface; no nominee is required during this design interview.
2. The study role must be properly scoped and gated by an Admin-issued invitation.
3. Existing research, hosting, consent, enrollment and acceptance gates remain distinct. Specifying UI implementation is not permission to execute them.

## Solution

Provide a control-plane study workspace with separate experiences for an existing Admin, an invited study user, and a designated steward. Admins initiate and revoke invitations and configure study-scoped grants. Invitees authenticate as the intended identity and explicitly accept before any grant becomes active. Server authorization enforces study scope and capability on every request; navigation hiding is not security.

A study-access grant, a steward designation, acceptance of steward responsibilities, participant consent, Controller enrollment, study-run authority and data-release authorization are separate records or decisions. None implies another.

Preparatory UI can show Draft or Blocked states. It must not expose operative research/export/run actions until their separate contractual and authorization gates are fulfilled.

## User Stories

1. As an Admin, I want a study setup overview so that I can distinguish preparatory configuration from authorized research activity.
2. As an Admin, I want each invitation bound to one explicit study scope so that access cannot silently extend to other studies or worlds.
3. As an Admin, I want to invite a specific authenticated identity so that possession of a forwarded link alone does not grant access.
4. As an Admin, I want a capability summary before issuing an invitation so that I can see exactly what access I am granting.
5. As an Admin, I want pending invitations listed with status and expiry so that I can manage unfinished onboarding without exposing invitation secrets.
6. As an Admin, I want to revoke a pending invitation so that it can no longer be accepted.
7. As an Admin, I want reissuing an invitation to invalidate the old credential so that two usable links cannot remain active accidentally.
8. As an Admin, I want to revoke an active membership so that future protected requests stop being authorized.
9. As an Admin, I want steward assignment to be optional during setup so that absence of a nominee does not prevent planning.
10. As an Admin, I want to designate an invited, explicitly scoped steward so that naming a role does not create a global administrator.
11. As an invitee, I want to see the inviter, intended study and proposed capabilities after identity verification so that acceptance is informed.
12. As an invitee, I want to decline without receiving access so that an invitation is not treated as enrollment or consent.
13. As an invited study user, I want to view only authorized study metadata and redacted readiness summaries so that I do not gain unrelated data access.
14. As an invited study user, I want precise reasons why work is blocked so that I do not mistake an unfinished prerequisite for a broken interface.
15. As an invited study user, I want valid empty, loading, unavailable, unauthorized and revoked states so that stale UI does not imply continuing permission.
16. As a designated steward, I want to review and explicitly accept my responsibilities so that an Admin's nomination is not mistaken for my acceptance.
17. As a designated steward, I want the consent, eligibility, retention and release responsibilities to be visible without automatically enabling release so that duties and permissions remain distinct.
18. As a research operator, I want participant consent and Controller enrollment shown as independently evidenced states so that accepting a UI invitation does not satisfy either.
19. As an accountable owner, I want required study gates and promotion authority preserved so that setup cannot bypass PSR prerequisites or human sign-off.
20. As an auditor, I want attributable invitation, acceptance, grant-change and revocation events without raw tokens or prohibited private data so that access changes are reviewable.
21. As a keyboard or assistive-technology user, I want accessible forms, dialogs, error summaries and focus recovery so that invitation and membership management do not require pointer-only operation.
22. As an Admin, I want duplicate submissions and stale edits handled safely so that races cannot create duplicate grants or undo revocation.

## Terminology and Boundaries

These are proposed UI distinctions, not assertions that new canonical entities or wire fields already exist:

- **Admin:** an existing authorized control-plane administrator, not a Player and not merely someone who can view a study.
- **Study scope:** the one logical study/campaign workspace and verified world partition authorized by a grant. A new canonical Study or membership entity is not assumed to exist: the inspected canonical entity inventory does not establish either. Define the mapping and persistence through the required RFC. An identifier alone is never authorization. World identity, study identity and research-run identity are not interchangeable; cross-world aggregation is not part of this feature.
- **Study-role grant:** an accepted, active, explicit binding between an authenticated identity, a study scope and a permitted capability set. No wildcard scope is implied.
- **Invitation:** an Admin-issued, identity-bound, expiring offer of a scoped grant. It is not an active grant.
- **Steward designation:** the named responsibility assignment for consent/opt-in, eligibility, retention and release sign-off. It neither grants global Admin nor records the designated person's acceptance automatically.
- **Steward acceptance:** explicit acceptance of the assigned responsibilities. It is separate from ordinary invitation acceptance and does not by itself authorize a study window or data release.

Do not add technical workflow rules to a glossary. Reconcile any new term against the canonical glossary before publication.

## Current Source Baseline

The pinned Worker serves an observational public Study page, not authenticated study administration. Its Admin pages load HTML before API authorization; the actual Admin API boundary verifies an Admin bearer type, ADMIN role and Admin scope. The present console uses bearer/sessionStorage, not a demonstrated Admin cookie session. None of those mechanics supplies a per-study membership or invitation contract.

The existing human `researcher` label is not a per-study grant. Existing Controller enrollment issues Player Controller authority and is not a researcher invitation path. The new feature must not append study invitees to the Admin mailbox allowlist, reuse Controller issuance, or interpret a public Study page as an authenticated workspace.

Source-supported facts and exact test seams are recorded in `SOURCE-NOTES.md`, with pinned primary citations. These are source observations at the pinned commits, not production probes or executed tests.

## Workflows

### Delivery workflow and accountable review

- Use the existing `grill-with-docs`, `to-spec` and `code-review` flows for operator alignment, reviewable design publication and independent standards/spec checks.
- Apply repository `SKILL.ORIENT`, `SKILL.RFC`, `SKILL.SPEC_CHANGE` and `SKILL.VALIDATE` as applicable; these process names confer no implementation authority.
- Owner specialist: the existing NOEMA identity/security and STUDY contract maintainers; Danny retains the existing criteria/human-yes role. No research-and-ethics nominee is invented.
- Reuse the existing CI workflow for native validation and committed graph freshness. No workflow, bot, new RFC number or gate is invented.

### Proposed feature workflows

1. **Prepare:** an existing authorized Admin configures draft study scope metadata. An unassigned steward is valid; this does not start a window or enable hosted research. Study/world identifiers are established server-side, not accepted as authority from a form.
2. **Invite:** the Admin selects one study/world scope, identity and explicit baseline capability set, reviews the exclusions and finite expiry, then issues the invitation. Persisted invitation state and transport delivery status are reported separately. Sending a link activates no grant.
3. **Accept or decline:** the invitee completes suitable identity verification, sees the scope/capabilities and accepts or declines. The server atomically checks intended identity, current inviter authority, scope, expiry, revocation and one-use state. Acceptance creates one restricted grant; all invalid cases create none.
4. **Use the workspace:** each protected request rechecks current grant, study/world scope, action and relevant data policy. Study users see only their permitted setup/readiness view. A generic researcher label, Controller token or UI link does not supply this authority.
5. **Assign stewardship later:** the Admin designates an appropriately invited identity. Role designation, ordinary invitation acceptance, acceptance of stewardship duties and consent/opt-in sign-off remain separate. Steward-dependent research remains blocked while its prerequisites are incomplete.
6. **Revoke or change access:** the Admin explicitly revokes the grant or proposes a replacement. The next protected read/write is denied after revocation; queued or long-running work must recheck before accessing protected material or producing a protected destination. No silent upgrade or stale-form reactivation.
7. **Handle failures:** the UI distinguishes authorization failure, stale version, expired invitation, unknown delivery and unavailable dependency without leaking another study or claiming an ambiguous write succeeded. The operator reads back the exact affected object before retrying a potentially completed change.

## UI Surfaces

### 1. Admin study overview

Show accessible study scopes, setup/readiness state, unresolved prerequisite summaries and membership/invitation counts. An empty or unassigned steward state is valid. Do not present “Ready”, “Complete”, “Run authorized” or “Hosted enabled” solely because a study exists or members accepted invitations.

### 2. Study workspace

Use a persistent study-scope label and capability-aware navigation. Initial sections are Overview, Access & invitations, Steward & responsibilities, and Readiness evidence. Show only fields authorized for the viewer. Do not expose participant private data, research raw payloads or exports merely to populate a dashboard.

The selected design baseline grants metadata/readiness inspection only. Editing study configuration, collecting evidence, starting runs or releasing data requires separately explicit capabilities and governing approval. No such elevated default is assumed.

### 3. Invite dialog

An Admin selects the existing study scope, verified invitee identity and the least permitted capability set. Show a plain-language access summary, expiry and explicit exclusions before confirmation. The server derives the issuer and authority from the authenticated session; the client cannot choose an issuer or grant capabilities the issuer lacks.

No public sign-up, self-issued invitation by a non-Admin, wildcard study access or global-role upgrade. Only an independently authorized Admin may issue a grant; a study user cannot manufacture that authority. Preserve existing legitimate Admin powers, including any independently permitted deliberate self-designation, rather than inventing a two-Admin requirement. Do not add study invitees to the global Admin mailbox allowlist to make sign-in work.

### 4. Invitation acceptance

Before identity verification, expose no sensitive study, member or consent details. After verification, display the scope, capabilities, issuer and expiry, with Accept and Decline actions. Reject mismatched identity, consumed, expired or revoked invitations without granting membership. An authentication round-trip must not drop the intended scope or permit an unvalidated redirect.

Invitation credentials are secrets: keep them out of analytics, logs, public URLs copied into evidence, referrers and unrelated requests. Use existing secure transport/session patterns only where their actual authorization semantics are appropriate.

### 5. Access management

Show pending invitations and active/revoked grants as distinct objects. Allow authorized Admins to revoke access and view a redacted audit trail. Avoid client-side optimistic success for access changes: confirm persisted server state before showing completion. Conflicts and ambiguous failures require readback, not blind reissue.

### 6. Steward setup

Display Unassigned as a legitimate preparatory state. Later, an Admin can invite or select an appropriately scoped identity and designate the role. Display Assigned / acceptance pending separately from Accepted. Show the responsibilities and the applicable gate impact. No default steward and no assumption that Bob, Prabu, an Admin or a study user accepted the role by participating elsewhere.

### 7. Readiness and evidence

Show criterion-level evidence references and unmet prerequisites without upgrading canonical states. Distinguish operator-entered assertions, verified evidence and accountable-owner disposition. Missing prerequisites disable dependent operations server-side; a tooltip or disabled button alone is insufficient. Hosting, export and run actions remain unavailable unless separately specified and authorized.

## Implementation Decisions

### Authority and role model

- Separate authentication from authorization. Reuse a proven identity-verification primitive if compatible, not an existing global-Admin authorization shortcut.
- Use the canonical HumanPrincipal/control-plane identity boundary for invited study access; a human `researcher` label alone is insufficient. Controller tokens cannot be converted into study access or vice versa. New claims, session type, scope and persistence are proposed contracts requiring RFC/security review, not fields already present in the current Admin principal.
- Preserve the existing Admin bearer flow. Do not describe cookie sessions as already supported. Prefer its established explicit bearer-request pattern for the initial proposed study-specific session where security review finds it suitable, but issue no global Admin token to a study invitee. A cookie alternative would be a separately specified security design with HttpOnly/Secure/SameSite, CSRF and redirect tests, not a cosmetic UI change.
- Existing Admin routes retain their existing Admin-only gate. A study-role session or invitation must not satisfy that gate.
- The server checks active grant, exact study scope, capability, resource ownership and applicable research prerequisites for every protected read and write, including direct API requests, downloads and background operations.
- Do not trust client-provided role labels, study identifiers, hidden fields, navigation state or cached capability lists.
- Partition reads, writes, caches, queued work and object references by the verified world as well as study. Identical identifiers in two worlds must not collide or disclose content/existence across the boundary.
- An Admin may administer invitations without automatically gaining access to all research data. Data entitlement and any release authority must be evaluated separately.
- Invitation issuance, scoped membership and steward responsibility acceptance must not confer Player identity, Controller enrollment, participant consent, PSR acceptance or permission to deploy.
- Any new identity, role, persistence, hosting, export or security-boundary contract requires the applicable intent/RFC review before implementation. This draft proposes requirements, not a silent schema amendment.

### Invitation and membership lifecycle

- Invitations can be Pending, Accepted, Declined, Expired or Revoked. The server, not the browser clock, determines expiry and validity.
- Only a valid Pending invitation can be accepted, by its intended authenticated identity. Successful acceptance consumes the invitation atomically and creates at most one active matching grant.
- Repeated acceptance cannot duplicate membership or widen permissions. Define idempotent acknowledgement for the same completed acceptance; consumed credentials never issue a second grant. If the resulting grant has since been revoked, return truthful inactive/revoked status rather than claiming current access or reactivating it.
- Reissue invalidates the old credential before the new one becomes usable. Never show a failed or ambiguous send as a confirmed invitation delivery.
- Invitation acceptance history remains distinct from membership state. Revoking membership does not rewrite history to pretend the invitation was never accepted.
- Concurrent acceptance, expiry, role change and revocation must resolve through authoritative versioned or transactional state. Revocation wins over a stale client write attempting to reactivate access.
- Revocation invalidates future protected requests and stale sessions/grants as required by the server boundary. Clear unauthorized local views on the next authoritative denial; do not claim downloaded data can be recalled or knowledge erased.
- Invitation lifetime, transport, resend limits and exact error vocabulary remain review decisions until checked against existing contracts. No arbitrary numeric security policy is silently adopted here.
- The accepted security contract must supply finite server-enforced lifetimes. Missing, invalid or unbounded lifetime configuration must not issue an invitation with unlimited validity. Session and queued-work authorization cannot outlive the effective grant or its revocation.

### Scope and data handling

- Default deny; one explicit study scope per grant. Access to one study cannot enumerate another study's membership, readiness, evidence or private identifiers.
- Prefer generic unauthorized/not-found behavior where appropriate, but test full responses and success/refusal differences before claiming existence privacy.
- Dashboard summaries use the minimum redacted data required for the viewer's capability. Keep private prompts, proprietary architecture, provider credentials and private agent metadata excluded.
- Consent withdrawal, eligibility exclusions, retention and release restrictions remain effective independently of UI access. An Admin invitation is not research consent.
- Capture, retention, analysis, publication and export each retain their independent authorization. Effective policy is the most restrictive applicable participant/agent consent, study policy, world policy, visibility, retention, licensing and operator controls. Recheck before processing or creating a protected destination; missing, withdrawn, expired, contradictory or unverifiable consent fails closed. Preserve lineage and exclusions. Revocation starts the existing configured deletion/tombstone process; do not silently discard exclusions or claim UI de-identification removes those obligations.
- This feature supplies no research export button or new export authority. Any later export must satisfy explicit dataset opt-in, allowlisted paths and required signed scope-bound research receipts; a missing/invalid receipt is refusal, not an unsigned downgrade.
- Audit access changes with attributable actor, target scope, action, outcome and bounded timestamps; never persist raw invitation credentials in audit records.

### Accessibility and failure behavior

- Provide explicit labels, keyboard navigation, validation summaries, announced status changes, focus containment/restoration for dialogs and responsive layouts.
- Test real applicable browsers/assistive technologies under the existing platform contract. DOM or emulation checks do not constitute physical-device or human-study evidence.
- Server refusal must leave roles, invitations and research state unchanged except for an explicitly defined audit event. A display error must not trigger a retry that grants broader access.

## Proposed Capability Matrix

| Action | Existing Admin | Invited study role | Designated steward |
|---|---|---|---|
| Issue/revoke an invitation | Allowed within existing Admin authority and target study | Denied | Denied unless independently an authorized Admin |
| Grant global Admin | Not part of this feature | Denied | Denied |
| View scoped redacted setup/readiness | Explicit authorized scope/capability required | Active matching grant required | Active matching grant required |
| View another study | Separate authorization required | Denied without separate grant | Denied without separate grant |
| Change study configuration | Separate explicit capability | Not granted by baseline role | Not granted by designation alone |
| Designate a steward | Authorized Admin | Denied | Designation alone supplies no Admin authority |
| Accept steward duties | Cannot accept on another identity's behalf | Only if personally designated | Explicit personal acceptance required |
| Mark participant consent or enrollment satisfied | Not implied by Admin/invitation | Denied by baseline role | Not implied by acceptance |
| Start research, promote gates or enable hosting | Separate contractual authority; not part of this feature | Denied by baseline role | Denied by designation alone |
| Release/export research data | Separate consent/eligibility/release authorization | Denied by baseline role | Sign-off duty is not an automatic export capability |

This is the selected conservative design baseline for review, not a verified current permission model or enacted security contract.

## Testing Decisions

Use the mounted exported Worker `fetch(Request, Env)` boundary as the primary authorization/lifecycle test seam, with injected identity-provider and persistence dependencies. Exercise actual proposed routes and responses; a helper test alone cannot prove a mounted gate. Add real browser acceptance for invite acceptance, scoped navigation, revoked-session behavior, keyboard/dialog focus and truthful loading/error states against that same test boundary. Never contact production identity/mail/provider services in these tests.

Prior art is the maintained mounted Admin overview refusal, provider-session admission, frozen-world-before-object-lookup and Admin email-login tests. Reuse their Request/Env/authentication patterns, not Admin scopes or Controller issuance. Source locations and audit limitations are in `SOURCE-NOTES.md`. Existing generated-HTML/unit tests are supplemental; they do not replace mounted authorization or real-browser behavior. This test seam is selected for the proposed design; execution still requires a separately authorized implementation work order.

Required behavior matrix:

1. Anonymous visitor cannot issue invitations, read private study details or obtain active access by opening a link.
2. An authenticated non-Admin without a study grant is denied both via UI and direct requests.
3. A study-role grant alone is denied every unrelated global Admin action. A person who independently holds Admin authority retains it through the explicit Admin boundary; study membership must neither manufacture nor silently erase that authority.
4. A valid invite accepted by its intended identity creates one scope-limited grant and nothing broader.
5. A forwarded invitation used by another identity grants nothing and leaks no unauthorized study details.
6. Expired, declined, revoked and consumed invitations cannot grant new access.
7. Concurrent accepts and repeated clicks cannot create duplicate or broader grants.
8. Reissued links invalidate old credentials; revocation cannot be undone by a stale form or request.
9. A grant for study A cannot read or mutate study B through path, query, body, downloaded-file or background-operation identifiers. Repeat with identical IDs in different worlds, including pagination and cache hits; protected content or existence metadata must not cross the boundary.
10. A forged role, scope, issuer, capability or membership version is rejected.
11. Revoked membership is denied on the next protected request even with a previously valid session and cached UI.
12. State-changing requests resist CSRF and unsafe redirect/link handling using the established session boundary.
13. Unassigned steward permits preparatory setup but keeps steward-dependent research blocked.
14. Admin designation alone does not record steward acceptance; ordinary invitation acceptance alone does not accept steward duties.
15. Missing PSR prerequisites, consent, eligibility or release authority cannot be bypassed by invitation, membership or designation. Test withdrawal before a queued job or protected output, expired retention, mixed-consent aggregation and explicit dataset opt-out without materializing protected data in the destination.
16. No setup/acceptance workflow starts a research window, enrolls Players, changes canonical readiness, provisions resources or deploys.
17. Response payloads, audit output, rendered HTML and browser telemetry exclude secret invitation material and prohibited private data.
18. Network interruption, ambiguous persistence, expired sessions, unavailable dependencies and stale edits produce truthful recoverable states without broadening access.
19. Keyboard/dialog/focus and responsive workflows pass applicable UI checks, with real-platform obligations reported separately.
20. Legacy Admin-only routes and existing Player/Controller admission invariants retain their prior behavior.

These are proposed acceptance tests, not executed passes. No full-suite blast-radius measurement is claimed: no implementation/default/shared-contract patch has been applied. Any such patch requires a complete isolated probe after the implementation scope is authorized, preserving failures and reporting affected test groups.

## Out of Scope

- Implementing or deploying UI/API/storage now; sending actual invitations or assigning a steward.
- Public study registration or automatic role assignment from an email domain, shared link, Player/Controller identity or organization membership.
- Broad global Admin privileges for study invitees.
- Opening hosted STUDY, creating research routes or schemas without the required RFC, starting runs or satisfying PSR gates by configuration alone.
- Recruitment, participant enrollment, collection of natural-play evidence, new resources, billing, production changes, exports or new consent policy.
- Reopening settled Q1–Q5, releasing PR882, changing PR851's draft status, renewing frozen777 allowances or changing issue733 disposition.

## Further Notes

The canonical PSR-2 scenario separates PSR-1 completion, named/accepting stewardship, signed consent/opt-in basis, locked evidence floors, accountable-owner human sign-off and a separate hosted-STUDY RFC. Successful setup or invitation does not move either gate. Even after an evidence-backed PSR-2 promotion and Danny's human-yes, only `hosted_study_pipeline` may move BLOCKED to NEXT; `surfaces.study_hosted` stays BLOCKED pending its separate hosting RFC. Preserve all locked population/cycle/K/N floors unchanged.

### Delivery and review sequence

1. Review the selected read-only baseline and mounted-plus-browser testing seam below; keep all other execution holds unchanged.
2. Reconcile the proposed intent and Workflows into canonical Specs with appropriate security/hosting RFC dependencies. A new finer study partition, grant/persistence or identity boundary is not docs-only hygiene exempt from RFC review.
3. Define the security-reviewed identity/session contract, invite/grant storage and transactional/versioning guarantees. Do not choose a storage provider or migration merely to complete a UI draft.
4. Only under a separate implementation work order, build scope/authorization and negative cases first, then the Admin invite/membership UI and invitee workspace, then steward designation/acceptance. No UI-only scaffold may be reported as secured while its server gates are absent.
5. Validate native affected/full suites, typecheck and controlled browser workflows after authorized implementation; seek exact-head review/CI. Deployment, research execution, data exports and canonical acceptance remain separate.

### Selected baseline and remaining RFC work

- **STUDY-ROLE-BASELINE — selected for this proposal:** invited study users inspect only authorized redacted setup/readiness within their study/world. Existing Admins manage invitations/configuration and later steward designation. No transitive invitation, draft-edit, run or export capability is added to the baseline role.
- **STUDY-TEST-SEAM — selected for this proposal:** mounted Worker request/auth tests plus controlled real-browser workflows, with injected non-production identity and persistence dependencies.
- Precise finite lifetimes, wire/session contracts, role names, persistence/versioning, invitation delivery and required RFC acceptance remain design/security work before runtime implementation; do not fill them by treating this proposal as an Accepted contract.
- The proposal preserves every locked PSR floor and hosting/consent/owner gate. Existing generic roles and Admin capabilities do not supply a per-study grant. This is not a Q6 release, a study launch or a deployment grant.
