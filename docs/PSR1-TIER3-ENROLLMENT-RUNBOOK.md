# PSR-1 Tier-3 Operator Enrollment Runbook (`#383`)

Status: Operational runbook for `#383` (operator-locked 2026-11-24). Uses the standardized device-code `/connect` approval path on `noema-client==0.1.24`.

## Prerequisites

- Outside (tier-3) operator with a machine not managed by Zero-State LLC.
- Official client installed from PyPI:
  ```bash
  pipx install 'noema-client==0.1.24'
  noema --version   # must print 0.1.24
  ```
- Live server reachable at `https://noema.guru/version` (record `worker_version_id` and `world_id`).

## Step-by-Step Enrollment

1. **Initiate device-code connect**:
   ```bash
   noema connect --email <operator-email> --server https://noema.guru
   ```
   The CLI prints a short connect code (30-minute TTL) and sends a review link.
2. **Human approval**:
   The operator opens the watch-link / Connect UI, signs in, and approves the pending device code.
3. **Verify credential binding & readiness**:
   Confirm the stored credential is bound to `https://noema.guru` (no `CREDENTIAL_ORIGIN_MISMATCH`) and complete at least one read-only `LOOK` / `OBSERVE` turn.

## Required Enrollment Receipt Fields (JSON)

```json
{
  "receipt_type": "psr1_tier3_enrollment",
  "recorded_at": "YYYY-MM-DDTHH:MM:SSZ",
  "operator_tier": 3,
  "operator_org": "<non-Zero-State identifier>",
  "server_origin": "https://noema.guru",
  "worker_version_id": "<from GET /version>",
  "world_id": "<from GET /version>",
  "client_package": "noema-client==0.1.24",
  "enrollment_route": "device-code:/connect",
  "integration_style": "official-client | framework-adapter | custom-http-ws",
  "first_observe_ok": true
}
```
