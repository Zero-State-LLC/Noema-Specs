# RFC-0107 — Agent orientation S1 situation fields

## Status

**Accepted**

Specification-only until hosted. No new verbs. No arrival speech. No invented strain.

## Problem

[AGENT-ORIENTATION-S0.md](../docs/AGENT-ORIENTATION-S0.md) withholds a thesis but leaves place and strain buried in `LOCATION`. An implementer would add an arrival brief, or an agent would treat `AVAILABLE_ACTIONS` as the mission.

## Proposed change

Accept AGENT-ORIENTATION-S1. First `OBSERVE` MAY attach a `situation` object derived from the live room:

- `place` is the existing room name
- `strain` is present only when the room already shows strain (condition, empty stock, true public report)
- Quiet rooms omit `strain`
- S0 withhold still applies: no thesis, class, “you should…”, research objective, verb dump, memory lecture, arrival speech
- Same facts as humans. No new events
- WATCH does not carry `situation`
- CONNECT / skill thesis lock stays S2

Catalog: [`agent-orientation-catalog.s1.json`](../specs/agent-orientation-catalog.s1.json).  
Slice: [AGENT-ORIENTATION-S1.md](../docs/AGENT-ORIENTATION-S1.md).

## Alternatives rejected

| Alternative | Why |
|-------------|-----|
| Arrival speech | S0 rejected |
| Invented entry-room pressure | Fake quest |
| Change `LOCATION` meaning | Breaks existing consumers |
| WATCH situation | Spectator leak of a player-facing aid |
| CONNECT/skill lock in this RFC | Deferred S2 |

## Compatibility

Additive optional field. Worlds ignoring S1 keep S0 withhold only.

## Data / security

`situation` is derived. Hidden rooms stay hidden. No new WorldState.

## Validation

`check_agent_orientation_s1`: place matches room name; strain only when live strain exists; quiet omits strain; S0 forbidden phrases still reject.

## Rollback

Omit `situation`. S0 withhold remains.

## Unresolved

CONNECT/skill thesis lock (S2). Human first-screen withhold.
