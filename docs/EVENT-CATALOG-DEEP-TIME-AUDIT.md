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

## Extension Points (additive, i18n AX R3 Gate B handoff + MUD/PLAY craft per noema-specs-mud-craft)

- **i18n centralization (STRINGS + t() in ui.py/8765 Chamber)**: Keys for "event_catalog_deep_time_audit", "role_assigned", "role_vacated", "succession_recorded", "institution_transformed", "artifact_created", "artifact_decayed", "derived_machine_records", "organization_create", "infrastructure_damage", "contestation_transfer", "documents_artifacts". Use t() for coverage tables, candidate lists, decision notes in Chamber deep-time/audit/PLAY surfaces.

- **R3 Chamber (RFC-0120 agent-only Player identity + human S0 withhold)**: Agent-derived records for institutions/succession/artifacts/claims/scars/names from ledger. Human S0 separate.

- **Gate B S0-S3 + version comparisons (event-catalog/0.2 strategic + future RFCs)**: No 0.3 in v0.6; RFC-only expansion with schemas/fixtures/isolation. Version comparisons for org/infra/contest/artifacts.

- **AX (semantic/ARIA/keyboard/contrast/live regions per omh patterns + CDP)**: Tables for existing coverage/candidates with aria-labels, keyboard for rows, live for decisions.

- **Plugin atoms / graft / ops / maint-evolve (noema-specs-mud-craft)**: Atoms for deep-time record packs, candidate RFC validation. Graft for ledger evidence traceability. Maint for derived records.

- **MUD native interaction / PLAY craft / LCA2 handoff (per noema-specs-mud-craft + MUD-PLAY-CRAFT)**: Native i18n for deep-time projections (institution lineage, world scars) in MUD/PLAY. Handoff to MUD-NATIVE-*, EVENT-CATALOG.md, PLAYER-*, AGENT-PLAY, LCA2. Room order, no new canonical verbs.

- Cross-refs: EVENT-CATALOG.md, EXPERIENCE.md, MUD-PLAY-CRAFT.md, noema-specs-mud-craft, ui.py, elevation plan, graft, 8765, R3/Gate B, prior EPs (EVENT-CATALOG-AUDIT etc.), full list incl. INSTITUTIONS, DEEP-TIME, EMERGENT-CULTURE, GC*/LCA*.
