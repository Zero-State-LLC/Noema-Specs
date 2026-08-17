# RFC-0106 — Agent orientation S0 first-OBSERVE withhold

## Status

**Accepted**

Specification-only. No runtime change. No new verbs. No arrival speech.

## Problem

[AGENT-ONBOARDING.md](../docs/AGENT-ONBOARDING.md) covers CONNECT and handshake. [COMMAND-DISCOVERY.md](../docs/COMMAND-DISCOVERY.md) gives `AVAILABLE_ACTIONS`. Nothing machine-checks first `OBSERVE` copy. An implementer would brief a win condition, dump the verb dictionary, or invent pressure so the agent has a quest.

## Proposed change

Accept AGENT-ORIENTATION-S0. First `OBSERVE` after `ENTER_WORLD` is the whole orientation.

- Must be answerable: where am I (`LOCATION` name/description); what is strained here only if the live room already shows it
- Quiet rooms stay quiet. Do not invent strain
- Must never include a thesis, win, class, “you should…”, research objective, verb dump, memory lecture, or arrival speech
- Persistence is learned later, when a mark is still there
- Same facts as humans. No new observation fields
- `AGENT-ONBOARDING` stays the handshake

Catalog: [`agent-orientation-catalog.s0.json`](../specs/agent-orientation-catalog.s0.json).  
Slice: [AGENT-ORIENTATION-S0.md](../docs/AGENT-ORIENTATION-S0.md).

## Alternatives rejected

| Alternative | Why |
|-------------|-----|
| Arrival speech | Briefing, not discovery |
| Invented entry-room pressure | Fake quest |
| Operator/skill thesis | Agents would know something humans are not shown |
| Clearer observation fields | Deferred S1 |
| CONNECT/skill lock as this RFC | Deferred S2 |
| Teach “the world remembers” on first OBSERVE | Learned from persistence |

## Compatibility

Withhold-only. Worlds ignoring S0 keep current observations.

## Data / security

No new fields. Hidden rooms and private cognition unchanged.

## Validation

`check_agent_orientation_s0`: location-only and quiet rooms ACCEPT; live strain ACCEPT; thesis, you-should, class, research, arrival, verb dump, invented strain REJECT.

## Rollback

Delete the slice, RFC, catalog, fixtures, and check.

## Unresolved

Clearer observation (S1). CONNECT/skill thesis lock (S2). Human first-screen withhold.
