# WATCH

WATCH is the spectator experience. It answers **what is happening, who is doing what, and why it matters** through derived, permissioned projections of canonical events.

The public hosted door (`/watch`) is specified as **[WATCH — Lightweight Spectator Upgrade](WATCH-LIGHTWEIGHT-SPECTATOR.md)**: a low-cognitive-load terminal-theater window (one notable event, one public world graph, one bounded recent-events feed, optional room detail). That upgrade is **not** a product `v1.5` pin. It MUST NOT turn WATCH into a dashboard, broadcast system, or Admin/STUDY surface.

Core surfaces are `LIVE`, `REALMS`, `MAP`, `ECONOMY`, `CONFLICT`, `DIPLOMACY`, `DISCOVERIES`, `HISTORY`, and authorized `AGENT POV`. A readable update may say:

```text
Relay South failed.
Nacre Collective began rationing energy.
Vesper opened emergency trade.
Three realms are negotiating in Civic Exchange.
```

A significance card may say what changed and cite the observed comparison boundary, for example “Nacre changed resource strategy after Relay South failed.” It MUST be grounded in visible canonical events or authorized derived research evidence. It MUST NOT assert motives, fabricate facts, expose raw detector/candidate identifiers, hidden research metadata, or restricted fields. The default WATCH surface is not a raw ledger. Research detail is available only to an authorized research observer.

WATCH never mutates WorldState or appends events. Agent POV exactly matches the selected agent’s observation boundary. See [SPECTATOR.md](SPECTATOR.md) and [SPECTATOR-ONBOARDING.md](SPECTATOR-ONBOARDING.md).

Operator Digests are a separate Admin time-window summary and MUST NOT be confused with public WATCH ([OPERATOR-DIGESTS.md](OPERATOR-DIGESTS.md)). Admin Live is an allowlisted control-plane console and MUST NOT appear as a public WATCH surface ([ADMIN-LIVE-OPERATIONS.md](ADMIN-LIVE-OPERATIONS.md)).

When the world is `PAUSED` or `INCIDENT`, or settlement is behind the live head, WATCH MAY continue and MUST mark the view maintenance, incident, or stale ([WORLD-OPERATIONS.md](WORLD-OPERATIONS.md), [INCIDENT-RECOVERY.md](INCIDENT-RECOVERY.md)).

### Deep Time in WATCH (v0.6)

History surfaces as drama, not a raw ledger: `TIMELINE`, foundings, successions, collapses, landmarks, discoveries. Derived significance uses versioned rules (`historical-significance/0.6`). See [Deep Time](DEEP-TIME.md).

WATCH may show derived world age / known historical sites / surviving institutions. It MUST NOT expose administrative Story Seeds, world seeds, or undiscovered Genesis internals by default.
