# Proposed RFC scope — invitation-scoped study control plane

**Status: outline only. No RFC number, approval, implemented API or run authority is claimed.** This supplements the intent/spec draft and must not be mistaken for a published hosting RFC.

## Decisions the RFC must make precise

1. **Identity and admission:** define the authenticated HumanPrincipal boundary used by invitees, verification of intended identity and how study-specific credentials are issued without passing the global Admin gate or minting Player/Controller authority. Preserve existing legitimate Admin rights through their own boundary.
2. **Study/world scope:** define the new logical study scope and its canonical identifier/world mapping, if no existing entity fits. Partition records, queries, sessions, caches, jobs and output by verified scope; default deny cross-study/world access and enumeration.
3. **Capabilities:** enumerate the initial baseline grant and privileged Admin actions. Keep any future study-admin delegator, draft-editing, research execution or export permission explicit and separately reviewed. No implication from a generic researcher role or an invitation link.
4. **Invitation state machine:** define Pending/Accepted/Declined/Expired/Revoked transitions, server-clock finite validity, issuer authority at acceptance, identity binding, credential hashing/storage, one-use semantics, delivery status, resend/reissue invalidation and bounded abuse controls.
5. **Membership state and revocation:** keep consumed invitation history distinct from current grant state; define transactional/version checks for accept/change/revoke races, no stale reactivation, and authorization rechecks before protected reads or outputs from queued/long-running work. Define session expiry and revocation behavior without claiming downloaded information can be recalled.
6. **Persistence and failure atomicity:** choose a durable store only after its consistency/conditional-write behavior is qualified. Define refusal under unavailable or ambiguous state, idempotency/recovery/readback and the minimum non-sensitive audit witness. A successful UI click or invitation send is not persistence or delivery proof.
7. **Transport/browser security:** specify the study-specific bearer/session approach and identity-provider integration; retain global Admin isolation. Any cookie alternative must explicitly define secure attributes, CSRF, redirects and replay behavior. Keep invitation credentials out of logs, analytics, referrers, rendered lists and later browser history where possible.
8. **Stewardship and consent:** Admin designation may happen later; ordinary invite acceptance, duty acceptance and signed consent/opt-in basis are separate. Preserve independent capture/retention/analysis/publication/export checks, most-restrictive effective policy, withdrawal, exclusions and required deletion/tombstone workflow.
9. **Hosting boundary:** preparatory metadata UI and access-management APIs must not be treated as authorization for hosted NOTICE/TEST/COMPARE/CAPTURE, research export or a STUDY reopen. Specify the dependency on the separate hosting/isolation RFC and retain PSR/owner sign-off gates.
10. **Threat model and external tests:** unauthorized, forged, forwarded, expired, replayed, revoked and wrong-scope requests; duplicate submissions; stale grants; same IDs in different worlds; cache/queue/output races; mixed/withdrawn consent; secret/existence disclosure; and privilege crossings into Admin or Player routes. Use mounted request/auth tests and real-browser workflows, not helper-only proofs.

## Phase boundaries

- **Design phase:** confirm capability/test-seam choices; canonicalize intent, Workflows/spec and RFC/security design. No feature implementation is implied.
- **Future authorized implementation:** build and verify server authorization/persistence first, then Admin invitation/membership UI, invitee workspace and later steward acceptance UI. An authorization-free visual scaffold is not the secured deliverable.
- **Excluded from this feature:** data collection, participant enrollment, natural-play windows, research execution/exports, PSR promotion, hosting enablement, production deploy, new infrastructure or billing changes. Those require their own contracts and authority.

## Evidence

See [source notes](SOURCE-NOTES.md) for pinned primary-source facts. This outline records proposed obligations; it does not report tests as passed or security as qualified.
