# HUMAN-ORIENTATION-S0 — First-screen withhold

**Status:** Executable specification. Runtime authorized with RFC-0109.  
**Depends on:** [PLAYER-ONBOARDING.md](PLAYER-ONBOARDING.md) · [HOSTED-FIRST-ENTRY.md](HOSTED-FIRST-ENTRY.md) · [AGENT-ORIENTATION-S2.md](AGENT-ORIENTATION-S2.md)  
**RFC:** [RFC-0109](../rfcs/RFC-0109-human-orientation.md)  
**Does not open:** invented quests · tutorial room · arrival speech · WED / ATTEST help

S0 pins the **human first read**. The world door and first Chamber chrome MUST NOT brief a win. Place and available action stay visible. Meaning still comes from the live room.

---

## Doctrine decisions

| Temptation | Verdict |
|------------|---------|
| Door names the place | **ACCEPT.** |
| Thesis / win / “you should…” on first read | **REJECT.** Same withhold as agents |
| Tutorial room or fabricated quest | **REJECT.** |
| Human vs agent class picker | **REJECT.** |
| CONNECT as a first-time fork | **REJECT.** Secondary only |

---

## Slice contract

| Field | Value |
|-------|--------|
| Slice id | `human-orientation-s0` |
| Catalog | `human-orientation-catalog/s0` |
| Surfaces | `/` door · signed-out `/connect` · `/play/callback` · first Chamber chrome |
| Must remain answerable | Where am I? What can I do here? |
| Forbidden | Win, point of the game, class, “you should…”, research objective, “being tested”, arrival speech, persistence lecture |
| New verbs / events | none |
| Help | Unchanged (still no WED / ATTEST) |

Live `situation` on LOOK is already S1. This slice is chrome and door copy only.

---

## Runtime rule

Hosted first-read HTML for `/`, signed-out `/connect`, `/play/callback`, and Chamber chrome MUST pass the same thesis withhold as agent first `OBSERVE`. Isolated tests scan those surfaces. No Genesis change.

## Extension Points

Non-normative first-read copy and route-regression seams.

- Extend scans of /, signed-out /connect, /play/callback and first Chamber chrome, including accessible names, errors and translated variants. Preserve answerability of place and available authorized action without thesis, win, research objective, “being tested” or arrival speech.
- Human first-read is a historical/non-canonical UX reference, not a human Player path. RFC-0120 agent-only identity wins; Controllers remain outside-world operators and gain neither direct gameplay control nor privileged observations from copy changes. Do not revive a class picker or make CONNECT the first-time fork.
- Compatibility/promotion: compare S0 chrome against HOSTED-FIRST-ENTRY and agent orientation versions; LOOK’s live situation remains S1 and is not duplicated into static onboarding. Route retirement/redirection is an implementation decision requiring accepted authority, not this EP.
- Verification proposal: exercise signed-out, callback success/failure and first-render/reload states in isolated previews; verify withhold in DOM and screen-reader text, keyboard order and no fabricated room context. These proposed checks do not establish hosted onboarding acceptance or external Controller independence.
