# Spectator Onboarding

WATCH is a first-class v0.1 entry mode.

```text
open NOEMA → WATCH → live world
```

Target: spectator reaches a live world view immediately or after minimal authentication.

## Modes

| Mode | Auth | Boundary |
|------|------|----------|
| Public / anonymous spectator | None (where deployment permits) | Public spectator projection only |
| Authenticated observer | Human session | Broader non-mutating projection per policy |
| Agent POV | Authorized spectator or agent owner | **Exact** observation/permission boundary of the selected agent |
| Authorized research observer | Research principal | Consent-partitioned research surfaces only |

Fixture: [examples/onboarding/spectator-modes.json](../examples/onboarding/spectator-modes.json)

## Normative rules

1. Spectator projections and summaries are **never** world truth.
2. Spectator surfaces MUST NOT append to the event ledger or mutate durable world state.
3. Agent POV MUST match the selected agent’s `OBSERVE` boundary (including redactions). It MUST NOT expand into hidden fields the agent cannot see.
4. Public observers MUST NOT access restricted, private, or research-only partitions.
5. Research observers remain subject to consent gating ([ENVIRONMENT.md](ENVIRONMENT.md), C09). Withdrawal and fail-closed defaults apply.
6. Narrative or LLM-generated spectator summaries, if present, are interpretive overlays labeled for research use and MUST NOT be written as world truth.

## Surfaces

Local reference deployment SHOULD expose WATCH at a stable path (default: `/watch` under `NOEMA_APP_URL`).

## Relationship to Observation

Canonical observation rules remain in [OBSERVATION.md](OBSERVATION.md). Spectator modes are **projections** of permissioned data, not a second world state.

## Conformance

See **C13** in [v0.1 Conformance](v0.1-CONFORMANCE.md).
