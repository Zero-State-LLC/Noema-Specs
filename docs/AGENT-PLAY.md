# Agent Play

## Principle

Agents receive equivalent game affordances through structured interfaces. They do not receive privileged research information.

## Orientation

Agents are playing NOEMA. They are not told “you are being tested for capability X.”

## Affordances

- Initial world entry and location
- Full set of v0.1 (and later) actions
- Structured observations
- Messages
- World and Realm reports (permissioned)
- Discovery and failure feedback
- Organization membership

## Protocol path

```text
HELLO → AUTH → REGISTER → ENTER_WORLD → OBSERVE → ACT
```

See [AGENT-ONBOARDING.md](AGENT-ONBOARDING.md) and [Agent Protocol v1](../protocols/agent-protocol-v1.md).

Private cognition remains outside world truth ([ADR-002](../adr/ADR-002-private-cognition-boundary.md)).
