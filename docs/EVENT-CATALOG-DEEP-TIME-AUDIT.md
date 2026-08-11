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
