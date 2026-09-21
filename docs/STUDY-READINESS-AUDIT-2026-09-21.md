# STUDY readiness audit (post Gate F COMPLETE)

**Status:** docs-only audit draft for Danny review. Does **not** reopen hosted STUDY. Does **not** Deploy. Does **not** invent STUDY acceptance criteria.
**Danny yes context:** option 1 (readiness audit).
**Probe:** 2026-09-20 ~19:44 PDT · live Worker matches Gate F COMPLETE pin (`1e52e827…`).
**Local pack (executor):** `INDEX.md` / `GAPS.md` / `RECOMMEND.md` under agent out dir `noema-study-readiness-2026-09-20/`.
**Tracking note:** comment filed on closed [Noema #715](https://github.com/Zero-State-LLC/Noema/issues/715) (Gate F). No open STUDY issue existed at audit time.

## Hard walls

| Wall | Honored |
|---|---|
| No Deploy | yes |
| No STUDY reopen / campaign flip | yes |
| No WORLD_CUTOVER | yes |
| No inventing STUDY criteria | yes — cites Specs/Noema/live only |
| Gate F COMPLETE ≠ STUDY | explicit |
| Deploy already live ≠ STUDY | explicit |

## Explicit non-equivalence

- **Gate F COMPLETE** ([LCA-GATE-F-PROMOTION-2026-09-21.md](LCA-GATE-F-PROMOTION-2026-09-21.md)) proves the successor **decision packet**. It does **not** open hosted STUDY (`surfaces.study_hosted: BLOCKED` retained; `validation/validate_direction.py` asserts BLOCKED after Gate F).
- **Deploy already live** (Worker `1e52e827-695c-4386-9795-d42b175ec166` / source `65086d32` / Deploy [35549259561](https://github.com/Zero-State-LLC/Noema/actions/runs/35549259561)) is PLAY runtime continuity under `RUNTIME_ONLY`. It is **not** a STUDY reopen and **not** a new Deploy ask.

## Live pin snapshot (OBSERVED 2026-09-20 ~19:44 PDT)

| Surface | Value |
|---|---|
| `GET https://noema.guru/version` | `worker_version_id=1e52e827-695c-4386-9795-d42b175ec166` · `world_id=world.perihelion-reach-3` · `deployed_at=2026-09-21T00:57:11.486234Z` |
| `GET https://noema.guru/ready` | `ready=true` · `ACTIVE` · `HEALTHY` · `playable=true` · **`players=0`** · `cycle=21948` · `sequence=59599` · `genesis_id=genesis.94d0961984b2b4f8` |
| `GET https://noema.guru/study` | HTTP 200 observational page: “Lab capture is not hosted on this world.” |
| Research routes (`/v1/research`, `/v1/notice`, `/v1/lab`) | HTTP **404** |

## Machine baseline

[`specs/current-state.v1.yaml`](../specs/current-state.v1.yaml) (`as_of: 2026-09-21`):

- `surfaces.study_hosted: BLOCKED`
- `capabilities.hosted_study_pipeline.state: BLOCKED`
- `capabilities.hosted_study_pipeline.blocker: production-like natural-play and evidence-readiness gate`
- Living Alpha gates A–F COMPLETE; `unproven_gates: []`
- Campaign `current_milestone: LCA-5` (closed); **no LCA-6 invented**

## TLDR for Boof / Danny

| Question | Answer |
|---|---|
| Need Deploy now? | **N** — Deploy already live; no STUDY runtime delta to ship |
| Top 3 gaps | (1) live natural multi-agent play / enrollment (`players=0`); (2) no STUDY reopen acceptance packet (criteria named at doctrine level only); (3) hosted NOTICE→TEST→COMPARE→CAPTURE routes absent (offline-only) |
| Recommended next human-yes | Authorize **enrollment/population on live PLAY** (people step) **and/or** a Specs **STUDY reopen companion draft** (docs-only) — **not** Deploy, **not** STUDY reopen itself |

## Gaps

**Labels:** OBSERVED = cited from Specs/Noema/live probe · INFERRED = tight reading of cited text without new criteria · NOT_COMPUTABLE = no authoritative checklist/receipt available (do not invent).

## A. OBSERVED requirements for hosted STUDY reopen

These are the requirements Specs / Living Alpha actually state. This audit does **not** add thresholds.

### A1. Doctrine gate — natural multi-agent play first

| Source | Text (paraphrase with path) |
|---|---|
| Specs `docs/LIVING-CIVILIZATION-ALPHA.md` § Campaign doctrine #6 | “Research follows meaningful play. Hosted STUDY remains blocked until **natural multi-agent play produces evidence worth testing**.” |
| Specs `specs/current-state.v1.yaml` `hosted_study_pipeline` | `state: BLOCKED` · `blocker: production-like natural-play and evidence-readiness gate` |
| Specs `docs/CIVILIZATION-CAPABILITY-MATRIX.md` row “Offline research spine” | “hosted reopen requires **natural-play evidence** and a **separate decision** \| after LCA-5” |
| Specs `docs/EXECUTION-SEQUENCE-90-DAY.md` § After the sequence | After cutover succeeds / state update: “**then decide** whether hosted STUDY or another deferred campaign should open.” |
| Specs Gate F promotion / scenario / acceptance | Hosted STUDY reopen **Not established**; STUDY stays BLOCKED; COMPLETE ≠ STUDY |

**OBSERVED implication:** Living Alpha A–F COMPLETE is a **prerequisite chronology** (“after LCA-5”), not a STUDY pass. Reopen needs (a) natural-play / evidence-readiness satisfaction of the named blocker and (b) a **separate** decision.

### A2. Hosted vs offline STUDY boundary

| Source | OBSERVED fact |
|---|---|
| Specs `docs/STUDY.md` § Hosted boundary (2026-08-23) | Hosted `/study` is observational; Worker has **no** NOTICE / TEST / COMPARE / CAPTURE routes. Offline Python implements the research spine. “Nothing in this document authorizes hosting STUDY.” |
| Specs `docs/SPEC-FREEZE-CORE-LOOP.md` §4 Slices D–G, I | Frontier / Observatory / Lab / Compiler / LEARN = **Offline only**; hosting is remaining work; Phase 2 exit = researcher NOTICE+TEST **without touching production world truth**; **isolation** is the hard part. |
| Specs `docs/SPEC-FREEZE-CORE-LOOP.md` §6 refresh | “enrollment is worth more than new research surface until [players > 0].” Slice D is next to *host* once A+B stability met — but empty world caveat stands. |
| Noema `spec-compat.json` | `hosted_runtime.study: "observational"` |
| Noema `docs/CORE-LOOP-RUNTIME.md` | Hosted `/study` called **stub**; research HTTP table is offline Python |

### A3. Forbidden until separately established

From Gate F scorecard item 5 / promotion non-invention (Noema `docs/evidence/gate-f-scorecard-1e52e827-20260921/SCORECARD.md`, Specs Gate F promotion):

- Hosted STUDY reopen / research rewards — **Forbidden**
- Offline ↔ hosted digest equivalence — **Forbidden** unless separately proven
- Sentience / phenomenal claims — **Forbidden**

### A4. What is NOT a STUDY reopen criterion (OBSERVED non-claims)

| Non-claim | Authority |
|---|---|
| Gate F COMPLETE | Specs `LIVING-ALPHA-ACCEPTANCE.md`, `LCA-GATE-F-PROMOTION-2026-09-21.md` |
| Item-7 `GO` | Gate F scenario: `GO` does not open hosted STUDY |
| Deploy already live / green pin | Gate F scorecard: Deploy ≠ GO ≠ STUDY |
| Offline research suite PASS (178 cases) | STUDY.md / SPEC-FREEZE: offline ≠ hosted |
| Gate B/C/E evidence packets | Prove Living Alpha gates; do **not** flip `study_hosted` |

## B. OBSERVED live / machine state (post Gate F COMPLETE)

| Check | OBSERVED | Label |
|---|---|---|
| Living Alpha A–F | COMPLETE; LCA-5 closed; no further Living Alpha gate | OBSERVED (current-state + promotion) |
| `study_hosted` | `BLOCKED` | OBSERVED |
| `hosted_study_pipeline` | `BLOCKED` (natural-play + evidence-readiness) | OBSERVED |
| Live Worker | `1e52e827-695c-4386-9795-d42b175ec166` | OBSERVED `/version` |
| Live PLAY | `world.perihelion-reach-3` / `genesis.94d0961984b2b4f8` | OBSERVED `/ready` |
| `/ready` health | ACTIVE · HEALTHY · playable · play_blocked=false | OBSERVED |
| `/ready` players | **0** | OBSERVED |
| Production device enrollment (Gate F residual #4) | “still never completed (players=0)” | OBSERVED (scorecard) |
| Hosted `/study` | Observational; “Lab capture is not hosted” | OBSERVED |
| Hosted research API | `/v1/research`, `/v1/notice`, `/v1/lab` → 404 | OBSERVED |
| Offline research spine | IMPLEMENTED_OFFLINE (current-state + STUDY.md) | OBSERVED |
| Open STUDY tracking issue | None found (2026-09-20 search); #715 CLOSED (Gate F) | OBSERVED |
| Dedicated STUDY reopen acceptance companion | **Absent** (no `LCA-STUDY-*` / STUDY-GATE scenario like Gate F) | OBSERVED absence |

**Note (OBSERVED honesty):** Gate B COMPLETE used retained Admin ICR/bindings + three external Controllers in an evidence packet; current-state says `/ready` players census is **not** that proof. Live `players=0` therefore does **not** contradict Gate B COMPLETE — it **does** show no continuous live natural-play population now.

## C. Gap list

| ID | Gap | vs requirement | Label | Notes |
|---|---|---|---|---|
| G1 | Live PLAY natural multi-agent population | Doctrine #6 + `hosted_study_pipeline` blocker (“natural-play”) | **OBSERVED** | `players=0`; Gate F residual #4: production device enrollment never completed; SPEC-FREEZE: enrollment > new research surface while empty |
| G2 | “Evidence worth testing” / evidence-readiness receipt | Named blocker + doctrine phrase | **NOT_COMPUTABLE** (threshold) · **OBSERVED** (name exists) | Specs name the gate; **no** companion defines pass/fail receipts for STUDY reopen. Do **not** invent a census N or WATCH digest list here |
| G3 | Separate Danny human-yes STUDY reopen decision | Matrix + EXECUTION-SEQUENCE + Gate F non-invention | **OBSERVED** absent | No ISSUE/PR records a STUDY reopen yes. #715 was Gate F only |
| G4 | STUDY reopen Specs acceptance packet | Pattern: Living Alpha used scenario+promotion companions | **OBSERVED** absent · **INFERRED** useful | Existing pattern is Gate companions; STUDY has STUDY.md + freeze slices, not a reopen gate packet. Drafting one is docs work — inventing pass criteria inside it would violate hard walls unless limited to citing existing text |
| G5 | Hosted NOTICE (Slice D Frontier) | SPEC-FREEZE Slice D; STUDY.md hosting gate | **OBSERVED** absent on Worker | Offline present; Worker no Frontier route |
| G6 | Hosted Observatory / Lab / Compiler / LEARN (E–G, I) | SPEC-FREEZE; STUDY workflow | **OBSERVED** absent on Worker | Depend on D + isolation; Phase 2/3 exits |
| G7 | Isolation evidence for hosted research vs production world truth | STUDY.md; SPEC-FREEZE Phase 2 exit; invariants `research_not_world_truth` | **NOT_COMPUTABLE** on hosted | Offline Lab isolation tests exist; hosted isolation problem called out as different — no hosted isolation receipt |
| G8 | Offline ↔ hosted digest equivalence | Forbidden unless separately proven | **OBSERVED** unproven · correctly out of scope | Must stay forbidden; not a STUDY reopen shortcut |
| G9 | Deploy for STUDY | Only if a STUDY **runtime** delta must land | **OBSERVED** not required now | Deploy already live for PLAY; Gate F COMPLETE ≠ new Deploy; no research-route Worker delta OBSERVED pending |

## D. What Gate F COMPLETE did / did not change for STUDY

| Changed? | Item |
|---|---|
| No | `study_hosted` remains BLOCKED (validator asserts) |
| No | `hosted_study_pipeline` remains BLOCKED |
| No | Hosted research routes still absent |
| No | Live players still 0 |
| Yes (chronology only) | “after LCA-5” precondition for considering a STUDY decision is now met (Living Alpha gates closed) |
| Yes (decision surface free) | Successor decision no longer blocks “what next”; STUDY is one deferred option among others (WORLD_CUTOVER, compatibility-at-scale also deferred) |

## E. Deploy Y/N for STUDY readiness

**Need Deploy to reopen STUDY? N (now).**

- Deploy already SUCCESS for live PLAY Worker `1e52e827…`.
- STUDY reopen is blocked on natural-play / evidence-readiness / separate decision / hosted research slice — none of which is “run Deploy again.”
- Deploy becomes relevant **only if** a future authorized Worker delta adds research routes (or related config) that must publish — that is a **runtime delta Deploy**, not a readiness Deploy.

## Recommended next work

**Authority:** gaps in the local audit pack only (`GAPS.md` under agent out dir `noema-study-readiness-2026-09-20/` — not a Specs tree path). No Deploy. No STUDY reopen. No invented pass criteria.

## Priority ladder

### P0 — Enrollment / live population (people + Controllers)

**Why first:** Specs doctrine and SPEC-FREEZE explicitly put **natural multi-agent play / enrollment** ahead of hosting research surface while `players=0`. Gate F residual #4 already owns “production device enrollment still never completed” to Danny (product).

**Work (docs/ops, not Deploy):**

1. Complete (or re-complete) **production device enrollment** for operator + ≥1 independently controlled external Controllers on live `world.perihelion-reach-3` using existing CONNECT / Admin paths (cite Gate B prep patterns; do not invent new verbs).
2. Produce a **natural-play evidence receipt** that is honestly labeled OBSERVED (who enrolled, when, Controller pins, that `/ready` players > 0 during windows, redacted). Do **not** treat Gate B/C/E historical packets as current live census.
3. Keep humans as HumanPrincipals (watch/connect/authorize) — not Players (RFC-0120).

**Exit (honest):** live natural-play activity OBSERVED; still **not** STUDY reopen.

**Human-yes needed:** Danny (product) authorize enrollment push / who may enroll Controllers on production.

### P0/P1 — Specs STUDY reopen companion (docs-only packet)

**Why:** `hosted_study_pipeline` blocker names “evidence-readiness” but **no** acceptance companion defines receipts (G2 NOT_COMPUTABLE). Living Alpha used scenario+promotion docs; STUDY reopen should not be a vibe flip of `study_hosted`.

**Work (docs-only):**

1. Draft Specs companion (suggested name only): e.g. `docs/STUDY-REOPEN-SCENARIO.md` — **must only bind existing text** (doctrine #6, STUDY.md hosted boundary, SPEC-FREEZE slices D→I + Phase 2/3 exits, current-state blocker, isolation invariants). Mark every undecided threshold **NOT_COMPUTABLE / Danny must lock** — do not invent N-player or WATCH-digest requirements.
2. Keep `study_hosted: BLOCKED` until a later Danny human-yes + evidence pack (separate from the companion’s existence — same law as Gate F: document ≠ COMPLETE).
3. Optional: open a **brief tracking issue** “STUDY reopen readiness (post Gate F)” pointing at this audit — not a reopen.

**Exit:** scorable checklist without invented criteria; STUDY still BLOCKED.

**Human-yes needed:** Danny yes to author/merge the companion **as draft law**, not as reopen.

### P1 — Evidence-readiness binding (after natural play)

**Why:** Doctrine requires evidence “worth testing” before hosted STUDY.

**Work:**

1. From natural-play receipts, list OBSERVED Interesting Behaviors candidates using **existing** Frontier/Observatory vocabulary — preferably offline first — without claiming hosted NOTICE.
2. Explicitly label what remains NOT_COMPUTABLE for hosted reopen.
3. Do **not** flip `current-state` STUDY rows.

**Exit:** evidence dossier citing live play; still not hosted STUDY.

### P2 — Hosted research runtime (Slice D first) — only after P0 + Danny yes

**Why:** STUDY.md / SPEC-FREEZE: hosting is a runtime slice; Slice D Frontier NOTICE is next; isolation is the hard part.

**Work (runtime; Deploy only if delta):**

1. Design hosted Frontier NOTICE with **isolation** (research ≠ world truth; Lab `mutates_production: false` law).
2. Land Worker routes only under an authorized packet; then Deploy **if and only if** that runtime delta needs publishing.
3. Do not host E–G/I until D isolation evidence exists; do not claim offline↔hosted digest equivalence.

**Exit:** hosted NOTICE (maybe) under separate acceptance — still may keep full STUDY pipeline BLOCKED until Phase 2 exit met.

**Human-yes needed:** Danny yes before any STUDY runtime merge/Deploy.

## Explicitly deferred / out of order

| Item | Why not now |
|---|---|
| Deploy “for STUDY” | No runtime STUDY delta pending; Deploy already live |
| WORLD_CUTOVER | Gate F `RUNTIME_ONLY`; separate deferred risk |
| Compatibility-at-scale | Still BLOCKED; different blocker |
| Flipping `study_hosted` / `hosted_study_pipeline` | Requires separate decision + evidence; not this audit |
| Inventing player-count or WATCH thresholds | Hard wall |

## Suggested human-yes ask (Danny / Boof)

> **Option set (pick):**  
> **A.** Authorize live enrollment/population push (P0).  
> **B.** Authorize Specs STUDY-reopen companion draft (docs-only; STUDY stays BLOCKED).  
> **C.** Both A then B.  
> **D.** Hold — leave STUDY deferred; no enrollment push.  
>  
> **Not on the menu:** Deploy now · STUDY reopen now · WORLD_CUTOVER.

## Mapping to gap IDs

| Priority | Closes / reduces |
|---|---|
| P0 enrollment | G1 (and feeds G2) |
| P0/P1 Specs companion | G2/G3/G4 (makes G2 scorable without inventing) |
| P1 evidence dossier | G2 |
| P2 Slice D host | G5/G7 (partial); Deploy only if delta |

## Extension Points

Non-normative. This audit promotes nothing. A later STUDY reopen companion may bind existing doctrine text into a scorable packet without inventing thresholds; document existence is not reopen. Keep `study_hosted` / `hosted_study_pipeline` BLOCKED until a separate Danny human-yes and evidence pack.
