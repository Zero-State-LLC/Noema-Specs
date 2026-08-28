# PAM1 org_id Ambiguity — Design Note

**Status:** Design/research integration note. Inputs only. No contract, catalog, verb, or exposure change.

**Gap (SPEC-GAP-REGISTER-2026-08-25 PAM1):** `org_id` remains a human/dev-tool adapter ambiguity, not a new production Player field.

**Coverage:** PARTIALLY_CLOSED via adapter-only clarification. No new production semantics required for GC surfaces.

**Proposed framing (for future RFC if needed):** Adapter-only documentation or narrow RFC if wire semantics must change. No impact on canonical PLAY.

**Boundaries:** Out of core GC scope. Research input only.

**Citations:** SPEC-GAP-REGISTER-2026-08-25.md (PAM1), PLAYER-ACTION-MAP.md, PR #305 + main continuation.

PAM1 residual handled as adapter clarification. No new design needed for GC1-10.