# RFC-0131 operation-preparation catalogue

**Status: Draft, unaccepted, unregistered, not runtime-ready.**

`operations.json` is a review catalogue of logical request/response candidates and operation invariants. It is not an HTTP/API contract, JSON Schema, OpenAPI definition, credential verifier, transition engine or persistent store. No method/path/status code, numeric policy or bootstrap authority is reserved by this catalogue. Every `UNRESOLVED` decision stays gated.

Use the [owning Draft RFC](../../../../rfcs/RFC-0131-study-access-control-plane.md) for requirements and the [record-shape packet](../README.md) only for hypothetical server-owned representations. A record field is not automatically a client input. New catalogue names are proposal metadata, not registered wire fields.

The plan's inline verifier checks catalogue identity, completeness and proposal boundaries only. Existing record `validate.py`, the native specification suite and ordinary CI do not validate these capsules as request/response or authentication contracts. No future SA case is an executed pass.

Before acceptance, resolve route/identity/bootstrap/schema/error/idempotency/version/policy/durable/output-fence decisions, write actual machine schemas and discriminating fixtures, and obtain formal review. The confirmed future mounted Worker authorization plus controlled-browser injected-dependency seam remains required and unexecuted. No real invitations, roles, resources, migrations, deployment, research, exports or hosting follow from publication.

## Offered grant deadline — selected Draft representation

The [D10 design note](OFFER-EXPIRY-DESIGN.md) records the operator-selected Draft representation A: a fixed server-owned offered grant deadline on the invitation. It changes no schema or lifetime value and remains unaccepted/unimplemented. D10 stays UNRESOLVED for full contract/qualification; future tests and ordinary CI are not behavior or security proof.

## Isolated D10 shape proposal

The [offered-expiry shape packet](offer-expiry-shapes/README.md) tests hypothetical selected-A record shapes only. Existing records, catalogue and canonical registration are unchanged; matching fixture pairs or recorded dates do not prove identity, live acceptance, policy, clocks, persistence or the output fence. All D01-D10 remain unresolved for full qualification.

## Setup/readiness disclosure — Draft design

The [D03 projection design note](SETUP-PROJECTION-DESIGN.md) traces the existing seven candidate response fields to qualified value sources and disclosure obligations. It is not a DTO, a selected criterion registry, an implemented projector or privacy qualification; the record-only discriminator and all wire/policy/identity/durable decisions remain gated. Existing schemas/catalogue/fixtures and D10 proposals are unchanged. D03 remains UNRESOLVED for full contract and qualification.

## Account binding and management configuration — selected Draft boundary

The [D02 identity/authority design note](IDENTITY-AUTHORITY-DESIGN.md) records the operator-selected initial model: owner-authorized out-of-band registry setup, changes and recovery, with no registry-configuration UI capability in this phase. It separates Account attribution, same-actor Admin admission and exact management authorization; it appoints nobody and applies no configuration. Full D02 and all D01–D10 qualification remain unresolved; schemas/catalogue/fixtures and runtime are unchanged.

## Existing Account resolution — selected Draft boundary

The [Account-resolution design](ACCOUNT-RESOLUTION-DESIGN.md) records the selected initial study-management issuer rule: an existing uniquely qualified eligible Account link only; missing/ambiguous or unavailable linkage refuses without implicit provisioning. It distinguishes the combined offline Account/Player/Controller producer from a qualified hosted Account-only resolver. General human onboarding, invitee contact recovery, concrete Account/Admin binding and full D02 qualification remain separate; no schema/runtime or live authority changes.
