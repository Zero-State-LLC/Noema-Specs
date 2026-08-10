# Partial Observability (v0.2)

Agent-facing uncertainty and world truth remain **separate domains**.

## Visibility classes

| Class | Meaning |
|-------|---------|
| `visible` | field present at full declared resolution |
| `hidden` | field absent; not inferable from this observation |
| `partial` | subset of fields / reduced resolution |
| `noisy` | value present with noise provenance |
| `stale` | value older than current cycle; `observed_at_cycle` &lt; current |
| `contradictory` | member of a contradiction_set |
| `permission_restricted` | redacted for authz |

## Observation field provenance (v0.2 extensions)

Where applicable, observation content fields SHOULD carry:

```text
source
observed_at_cycle
resolution          # full | reduced | minimal
quality_class       # clear | degraded | unreliable
noise_provenance    # noise_id / model version / stream
staleness_cycles    # integer ≥ 0
contradiction_set_id
redaction_reason
```

Machine examples: [`examples/v02-frontier/observations/`](../examples/v02-frontier/). Full observation envelope remains [observation.schema.json](../specs/observation.schema.json); provenance may nest under `content` or `provenance` extensions allowed by schema `additionalProperties` rules for content objects.

## Leak rule

Partial observability MUST NOT leak hidden world truth through errors, side channels, or spectator public projections.
