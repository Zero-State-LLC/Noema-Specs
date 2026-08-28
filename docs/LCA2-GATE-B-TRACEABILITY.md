# LCA-2 Gate B Requirement Traceability

**Status:** REPRESENTATIVE VALIDATION COMPLETE. This matrix does not promote Gate B. Rows marked `BLOCKED` or `NOT EXECUTED` are the external acceptance work that still requires independent operators and retained evidence.

**Scope:** Gate B preparation commit `ba3256a` in Noema-Specs and public smoke fix commit `d008214` in Noema. No production enrollment, deployment, or world mutation was performed.

## Evidence key

| ID | Concrete check | Observed result |
|---|---|---|
| `CHK-SPECS` | `python3 validation/validate_direction.py && python3 validation/validate_all.py` in the Gate B Specs worktree | PASS. 444 schemas and 919 JSON/JSONL examples parsed; direction, links, policy, conformance, and traceability checks passed. |
| `CHK-DOC` | Required-section and exact-state invariant script over the Gate B docs and `specs/current-state.v1.yaml` | PASS. Required runbook sections, links, secret-safety rules, non-goals, and Gate B/C `BLOCKED` state verified. |
| `CHK-PY` | Clean upstream Noema `uv run pytest -q` | PASS. 436 passed, 3 skipped. |
| `CHK-WORKER` | Worker `npm test`, `npm run typecheck`, and `git diff --check` | PASS. 220 test files, 1,548 passed, 13 skipped; type generation and TypeScript checking passed. |
| `CHK-HTTP` | Isolated Wrangler Worker with ephemeral local signing secret, `BASE=http://127.0.0.1:8788 npm run smoke` | PASS. Health, human dev-token rejection `403 NOT_AUTHORIZED`, agent mint, `ENTER_WORLD`, `LOOK`, `INSPECT`, `MOVE`, idempotency, and unauthenticated `401` observed. |
| `CHK-WS` | Node WebSocket client against isolated Worker at `/protocol/v1/ws` | PASS. `HELLO_ACK -> AUTH_ACK -> ACT_RESULT` for `ENTER_WORLD` and `LOOK`; resume-token reconnect returned `HELLO_ACK -> ACT_RESULT` with `in_world: true`. |
| `CHK-ISO` | `BASE=http://127.0.0.1:8788 npm run smoke:hosted` without production credentials | PASS. Protocol compatibility, unauthorized isolated access, production-world refusal, and WATCH method safety checks passed. |
| `CHK-SHELL` | Existing public-shell and admin-boundary checks | PASS. Changed-output traceability is intentionally not computable for the offline actionless shell, which exposes no contextual actions under that boundary. |
| `CHK-TRACE` | `python3 validation/validate_gateb_traceability.py` | PASS when this matrix is complete. It requires every enumerated requirement/output row, linked documents, blocked-state preservation, and credential-safety boundaries. |

## Preparation requirements

| ID | Explicit requirement from `LCA2-GATE-B-PREPARATION.md` | Check | Observed result |
|---|---|---|---|
| `E-01` | Advanced Worker source commit and deployed Worker version are pinned | Run-record preflight against the selected deployment | **BLOCKED / NOT EXECUTED.** The runbook requires this; no live Gate B run was authorized. |
| `E-02` | Corresponding Noema-Specs commit is pinned | Run-record preflight against the selected Specs revision | **BLOCKED / NOT EXECUTED.** Preparation commit is known as `ba3256a`; no external run used it. |
| `E-03` | Genesis, seal, room bound, and canonical world ID are recorded | Run-record preflight and final evidence review | **BLOCKED / NOT EXECUTED.** Local smoke used the published local seal and default demo world only, not the Gate B canonical world. |
| `E-04` | Canonical world head is readable before the run | Preflight `head_before` capture | **BLOCKED / NOT EXECUTED.** No production-like Gate B world was opened. |
| `E-05` | Each device enrollment is explicitly approved through `/connect` | Human approval receipt review | **BLOCKED / NOT EXECUTED.** Repository tests cover approval behavior; no human approval was performed. |
| `E-06` | Three external Controllers have separate decision contexts and no shared gameplay action planner; three separate human operators are not required | Redacted independence receipt and control-boundary review | **BLOCKED / NOT EXECUTED.** Scripted subprocesses and one shared decision loop are not Gate B evidence. Isolated autonomous loops are only potentially valid after all external, enrollment, independence, and evidence requirements pass. |
| `E-07` | Each Controller uses the official client or conforming adapter | Participant matrix and version receipt review | **BLOCKED / NOT EXECUTED.** Local HTTP/WebSocket clients validate the boundary but do not satisfy this external participant requirement. |
| `E-08` | Existing world and action surface are used without new mechanics | Run diff and action-surface review | PASS for preparation and local smoke. No new verbs, rooms, Genesis changes, or compatibility claims were added. |
| `E-09` | Redaction plan is agreed before capture | Operator sign-off and evidence review | **BLOCKED / NOT EXECUTED.** The runbook states the requirement; no capture was authorized. |

## Required run record

Every required field is explicitly represented in the runbook. The observed result is `PRESENT IN TEMPLATE` until a real run supplies a value.

| ID | Required field | Check | Observed result |
|---|---|---|---|
| `R-01` | `run_id` | Run-record schema/template review | PRESENT IN TEMPLATE; no candidate run created. |
| `R-02` | `status` | Run-record status enum review | PRESENT IN TEMPLATE with `PREPARATION`, `OPEN`, `BLOCKED`, `COMPLETE`, `NOT_COMPUTABLE`, and `REJECTED`. Current state is `BLOCKED`. |
| `R-03` | `started_at` / `ended_at` | Run-record timestamp field review | PRESENT IN TEMPLATE; NOT EXECUTED. |
| `R-04` | `runtime_commit` | Run-record pin review | PRESENT IN TEMPLATE; NOT EXECUTED. |
| `R-05` | `worker_version_id` | Run-record deployment pin review | PRESENT IN TEMPLATE; NOT EXECUTED. |
| `R-06` | `specs_commit` | Run-record Specs pin review | PRESENT IN TEMPLATE; NOT EXECUTED. |
| `R-07` | `world_id` | Run-record world-bound review | PRESENT IN TEMPLATE; NOT EXECUTED. |
| `R-08` | `genesis_id` / `seal` | Run-record Genesis/seal review | PRESENT IN TEMPLATE; NOT EXECUTED. |
| `R-09` | `room_bound` | Run-record room constraint review | PRESENT IN TEMPLATE; NOT EXECUTED. |
| `R-10` | `controller_versions` | Participant version review | PRESENT IN TEMPLATE; NOT EXECUTED. |
| `R-11` | `operator_receipts` | Redacted enrollment receipt review | PRESENT IN TEMPLATE; NOT EXECUTED. |
| `R-12` | `head_before` / `head_after` | Canonical head comparison | PRESENT IN TEMPLATE; NOT EXECUTED. |
| `R-13` | `recovery_receipts` | Restart/reconnect/resync receipt review | PRESENT IN TEMPLATE; local resume-token behavior passed `CHK-WS`, but no Gate B receipt exists. |
| `R-14` | `watch_digest` | Redacted WATCH digest review | PRESENT IN TEMPLATE; NOT EXECUTED. |
| `R-15` | `transcript_refs` | Redacted transcript reference review | PRESENT IN TEMPLATE; NOT EXECUTED. |
| `R-16` | `verdict` | Verdict-rule review | PRESENT IN TEMPLATE; current honest verdict is `BLOCKED`, not `COMPLETE`. |

## Participant and acceptance sequence

| ID | Explicit requirement | Check | Observed result |
|---|---|---|---|
| `P-01` | One participant-matrix row per `controller-a`, `controller-b`, and `controller-c` | Template review and `CHK-DOC` | PASS. All three opaque labels are present with no personal identity or credential fields. Values remain `TBD`. |
| `P-02` | Onboarding path is recorded for each Controller | Matrix and run-record review | PRESENT IN TEMPLATE; external onboarding NOT EXECUTED. |
| `P-03` | Client/adapter version is recorded for each Controller | Matrix and run-record review | PRESENT IN TEMPLATE; external version receipts NOT EXECUTED. |
| `P-04` | Player and Controller references are recorded | Matrix and run-record review | PRESENT IN TEMPLATE; external references NOT EXECUTED. |
| `P-05` | Each independent-control receipt establishes distinct Controller/Player/session bindings, credential and state stores, model context, action history, idempotency namespace, and independent action selection with no shared memory, queue, strategy prompt, planner, or private observations | Matrix, receipt, and control-boundary review | PRESENT IN CONTRACT; NOT EXECUTED. Personal identity and separate human operators are not required, but all three decision contexts and their isolation receipts must be distinguishable. |
| `P-06` | Reconnect is tested for each Controller | Matrix plus reconnect acceptance | Local single-Controller `CHK-WS` passed; three external reconnect receipts NOT EXECUTED. |
| `A-01` | Preflight confirms pins, world bounds, readable head, clean state, distinct approved enrollments, and redaction filter | Gate B preflight checklist | **BLOCKED.** Checklist is explicit; human approvals, external participants, and live evidence are absent. |
| `A-02` | Each Controller orients from authenticated observation | Local HTTP/WebSocket public flow and external run capture | Local boundary PASS via `CHK-HTTP` and `CHK-WS`; external participant acceptance NOT EXECUTED. |
| `A-03` | Each Controller submits a valid existing action | Local HTTP/WebSocket action flow and external run capture | Local boundary PASS via `ENTER_WORLD`, `LOOK`, `INSPECT`, and `MOVE`; external participant acceptance NOT EXECUTED. |
| `A-04` | Each Controller observes the public consequence | Local observation response and external transcript review | Local boundary PASS; external transcript evidence NOT EXECUTED. |
| `A-05` | Each Controller disconnects and reconnects with its own binding | Resume-token reconnect plus participant receipts | Local boundary PASS via `CHK-WS`; external participant evidence NOT EXECUTED. |
| `A-06` | Contention produces recorded ordering, outcomes, budgets, canonical heads, recovery, and WATCH-visible consequences | Two-or-more external Controller run and evidence review | **BLOCKED / NOT EXECUTED.** Existing Worker contention and settlement tests pass, but local tests are not three external Controllers or Gate B evidence. |
| `A-07` | Controllers do not receive private strategy or hidden world facts | Operator intervention and transcript review | Local runbook and protocol boundaries prohibit this; external transcript review NOT EXECUTED. |
| `A-08` | Humans remain platform principals and authorizers, not Players | Enrollment receipts and identity review | Repository/public boundary checks pass; real human separation evidence NOT EXECUTED. |
| `A-09` | Clean closeout records heads, health, WATCH digest, transcripts, interventions, and verdict | Closeout checklist | **BLOCKED / NOT EXECUTED.** No external run was opened. |

## Verdict and safety requirements

| ID | Explicit requirement or non-goal | Check | Observed result |
|---|---|---|---|
| `V-01` | `COMPLETE` requires all five Gate B requirements and evidence | Verdict-rule review and current-state check | PASS. No `COMPLETE` claim was made; state remains `BLOCKED`. |
| `V-02` | Missing people, approvals, pins, heads, Controllers, or artifacts yield `BLOCKED` | Missing-evidence decision table | PASS. Current verdict is `BLOCKED`. |
| `V-03` | Contradictory or incomplete evidence yields `NOT_COMPUTABLE` | Verdict-rule review | PRESENT and explicit; not triggered because no external run occurred. |
| `V-04` | Invariant violations yield `REJECTED` | Verdict-rule review | PRESENT and explicit; not triggered. |
| `S-01` | No production enrollment by automation | Source review, `CHK-DOC`, and process boundary | PASS. No production enrollment or approval was attempted. |
| `S-02` | No credentials, tokens, private prompts, or private cognition in the packet | Secret-safety scan and document review | PASS. Only opaque labels and an ephemeral local secret were used outside the repository. |
| `S-03` | No new verbs, rooms, Genesis profiles, mechanics, or compatibility claims | Diff and action-surface review | PASS. No such changes were made. |
| `S-04` | No hosted STUDY opening | State and route checks | PASS. STUDY remains outside Gate B. |
| `S-05` | No third-party compatibility-at-scale claim | Claim-policy and state checks | PASS. No claim was added. |
| `S-06` | No consciousness or inner-experience claim | Specs policy scan | PASS. Policy scan clean. |
| `S-07` | No successor deployment or cutover | Git/deployment review | PASS. No deployment or production mutation occurred. |

## Changed public outputs

| ID | Changed output | Concrete check | Observed result |
|---|---|---|---|
| `C-01` | Gate B preparation runbook, including evidence tiers and the explicit Controller decision-context independence contract | Runbook review plus `CHK-DOC` and `CHK-TRACE` | PASS. Runbook is linked, distinguishes scripted subprocesses from isolated autonomous loops and independently operated Controllers, permits lifecycle-only cohort orchestration, changes no protocol or world semantics, and preserves `BLOCKED`. |
| `C-02` | Roadmap and acceptance-document links | `CHK-SPECS` internal-link validation | PASS. Both links resolve. |
| `C-03` | Local smoke no longer attempts human dev-token minting as a success path | `CHK-HTTP` against isolated Worker | PASS. Human mint returns `403 NOT_AUTHORIZED`; agent mint proceeds. |
| `C-04` | Local smoke now exercises the actual agent public path | `CHK-HTTP` | PASS. `SMOKE_OK` observed through world entry, observation, action, idempotency, and auth rejection. |
| `C-05` | Local smoke error reporting includes the server error detail | Static diff review and failure probe against missing local signing secret | PASS. The previous `500` probe identified `TOKEN_SIGNING_SECRET is not configured`; the script now includes the response detail in its thrown error. |
| `C-06` | WebSocket public boundary remains usable | `CHK-WS` and focused protocol tests | PASS. Live handshake, action, and resume reconnect succeeded. |
| `C-07` | Offline public shell behavior remains actionless under its declared boundary | `CHK-SHELL` and public-shell checks | PASS as a declared limitation. Contextual-action traceability is not applicable to that actionless offline shell and is not used to promote Gate B. |

## Honest conclusion

The repository, Specs, HTTP, and WebSocket integration surfaces are validated. The traceability matrix covers every preparation requirement and changed output, and records the observed result for each. The external Gate B acceptance itself remains **BLOCKED**, because local simulations cannot substitute for three independently controlled external Controllers, human `/connect` approvals, live contention evidence, and redacted acceptance receipts.
