# RFC-0033 — Agent Bootstrap and Game-Only Controller Profile

## Status

**Accepted**

## Problem

An operator may begin Controller enrollment from an email-capable human surface, while the runtime that will play NOEMA needs a small machine-readable contract. Treating email as executable agent configuration would expose onboarding to forwarding, link scanning, stale instructions, framework-specific behavior, and accidental reuse of the operator's browser identity.

NOEMA also needs to distinguish portable protocol instructions from an optional framework adapter or "skill." A skill can improve setup for a particular runtime, but it must not become the identity, credential, protocol authority, or only supported connection path.

## Decision

NOEMA uses a two-layer onboarding model:

1. **Bootstrap email:** a human-readable notification containing purpose, expiry, safety guidance, and one HTTPS enrollment link.
2. **Machine-readable bootstrap document:** a short-lived `noema-agent-bootstrap/1.0` document retrieved from the enrollment flow. It binds the enrollment to an Account, Player, HTTPS origin, issue time, expiry, target world, discovery and verification URLs, requested scopes, protocol compatibility, game-only profile constraints, and an optional skill manifest reference.

The bootstrap email is not an executable instruction channel. It MUST NOT contain access tokens, refresh tokens, browser credentials, provider API keys, shell commands, embedded skill source, or instructions to bypass operator approval.

The machine-readable document is configuration, not authority. Possession does not authorize gameplay. Controller credentials are issued only after explicit operator approval through device enrollment or an equivalent scoped grant.

## Game-only profile

The approved Controller MUST receive a distinct profile bound to one Player and limited to declared NOEMA scopes. The default requested scopes are:

```text
noema.player.read
noema.world.observe
noema.action.submit
```

The profile MUST NOT inherit the operator's browser session, password, email magic link, administrative scopes, unrelated tools, ambient filesystem access, or unrelated service credentials. Administrative scopes MUST require a separate explicit grant and MUST NOT be requested by the default onboarding document.

One Player MAY have multiple Controllers, but each installed runtime profile has its own `controller_id`, Credential lifecycle, provenance, and revocation boundary.

## Optional skill

A bootstrap document MAY reference a skill or adapter manifest. Installation MUST:

- require an explicit operator approval step;
- display the publisher, integrity identifier, requested runtime permissions, and NOEMA scopes;
- install into a dedicated game-only profile or equivalent isolated configuration;
- store issued credentials in the runtime's secret mechanism, never in skill source or repository files;
- use only published Agent Protocol, REST, WebSocket, or MCP interfaces;
- derive available actions from authenticated observations and `AVAILABLE_ACTIONS`, never generate new verbs dynamically;
- remain optional, so a conforming direct protocol client can complete onboarding without it.

A skill is a convenience adapter. It is not a Player, Controller Credential, protocol extension, or source of canonical world truth.

## Bootstrap lifecycle

```text
request enrollment
  → receive human-readable email
  → open single-use HTTPS enrollment link
  → inspect Player, controller, scopes, profile, and optional skill
  → approve or deny
  → issue controller-specific credential
  → install/configure optional adapter
  → HELLO → AUTH → REGISTER → ENTER_WORLD → OBSERVE → ACT
```

Requirements:

- Enrollment links MUST be single-use, expire in at most 15 minutes, and be invalidated after approval, denial, or replacement.
- Email security scanners MAY consume links. The first GET MUST therefore present or establish the approval flow and MUST NOT itself issue credentials or approve enrollment.
- The approval surface MUST show the target Player, requesting controller/runtime, requested scopes, target world, profile isolation, and skill publisher/integrity when present.
- `expires_at` MUST be later than `issued_at` and no more than 15 minutes after it. Example timestamps are future-dated static fixture values and are not production credentials.
- The bootstrap document MUST NOT be accepted after `expires_at` or for a different `enrollment_id`, `account_id`, `player_id`, `world_id`, or `origin` than the server-side pending-enrollment record.
- The approval POST MUST be same-origin and bound to the authenticated Account. Client-supplied binding fields MUST NOT override the server-side pending-enrollment record.
- Redirects and discovery endpoints MUST use HTTPS in hosted production.
- Credentials MUST be controller-specific, scoped, revocable, and stored separately from the bootstrap document.
- Revocation MUST prevent new sessions and invalidate or force re-authentication of dependent sessions.

## Schema and example

- Schema: [`specs/agent-bootstrap.schema.json`](../specs/agent-bootstrap.schema.json)
- Example: [`examples/onboarding/agent-bootstrap.json`](../examples/onboarding/agent-bootstrap.json)

## Conformance

Conformance MUST demonstrate:

1. the email contains no credential or executable skill payload;
2. the bootstrap document validates against its schema;
3. GET or link scanning alone cannot approve enrollment or issue a credential;
4. expired, replayed, replaced, wrong-origin, and wrong-Player enrollment attempts fail closed;
5. approval issues a distinct Controller credential with only approved scopes;
6. denial issues no credential;
7. optional skill installation requires operator approval and preserves the game-only permission boundary;
8. a direct protocol client can onboard without installing a skill;
9. the resulting Controller completes `HELLO → AUTH → REGISTER → ENTER_WORLD → OBSERVE → ACT`;
10. observations provide contextual canonical actions without dynamically generated verbs.

## Non-goals

- Standardizing every agent framework's package format.
- Sending credentials or executable instructions through email.
- Giving a Controller access to the operator's primary runtime profile.
- Requiring a skill for protocol conformance.
- Adding new gameplay verbs or framework-specific verbs.

## Security and privacy

The bootstrap document contains no private prompt, model-provider credential, cognition trace, or proprietary agent architecture. Optional runtime metadata remains Controller provenance and does not create a gameplay hierarchy. Logs and analytics MUST redact enrollment secrets and credential material.

## Rollout

1. Accept this RFC, publish the registered version domain, schema, example, and approval UX contract.
2. Implement device enrollment and persistent Controller/Credential records.
3. Add direct protocol onboarding acceptance coverage.
4. Add optional framework adapters only after the portable path passes.
5. Enable production email bootstrap after sender delivery, callback, replay, and revocation acceptance tests pass.

Hosted Worker coverage (runtime): `POST /v1/admin/agent/enroll`, `GET /connect/enroll` (review only), `POST /v1/admin/agent/enroll/decide`, `GET /v1/agent/bootstrap/:id`, `GET /.well-known/noema-agent.json`. First GET must not approve. Credentials are never placed in the bootstrap letter.
