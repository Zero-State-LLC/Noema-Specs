# Intent: invitation-scoped study administration

**Status:** `draft`

**Next stage:** [study administration UI design](../specify/study-admin-ui/spec.md)

**Author:** Bob / Applied Alchemy Labs

**Date:** 2026-11-13

This record is process only. It is not a normative spec, an Accepted RFC, a runtime plan or implementation authority.

## Problem

The operator needs study-preparation UI, later Admin-interface steward assignment and a study role scoped and gated by Admin invitation. **OBSERVED:** the inspected Worker has a public observational Study page and global Admin bearer authorization, not an established study-invitation or per-study grant API. The generic researcher role and Player Controller enrollment are not that authorization. See the [pinned source notes](../specify/study-admin-ui/SOURCE-NOTES.md).

## Proposed outcome

**INFERRED design:** reviewable preparatory workspaces, identity-bound invitations, explicit acceptance, study/world-scoped read-only access, revocation/audit and later steward designation plus separate duty acceptance. The proposed test seams are mounted Worker request/auth tests and controlled browser workflows. The operator explicitly confirmed both design choices on 2026-11-13 UTC through the structured confirmation form; the earlier attribution to a bare continuation was too strong. This later explicit answer is the decision record, not implemented behavior. New auth/persistence/security contracts remain RFC work.

## Affected users / systems

Existing Admin control-plane principals; invited study HumanPrincipals; later designated research-and-ethics stewards; Worker authentication/UI; study/world-partitioned research metadata. Agent Players and Controllers retain existing admission and action boundaries. No human receives Player mutation authority.

## Constraints / non-goals

No runtime implementation in Specs. No global Admin escalation, adding invitees to the Admin allowlist, transitive study-role invitations, implicit participant consent, recruitment, enrollment, research execution/export, PSR promotion, hosted STUDY enablement, production deploy, new resources, settings changes or bypass. Missing stewardship permits preparation, not dependent research. Preserve PSR-1/steward-consent prerequisites and locked PSR-2 floors. Any new identity/role/schema/persistence/hosting/export boundary requires the governing RFC/security process before implementation. The linked [RFC-0131 Draft](../rfcs/RFC-0131-study-access-control-plane.md) proposes the security contract; it is not Accepted and creates no schema or execution authority.

## Open questions

Precise role/session wire contracts, identity-provider integration, durable grant/transaction/versioning design, finite lifetime values, delivery/reissue controls and applicable security/hosting RFC acceptance are **NOT_COMPUTABLE as implemented facts**. The later RFC must settle them before runtime work; they are not grounds to claim this design is implemented. No steward nominee is needed now.

## Verified / assumed claims

| Claim | Label | Basis |
|---|---|---|
| Current public Study is observational; Admin API verifies a global Admin bearer | OBSERVED | [runtime and auth citations](../specify/study-admin-ui/SOURCE-NOTES.md) |
| Existing generic researcher/Controller enrollment is not a study-membership grant | OBSERVED | Same primary sources; no mounted study-admin/invite path established in inspected router |
| Least-privileged scope plus Admin-only invitation addresses the requested boundary | INFERRED | User requirements and selected read-only design baseline |
| Steward assignment can happen later through an Admin UI | INFERRED | Operator-selected desired workflow, not existing UI proof |
| New grant/storage/role UI is deployed or security-qualified | NOT_COMPUTABLE | No implementation, production probe or product test performed |

## Author / date

- **Author:** Bob / Applied Alchemy Labs
- **Date:** 2026-11-13
