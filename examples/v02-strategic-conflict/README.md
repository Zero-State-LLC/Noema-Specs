# v0.2 Strategic Conflict Fixtures

Deterministic multi-agent scenario for `event-catalog/0.2` / RFC-0002.

## Scenario

1. Nacre and Vesper form a formal ACCESS agreement (forbids infrastructure contests).
2. Nacre declares `INFRASTRUCTURE_DISRUPTION` on `entity.relay-main`.
3. Vesper defends with stake; world resolves `PARTIAL_SUCCESS`.
4. Relay condition drops 70 → 55.
5. Sensor detects sabotage; moderate crime.
6. Vault exit restricted.
7. Agreement broken for contest violation.

## Files

| File | Role |
|------|------|
| `world-seed.json` | Chamber map pin, catalog 0.2 |
| `trajectory.jsonl` | Seven new event types in order |
| `events/*.json` | Per-type positive envelopes |
| `payloads/*.json` | Payload-only positives |
| `resolution-example.json` | Integer resolution walkthrough |
| `expected-final-state.json` | world-state/1.0 projection |
| `strategic-state.json` | Contests/agreements/crimes/restrictions |
| `equivalence-boundary.json` | Replay boundary |
| `spectator-projections.json` | Public projections |
| `world-report.json` | BBS-style sections |
| `observatory-features.json` | OBSERVED feature counts |
| `negative/` | Invalid payloads / catalog isolation |

## Catalog

Validates against `specs/event-types.0.2.json`. Worlds on `event-catalog/0.1` MUST reject these types.
