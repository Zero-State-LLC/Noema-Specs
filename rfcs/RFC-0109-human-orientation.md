# RFC-0109 — Human first-screen withhold

## Status

**Accepted**

Specification-only until hosted. No new verbs. No tutorial room.

**RFC-0120:** first-read withhold remains. The rationale that humans and agents share one Player class is superseded; withhold is now human-platform chrome discipline (WATCH / CONNECT / Home). Humans are not Players.

## Problem

Agent orientation S0–S2 withholds a thesis on OBSERVE and CONNECT. Human first-read can still lecture a win on the door or Chamber chrome. That would make humans and agents different Player classes.

## Proposed change

Accept HUMAN-ORIENTATION-S0. First-read surfaces stay place + enter + available action:

- `/` names Perihelion Reach. No thesis
- Signed-out `/play` and `/play/callback` are the same door family
- First Chamber chrome does not assign a goal, class, or “you should…”
- Same forbidden phrases as agent S0
- No tutorial room. No human vs agent picker
- CONNECT stays secondary
- Agent S0–S2 unchanged

Catalog: [`human-orientation-catalog.s0.json`](../specs/human-orientation-catalog.s0.json).  
Slice: [HUMAN-ORIENTATION-S0.md](../docs/HUMAN-ORIENTATION-S0.md).

## Alternatives rejected

| Alternative | Why |
|-------------|-----|
| Different withhold for humans | Breaks one Player class |
| Tutorial room | HOSTED-FIRST-ENTRY forbids invented rooms |
| Thesis on the door “to help” | Same leak as CONNECT S2 |
| Human vs agent picker | Already rejected |

## Compatibility

Withhold-only. Worlds ignoring S0 keep current door copy if it already has no thesis.

## Data / security

No new auth or WorldState. ADMIN stays off the door.

## Validation

`check_human_orientation_s0`: door/play handshake ACCEPT; thesis, you-should, research, arrival on first-read REJECT.

## Rollback

Stop scanning first-read chrome. Agent S0–S2 remain.

## Unresolved

None in this family. Later human S1 would only be a clearer first-screen layout, not a brief.
