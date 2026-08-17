# RFC-0104 — ACCESS_POLICY S3 Chamber ACCESS help

## Status

**Accepted**

Specification-only until hosted. No new modes. WED / ATTEST stay omitted. Schema name ACCESS_POLICY stays off the player help line.

## Problem

[ACCESS-POLICY-S2.md](../docs/ACCESS-POLICY-S2.md) hosts EXIT/ROOM DENY, CLEAR, and ALLOW_ONLY. PLAY already parses `access`. Chamber help still hides it. An implementer would keep the verb secret or invent a second command language.

## Proposed change

Accept first-world PLAY advertising of **existing** ACCESS aliases:

- `help` KNOWN COMMANDS names ACCESS
- `help access` lists deny / clear / allow
- GRANT_ACCESS + `acting_for` unchanged
- No new verb, mode, cost, or event
- WED / ATTEST remain unlisted
- Schema name ACCESS_POLICY remains unlisted

Catalog: [`access-policy-catalog.s3.json`](../specs/access-policy-catalog.s3.json).  
Slice: [ACCESS-POLICY-S3.md](../docs/ACCESS-POLICY-S3.md).

## Alternatives rejected

| Alternative | Why |
|-------------|-----|
| New ACCESS verb | Extra command |
| Help WED / ATTEST | Separate pins |
| Print ACCESS_POLICY | Schema leak |
| WATCH ticker | Spectator leak |

## Compatibility

Help-only. Worlds ignoring S3 keep ACCESS parsed and unlisted.

## Data / security

No new fields. Hidden rooms unchanged.

## Validation

`check_access_policy_s3`: help_access true; WED/ATTEST still false; ACCESS_POLICY schema name unlisted; no new verbs.

## Rollback

Omit ACCESS from Chamber help again.

## Unresolved

WED / ATTEST help. YOUR POSITION.
