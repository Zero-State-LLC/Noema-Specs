# D02 — Server-side management binding and opaque carrier (Draft design)

**Status: selected Draft design only; unaccepted, unregistered and unimplemented.** After an unanswered form, the operator explicitly said **“do as recommended”**, selecting a **server-side binding record with an opaque credential/reference and authoritative revalidation per management request**. The later answer supplies this selection; the timeout remains unanswered history. This selects the initial management-binding carrier model, not machine fields, an accepted credential protocol, live sessions or runtime implementation. Full D02 and D01–D10 remain UNRESOLVED for contract and qualification.

## Problem Statement

The [selected same-actor model](SAME-ACTOR-BINDING-DESIGN.md) requires one controlled server-established relation between verified identity, its qualified existing Account and the SAME actor's existing valid Admin admission. A signed session claim, fresh identifier or two independently valid credentials do not establish that relation or its current state. The carrier between its qualified producer and later management consumers remained unspecified. The [owning Draft RFC](../../../../rfcs/RFC-0131-study-access-control-plane.md), §§1–2 and §§5–6, also requires separate exact current authorization and qualified durable/output boundaries.

At Specs `204eabc74afc2553a10d3a3ad09093cca03269a0` and runtime `5ed9635f7fbd73bbab6dbc5bd3fad6ffbe51d627`, bounded source inspection traces existing human/Admin credential producers and consumers. This is source prior art, not a qualified management-binding store, provider/runtime execution, global store-absence claim or demonstrated production defect.

## Solution and selected Draft model

The new management path MUST resolve a server-issued credential-bearing opaque reference to a dedicated logical binding in Noema's authoritative control plane. A qualified controlled producer MUST establish the verified principal context, uniquely qualified eligible EXISTING Account and SAME actor's existing VALID Admin admission before making a reference usable. An arbitrary record identifier, caller-selected Account or independently paired credential MUST NOT authenticate this binding.

Each management request MUST validate required current binding/actor/link/Admin conditions and its independent exact study/world/operation authorization. Reference possession authenticates only through its qualified presentation/resolution protocol; it is not scope permission. Missing, stale, revoked, expired, ambiguous or unavailable required state MUST refuse. No offline signed-claim, positive stale-cache, default-owner or shared/legacy fallback is selected.

The binding is a proposed logical control-plane record, not an installed schema/table, new canonical Session or PlayerSession. The opaque carrier selects neither wire fields nor bearer/cookie/proof-of-possession protocol, browser storage, entropy/digest/key algorithm, ID prefix, numeric validity/retention/rate/timing policy, refresh mechanism, concrete adapter/RLS/SQL or migration. An unpredictable credential and a public record locator are not interchangeable. A concrete reference format and secure presentation/storage still need review and qualification.

The separate proposed read-only study credential is unchanged. Its audience, proposed durations and claims are not adopted management values. Existing Admin/global human/platform/Player/Controller credentials are not silently retagged; no old signed material becomes retroactively bound.

## User Stories

1. As an accountable issuer, I want the acting identity relation stored under authoritative server control rather than asserted by a client field.
2. As an Admin, I want current binding and exact management permission checked for every new operation without losing independently legitimate existing powers.
3. As an operator, I want unknown or unavailable binding state to refuse rather than manufacture a session, owner or permission.
4. As a human principal, I want Account resolution and binding to create no Player, Controller or gameplay PlayerSession.
5. As a security reviewer, I want reference possession distinguished from scope permission, public identifiers and current authorization evidence.
6. As an auditor, I want actual actor/link/version and truthful outcomes preserved without raw reference credentials or unauthorized contact details.
7. As an owner, I want revocation, replacement, recovery and replay to preserve terminal truth instead of resurrecting authority.
8. As a maintainer, I want the existing human/Admin and different dual-auth/device paths left unchanged by this new carrier model.
9. As a study invitee, I want my read-only study credential and later stewardship duties kept separate from management-session authority.
10. As a future implementer, I want selected logical representation distinguished from unselected wire, policy, adapter and security mechanisms.

## Source-grounded carrier distinctions

| Pinned source | What the inspected boundary establishes | Remaining qualification |
|---|---|---|
| [Human token mint](https://github.com/Zero-State-LLC/Noema/blob/5ed9635f7fbd73bbab6dbc5bd3fad6ffbe51d627/workers/noema/src/auth.ts#L237-L280) | Signed platform identity/scopes/session/time claims | A same-actor Admin/Account producer and authoritative current management binding; existing duration defaults are not selected policy |
| [Session extraction and human resolution](https://github.com/Zero-State-LLC/Noema/blob/5ed9635f7fbd73bbab6dbc5bd3fad6ffbe51d627/workers/noema/src/auth.ts#L19-L91) | Carried or generated session identifier, human principal and optional Account claim | A fresh identifier alone is not a current server binding lookup or qualified Account relation |
| [Human login consumer](https://github.com/Zero-State-LLC/Noema/blob/5ed9635f7fbd73bbab6dbc5bd3fad6ffbe51d627/workers/noema/src/play-auth.ts#L138-L212) | Provider-response identity forwarded to human-platform mint | Existing valid Admin admission, unique eligible Account join and management binding; ordinary login is not changed or executed here |
| [Admin mint/verifier](https://github.com/Zero-State-LLC/Noema/blob/5ed9635f7fbd73bbab6dbc5bd3fad6ffbe51d627/workers/noema/src/admin-auth.ts#L41-L148) and [mail consumer](https://github.com/Zero-State-LLC/Noema/blob/5ed9635f7fbd73bbab6dbc5bd3fad6ffbe51d627/workers/noema/src/admin-auth.ts#L298-L354) | Signed Admin operator/session context and mailbox-derived operator mint | Qualified provider-principal/Account relation and current management carrier; shared/legacy/mailbox labels remain insufficient |

The proposed binding MUST preserve [canonical ownership](../../../../docs/AUTH-AND-IDENTITY.md#planned-compatibility): Supabase Auth supplies human proof; Noema's Postgres control plane owns Accounts, sessions and scopes; World DO owns live game transitions. Provider subjects are links, not Noema domain IDs. Gameplay PlayerSession and World DO MUST NOT replace control-plane identity/scope authority for this binding. Existing Postgres durability does not qualify a particular adapter, currentness check or recovery protocol.

## Required producer → record → consumer obligations

| Boundary | Proposed obligation | Refused substitute |
|---|---|---|
| Qualified producer → binding | MUST establish the verified acting-principal context, uniquely eligible existing Account, SAME actor's existing valid Admin admission and attributable provenance before a usable carrier exists | Shared/legacy upgrade, optional Account/human-role claim, request-supplied actor or first-row Account lookup |
| Binding → reference presentation | MUST bind a server-issued secret credential/reference to exactly its intended established context through a qualified presentation/resolution protocol | Public/guessable record ID, caller-chosen reference, unrelated credential class or client-provided binding contents |
| Presentation → current admission | MUST check required authoritative binding/actor/link/Admin state and exact independent management authorization before protected disclosure or mutation | Reference possession alone, stale positive cache, offline signature, default-owner/wildcard or ordinary study membership |
| Replacement/retry → retained state | MUST preserve actor, scope, terminal/revoked state and bounded validity through separately qualified replay/recovery rules | Blind recreation after ambiguous outcome, silent lifetime extension, actor swap or revoked-binding resurrection |
| Transition → audit/output | MUST preserve actual actor/current binding and authorization linkage, complete disclosure policy and separately qualified durable/output witness | Raw reference in audit, fabricated success, restored stale authority or a second read claimed to solve output races |

Necessary identity/authorization-store reads are distinct from protected study-content lookup. Refusal prevents domain authority creation/widening; separately reviewed audit/idempotency bookkeeping is not falsely asserted write-free. A future creation/replacement operation MUST distinguish committed, refused and ambiguous outcomes and use qualified readback/recovery rather than blindly mint another usable reference.

Reference credentials MUST remain excluded from raw logs, audit text, error bodies, analytics and browser evidence; unauthorized principal/contact/scope information MUST follow its reviewed disclosure policy. Safe credential-at-rest handling, resolution resistance, non-enumerating complete responses, transport/browser security and retention/backup treatment remain explicit qualification gates, not claims of privacy established by an opaque string.

Finite validity, authoritative clock/currentness, invalidation, replacement and recovery MUST be specified before adoption; this note adopts no duration or refresh policy. A server-side record alone does not solve revocation between lookup and output: the adapter/consumer's linearization point and output fence still need their own contract and adversarial evidence. Restore or rollback MUST NOT resurrect terminal/revoked authority or treat an old snapshot as current.

## Compatibility and neighboring authority

The [existing Account-only boundary](ACCOUNT-RESOLUTION-DESIGN.md), [same-actor model](SAME-ACTOR-BINDING-DESIGN.md) and [owner-authorized out-of-band registry/no-UI model](IDENTITY-AUTHORITY-DESIGN.md) remain settled. The proposed binding is not registry bootstrap authority, a study-configuration patch or removal of Admin invite/access/later-steward interfaces. No real owner/Account, role, record or configuration is installed.

General human onboarding and intended-invitee/contact acceptance/recovery remain separate. Account attribution is not proof of one natural person; matching Account values alone are not the complete acting-principal relation. Existing legitimate Admin, different isolated Agent Player-plus-Admin/device approval and ordinary human behavior remain unchanged. No invented two-Admin rule, Player/Controller coercion or automatic Account/Player/Controller/PlayerSession provisioning/relinking follows.

A signed management-binding claim envelope was not selected as the initial carrier and is not an offline fallback. The read-only role remains `study.setup.read`; membership, management, Controller enrollment, steward designation/duty acceptance, consent, research, runs, export and hosting remain distinct.

## Testing Decisions — future observations, not executed

Future qualification MUST use the already selected mounted Worker `fetch(Request, Env)` boundary with injected non-production identity/persistence, then controlled browser workflows. The qualified producer, authoritative resolution/currentness and actual protected consumer MUST be exercised; matching helper strings or record shapes alone do not prove this boundary. These document-local BC labels are unregistered future observations, not executed SA/native/browser/security coverage.

- **BC-01 — Qualified creation**: Only a qualified controlled producer may establish a binding from verified identity, one eligible existing Account and SAME actor existing valid Admin admission; no independently paired or unbound shared input.
- **BC-02 — Opaque reference is not scope authority**: A valid credential/reference resolves only its established binding; exact current management scope/operation remains independently necessary.
- **BC-03 — No record fabrication**: Unknown, malformed, forged, unavailable or unqualified binding refuses rather than minting a default record or owner.
- **BC-04 — Revocation and currentness**: Expired/revoked/stale binding, changed Account/link or unverifiable required Admin/management state denies; no offline positive-cache fallback.
- **BC-05 — Replay and replacement**: Replay, lost credentials, reauthentication or replacement cannot change actor, widen authority, extend validity implicitly or revive a terminal binding.
- **BC-06 — Namespace isolation**: Other credential classes, another verified identity context or other study/world/operation cannot alias or inherit this admission.
- **BC-07 — No domain onboarding**: Binding preparation creates/relinks no Account, Player, Controller or PlayerSession and installs no registry permission.
- **BC-08 — Secret/privacy boundary**: Credential-bearing reference, provider/contact data and unauthorized Account/scope existence are absent from complete logs/audit/errors/browser evidence under the reviewed disclosure policy.
- **BC-09 — Authoritative store ownership**: Required current binding/scope authority resolves through qualified Noema control-plane state, not client claims/WorldDO/default world/eventual positive cache.
- **BC-10 — Recovery and output fence**: Restore/crash/ambiguous persistence preserves terminal state and truthful outcome; output races need their separately qualified linearization/evidence, not merely another read.

Positive/refusal and retained-state observations MUST establish the same actor/context and exact operation, including complete responses/audit and the separately qualified output boundary. Existing native/shape checks are supplemental. No runtime/helper/provider/browser probe is authorized by this document.

## Out of Scope and remaining gates

No installed machine field/schema/table/identifier/version, accepted credential/session protocol, endpoint/HTTP/DTO/error contract, numeric policy, concrete cryptographic/storage/transport mechanism, adapter/RLS/query/migration or runtime implementation. Canonical contracts, record packet, operation catalogue, fixtures, RFC status, acceptance checklist and native tooling/workflows remain unchanged.

Qualified producer/Account currentness/recovery, exact trusted registry, finite policy, secure carrier resolution/presentation, complete machine/wire/durable/backup/output guarantees, compatibility and recorded formal security review plus eventual mounted/browser evidence remain prerequisites. Full D02/D01–D10 remain UNRESOLVED; RFC-0131 stays Draft/unaccepted/unimplemented; issue #396 stays OPEN/not runtime-ready. Publication/CI/static PASS or a missing-review exception is not formal acceptance. PR #408 and earlier exceptions are consumed and cannot authorize this publication's merge.

No live identity/Account/role/auth/registry/session/provider/resource/data/migration/deployment/enrollment/research/export/hosting or coding-partner action. Preserve #882/Q6, #851, frozen #777/source0, #733 OPEN, RFC-0128, PSR, consent, steward, hosting and protected scratch holds. Refs #396.
