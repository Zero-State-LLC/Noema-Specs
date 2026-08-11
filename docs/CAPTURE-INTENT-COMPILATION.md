# Capture Intent Compilation

## Purpose

Define the deterministic mapping from ordinary **CAPTURE AS TEST** to a canonical [compilation request](../specs/compilation-request.schema.json).

The capture intent is an experience-layer convenience. It is **not** independent authority. Canonical Compiler semantics remain in [PHENOMENON-COMPILER.md](PHENOMENON-COMPILER.md).

## Ordinary action

```text
[ CAPTURE AS TEST ]
```

## Required source fields

From the referenced Lab Result and its lineage:

- `lab_result_id` with `compiler_readiness == READY`
- `experiment_id`, `source_candidate_ids`, claim label, confounds
- resolvable source trajectory + interval for the candidate behavior
- completed required control outcomes (or explicit blocking reason)
- authorized policy context (consent, retention, export class)

## Recommended defaults

Resolved from versioned [`capture-defaults.v05.json`](../specs/capture-defaults.v05.json):

| Field | Default identity |
|---|---|
| minimization strategy | `dependency-closed-hierarchical-ddmin/1` |
| oracle policy | `behavioral-oracle/0.5.0` |
| seed policy | `SOURCE_TRAJECTORY_SEED` |
| replication policy | `DECLARED_PLAN_BEFORE_COMPILE` |
| budget profile | `ordinary-capture/0.5.0` |
| generalization default | `SCENARIO_FAMILY` |
| visibility | `RESEARCH_ISOLATED` |

Defaults are inspectable. They MUST NOT be mutable hidden settings.

## Allowed overrides

Only fields listed in `allowed_override_fields` on the defaults document may be supplied via `user_overrides` on the capture intent (budget profile, seed policy, replication policy, generalization boundary, max oracle calls, export class). Overrides are claim-bearing and change compilation identity.

## Eligibility failures

If not eligible, do not compile. Return a simple state + machine reason code, for example:

| Condition | Simple | Reason |
|---|---|---|
| `compiler_readiness != READY` | Needs more evidence | `NOT_READY` / `CONTROL_REQUIRED` |
| missing trajectory/predicate | Cannot determine | `NOT_COMPUTABLE` |
| broken digests/lineage | Source evidence is invalid | `INVALID_EVIDENCE` |
| public export needs private evidence | Cannot create a public test | `PRIVACY_PARTITION` |

## Compiled output

`capture-intent` + defaults + Lab/trajectory evidence → `compilation-request/0.5` with stable `compile_id` and content digest under `noema-jcs/1`.

## Version identity

Changing any claim-bearing input (source, interval, target, boundary, units, graph, controls, perturbations, budgets, policy, compiler/oracle/replay/canonicalization versions, or defaults version) MUST yield a new compilation identity. See [COMPILATION-IDENTITY.md](COMPILATION-IDENTITY.md).

## Forbidden

Hidden LLM planning on the authoritative path. Optional assistive UI copy must not alter machine fields.
