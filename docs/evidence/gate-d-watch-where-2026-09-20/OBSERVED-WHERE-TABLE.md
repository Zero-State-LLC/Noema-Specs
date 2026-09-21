# OBSERVED — Consequence ≠ headline · Where

**Label:** **AGENT_REVIEW · NOT human stranger · NOT Specs Gate D COMPLETE**

Source capture: `/workspace/out/noema-gate-d/capture-2026-09-20-2120/` (RUN-PACKET + `watch-live.json`). Worker `86978241-3983-4075-b289-fa28f9e75c46` / [Noema #729](https://github.com/Zero-State-LLC/Noema/pull/729).

## Re-capture window (post–Where Deploy)

| Event | Seq | Headline (`line`) | Consequence | Consequence ≠ headline | Where (`room_id`) |
|---|---|---|---|---|---|
| Org form | 59653 | An organization acted at Civic Exchange | An organization formed | **OBSERVED** (YES) | **OBSERVED** `room.civic-exchange` |
| Institution repair pulse (this stretch) | 59657 | An institution declared a temporary repair authority. | Temporary repair authority is in force | **OBSERVED** (YES) | **OBSERVED** `room.civic-exchange` |
| Pre-stretch institution row (feed) | 59641 | same institution line | Temporary repair authority is in force | OBSERVED | **MISSING** (`room_id` null) — honest; not this stretch’s emergency |

**#729 proof:** institution emergency declared from a locatable public room (Civic Exchange) now projects **Where** on the public WATCH row (seq **59657**).

## SHADOW re-score table (public JSON only)

| Pulse (OBSERVED line) | Consequence | ≠ headline? | Where |
|---|---|---|---|
| “An institution declared a temporary repair authority.” (seq **59661** in SHADOW fetch; stretch row **59657**) | “Temporary repair authority is in force” | **YES** | **PRESENT** — `room.civic-exchange` |

**Delta vs prior HOLD:** Previous fetch had the same institution headline + consequence rewording but `room_id: null`. Re-capture / SHADOW fetch shows `room_id: "room.civic-exchange"` on `/v1/watch/live` (and map river per SHADOW).

## Prior HOLD (for contrast)

Capture: `/workspace/out/noema-gate-d/capture-2026-09-20-2055/`

| Pulse | Consequence ≠ headline | Where |
|---|---|---|
| Institution repair authority (seq 59633) | YES | **MISSING** |
| Organization acted at Civic Exchange (seq 59631) | YES | PRESENT `room.civic-exchange` |

## Non-claims

Not COMPLETE · Not human stranger · No Deploy · STUDY unchanged BLOCKED.
