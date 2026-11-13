# RFC-0131 records-only machine-contract proposal

**Status: isolated, provisional Draft. Not accepted, registered or implemented.**

This packet makes selected logical record *shapes* from Draft RFC-0131 executable through JSON Schema 2020-12. It is not an HTTP/API contract, request DTO, authentication service, JWT verifier, grant store, lifecycle implementation or security qualification. Do not wire it into canonical schemas, native validators, a runtime or a deployment merely because its examples match.

The operator already explicitly chose read-only redacted assigned-study/world setup/readiness and eventual mounted Worker authorization plus controlled browser tests with injected identity/persistence. This packet does not reopen or replace those choices. It uses the repository's separate `SKILL.SCHEMA` shape-validation procedure for a proposed artifact, not as a substitute for the agreed future product acceptance seam.

## Files and execution

- `records.schema.json`: isolated draft URN, internal references only, closed hypothetical server-owned records. No canonical schema ID or version registration.
- `case-index.json`: independent case identity/expectation/tier inventory.
- `examples.json`: synthetic records only. Fixture references and the all-zero digest are not real identities, grants, credentials, data or authority.
- `test_validate.py`: opt-in subprocess/CLI tooling tests using only test-owned temporary packet copies; not product authorization tests.
- `validate.py`: explicit offline shape checker. It rejects non-local schema references, duplicate JSON keys and missing/extra/duplicate example identities. It emits counts and sanitized schema-keyword diagnostics, never record values. Both static and dynamic non-local schema references are rejected before resolution; a no-retrieval registry provides a second offline boundary.

Run with an existing environment containing `jsonschema`:

```text
python -I specify/study-admin-ui/contracts-draft/validate.py --json
```

Set `TMPDIR` to an existing owned temporary workspace, then run the checker CLI tests separately:

```text
python -I specify/study-admin-ui/contracts-draft/test_validate.py
```

Those tests make private temporary packet copies and clean them up; the ordinary checker itself writes nothing. A platform unable to create a test-owned symlink reports that single case as skipped rather than claiming coverage. Tooling tests exercise baseline completeness, exact negative predicates, missing/duplicate input, static/dynamic reference refusal, calendar/capability discrimination and symlink refusal. They do not perform HTTP or authenticate anybody.

No dependency installation, provider, network, live auth, browser, database or production call is needed. The validator reads only its adjacent packet files and writes nothing. The supplied JSON Schema's custom `noema-draft-utc-second` format requires this explicit runner: JSON Schema formats are not automatically assertions, and an optional library date-time plugin must not be assumed present. The runner checks the exact UTC-second spelling and real calendar date with Python's standard library. This proposed subset deliberately excludes offsets, fractional seconds and leap seconds; it is not a claim about an existing wire protocol.

## Record scope

The proposed records cover human identity bindings, study scope, Admin management authorization, invitations, read-only grants, study access **claims shape**, bounded audit transitions, steward designation/responsibility references and redacted readiness projections. They are server-owned logical records, **not objects a client may submit to set its issuer, identity or permissions**. A future API must define its own authenticated input DTOs and server-derived fields.

The read-only capability is closed to `study.setup.read`. Management operations have a separate proposed closed vocabulary, not an invited role's powers. Fields cannot supply Player/Controller authority, global Admin, draft editing, onward invitations, research execution, exports or gate promotion. An unassigned steward and a missing/nonverified prerequisite indicator are valid setup shapes; they confer no research authority.

Canonical Account/world regular expressions are copied verbatim from [id-rules.v01](../../../specs/id-rules.v01.json), including the legacy world spelling. A separate draft input guard refuses whitespace/control/wildcard characters; no canonical identifier rule is modified and no value is normalized. New principal/study/invitation/grant/contact/proof identifiers remain proposed opaque references, not aliases for PlayerSession IDs. The other field names, draft record/type/version identifiers, new opaque-reference length bound, numeric representation bounds, management operation vocabulary and readiness row bound are **proposal choices**, pending compatibility/security review. They are not adopted configuration defaults or evidence of existing canonical fields. The packet does not select a bootstrap/configuration authority, provider, database adapter, retention duration or delivery method. RFC-0131's proposed invitation/grant/session lifetimes remain proposals; no lifetime policy is adopted or proved by these shapes.

## What the checker proves

For the committed packet bytes and indexed examples only:

- required fields, types, exact constants and closed vocabulary;
- no additional object properties or widened/duplicate baseline capability;
- nonempty explicit study/world shape without a wildcard/default spelling;
- representation bounds and exact UTC-second/calendar format;
- accepted-invitation binding-field and accepted-responsibility reference-field requirements;
- correspondence between the complete case index and example collection; each negative must fail at the independently named instance path and schema keyword, not merely fail incidentally.

The inventory includes **limitation controls** that remain shape-valid despite reversed chronology or a different world's spelling. They demonstrate the boundary of the validator, not permission to accept those records at runtime. `expected_shape_valid` never means authenticated, authorized, unexpired, active, consented, deliverable, durable or safe.

## What remains unproved and blocked

Schema-valid identity/account/proof references do not establish a verified HumanPrincipal or Account mapping. Even an opaque account field cannot prove that a shared/legacy/mailbox operator label has been correctly linked. Only a qualified server identity boundary and authoritative lookup can establish that. Client input must never manufacture it.

The packet cannot prove issuer authority, exact target entitlements, cross-record identity/scope linkage, immutable fields over time, current version/state, chronological ordering or duration limits, present clock/expiry, uniqueness, valid transitions, replay behavior, atomicity, crash/recovery, revocation, backup freshness or the output linearization fence. It creates no grant and demonstrates no one-use acceptance or fail-closed real store behavior.

Closed fields do not prove redaction: a schema-valid string or reference may still encode private data. The future server must authorize its audience, construct an allowlisted projection and apply content/privacy policy before output. A criterion's `recorded` marker is not canonical acceptance, consent, research eligibility, a PSR promotion or operational authority. An audit outcome is not evidence that the operation actually happened. A duty-acceptance reference is not a human signature.

No invitation credential, JWT signature, provider identity proof, API handler, cookie/browser policy, persistent record, live study, migration, enrollment, research action, export or hosted feature is implemented. Full API/error/idempotency/version contracts and machine fixtures, registry/bootstrap and Account mapping, qualified durability/revocation/output fence, adopted policy limits, formal security review and eventual mounted/browser tests remain separate prerequisites. RFC-0131 stays Draft.

## Publication boundary

Placement and existing identifier constraints were audited against Specs `1ed3f68aa277b83fb193802c411545dc1aa8c272` and reconciled; this remains a proposed, unaccepted records-only packet. Native validation parses `specs/` and `examples/`, not this isolated area: ordinary CI does not run this opt-in checker or certify its cases. Any future CI adoption needs its own reviewed scope. The [Draft RFC](../../../rfcs/RFC-0131-study-access-control-plane.md) retains all incomplete contract/security and eventual mounted/browser qualification gates. Any repository publication must stay under the isolated draft area, preserve canonical schema/protocol/version/acceptance surfaces, pass actual local validation and independent review, and obtain its own current-head CI/code-owner gate. PR398's admin review exception is consumed and cannot be reused.
