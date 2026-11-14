# D02 — Same-actor Admin and Account binding (Draft design)

**Status: selected Draft design only; unaccepted, unregistered and unimplemented.** The operator explicitly selected **one server-established binding of verified identity, existing Account and that actor's valid Admin admission; reject unbound or independently paired credentials**, for the initial study-management issuer path. This selects an admission model, not accepted security policy, an existing qualified producer, installed authority or runtime implementation. Full D02 and all D01–D10 remain UNRESOLVED for contract and qualification.

## Problem Statement

The [owning Draft RFC](../../../../rfcs/RFC-0131-study-access-control-plane.md), §§1–2, requires attributable Account identity, existing valid Admin admission and exact current management authorization for the same acting context. Two independently valid credentials do not prove that relation. The [existing-Account selection](ACCOUNT-RESOLUTION-DESIGN.md) and [out-of-band registry selection](IDENTITY-AUTHORITY-DESIGN.md) remain settled, but neither supplies a qualified same-actor producer.

At Specs `5bf759a90035b748b4199aa6a7b0f95eb87ca02b` and runtime `5ed9635f7fbd73bbab6dbc5bd3fad6ffbe51d627`, bounded source inspection distinguishes the Admin operator/session context, the separate human/provider/optional Account path and legitimate existing dual-auth consumers. This is source analysis, not a provider/production test, global capability-absence claim or reproduced vulnerability.

## Solution and selected Draft model

Before NEW study-management operations rely on it, a controlled server-side producer MUST establish one attributable acting context linking verified human identity, its uniquely qualified eligible existing Noema Account and the SAME actor's existing valid Admin admission. New management consumers MUST refuse unbound/shared legacy contexts and independently paired credentials; mere possession of both does not create the binding. The model does not claim that a single check, token, browser tab or matching string solves currentness, recovery or output races.

This context is a logical proof obligation, not a newly registered record, DTO, JWT claim, endpoint, session format or login UI. The producer's mechanism, retention, transport, replay protection, lifetime, binding version and currentness checks remain to be specified, reviewed and qualified. Existing signed material is not retroactively made attributable by this design. No generic human role, Account claim or study membership can mint Admin admission.

The initial Account rule is unchanged: existing uniquely qualified eligible link only; missing/ambiguous/unavailable refuses without implicit provisioning or relinking. General canonical Account-only human onboarding and intended-invitee/contact acceptance/recovery remain separate and unchanged. Account attribution is not proof of one natural person. Matching Account values alone need not distinguish actors under future organizational/shared-account arrangements; qualify the actual verified principal context and same-actor relation rather than assume Account equality proves them.

## User Stories

1. As an accountable issuer, I want the recorded Account and admitted Admin actor to come from one qualified server-established relation, not a caller's claimed identity.
2. As an independently qualified Admin, I want existing legitimate operations preserved while the new management boundary requires its own proof.
3. As an owner, I want unrelated valid credentials to fail rather than compose into somebody else's management authority.
4. As a human principal, I want identity proof and Account resolution to remain non-Player operations without credential or enrollment side effects.
5. As an invited study user, I want my read-only grant to remain separate from Admin, registry configuration and steward powers.
6. As a reviewer, I want missing, stale, ambiguous or unavailable binding state to refuse rather than pick a default owner.
7. As an auditor, I want current actor/link/authorization provenance preserved through the transition and its qualified audit/output boundary.
8. As an operator, I want reauthentication, recovery and replay not to swap actors, widen rights or resurrect revoked authority.
9. As a maintainer, I want legitimate isolated Player-plus-Admin and device-approval paths left unchanged rather than reinterpreted as this new human binding.
10. As a future implementer, I want a selected Draft model clearly separated from unselected credential, durable and wire mechanisms or formal acceptance.

## Source-grounded producer and consumer distinctions

| Pinned source boundary | What the inspected source establishes | What it does not qualify |
|---|---|---|
| [Admin mint/verifier](https://github.com/Zero-State-LLC/Noema/blob/5ed9635f7fbd73bbab6dbc5bd3fad6ffbe51d627/workers/noema/src/admin-auth.ts#L41-L148) and [Admin principal](https://github.com/Zero-State-LLC/Noema/blob/5ed9635f7fbd73bbab6dbc5bd3fad6ffbe51d627/workers/noema/src/types.ts#L48-L55) | Signed Admin type/role/scope, operator label, authentication context and session | A current provider-principal-to-Account relation for the same admitted actor; session freshness and an opaque label are not that proof |
| [Mailbox consumer](https://github.com/Zero-State-LLC/Noema/blob/5ed9635f7fbd73bbab6dbc5bd3fad6ffbe51d627/workers/noema/src/admin-auth.ts#L298-L354) | Provider verification, normalized email, existing Admin allowlist and mailbox-derived Admin mint | Its inspected parsed/forwarded inputs do not retain a demonstrated provider-subject/Account join; this does not assert that the upstream provider cannot return a subject |
| [Human/provider path](https://github.com/Zero-State-LLC/Noema/blob/5ed9635f7fbd73bbab6dbc5bd3fad6ffbe51d627/workers/noema/src/auth.ts#L54-L167) | Separate HumanPrincipal resolution and optional Account-shaped claim | Unique current authoritative Account linkage, existing valid Admin admission or same-actor proof; a human role text is not the Admin verifier |
| [Isolated command admission](https://github.com/Zero-State-LLC/Noema/blob/5ed9635f7fbd73bbab6dbc5bd3fad6ffbe51d627/workers/noema/src/index.ts#L990-L1010) and [Player command consumer](https://github.com/Zero-State-LLC/Noema/blob/5ed9635f7fbd73bbab6dbc5bd3fad6ffbe51d627/workers/noema/src/protocol-ws.ts#L136-L184) | An existing Agent Player path plus separate signed Admin admission for an isolated boundary | A same-human-actor relation for study management; this different legitimate boundary is not labelled defective or changed |
| [Device approval](https://github.com/Zero-State-LLC/Noema/blob/5ed9635f7fbd73bbab6dbc5bd3fad6ffbe51d627/workers/noema/src/device-enrollment.ts#L644-L651) | Existing human-approval or Admin admission alternatives | The new same-actor Account relation or study-management authority |

Preserve [canonical ownership and identifiers](../../../../docs/AUTH-AND-IDENTITY.md#planned-compatibility): Supabase Auth supplies human proof; Noema's Postgres control plane owns Accounts, sessions and scopes; World DO owns live game transitions. Provider subjects are links, not Noema domain IDs. A source query/helper name or existing role label is not evidence that this new producer is qualified.

## Required proof chain for the proposed boundary

| Boundary | Proposed obligation | Refused substitute |
|---|---|---|
| Verified identity → existing Account | Establish qualified issuer/provider/audience context and exactly one eligible current authoritative Account under reviewed linkage/recovery rules | Caller-selected identity, optional Account claim, fetch-first result, mailbox hash or silent provisioning |
| Account and Admin → bound acting context | Establish the SAME actual verified actor satisfying existing valid Admin admission through the controlled producer | Independently paired credentials, equal names/mailboxes/Account claims, a shared operator or human roles.admin text |
| Bound context → management admission | Require current qualified actor/link/binding plus independent exact study/world/operation authority from the owner-authorized registry | Binding alone as permission, positive stale cache, ordinary study grant, readiness or steward badge |
| Admission → transition/audit/output | Preserve actual actor, qualified link/currentness, exact authorization and the separately qualified transition/recovery/output witness | Refusal/default labelled success, audit reference as authority, second read claimed to close a race or old backup as fresh permission |

Necessary identity/authorization-source reads remain distinct from protected study-content lookup. Missing, ambiguous, stale, revoked or unavailable required state MUST refuse new management; there is no default-owner or legacy/shared fallback. Refusal prevents creation/widening of domain authority; separately reviewed audit/idempotency bookkeeping is not falsely asserted to perform zero writes. Complete response, log, audit and browser disclosure/timing policy still needs qualification; this design proves no existence privacy by prose alone.

## Compatibility and authority boundaries

Existing Admin operations remain unchanged. Study membership neither creates nor removes independently legitimate Admin power; the same independently qualified Admin can hold separately authorized management/configuration responsibility without an invented two-Admin rule. Human/Player/Controller classes remain separate. No token is coerced into another class and no shared operator is relabelled an individual.

The selected [registry model](IDENTITY-AUTHORITY-DESIGN.md) stays owner-authorized out-of-band seed/changes/recovery with no registry-configuration UI yet. It is not ordinary study configuration editing or removal of proposed Admin invite/access/later-steward interfaces. No real owner, Account, grant or registry is configured. Invited study access remains `study.setup.read` only; steward nomination, personal duty acceptance, consent, enrollment, research and export remain independent.

A paired-credential binding protocol was NOT selected for the initial model. Two valid signatures or adjacent requests are insufficient; any later alternative needs its own explicit reviewed design rather than reuse of the isolated Player-plus-Admin precedent.

## Testing Decisions — future observations, not executed

Use the already selected mounted Worker `fetch(Request, Env)` seam with injected non-production identity/persistence, then controlled browser workflows. A separately qualified bound-context producer and consumer MUST be exercised, not just a helper asserting matching strings. These document-local SB labels are unregistered future observations, not SA coverage or native/browser/security passes.

- **SB-01 — Qualified positive**: One server-established acting context binds verified human identity, one eligible existing Account, existing valid Admin admission and independent exact management authorization.
- **SB-02 — Credential splicing**: Admin for A plus human/Account for B refuses; no authority transition.
- **SB-03 — Opaque labels**: Shared, legacy and mailbox-hash operator labels or session freshness alone cannot prove Account/provider linkage.
- **SB-04 — Principal classes**: Human roles.admin text, ordinary study membership and Player/Controller credentials cannot become valid Admin admission or Account proof.
- **SB-05 — Currentness**: Stale, revoked, missing, ambiguous or unavailable binding refuses without positive-cache/default-owner fallback.
- **SB-06 — Identity namespace**: Bare subject/mailbox/Account claim lacks qualified issuer/provider/audience/link context; matching Account alone does not prove one acting human.
- **SB-07 — Legacy compatibility**: New management refusal leaves legitimate existing Admin, isolated Player-plus-Admin, device approval and ordinary human behavior unchanged.
- **SB-08 — No implicit onboarding**: Proof verification creates/relinks no Account, Player, Controller, PlayerSession, credentials or registry authority in this initial path.
- **SB-09 — Exact authority/privacy**: Same-actor proof alone does not grant a study/world/operation; complete outputs/logs/audit/browser obey qualified non-enumeration/disclosure policy.
- **SB-10 — Recovery/output**: Reauthentication/recovery/replay cannot swap actor, widen permission or restore revoked rights; durable/audit/output guarantees need separate evidence.

Positive and refusal twins MUST verify the actual actor relation, required current authority, complete response/audit privacy and retained state at the agreed boundary. Existing source tests, shape packets and ordinary CI are supplemental, not executed proof of this proposed binding. No live provider, legacy binder, mounted feature or browser execution is authorized by this note.

## Out of Scope and remaining gates

No new accepted credential/claim/record/DTO/session/transport/route/method/error/timing/rate/retention/lifetime/version, numeric policy, concrete lookup/index/migration, provider, adapter/RLS/transaction or output-fence mechanism is selected. No legacy auth defaults/shared consumers, runtime files, canonical schema/catalogue/fixtures/identifiers/RFC status/native tooling or acceptance checklist changes.

Current Account uniqueness/eligibility/recovery, qualified actor-binding producer/consumer/currentness, exact trusted registry configuration, machine/wire/policy/durable/output guarantees, compatibility and formal security review plus eventual mounted/browser evidence remain prerequisites. D02 and D01–D10 stay UNRESOLVED for complete contract/qualification; RFC-0131 stays Draft/unaccepted/unimplemented; issue #396 stays OPEN/not runtime-ready. Publication/static review/CI or a merge exception is not formal security acceptance. PR #407 and earlier exceptions are consumed and cannot authorize this publication's merge.

No live identity/Account/role/auth/registry/provider/resource/data/migration/deployment/enrollment/research/export/hosting or coding-partner action. Preserve #882/Q6, #851, frozen #777/source0, #733 OPEN, RFC-0128, PSR, consent, steward, hosting and protected scratch holds. Refs #396.
