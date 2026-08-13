# RFC-0018 — Archive-Claim Field Writer

## Status

**Accepted**

Closes the GC6-S0 “who writes the claim fields” gap. No Genesis pack. No flavor-text inference. No QUEST. No `event-catalog/0.3`.

## Problem

RFC-0015 named `archive_subject_entity_id` and `archive_claim` on an `ARTIFACT`. It left the writer unspecified. An implementer would parse labels or reseed Perihelion.

## Proposed change

| Field | Rule |
|-------|------|
| Sole writers | `ENTITY_CREATE` (initial properties) or `ENTITY_UPDATE` allowlisted to those two keys |
| Not a writer | `INSPECT`, `LOOK`, World Services, WATCH, Admin flavor, Genesis on Perihelion |
| Chamber v0.1 verb | **None.** No first-world action sets the fields |
| Pairing | Both fields MUST be set together; claim ∈ {DESTROYED, OPERATING} |
| Immutability | First successful set is immutable; amendment is a later RFC |
| Provenance | Creating/updating event id is the evidence ref |
| Visibility | Fields are not PLAY text; GC6 projects only the conflict line after INSPECT access |

`INSPECT` remains a reader (RFC-0015 access). It MUST NOT mutate the ARTIFACT ([REDUCER-REGISTRY.md](../docs/REDUCER-REGISTRY.md)).

Perihelion still has no such fields. PLAY stays unprojected until a later authorized create/update (not this RFC, not a content pack).

## Alternatives rejected

| Alternative | Why |
|-------------|-----|
| INSPECT writes claims | Registry: INSPECT must not mutate target fields |
| Parse artifact label | RFC-0015 |
| Genesis DESTROYED pack | RFC-0010 / first-world freeze |
| New RECORD verb / DISCOVERY_* | Verb/catalog inflation |

## Compatibility

No Chamber BUILD thaw. GC2-S0 classes do not include archive artifacts.

## Validation

`check_rfc_0018`: Accepted; ENTITY_CREATE/UPDATE only; INSPECT not a writer; no Genesis pack.

## Rollback

Omit the writer pin. RFC-0015 source remains; adapter stays silent without fields.

## Unresolved

Closed for naming: [RFC-0020](RFC-0020-archive-claim-attest.md) specifies later `COMMIT.ATTEST`. Runtime for that operation is still unauthorized.
