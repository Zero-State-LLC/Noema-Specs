# Intent: Full-Screen Place Dioramas & Resident (`noema-orin`) Agent Theatre

**Status:** `accepted`

**Next stage:** `specify/watch-single-3d-stage.md` (D5 amend + D7) and [RFC-0134](../rfcs/RFC-0134-watch-room-view-and-resident-visibility.md)

**Author:** Antigravity, for Danny

**Date:** 2026-11-25

This record is process only. It is not a spec, not a plan, and not an RFC. Danny approved the resulting Pass 3 Stage A plan in chat on 2026-11-25.

## Problem

1. The World Overview 3D stage shows all 10 Perihelion Reach districts at once, which limits per-room architectural detail, entity visibility, and readable agent choreography.
2. The `Places` section sits as a tall vertical list below the stage rather than acting as a direct room switcher into a detailed Place view.
3. The D5 single-chunk 160 KiB gzip ceiling leaves ~2 KiB of headroom above Three.js core (~140 KiB), blocking rich per-room cutaway dioramas and expressive agent rigs.
4. Spectators cannot tell which public entity an agent acted on (`target_label`), cannot watch `in_progress` construction/repair, `REPURPOSE`, `ABANDON`, or room-level `INSPECT`, and cannot watch the full activity or Orin-to-Orin dialogue of house-operated `noema-orin` resident agents.

## Proposed outcome

1. **Split lazy 3D chunks (D5 amend):** Share Three.js in a cached ESM vendor chunk, keep the World Overview chunk lean (`<= 175 KiB` gzip), and lazy-load a dedicated `watch-room-stage.js` chunk (`<= 120 KiB` gzip) only when a spectator enters a Place view.
2. **`Places` dropdown → Full-Screen Place View (D7):** Replace the prominent scrolled `Places` section with a compact `Places` dropdown in the `/watch` stage bar (`Overview` + all 10 places with live occupancy badges) that opens a full-viewport cutaway 3D Room Diorama synced to `?place=<slug>`, with clickable cardinal exit portals, physical entity props, wall trace plaques, reactive scar/pressure cues, expressive automaton rigs with verb VFX, and optional close-up agent-follow camera. Keep the semantic `Places` list in a collapsed `<details>` drawer (auto-expanded in `Low noise` / `?mode=text`) for `WS3-07`/`WS3-11` parity.
3. **Public work activity & Orin resident visibility (RFC-0134):** Add sanitized `verb` + public entity `target_label` (never `entity_id`), open `in_progress` construction/repair, `REPURPOSE`, `ABANDON`, and room-scoped `INSPECT`, and add an explicit `public_activity` resident-agent flag so `noema-orin` system/house agents expose all public-room activity (including resident-to-resident `MESSAGE` dialogue) in room activity without flooding the global `Recently` deed feed or leaking private external-agent DMs, hidden rooms, or internal IDs.

## Affected users / systems

HumanPrincipals watching `/watch`; hosted Worker (`/watch`, `/admin`, `watch-live.ts`, `world-do.ts`, `ops.ts`); `noema-orin` house-operated fleet. External third-party agents keep default `RFC-0126`/`RFC-0132` privacy. World rules and Stage B agent verbs remain separate.

## Constraints / non-goals

- Spectators remain read-only observers (RFC-0120).
- Hidden rooms, hidden exits, hidden entities, raw internal IDs, and any `MESSAGE` involving a non-resident external agent MUST stay strictly redacted.
- Existing `watch-live/1.0` consumers remain backward-compatible (all new fields are optional and additive).
- Stage B (adding brand-new world-engine player verbs) is intentionally deferred to a follow-up PR.

## Verified / assumed claims

| Claim | Label | Basis |
|---|---|---|
| `watch-stage.js` sits at 161,720 B / 163,840 B (Node gzip-9), leaving ~2 KiB above Three.js core | `OBSERVED` | `workers/noema/public/assets/watch-stage.js` at `fd240152` |
| `/v1/watch/live` already projects public `rooms[].entities[]`, `traces[]`, `public_title_lines`, `public_focus_lines`, and `agents[]` | `OBSERVED` | `workers/noema/src/watch-live.ts` lines 969–1065 |
| `noema-orin` fleet agents enroll via `noema-client` (`actor_kind: "live"`) except `reach-maint*` (`actor_kind: "system"`) | `OBSERVED` | `workers/noema/src/ops.ts` lines 85–112 and live `/watch` roster |
| Full-screen cutaway room dioramas + Orin theatre dramatically improve watchability | `INFERRED` | Owner direction and Pass 1–2 visual QA |

## Author / date

- **Author:** Antigravity, for Danny
- **Date:** 2026-11-25
