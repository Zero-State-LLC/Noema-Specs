# Event Catalog Audit — Deep Time (v0.6)

## Existing coverage

| Need | Existing support |
|---|---|
| Organization create/membership | `ORG_CREATE`, `ORG_MEMBER_ADD`, `ORG_MEMBER_REMOVE` |
| Infrastructure damage/repair | infrastructure entities + REPAIR-related actions/events as already specified |
| Contestation / transfer pressure | event-catalog/0.2 strategic conflict types |
| Documents/artifacts as entities | entity types ARTIFACT, DOCUMENT |

## Derived records (this package)

Institution, succession, historical-artifact, claims, reconstruction, scars, names — **derived machine records** grounded in ledger evidence digests. They are not new closed ledger event types.

## Candidates for future RFC (not added here)

| Candidate | Why deferred |
|---|---|
| `ROLE_ASSIGNED` / `ROLE_VACATED` | Explicit role machine if org protocol insufficient |
| `SUCCESSION_RECORDED` | First-class ledger succession |
| `INSTITUTION_TRANSFORMED` | Explicit transform event |
| `ARTIFACT_CREATED` / `ARTIFACT_DECAYED` | If entity events insufficient for integrity path |

**Decision:** No event-catalog/0.3 in v0.6 foundation. Expand only via RFC workflow with schemas, fixtures, and isolation tests.

## Extension Points

Non-normative catalog-coverage and derived-record audit seams.

- Extend coverage matrices linking institution, succession, artifact, scar and naming records to exact existing ledger evidence digests. Derived projections may be rebuilt but cannot masquerade as new event types or rewrite the source ledger.
- Preserve the v0.6 foundation decision: ROLE_ASSIGNED/ROLE_VACATED, SUCCESSION_RECORDED, INSTITUTION_TRANSFORMED and artifact lifecycle candidates remain deferred here. A localized candidate label or plugin export does not admit that type to a closed catalog.
- Compatibility/promotion: any event expansion follows a separate RFC with schema bindings, fixtures and isolation tests; do not infer event-catalog/0.3 from this audit. Pin source catalog and derivation version when comparing coverage.
- Verification proposal: rebuild a derived succession/scar record from referenced evidence, detect a missing digest and reject a deferred type at catalog admission. Check historical interpretations remain distinguishable from canonical transitions and public projections omit private lineage. Provide readable coverage and deferred-status tables rather than color-only coverage claims.
