# Contest Resolution (v0.2)

## Status

Normative algorithm for strategic contest outcomes under `contest-rules/0.2.0`.
Machine config: [`specs/contest-config.v02.json`](../specs/contest-config.v02.json).
Schema: [`specs/contest-config.schema.json`](../specs/contest-config.schema.json).

Changing any numeric constant requires a new `contest_rules_version`.

## Inputs

| Input | Source |
|-------|--------|
| `contest_form` | `CONTEST_DECLARED.payload.contest_form` |
| `declarer_stake` | reserved map on open contest |
| `defender_stake` | reserved via `COMMIT.CONTEST_DEFEND` (may be empty) |
| `infra_condition` | target entity `state.condition` if form is infrastructure-related; else 0 |
| `org_defense_support_millipoints` | sum of active `MUTUAL_DEFENSE` agreement supports for defender, capped |
| `seed_stream_id` | from declaration |
| form config | `contest-config.v02.json` → `forms[form]` |
| modifiers | `contest-config.v02.json` → `modifiers` |

## Arithmetic

All power and scores are **integers** (millipoints). No IEEE floats in the claim-bearing path.

### Stake power

For each resource `r` in stake map:

```text
power += stake[r] * weights_millipoints[r]
```

Missing weight keys contribute 0. Unknown resources in stake are rejected at declare/defend time.

- Declarer uses `stake_weights_millipoints`
- Defender uses `defense_weights_millipoints`

### Infrastructure modifier

```text
infra_mod = (infra_condition // infra_condition_divisor) * infra_condition_weight_millipoints
```

Applied as a **defender-favoring** offset: subtracted from declarer net when the target is infrastructure the defender protects; when no defender, still applied as environmental resistance (same formula).

Normative net score:

```text
score = declarer_power
      - defender_power
      - infra_mod
      - org_defense_support_millipoints
      + seed_perturbation
```

Where `org_defense_support_millipoints` is clamped to `[0, org_mutual_defense_cap_millipoints]` and **subtracted** from `score` (helps defender).

### Seed perturbation

With `seed_stream_rule = sha256_stream_u32_mod_1000`:

1. Compute `h = SHA256(seed_stream_id || ":" || contest_id || ":" || contest_rules_version)` as bytes.
2. Interpret first 4 bytes as big-endian `u32`.
3. `draw = u32 % 1000` → millipoints in `[0, 999]`.
4. Map to signed perturbation in `[-R, +R]` where `R = seed_perturbation_range_millipoints`:

```text
seed_perturbation = (draw % (2 * R + 1)) - R
```

Fixtures may pin `seed_draw_millipoints` only for documentation; implementations MUST recompute from the stream rule.

## Outcome thresholds

Using form thresholds from config:

| Condition | Outcome |
|-----------|---------|
| `score >= success_threshold_millipoints` | `SUCCESS` |
| `score >= partial_threshold_millipoints` | `PARTIAL_SUCCESS` |
| else | `FAILURE` |

Special outcomes (command layer, not score):

| Condition | Outcome |
|-----------|---------|
| Declarer aborts while OPEN | `ABORTED` |
| `cycle > expires_cycle` at resolve | `EXPIRED` |

## Defense model

v0.2 defense is **both**:

1. **Passive:** infrastructure condition and mutual-defense agreement millipoints enter the score.
2. **Active:** `COMMIT.CONTEST_DEFEND` reserves defender stake against an OPEN contest before resolve. No new event type. Settlement appears only on `CONTEST_RESOLVED.defender_stake_spent`.

Response deadline: `expires_cycle` of the contest. After expiry, resolve as `EXPIRED` without defense stake spend (release declarer residual).

## Resolution event

Command resolution computes outcome and emits, in order:

1. `CONTEST_RESOLVED` — closes contest, spends/releases stakes, records `score_millipoints` and `resolution_digest`
2. Zero or more follow-ons: `RESOURCE_TRANSFER`, `INFRASTRUCTURE_DISRUPTED`, `ACCESS_RESTRICTED`, `CRIME_DETECTED`, optional `MOVE`

`condition_delta_on_resolve` is **false**. Condition changes require `INFRASTRUCTURE_DISRUPTED`.

### resolution_digest

```text
resolution_digest = "sha256:" || hex(SHA256(
  contest_id || ":" ||
  outcome || ":" ||
  score_millipoints || ":" ||
  canonical_json(declarer_stake_spent) || ":" ||
  canonical_json(defender_stake_spent) || ":" ||
  seed_stream_id || ":" ||
  contest_rules_version
))
```

`canonical_json` = UTF-8 JSON with sorted keys and no insignificant whitespace.

## Resource seizure follow-on

On `SUCCESS` / `PARTIAL_SUCCESS` for `RESOURCE_SEIZURE`:

- Emit `RESOURCE_TRANSFER` for `min(max_seizure_amount, available, storage_capacity_remaining)`.
- Partial success uses `ceil(max_seizure_amount / 2)` before min with available.
- Never overdraft target. Never move holdings inside `CONTEST_RESOLVED`.

## Infrastructure disruption follow-on

On success: `condition_after = max(0, condition_before - max_condition_delta)`.
On partial: use `partial_condition_delta`.
On failure: no disruption event.

## Access contest follow-on

On success/partial: `ACCESS_RESTRICTED` with duration `restriction_duration_cycles` from resolve cycle.

## Presence pressure follow-on

On success: optional temporary disable ≤ `max_disable_cycles` via allowlisted agent state flag (recorded with `ENTITY_UPDATE` on agent entity if present) and/or forced `MOVE` to a valid adjacent exit chosen deterministically (lexicographically smallest open exit). If no valid exit: disable only. **Never** permanent removal.

## Worked example

See [`examples/v02-strategic-conflict/resolution-example.json`](../examples/v02-strategic-conflict/resolution-example.json).

With stakes energy 12 / influence 8 / compute 4 vs defense energy 10 / influence 14 / compute 4, infra 70, seed pert 17, form `INFRASTRUCTURE_DISRUPTION`:

```text
declarer_power = 12*45 + 8*40 + 4*15 = 920
defender_power = 10*25 + 14*45 + 4*15 = 940
infra_mod = (70//10)*5 = 35
score = 920 - 940 - 35 + 0 + 17 = -38
```

If fixture pins seed pert differently, recompute. The package fixture documents an integer path that yields `PARTIAL_SUCCESS` under the published thresholds when score is between partial and success bands; implementations must match config arithmetic exactly.

## Anti-grief

- Max open contests per agent / room from config
- Minimum stakes per form
- No permanent elimination
- Access restrictions expire by cycle
- Crime requires detection path
