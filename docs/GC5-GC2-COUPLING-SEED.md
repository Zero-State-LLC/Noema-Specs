# GC5–GC2 Infrastructure/Relay Coupling — Design Note

**Status:** Smallest coupling micro-note. Inputs only. No contract, catalog, verb, or exposure change.

**Parents:** GAME-COMPLETENESS-PLAN.md (coupling table + GC5/GC2) · COMMUNICATION-ECOLOGY.md · CONSTRUCTION.md · INFRASTRUCTURE.md

**Proposed framing:**
- Relays (GC5) can be damaged or constructed (GC2) affecting MESSAGE latency/bands.
- CONSTRUCTION on relay infrastructure couples to GC5 delivery quality without new verbs.
- Ties to existing INFRASTRUCTURE repair/condition.

**Boundaries:** Extends GC5 S0 + GC2 S0 pins. Research input only.

**Citations:** GAME-COMPLETENESS-PLAN.md (coupling table, GC5/GC2 sections), COMMUNICATION-ECOLOGY.md, GC5-FIRST-SLICE.md, CONSTRUCTION.md, PR #305 + main.

Smallest unit (step 2).

## Extension Points

Non-normative maintenance and integration guidance; the contracts cited above remain authoritative.

### Document-specific seam

Extend relay coupling evidence from construction or damage, through the relay’s live condition band, to ordinary MESSAGE reachability or delay. Distinguish a pending relay shell from functioning infrastructure so construction progress does not silently improve communications.

### Compatibility and promotion

This seed composes existing GC2 construction and closed GC5 relay contracts. It neither retunes latency bands nor opens a new channel, auto-send rule, or delivery event. Controller strategy may react to authorized observations but cannot inspect hidden relay topology.

### Verification before adoption

Compare local delivery, long-range healthy/degraded/unreachable conditions, repair recovery, and an in-progress relay. Preserve scheduled delivery across restart and check that message content and recipient permissions are unchanged. Require settled traces for the same candidate revision; a coupling diagram alone is not Gate C evidence.
