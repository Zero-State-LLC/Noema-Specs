# RFC-0103 — ACCESS_POLICY S2 ALLOW_ONLY

## Status

**Accepted**

No new events. No `event-catalog/0.3`. ACCESS_POLICY help stays omitted. WED / ATTEST stay omitted.

## Problem

[ACCESS-POLICY-S1.md](../docs/ACCESS-POLICY-S1.md) hosts EXIT/ROOM DENY and CLEAR. `ACCESS_RESTRICTED` already names `ALLOW_ONLY`. Hosted MOVE only checks DENY. An implementer would invent a second policy table, treat `*` as a whitelist, or let ALLOW_ONLY punch through DENY.

## Proposed change

Accept ACCESS_POLICY S2. Add **ALLOW_ONLY** to the same verb and restriction store:

- `access <dir|here> allow for <org> applies_to=<player>` / structured `COMMIT.ACCESS_POLICY` `mode=ALLOW_ONLY`
- Same occupied `GRANT_ACCESS` + treasury cost as S0/S1
- `applies_to` MUST be a named Player (not `*`)
- Writes existing `access_restrictions` + `ACCESS_RESTRICTED` (`mode=ALLOW_ONLY`)
- MOVE: if a live ALLOW_ONLY hits the route, only the listed player may take it; anyone else is rejected
- Live DENY still rejects, including the listed player
- CLEAR removes a matching ALLOW_ONLY row
- Help still omits ACCESS_POLICY / WED / ATTEST

Catalog: [`access-policy-catalog.s2.json`](../specs/access-policy-catalog.s2.json).  
Slice: [ACCESS-POLICY-S2.md](../docs/ACCESS-POLICY-S2.md).

## Alternatives rejected

| Alternative | Why |
|-------------|-----|
| New events | Catalog closed |
| `applies_to=*` | Not a list |
| ALLOW_ONLY beats DENY | DENY remains the hard block |
| Help ACCESS_POLICY | Separate pin |
| Second policy table | One store, one MOVE check |

## Compatibility

Additive mode. Worlds ignoring S2 keep DENY/CLEAR only.

## Data / security

Public rooms only. Named list only. WATCH uses existing restriction projections.

## Validation

`check_access_policy_s2`: ALLOW_ONLY accepted with grant + named list; `*` rejected; DENY still accepted; help still omits ACCESS_POLICY.

## Rollback

Reject `allow` / `ALLOW_ONLY` again. Keep S0/S1 DENY/CLEAR.

## Unresolved

ACCESS_POLICY help. WED / ATTEST help. YOUR POSITION.
