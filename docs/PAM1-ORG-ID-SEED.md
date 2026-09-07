# PAM1 org_id Ambiguity — Design Note

**Status:** Design/research integration note. Inputs only. No contract, catalog, verb, or exposure change.

**Gap (SPEC-GAP-REGISTER-2026-08-25 PAM1):** `org_id` remains a human/dev-tool adapter ambiguity, not a new production Player field.

**Coverage:** PARTIALLY_CLOSED via adapter-only clarification. No new production semantics required for GC surfaces.

**Proposed framing (for future RFC if needed):** Adapter-only documentation or narrow RFC if wire semantics must change. No impact on canonical PLAY.

**Boundaries:** Out of core GC scope. Research input only.

**Citations:** SPEC-GAP-REGISTER-2026-08-25.md (PAM1), PLAYER-ACTION-MAP.md, PR #305 + main continuation.

PAM1 residual handled as adapter clarification. No new design needed for GC1-10.

## Extension Points

Non-normative guidance for future maintenance; this section changes no current behavior or promotion status.

- Adapter clarification can record how a non-canonical human/dev-tool form names an existing organization, including absent or ambiguous selection. Keep org_id here a presentation ambiguity, not a new production Player field or a source of institutional authority.

- Preserve the PARTIALLY_CLOSED classification unless a scoped clarification actually resolves its residual. A wire-semantics change needs a narrow RFC/version review; a documentation example does not reopen GC1–10 or permit human principals to issue Player actions.

- Check any future adapter example against PLAYER-ACTION-MAP and the identity boundary: an ambiguous organization stays unresolved, a human credential gains no mutation scope, and an explicit org selection does not bypass the Agent Player's existing membership/office authorization.
