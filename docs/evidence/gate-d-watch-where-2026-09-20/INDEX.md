# Gate D WATCH Where — agent review evidence (2026-09-20)

**Label:** **AGENT_REVIEW · NOT human stranger · NOT Specs Gate D COMPLETE**

Post-COMPLETE follow-on: institution-pulse **Where** fix ([Noema #729](https://github.com/Zero-State-LLC/Noema/pull/729)) → recapture → SHADOW re-score **PASS** (vs prior **HOLD**).

Historical Gate D COMPLETE ([LCA-GATE-D-PROMOTION-2026-09-09.md](../../LCA-GATE-D-PROMOTION-2026-09-09.md)) is **not** rewritten. This pack does **not** reopen COMPLETE, does **not** claim a human-stranger trial, and does **not** authorize Deploy.

## One-line status

SHADOW agent review: institution repair pulse now projects **Consequence ≠ headline** and **Where = `room.civic-exchange`** on public WATCH JSON (Worker `86978241…` / source `565ccc15…`). Prior HOLD was institution Where **MISSING**.

## Pins (OBSERVED)

| Field | Value |
|---|---|
| Live Worker | `86978241-3983-4075-b289-fa28f9e75c46` |
| Source | `565ccc1595c89f992110808401e147b7692b2735` ([Noema #729](https://github.com/Zero-State-LLC/Noema/pull/729)) |
| `deployed_at` | `2026-09-21T04:16:15.925274Z` (= **2026-09-20 21:16 PDT**) |
| World | `world.perihelion-reach-3` |
| Capture heads (post-stretch) | cycle **21956** / sequence **59658** |
| Institution pulse (this stretch) | seq **59657** · `room_id` **`room.civic-exchange`** |
| Specs live pin | already reconciled ([Specs #358](https://github.com/Zero-State-LLC/Noema-Specs/pull/358)) |

## Capture pointers (agent FS)

| Pack | Path | Role |
|---|---|---|
| Re-capture (PASS window) | `/workspace/out/noema-gate-d/capture-2026-09-20-2120/` | RUN-PACKET, watch-live, SHADOW re-score |
| Prior HOLD | `/workspace/out/noema-gate-d/capture-2026-09-20-2055/` | Institution Where MISSING |
| Pack index | `/workspace/out/noema-gate-d/INDEX.md` | Latest vs prior |

Also cite: [Noema #729](https://github.com/Zero-State-LLC/Noema/pull/729) · live Worker id above · SHADOW verdict **PASS**.

## HOLD → PASS (SHADOW)

| Round | Capture | Institution Where | Verdict |
|---|---|---|---|
| Prior | `capture-2026-09-20-2055` | **MISSING** (`room_id` null) on repair-authority pulse | **HOLD** |
| Re-score | `capture-2026-09-20-2120` | **PRESENT** `room.civic-exchange` (seq 59657 / SHADOW also saw 59661 in a later fetch) | **PASS** |

Full SHADOW write-up: [BLIND-REVIEW-SHADOW.md](BLIND-REVIEW-SHADOW.md). Key OBSERVED tables: [OBSERVED-WHERE-TABLE.md](OBSERVED-WHERE-TABLE.md).

## Explicit walls

- **Not** Specs Gate D COMPLETE (historical COMPLETE unchanged; this is follow-on agent review only).
- **Not** human stranger PASS (AGENT_REVIEW only).
- **STUDY** remains **BLOCKED** — unchanged; no flip of `study_hosted` / `hosted_study_pipeline`.
- **No Deploy** from this Specs PR (Deploy of #729 already happened under separate Danny authorization).
- No campaign flip · no new verbs · no Genesis · no WORLD_CUTOVER · humans observers only.

## Files in this folder

| File | Description |
|---|---|
| [INDEX.md](INDEX.md) | This summary |
| [OBSERVED-WHERE-TABLE.md](OBSERVED-WHERE-TABLE.md) | Consequence ≠ headline + Where tables |
| [BLIND-REVIEW-SHADOW.md](BLIND-REVIEW-SHADOW.md) | SHADOW re-score (PASS) |
