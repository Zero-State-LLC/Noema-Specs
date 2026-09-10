# Living Civilization Alpha — Evidence-Pack Structure

**Status:** docs-only hygiene companion. It changes no gate criterion, protocol field, schema, or verdict. It records the link structure the existing Gate B–E packs already use so later packs stay traceable and fail-closed.
**Authority:** [Living Civilization Alpha Acceptance](LIVING-ALPHA-ACCEPTANCE.md) § Extension Points (evidence-pack structure) · [DIRECTION-AUTHORITY.md](DIRECTION-AUTHORITY.md) § Extension Points (machine-checkable links)
**Companions:** [LCA-GATE-C-SCENARIO.md](LCA-GATE-C-SCENARIO.md) · [LCA-GATE-D-SCENARIO.md](LCA-GATE-D-SCENARIO.md) · [LCA-GATE-E-SCENARIO.md](LCA-GATE-E-SCENARIO.md) · [LCA-GATE-F-SCENARIO.md](LCA-GATE-F-SCENARIO.md)
**Derived from (OBSERVED):** Noema `docs/evidence/gate-b-2026-09-08/`, `gate-c-2026-09-08/`, `gate-d-2026-09-08/`, `gate-e-2026-09-09/`; Noema `docs/ISOLATED-ROLLBACK-REHEARSAL-555-EVIDENCE.json`; Specs promotion records for Gates A–D

Document existence promotes nothing. A pack that follows this structure is not thereby PASS.

## Purpose

Every claim in a gate packet must be traceable along one chain:

```text
candidate ─ pins ─ heads ─ receipts ─ WATCH digest ─ verdict
                   └─ intervention log (crosses every link)
```

Each link carries an identity key and a claim label. A break in the chain is marked `NOT_COMPUTABLE`; it is never bridged by inference, interpolation, or a later file rewriting an earlier one.

## Labels

Claim labels (per [DIRECTION-AUTHORITY.md](DIRECTION-AUTHORITY.md)): **OBSERVED** (read from a live surface, a merged PR, a workflow run, or a retained receipt) · **INFERRED** (derived; derivation shown) · **SPECULATIVE** (marked as such) · **NOT_COMPUTABLE** (no probe exists or the probe was not run; who holds the answer is named).

Row states already in use across the packs, kept exactly:

| State | Meaning |
|---|---|
| `DECLARED` | Written down before the window; a plan, budget, or bound |
| `PLANNED` / `SCHEDULED_NOT_FIRED` | Future action named; not yet executed |
| `RUNNING` | Window open; start receipt only |
| `FIRED_OK` | Action executed and its receipt is OBSERVED |
| `PASS` / `FAIL` / `NOT_COMPUTABLE` | Verdict on one slice or on the conjunctive whole |
| `HOLD` | Verdict withheld pending a named human-yes or unify |
| `HISTORICAL` | True at an earlier bind; not current live |
| `SUPERSEDED` | Replaced for a stated scope by a later row; retained |
| `WAIVED` | Requirement set aside by recorded human-yes; not invented |

Rules:

- A label is set by the file that first records the fact. A later file may add a **Closed by** row that points at the newer file; it does not edit the earlier label in place.
- `HISTORICAL` and `SUPERSEDED` rows stay in the pack. Deleting them is a rewrite.
- Receipts are not verdicts. A `FIRED_OK` recover receipt does not make Phase B `PASS`.
- A zero-population, un-sampled, or un-run item is `NOT_COMPUTABLE`, never "expected".

## Pack layout

Runtime evidence lives in Noema `docs/evidence/gate-<x>-<YYYY-MM-DD>/`. Specs holds the promotion record `docs/LCA-GATE-<X>-PROMOTION-<YYYY-MM-DD>.md` and flips campaign state only on recorded human-yes.

Required in every Noema pack:

| File | Role | Present in |
|---|---|---|
| `INDEX.md` | Banner (NOT COMPLETE until promoted), **Files** table, OBSERVED pins, gate checklist (unchecked until OBSERVED), **Still-open shortlist (do not invent)**, **Explicit non-claims** | B, C, D, E |
| `candidate-declaration.md` | Immutable pin bind at Prep; run fields `TBD` / `NOT_COMPUTABLE` until observed | C, D, E |
| receipts | One file per observed action: start/end, remint, recover, probe, blind score | B, C, D, E |
| `intervention-log.md` | Every operator action in or around the window | E (required by E and F companions) |
| `repin-<date>.md` | Re-pin when live `/version` moves after Prep; lineage table; historical rows retained | E |
| digest file | WATCH capture or cohort digests with method | B, D |

Optional: `runbook.md`, scoring sheets, notes that explain a surface (for example the `/v1/watch/live` `controllers` default note in the Gate E pack).

## Link structure

### candidate ↔ tracking ↔ companion

| Key | Source of truth | Rule |
|---|---|---|
| `candidate_id` | Specs companion "Suggested candidate" | Naming ladder B=`lca2` … F=`lca6`; Danny may lock a different id, recorded in the companion |
| Tracking issue | Noema declaration issue (for example Noema #682 for Gate E) | One issue per candidate; stays OPEN until the Specs promotion merges; never invented |
| Companion | `docs/LCA-GATE-<X>-SCENARIO.md` | The pack copies the companion checklist **unchecked**; it does not add bullets |

### candidate ↔ pins

| Pin | Source of truth | Rule |
|---|---|---|
| `worker_version_id`, `deployed_at` | `GET https://noema.guru/version` | `/version` wins over `spec-compat.json`, `current-state.v1.yaml`, and any prior pack |
| Source commit | Deploy workflow run `headSha` | Cite the run id; a pin PR body alone is not the source of truth |
| Pin PR + merge SHA | Noema generated post-deploy pin PR | Required for every production publish; a bare `wrangler deploy` is a defect |
| `specs_git` / `production_implements_specs` | Noema `spec-compat.json` `hosted_live.specs_git` mirrored in `current-state.v1.yaml` | A new Worker id does not imply a Specs pin change |
| Official-client pin | `hosted_live.official_client` | Record the OBSERVED Controller version beside it when they differ; do not flip the pin by observation |
| `world_id` / `genesis_id` / seal / room bound | `/ready` + `spec-compat.json` | Campaign pins; unchanged unless a Gate F `WORLD_CUTOVER` packet says otherwise |

Every Worker id that appears in a pack carries one of: current (OBSERVED at a stated time), `HISTORICAL`, or `SUPERSEDED`. When live moves mid-candidate, add a re-pin file with a lineage table (Deploy time, source PR, Worker, pin PR) and leave the Prep bind untouched.

### pins ↔ heads

Every head sample records all of:

```text
cycle / sequence            # the pair, never one alone
surface                     # /ready | /v1/watch/live | /v1/watch/map | Admin overview
                            #   (Admin overview adds head_revision / head_sequence / head_cycle / do_ne_head)
wall_clock_utc              # ISO-8601 Z
worker_version_id           # at the sample, from /version in the same probe
label                       # OBSERVED; a range is two samples, not one
```

Rules:

- Public `/ready` reports the Durable Object sequence; Admin overview reports the durable head. When they differ, record both and the `do_ne_head` / `mismatch` string. Do not pick the prettier number.
- Heads at a Deploy instant that were not sampled are `NOT_COMPUTABLE`. Monotonic public heads across a lineage are evidence of continuity, not a per-Deploy census.
- A phase window is `started_at`, `ends_at` (DECLARED), start heads (OBSERVED), end heads (OBSERVED at a stated check time with its lag after `ends_at`).

### heads ↔ receipts

**Recovery receipt (Path 8 style).** The existing Admin lifecycle JSON is the receipt. Its OBSERVED keys are `ok`, `status`, `settlement_health`, `revision`, `recover_mode`, `head_present`, `reason`, `operator_session`. A dedicated recovery-receipt schema remains `NOT_COMPUTABLE` and is not invented. Every recover receipt is bracketed:

```text
PRE   heads + head_revision (Admin overview) + /ready status
INCIDENT JSON (OBSERVED)                       # reason names the candidate drill
RECOVER JSON (OBSERVED)                        # revision compared to PRE head_revision
POST  heads (immediate /ready) + Admin overview moments later
```

If two captures of the same drill exist (for example operator and Admin), file both, name which one the packet uses, and do not merge them into one synthetic receipt.

**Controller receipts.** Keyed by `controller_id` **and** the Worker id the binding was observed on. Fields: device user code (redacted where the operator receipt omits it), `player_id`, `approver_amr`, `independent_control_receipt`, `controller_binding_digest`. A remint produces a new cohort row set; the prior set is `SUPERSEDED` for subsequent observe and stays in the pack. Two cohorts are never summed into one census.

**Census.** `/ready` `players` and `/v1/watch/live` `players_present` are weak public counts; `/v1/watch/live` `controllers` is a reconstruction default, not a trio census. A Controller census comes from Admin rows or Controller logs. Absent those, the census is `NOT_COMPUTABLE`.

### receipts ↔ WATCH digest

A digest file declares, in order:

1. capture wall-clock (start, end), Worker id from `/version` in the same window;
2. URLs and HTTP status per surface (`/v1/watch/live`, `/v1/watch/map`, HTML presence only as UX, never as digest ground);
3. heads at capture (single snapshot: start = end, stated);
4. pin side-by-side against the candidate declaration;
5. **method:** input material is the retained, redacted JSON, canonicalized with `json.dumps(obj, sort_keys=True, separators=(",", ":"))` as UTF-8, then SHA-256 hex. Raw material is not committed; the file states where the operator retains it;
6. digest values as opaque bindings (`<name>_evidence_digest` or a bound `sha256:` prefix), never presented as server fields;
7. redaction, exclusion, incident, and stale marks (private MESSAGE, `PLAYER_PRIVATE`, tokens absent; forbidden sources not used);
8. operator actions and external inputs during the window.

A digest that cannot be recomputed from stated material by a second operator is `NOT_COMPUTABLE`. The optional `acceptance_authority_digest` in a Specs promotion is SHA-256 over the canonical OBSERVED evidence-authority JSON of that promotion and is likewise opaque.

### digest ↔ verdict

- Verdict rows cite a file and section for every input. A verdict without a cited receipt is `NOT_COMPUTABLE`.
- Gate verdicts are conjunctive over the companion checklist. A slice `PASS` is recorded as a slice, never promoted to the whole.
- A later `PASS` closes an earlier `BLOCKED` / `FAIL` / `NOT_COMPUTABLE` only through a **Closed by** row in `INDEX.md` that names the closing file. The earlier row remains.
- Specs promotion cites the Noema pack, PR merge SHAs, Deploy run, live pins, human-yes, and the tracking issue. The campaign flip is a separate human-yes from the runtime PASS.

### intervention log ↔ every link

Rows use the closed classes `CONTROL_PLANE` / `WORLD_OPERATION` / `EXTERNAL_INPUT` / `RECOVERY` ([OPERATOR-INTERVENTIONS.md](OPERATOR-INTERVENTIONS.md)). Each row records: time (UTC), class, source (PR, run, session class), Worker before and after where a publish occurred, heads at the instant or `NOT_COMPUTABLE`, reason, and whether the row sits inside a declared budget (`NOT_COMPUTABLE` when the budget was not declared at Prep). Production Deploys inside a live window are `CONTROL_PLANE` rows even when they change only presentation. Remints are operator rows, not recovery drills.

## Proposed machine-readable index (optional; not a protocol field)

A pack MAY add `evidence-index.v1.yaml` beside `INDEX.md` so a reviewer can walk the chain without parsing prose. It is a documentation artifact: not a server field, not a public schema, not validated by this repository yet. Every entry carries `label` and `source` (a path or URL inside the pack or a merged PR / run).

```yaml
schema_version: noema-evidence-index/1
candidate_id: lca5-gate-e-endurance
tracking: https://github.com/Zero-State-LLC/Noema/issues/682
companion: Noema-Specs docs/LCA-GATE-E-SCENARIO.md
pins:
  - { worker_version_id: "…", deployed_at: "…Z", source_commit: "…", deploy_run: "…", pin_pr: "…", state: current|HISTORICAL|SUPERSEDED, label: OBSERVED, source: repin-….md }
heads:
  - { at: "…Z", cycle: 0, sequence: 0, surface: /ready, worker_version_id: "…", label: OBSERVED, source: phase-b-start.md }
controllers:
  - { slot: controller-a, controller_id: "…", worker_version_id: "…", state: current|SUPERSEDED, label: OBSERVED, source: phase-b-remint4.md }
receipts:
  - { kind: recover, pre: {…}, incident: {…}, recover: {…}, post: {…}, label: OBSERVED, source: phase-b-path8.md }
digests:
  - { name: watch_digest, value: "sha256:…", method: canonical-json-sha256, heads: {…}, label: OBSERVED, source: watch-digest.md }
interventions:
  - { at: "…Z", class: CONTROL_PLANE, source: "Noema#700", worker_after: "…", heads: NOT_COMPUTABLE, in_budget: NOT_COMPUTABLE }
verdicts:
  - { slice: phase_a_overall, verdict: NOT_COMPUTABLE, source: phase-a-end.md }
  - { slice: gate, verdict: NOT_COMPUTABLE, source: INDEX.md }
```

Adopting the index does not change any verdict. A validator for it is future work and is not implied by this file.

## Fail-closed checklist

Before a pack is cited by a Specs promotion:

- [ ] every Worker id is current, `HISTORICAL`, or `SUPERSEDED`, and `/version` at decision time is cited;
- [ ] every head is a (cycle, sequence, surface, UTC, Worker) tuple; un-sampled Deploy heads are `NOT_COMPUTABLE`;
- [ ] every recover receipt is the existing Admin JSON, bracketed PRE / INCIDENT / RECOVER / POST; dual captures are kept apart;
- [ ] every Controller row is keyed by `controller_id` + Worker id; remint cohorts are not summed;
- [ ] the census source is Admin rows or Controller logs, or the census is `NOT_COMPUTABLE`;
- [ ] every digest states method, input material, retention location, and heads at capture;
- [ ] every verdict cites a file and section; slice verdicts stay slices;
- [ ] every upgrade is a **Closed by** row, not an in-place edit;
- [ ] the intervention log covers every publish, remint, and recover in or around the window, with budget adjudication or `NOT_COMPUTABLE`;
- [ ] **Explicit non-claims** and **Still-open shortlist (do not invent)** are present and current;
- [ ] no tokens, `credential.json`, Authorization headers, private MESSAGE text, or device secrets appear anywhere in the pack.

Silence on any row above is a gap, not a pass.

## Worked cross-reference (OBSERVED, Gate E pack as of 2026-09-10)

Recorded to show the structure against a real pack; no verdict is changed here.

| Link | Present | Gap (labeled in the pack) |
|---|---|---|
| candidate ↔ tracking ↔ companion | `candidate-declaration.md`, Noema #682, Specs companion | — |
| candidate ↔ pins | Prep bind + `repin-2026-09-10.md` lineage (eight publishes; `HISTORICAL` rows retained) | — |
| pins ↔ heads | start/end receipts carry (cycle, sequence, surface, UTC, Worker) | heads at each Deploy instant `NOT_COMPUTABLE` |
| heads ↔ receipts | `phase-b-path8.md` bracketed PRE / INCIDENT / RECOVER / POST; dual fire kept apart; remint cohorts `SUPERSEDED` in sequence | census from public surfaces `NOT_COMPUTABLE` (`controllers-watch-live-note.md`) |
| receipts ↔ digest | — | Gate E WATCH digest not yet filed at authoring |
| digest ↔ verdict | Phase A overall `NOT_COMPUTABLE` recorded, not upgraded by Phase B start | end score pending; Phase B opened without Phase A `PASS` is a companion condition the score must address |
| intervention log | CONTROL_PLANE rows for #684/#686 and #688–#700; remints; recover | budget `NOT_COMPUTABLE` (not declared at Prep) |

## Explicit non-claims

- No gate criterion, verdict, or campaign state changes because this file exists.
- No new protocol field, schema, or server-returned digest. The index is a documentation artifact.
- Dedicated recovery-receipt objects remain `NOT_COMPUTABLE` (not invented).
- Gate E and Gate F remain unproven.

## Extension Points

Non-normative.

- **Validator:** a Specs check that walks `evidence-index.v1.yaml` and confirms every `source` resolves and every `label` is in the vocabulary. It must not compute a verdict.
- **Cross-gate reuse:** a later gate cites an earlier pack by path and merge SHA; it does not copy rows forward without their `HISTORICAL` label.
- **Preserved invariants:** `/version` wins; receipts are not verdicts; upgrades are **Closed by** rows; nothing is invented to fill a gap.
