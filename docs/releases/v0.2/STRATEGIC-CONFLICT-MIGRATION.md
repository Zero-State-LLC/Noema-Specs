# Migration: event-catalog/0.1 → event-catalog/0.2

## Rules

1. Historical 0.1 events remain valid and immutable.
2. No historical event is rewritten or retyped.
3. Existing snapshots retain their original `catalog_version` pin.
4. A world MUST explicitly migrate (or be created with 0.2) before accepting the seven new types.
5. Migration records new catalog identity on the world/runtime manifest.
6. Downgrade to 0.1 MUST fail if any 0.2-only event exists in the ledger, unless replay is intentionally pinned to a prior snapshot/history boundary that predates those events.

## New version domains

| Domain | Value |
|--------|-------|
| Event catalog | `event-catalog/0.2` |
| Contest rules | `contest-rules/0.2.0` |
| Agreement rules | `agreement-rules/0.2.0` |

## Runtime manifest

Running worlds SHOULD expose:

```text
event_catalog_version
contest_rules_version   # when contestation enabled
agreement_rules_version # when formal agreements enabled
```

See [runtime-manifest.schema.json](../../../specs/runtime-manifest.schema.json) extensions / deployment docs.

## Feature gate

Contestation is opt-in. Chamber v0.1 acceptance remains on `event-catalog/0.1` only.
