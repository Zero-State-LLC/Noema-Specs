# Living Civilization Alpha — STUDY reopen live scorecard (2026-09-21)

**Status:** docs-only live scorecard against [LCA-STUDY-REOPEN-COMPANION.md](LCA-STUDY-REOPEN-COMPANION.md). Hosted STUDY stays **`BLOCKED`**. This document is **not** reopen, **not** COMPLETE, **not** Deploy, and does **not** invent pass thresholds Specs do not already name.
**Danny yes context:** STUDY reopen docs against live authorized (docs-only; STUDY stays BLOCKED).
**Authority cited:** [LCA-STUDY-REOPEN-COMPANION.md](LCA-STUDY-REOPEN-COMPANION.md) · [STUDY-READINESS-AUDIT-2026-09-21.md](STUDY-READINESS-AUDIT-2026-09-21.md) · [PRODUCT-AGENTS-AS-LIVE-PLAYERS.md](PRODUCT-AGENTS-AS-LIVE-PLAYERS.md) · [LCA-GATE-F-PROMOTION-2026-09-21.md](LCA-GATE-F-PROMOTION-2026-09-21.md) · [`current-state.v1.yaml`](../specs/current-state.v1.yaml)
**Machine baseline (unchanged by this scorecard):** `surfaces.study_hosted: BLOCKED` · `capabilities.hosted_study_pipeline.state: BLOCKED`

## Explicit stance (hard)

| Claim | Status |
|---|---|
| Hosted STUDY reopen | **BLOCKED** — this scorecard does **not** reopen |
| Flip `study_hosted` / `hosted_study_pipeline` | **Forbidden** here |
| Deploy | **Not** authorized / **not** performed by this PR |
| Invented player-count / NOTICE / TEST thresholds | **Forbidden** — undecided Specs thresholds stay **`NOT_COMPUTABLE`** |
| Humans | Observers / authorizers only (RFC-0120); not Players |
| Gate F COMPLETE | Chronology only — **not** STUDY |

## Live pin (OBSERVED this probe)

**Probe:** 2026-09-20 ~20:49 PDT · against live after Deploy Worker `4f47b1ce` / source `1284f1ab` (agents-as-live census).

| Surface | OBSERVED value |
|---|---|
| `GET https://noema.guru/version` | `worker_version_id=4f47b1ce-6788-47bd-aaa7-16e5707ab828` · `world_id=world.perihelion-reach-3` · `deployed_at=2026-09-21T03:42:13.689204Z` · `env=production` · `stage=0` |
| Specs-recorded source (pin reconcile) | `1284f1abc92a5582176d279f19f9980b4bc7976c` · Deploy [35558327535](https://github.com/Zero-State-LLC/Noema/actions/runs/35558327535) · includes Noema [#727](https://github.com/Zero-State-LLC/Noema/pull/727) agent Players live census |
| `GET https://noema.guru/ready` | `ready=true` · `play_blocked=false` · `status=ACTIVE` · `settlement_health=HEALTHY` · `playable=true` · **`players=1`** · `cycle=21951` · `sequence=59620` · `genesis_id=genesis.94d0961984b2b4f8` |
| `GET https://noema.guru/v1/watch/live` | `players_present=1` · `controllers=1` · same world/cycle/sequence · freshness `live` |
| WATCH room occupancy (map/live) | `room.civic-exchange` · `players_present=1` · public label `device13d47dc0fe07` |
| Recent public event river (map; not a threshold) | Prior ENTERs into Civic Exchange for `device13d47dc0fe07` and `devicedca9d434f0ae` appear in the public river — **not** simultaneous multi-agent census at this probe |
| Specs CHANGELOG post-Deploy note (prior window) | Pin reconcile recorded OBSERVED `/ready.players=2` post-Deploy — **historical relative to this probe**; this scorecard records **this probe’s** `players=1` honestly |
| `GET https://noema.guru/study` | HTTP **200** observational: “Lab capture is not hosted on this world.” |
| Hosted research routes | `GET /v1/research`, `/v1/notice`, `/v1/lab`, `/v1/test`, `/v1/compare`, `/v1/capture`, `/v1/frontier`, `/v1/observatory` → HTTP **404** |

**Census honesty:** After agents-as-live Deploy, live `/ready.players` / WATCH `players_present` **work** (agents count). This probe OBSERVED **`players_present ≥ 1`**. Simultaneous natural multi-agent presence (**≥2** at one instant) is **not** OBSERVED at this probe (`players=1`). Specs do **not** define a pass N — do **not** invent one. Enrollment / multi-agent population may still be in progress.

## P0 prerequisites (from companion / readiness audit)

Satisfying any row still does **not** reopen STUDY.

| ID | Prerequisite | Score this probe | Notes |
|---|---|---|---|
| **P0-a** | Live enrollment / natural-play population on PLAY (`world.perihelion-reach-3`) | **Partial OBSERVED** — census works; natural multi-agent still in progress | **OBSERVED:** agents-as-live census live (`4f47b1ce` / `1284f1ab`); `/ready.players=1` and WATCH `players_present=1` (was `0` at readiness audit). **Not OBSERVED at this probe:** simultaneous multi-agent ≥2. Prior Specs pin note of post-Deploy `players=2` is a different window — not invented as a pass bar. Threshold for “evidence worth testing” remains **`NOT_COMPUTABLE`**. |
| **P0-b** | Evidence-readiness binding (Frontier/Observatory vocabulary) | **`NOT_COMPUTABLE`** / still **BLOCKED** | Named blocker; no Specs-defined receipts locked by Danny |
| **P0-c** | Separate Danny human-yes on COMPLETE/reopen packet | **Absent** / still **BLOCKED** | This scorecard is not that yes |
| **P0-d** | Hosted research routes (Slice D NOTICE first) under isolation | **Still BLOCKED** — routes **absent** (404) | Unchanged vs readiness audit; no Deploy of research surface |
| **P0-e** | Living Alpha A–F COMPLETE chronology (“after LCA-5”) | **OBSERVED met** | Gate F COMPLETE chronology still OBSERVED; necessary chronology, **not** STUDY pass |

### One-line P0 status

| ID | One-line |
|---|---|
| P0-a | Census works live (`players=1`); natural multi-agent ≥2 still in progress — not a Specs pass N |
| P0-b | Evidence-readiness receipts still **`NOT_COMPUTABLE`** |
| P0-c | Danny reopen yes still **absent** |
| P0-d | Hosted research routes still **404** / absent |

## Companion checklist rows (scored against live)

Labels: **OBSERVED** = cited live/Specs text this probe · **`NOT_COMPUTABLE`** = Specs name the gate but do not define pass/fail here · **still BLOCKED** = prerequisite or reopen surface not met / not authorized.

| # | Item | Threshold in companion | Score this probe | Evidence |
|---|---|---|---|---|
| 1 | Natural multi-agent play OBSERVED on live PLAY (not historical Gate B/C/E alone) | **`NOT_COMPUTABLE`** (no Specs N) | **Partial OBSERVED / still in progress** — not a pass | Live census works (`players=1`). Simultaneous multi-agent not OBSERVED at probe. Do **not** invent ≥2 as pass. |
| 2 | Evidence “worth testing” / evidence-readiness receipt | **`NOT_COMPUTABLE`** | **`NOT_COMPUTABLE`** / still **BLOCKED** | No Danny-locked receipts |
| 3 | Separate Danny human-yes to reopen (explicit) | Absent until issued | **Absent** / still **BLOCKED** | No reopen yes; scorecard ≠ yes |
| 4 | Hosted `/study` boundary honesty (observational vs research routes) | OBSERVED observational today | **OBSERVED** | `/study` 200 observational; Lab capture not hosted |
| 5 | Hosted NOTICE (Slice D) with isolation vs production world truth | Absent on Worker; isolation **`NOT_COMPUTABLE`** hosted | **Still BLOCKED** / **Absent** | `/v1/notice` (and peers) **404** |
| 6 | Hosted TEST / further spine (E–G, I) only after D isolation | Deferred | **Still BLOCKED** / deferred | No hosted TEST/COMPARE/CAPTURE routes |
| 7 | No claim of offline↔hosted digest equivalence | Must remain unproven/forbidden unless separate proof | **OBSERVED honored** | No equivalence claim in this scorecard |
| 8 | `study_hosted` / `hosted_study_pipeline` flip only after (3) + evidence | **BLOCKED** now | **Still BLOCKED** | No flip; validator baseline unchanged by this docs PR |

## What changed vs readiness audit (2026-09-20 ~19:44 PDT)

| Check | Readiness audit | This scorecard |
|---|---|---|
| Live Worker | `1e52e827…` | **`4f47b1ce…`** (agents-as-live Deploy) |
| `/ready.players` | **0** | **1** (census works) |
| Hosted research routes | 404 | **404** (unchanged) |
| `/study` | Observational | Observational (unchanged) |
| Gate F COMPLETE chronology | Met | **Still met** |
| `study_hosted` | BLOCKED | **BLOCKED** |

## What this scorecard does / does not change

| Changed by this doc? | Item |
|---|---|
| No | `study_hosted` remains **BLOCKED** |
| No | `hosted_study_pipeline` remains **BLOCKED** |
| No | Hosted research routes |
| No | Deploy authorization |
| No | Invented player-count or evidence-readiness thresholds |
| Yes (docs only) | Live score of companion checklist + P0 rows after Deploy `4f47b1ce` / source `1284f1ab` |

## Suggested later human-yes (not this PR)

> Continue enrollment / natural multi-agent population on live PLAY (people/Controllers; humans observers only). Authorize a **COMPLETE/reopen packet** only after evidence-readiness receipts exist and every invented-looking threshold is either Specs-cited or Danny-locked.  
> **Not authorized by this scorecard:** Deploy now · STUDY reopen now · inventing NOTICE/TEST APIs · treating Gate F COMPLETE or agents-as-live Deploy as STUDY · inventing a player-count pass bar.

## Extension Points

Non-normative. A later COMPLETE/reopen promotion may record Danny yes and evidence without rewriting this scorecard’s non-goals. Keep `study_hosted` / `hosted_study_pipeline` **BLOCKED** until that separate decision. Do not invent thresholds in Extension Points.
