# ADR-002: Private cognition boundary

## Status
Accepted

## Context
Agents may contain hidden prompts, chain-of-thought, latents, and local memory. Capturing these without explicit consent would create both ethical and scientific confounds.

## Decision
Private Agent Runtime state is outside the NOEMA system boundary. Only declared manifest metadata, authenticated actions/messages, opt-in self-reports, and world-visible artifacts may enter observations or evidence. No API, debug mode, or operator surface may request private cognition.

## Consequences
- Observations remain partial, permissioned projections.
- Self-reports are treated as agent-authored records, not ground truth of internal state.
- Containment and sandbox rules become critical for tool surfaces.
