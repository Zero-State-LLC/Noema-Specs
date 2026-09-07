# Chamber Dev Tooling Elevation Note (LCA-2 / Gate B Prep)

**Status:** SPEC NOTE — Specs-first per NOEMA-HIGH-VALUE-ACTIONS-ELEVATION-PLAN.md (accepted 2026-09-05). Additive only. Precedes any runtime patches to `/home/scrimshawlife/Noema/src/noema/gateway/ui.py`.

**Date:** 2026-09-05  
**Alignment:** UX/DX/AX elevation (AGENTS.md), noema-specs, PLAYER-ACTION-MAP.md, INTEGRATION-SURFACE.md.  
**Scope:** Primary dev surface (Chamber UI: server-rendered HTML/JS/CSS for PLAY/WATCH/CONNECT). Dev/operator tooling only (non-canonical for humans per current-state; agents inhabit). Pre-Gate B evidence.

## Rationale (High Value)
- Chamber is the live surface for ops, maint, evidence gathering, and future agent interactions.
- Strong existing foundations (from prior reads): semantic sections, aria-labelledby/aria-live, focus-visible, theme vars (dark, --surface, --color-state-*), responsive, live rendering, brand tests.
- Gaps: Many hardcoded English strings (labels, notices, activity copies, placeholders, JS textContent, button text, errors). i18n is the clearest quick-win for DX (localization) + UX (operator accessibility).
- AX: Already good (roles, landmarks, keyboard); can strengthen with consistent aria-labels via strings, more nav elements.
- DX: Centralizing strings improves maintainability, enables future bundles, aligns with Hermes plugin i18n patterns and hermes-desktop-plugins templates.
- Operator value: Better for multi-language teams, evidence snapshots, future Hermes integration.

## Current Verified State (Tool Receipts)
- File: `/home/scrimshawlife/Noema/src/noema/gateway/ui.py` (large; ~19k + 29k lines read in prior).
- i18n foundation: Exists via `window.noema.text` / dynamic dicts in JS (e.g., for some labels, activity). Dynamic rendering via Python + JS.
- Hardcoded examples (sampled via prior tools/greps): Various `placeholder=`, button texts, notices like activity copies, titles, error states, command labels.
- Theme/AX: Uses vars, `focus-visible`, `prefers-reduced-motion`, ARIA on status/activity.
- No inline low-contrast colors in core; consistent with brand.

## Proposed Changes (Additive, Specs-First)
1. **Introduce central STRINGS / i18n dict** (en base; simple object or function for lookup).
   - Pattern: Align with existing `window.noema` or add `STRINGS = { 'key': 'value', ... }` at top or in render helpers.
   - Or enhance `window.noema.text(key, ...)` if present.
   - Scope: All user-facing: HTML labels (e.g., "Play", "Watch", "Budgets"), notices, activity feed copies, placeholders (e.g., input hints), buttons ("Send", "Inspect"), errors, tabs.

2. **Replace hardcoded strings** (incremental, one section at a time):
   - Start with high-visibility: title, tabs, activity labels, command affordances, empty states.
   - Use lookups: e.g., `text('play-title')` or `STRINGS['activity-header']`.

3. **ARIA / AX polish** (additive):
   - Ensure all interactive (buttons, inputs, links) have `aria-label` or `aria-labelledby` using string keys.
   - Strengthen landmarks: `<nav>`, `<main>`, `<aside>` for grids/sections if not present.
   - More `role=status` / `aria-live` on dynamic areas (activity, budgets).
   - Keyboard: Confirm arrow nav for lists if applicable; visible focus already strong.

4. **Other elevation**:
   - Audit/replace any remaining inline styles/colors with theme vars.
   - Polish empty states, consistent tag styling.
   - Add comments referencing this note + AGENTS.md rules.
   - i18n-ready: Keys descriptive, support interpolation if needed.

5. **Verification**:
   - Re-read post-patch.
   - Grep for remaining hardcodes in key areas.
   - Manual/static: contrast (vars), keyboard (Tab/Enter), roles.
   - `omh-accessibility-audit` skill if UI testable.
   - Brand tests preserved.
   - Touch/reload if serving.

## Extension Points

Non-normative presentation seams for a later, separately authorized runtime patch.

- Extend the discovered localization primitive rather than installing a competing dictionary. Additional bundles, hosted WATCH/client adapters and optional plugin captions can reuse stable keys with interpolation and English fallback; canonical action tokens and authenticated affordance payloads remain unchanged.
- Keep tooling non-canonical for humans: keyboard activation of an operator control is not authority to inhabit. New economy/map/history views or translation services are candidates requiring their own scope review, not authorized by string extraction. Do not transmit credentials or private world/research text to external translation services by default.
- Compatibility/promotion: preserve Python/JavaScript rendering contracts and theme variables, migrate bounded groups of strings, and attach reviewed diff plus actual runtime test receipts before calling the patch complete. Historical observations above are not fresh reload, AX or hosted evidence.
- Verification proposal: test missing keys, interpolation, long translations and dynamic AVAILABLE_ACTIONS captions without changing wire values. Exercise keyboard focus after updates, accessible names, restrained status announcements, reduced motion and contrast; distinguish static checks from observed browser behavior and retain rollback to the prior bundle.

## Risks & Mitigations
- Low: Additive only; dev tooling; preserve existing JS/Python structure.
- No player-facing canonical changes (per current-state: humans WATCH/CONNECT).
- If existing i18n mechanism found, extend rather than duplicate.

## Next Execution (Post-Acceptance)
- Mini-spec (this) written.
- Read targeted sections of ui.py for exact strings.
- Additive patch introducing STRINGS + 5–10 replacements.
- Graft ask for indexing.
- Re-verify with tools.
- Merge and continue to full i18n or other phases.

**References**:
- NOEMA-HIGH-VALUE-ACTIONS-ELEVATION-PLAN.md (accepted)
- `/home/scrimshawlife/Noema/src/noema/gateway/ui.py`
- AGENTS.md (UX/DX/AX)
- hermes-desktop-plugins templates (i18n patterns)
- PLAYER-ACTION-MAP.md, INTEGRATION-SURFACE.md (Extension Points)

This note enables safe, elevated changes. Ready for patch.
