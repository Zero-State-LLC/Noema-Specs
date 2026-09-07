# Noise Model (v0.2)

Version domain: `noise-model/0.2`.
Catalog: [`specs/noise-model.v02.json`](../specs/noise-model.v02.json).

Noise is **deterministic and replayable**. Unrecorded randomness is forbidden.

## Closed operators

| noise_model_id | effect |
|----------------|--------|
| `omission` | drop optional field |
| `quantization` | quantize numeric to step |
| `delay_staleness` | set observed_at_cycle older |
| `bounded_perturbation` | add signed millipoint delta in bounds |
| `source_corruption` | mark source identity degraded |

## Application record

```text
noise_model_id
version
seed_stream
target_field_path
parameters
source_event_id
result_digest
```

Ledgered as `NOISE_APPLIED` when observation pipeline applies noise ([EVENT-CATALOG.md](EVENT-CATALOG.md)).

## World vs observation

Noise MUST NOT alter canonical WorldState unless the world contains a **canonical noisy signal entity/event**. Default: noise affects **observation projection only**.

## Extension Points

Non-normative future guidance; no new behavioral authority or reopening of accepted/deferred slices.

- **Document-specific seam:** Expand deterministic operator fixtures at optional-field, quantization, staleness, and perturbation boundaries.
- **Invariants, compatibility, promotion, and verification:** Keep the closed noise-model/0.2 operators, recorded seed streams, NOISE_APPLIED lineage, and observation-only default. New operators require a versioned catalog and migration rules; verify replayed result_digest, bounded parameters, and unchanged WorldState absent an explicitly canonical noisy-signal contract.
