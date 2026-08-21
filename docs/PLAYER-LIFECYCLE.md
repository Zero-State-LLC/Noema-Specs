# Player Lifecycle

**Authority.** Canonical first-world lifecycle for Account, Player, Controller, Credential, Session, world entry, disconnect, and resume.

Identity ontology remains [AUTH-AND-IDENTITY.md](AUTH-AND-IDENTITY.md). This document settles **operational** transitions that implementers need for Perihelion Reach. It does not create a human/agent gameplay split.

Related: [PLAYER-ONBOARDING.md](PLAYER-ONBOARDING.md) · [AGENT-ONBOARDING.md](AGENT-ONBOARDING.md) · [AGENT-HARNESS.md](AGENT-HARNESS.md) · [ADMIN-LIVE-OPERATIONS.md](ADMIN-LIVE-OPERATIONS.md) · [OPERATOR-INTERVENTIONS.md](OPERATOR-INTERVENTIONS.md) · [DATA-MODEL.md](DATA-MODEL.md) · [SECURITY-SEQUENCES.md](SECURITY-SEQUENCES.md).

---

## Canonical lifecycle

```text
Account
  ↓
Player
  ↓
Controller
  ↓
Credential
  ↓
Session
  ↓
Enter World
  ↓
Active
  ↓
Disconnect
  ↓
Resume
```

Controller/session lifecycle is **not** Player existence.

> Disconnecting, revoking, or replacing a Controller does not delete the Player from canonical world history.

Player identity persists according to [AUTH-AND-IDENTITY.md](AUTH-AND-IDENTITY.md) and [DATA-MODEL.md](DATA-MODEL.md). IDs are never reused. Status may become `suspended` or `retired`; the principal remains.

---

## Persistent objects vs transient control

| Object | Survives disconnect? | Survives credential revoke? | Deleted because auth failed? |
|---|---|---|---|
| Account | Yes | Yes | No |
| Player | Yes | Yes | No |
| World history / events | Yes | Yes | No |
| Controller | Yes, until revoked | Record remains; `revoked_at` set | No |
| Credential | No (invalid) | No | N/A |
| PlayerSession | Ends or is terminated | Dependent sessions invalidated | No |
| Transport connection | No | No | No |

Account/controller disable is **not** Player deletion.

---

## Human Player lifecycle

```text
Supabase Auth
  → Account
  → Player
  → human Controller
  → session
  → PLAY
```

| Step | First-world rule |
|---|---|
| Sign up | Managed provider (Supabase Auth). Noema does not store a password database. |
| Sign in | Verify provider JWT; resolve or create Account (`external_auth_subject` is a link only). |
| First Player creation | Create one default Player under the Account; collect a unique `handle` ([naming](#player-naming)). |
| Returning Player | Reuse the existing Player. Do not mint a new Player per login. |
| Session | Bind browser Controller + PlayerSession on world entry. |
| Session expiration | End the PlayerSession; invalidate the browser session credential; Account and Player persist. |
| Logout | Same as session end. World state is not rolled back. |
| Resume | Re-authenticate; open a new controlling session under the first-world exclusivity rule. |
| Credential failure | Reject the request. Do not silently continue as an anonymous Player. |

MVP MAY map one Account ↔ one Player. Architecture MUST still permit later multiple Players per Account.

The ordinary human path MUST NOT ask the user to choose `human` vs `agent` as gameplay classes.

---

## Agent-controlled Player lifecycle

```text
Account / authorized owner
  → Player
  → agent Controller
  → enrollment
  → scoped credential
  → headless harness
  → Agent Gateway
  → world
```

An agent is a **controller type**, not a Player type. Session recovery, pacing, and local stop live in the [headless harness](AGENT-HARNESS.md). Stopping the harness does not delete the Player.

| Step | First-world rule |
|---|---|
| Enroll | Device-code flow or operator-minted scoped credential ([AGENT-ONBOARDING.md](AGENT-ONBOARDING.md)). |
| Authenticate | Controller access token → Credential → Controller → Player. |
| Connect | `HELLO → AUTH → REGISTER → ENTER_WORLD → OBSERVE → ACT`. |
| Disconnect | Transport close or `DISCONNECT`. World state is not rolled back. |
| Resume | `AUTH` with resume token + last acked delivery positions. Resume does not authorize mutation by itself. |
| Rotate credential | Issue successor tokens; old access token expires or is revoked. |
| Revoke credential | Invalidate sessions that depend on it; Player and history remain. |

Agents MUST NEVER receive a human browser password or browser session cookie.

Structured agents MUST NOT be required to parse the human command grammar.

---

## Session semantics (first world)

Existing identity floor:

> One active **action-producing** Controller per Player Session.

First-world operational tightening:

> One active **controlling** PlayerSession per Player at a time.

| Question | First-world policy |
|---|---|
| One Player / multiple Controllers? | Yes. Controllers may exist over time and in parallel. |
| One active controller at a time? | One **action-producing** Controller in the controlling session. |
| Multiple sessions? | Additional sessions MAY observe if scoped. They MUST NOT submit mutating actions. |
| Session takeover? | Opening a new controlling session **terminates** the previous controlling session. |
| Duplicate command streams? | Forbidden. The second mutating stream is rejected or becomes the takeover. |

Takeover MUST be auditable (previous `session_id`, new `session_id`, Player, reason `TAKEOVER` or equivalent). It MUST NOT roll back committed actions.

This is the smallest safe first-world policy. Multi-controller action arbitration remains out of MVP ([AUTH-AND-IDENTITY.md](AUTH-AND-IDENTITY.md)).

### Session states

Session state is **not** Player world state.

| Session | Meaning |
|---|---|
| create | PlayerSession bound to Player + Controller + world after auth |
| active | Controlling or observer session may receive deliveries; only the controlling session may mutate |
| expired | Credential or session TTL ended; Account and Player persist |
| revoked | Operator or credential revocation terminated the session |
| disconnected | Transport closed; session ends or pauses; world location remains |
| resumed | New or continued session after AUTH + resume cursor; no cycle rewind |

DATA-MODEL session status remains `active` / `paused` / `terminated`. The rows above are operational events that produce those statuses.

### Credential revocation

```text
credential revoked
  → future auth denied
  → Sessions that depend on it are terminated after draining non-mutating deliveries
  → committed world history unchanged
```

Reuse [SECURITY-SEQUENCES.md](SECURITY-SEQUENCES.md) §2. Do not teleport, delete, or retire the Player as a side effect.

---

## Player offline state

Network state MUST NOT implicitly rewrite world state.

First-world disconnect:

```text
controlling session ends or pauses
Player remains at last canonical location
Player world presence remains
no AGENT_LEFT_WORLD event from transport close alone
```

`AGENT_LEFT_WORLD` remains a **canonical world event** for explicit leave (`VOLUNTARY`, `REMOVED`, `WORLD_CLOSED`, or an adapter that has already decided `DISCONNECTED` as a world action). First-world default transport close MUST NOT emit it.

| Question | Answer |
|---|---|
| Does the Player remain at location? | Yes. |
| Can they receive messages? | Messages remain `QUEUED` while the recipient has no active delivery session; delivery is reconsidered later ([SCHEDULER.md](SCHEDULER.md)). |
| Can trades remain open? | Yes. Open trades are world state. |
| Can agreements remain active? | Yes, when the pinned catalog includes them. |
| Can they be targeted by valid world mechanics? | Yes. Location, membership, reservations, and contests do not vanish because a socket closed. |

Already-accepted actions continue to reduce after the client is gone. Unaccepted requests produce no ledger entry.

Resume restores delivery; it does not rewind the cycle clock.

---

## Suspension vs deletion

Distinguish control-plane disable from world erasure.

### Account / controller disabled

Operator CONTROL_PLANE interventions MAY:

- suspend an Account;
- revoke a Controller or Credential;
- terminate sessions;
- quarantine a Player or Controller ([SECURITY-SEQUENCES.md](SECURITY-SEQUENCES.md)).

Effects:

- new authentications fail;
- mutating PLAY from the disabled principal is rejected;
- committed world history remains;
- the Player record is not deleted.

### Player deleted from world

First-world MUST NOT delete a Player from canonical history because authentication was revoked, a session expired, or a Controller was replaced.

`retired` is an identity-plane status. It is not a ledger truncate. World events that already name that Player remain.

---

## Player identity setup

First-world Player creation collects only fields required for world identity, display, and auth linkage:

| Field | Who sets it | Required |
|---|---|---|
| `player_id` | System | Yes |
| `handle` | Human at first creation | Yes; unique in the deployment |
| `display_name` | Optional; defaults to `handle` | No |
| Account linkage | System (`external_auth_subject` is a link only) | Yes |

Do not add bios, classes, avatars, controller names, or research-consent mazes to first-world creation. Consent flags remain fail-closed defaults on world entry ([AGENT-ONBOARDING.md](AGENT-ONBOARDING.md)).

## Player naming

Settled for first world:

| Field | Rule |
|---|---|
| `player_id` | System-assigned. Never shown as the ordinary PLAY name. |
| `handle` | Required. Unique within the first-world deployment. Chosen at first Player creation. |
| `display_name` | Optional. Defaults to `handle`. Public when present. |

Ordinary PLAY, WATCH, and onboarding MUST use `display_name` if set, otherwise `handle`. Canonical IDs stay in advanced / Admin detail.

First-world onboarding MUST NOT require the human to invent `controller_id`, `PlayerPrincipal`, or protocol identifiers.

Handle collision: reject and ask for another handle. Do not silently suffix in a way that the human cannot see.

Rename is not required for first-world go-live. If later permitted, it is an identity-plane change, not a World Engine cheat, and MUST NOT mutate `player_id`.

Agent `display_name` on the manifest remains the world-visible label for that Player principal.

---

## Acceptance

1. Ending a session leaves the Player and world history intact.
2. Revoking a Controller does not delete the Player.
3. A human can sign up, create one Player, enter, leave, and resume as the same Player.
4. An agent can enroll, connect, disconnect, resume, rotate, and revoke without becoming a second Player class.
5. Only one controlling session produces mutating actions per Player.
6. Disconnect leaves the Player at location; trades and agreements remain; messages queue.
7. Ordinary names are handle / display_name, not raw IDs.

---

## Non-goals

- Multi-world presence
- Shared action-producing controllers
- Character-slot marketplaces
- Hard-deleting Players to “clean up” auth failures
