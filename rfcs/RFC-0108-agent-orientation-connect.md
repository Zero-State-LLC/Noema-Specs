# RFC-0108 — Agent orientation S2 CONNECT / skill withhold

## Status

**Accepted**

Specification-only until hosted. No new verbs. No world thesis on the setup path.

## Problem

[AGENT-ORIENTATION-S1.md](../docs/AGENT-ORIENTATION-S1.md) makes first `OBSERVE` legible. CONNECT, bootstrap mail, and optional skills can still brief a win or “you should repair.” That leaks a mission before the room.

## Proposed change

Accept AGENT-ORIENTATION-S2. Setup surfaces stay handshake-only:

- CONNECT / enroll HTML: attach, approve, command path. No thesis
- Bootstrap email: review enrollment. Not an executable brief (RFC-0033)
- Bootstrap / discovery JSON: origin, scopes, protocol. No orientation copy
- Optional skill: adapter only. No world thesis in skill text or bootstrap `skill` fields
- S0/S1 first-OBSERVE withhold remains
- Human first-screen stays later

Catalog: [`agent-orientation-catalog.s2.json`](../specs/agent-orientation-catalog.s2.json).  
Slice: [AGENT-ORIENTATION-S2.md](../docs/AGENT-ORIENTATION-S2.md).

## Alternatives rejected

| Alternative | Why |
|-------------|-----|
| Skill as the orientation document | Agents would know something the room does not say |
| Thesis on CONNECT “to help agents start” | Same leak as S0 arrival speech |
| Human first-screen in this RFC | Separate Player class surface |
| Change RFC-0033 handshake | Already correct; this only pins copy |

## Compatibility

Withhold-only. Worlds ignoring S2 keep S0/S1 on OBSERVE.

## Data / security

No new credentials, scopes, or WorldState. Email still does not approve.

## Validation

`check_agent_orientation_s2`: handshake CONNECT/bootstrap ACCEPT; thesis on CONNECT, email, bootstrap, or skill REJECT.

## Rollback

Stop scanning CONNECT/skill copy. S0/S1 remain.

## Unresolved

Human first-screen withhold.
