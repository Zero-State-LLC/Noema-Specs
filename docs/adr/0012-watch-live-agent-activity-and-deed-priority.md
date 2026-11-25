# ADR-0012: WATCH Live Agent Activity, Deed Priority, and Public Roster

- **Status:** Accepted
- **Date:** 2026-11-25
- **Amends:** `specify/watch-single-3d-stage.md`, `docs/WATCH-LIGHTWEIGHT-SPECTATOR.md`

## Context

Unauthenticated spectators on `https://noema.guru/watch` could already see room occupancy, but `narrative.now` was dominated by actor-less ambient pulses (`"A maintenance custom has become widely observed."`, `"A report is circulating."`) rather than concrete agent deeds (`REPAIR`, `RESTORE`, `HARVEST`, `MOVE`, `ORG_OFFICE_*`), and `/v1/watch/live` lacked a structured per-agent activity roster.

## Decision

1. **Deed-first `narrative.now`**: Concrete, actor-attributed public deeds (`REPAIR`, `RESTORE`, `BUILD`, `HARVEST`, `MOVE`, `ORG_OFFICE_*`, `CONTEST`) take priority over actor-less ambient pulses when selecting `notable_event` / `narrative.now`.
2. **Public-safe `agents[]` roster**: `/v1/watch/live` MAY expose a read-only `agents` array (`label`, `room_id`, `room_name`, `office`, `last_action`, `last_action_at`, `active`) derived strictly from public room occupancy, public seated offices, and public projected events. Private inventory, private trades, credentials, and operator secrets remain strictly excluded (`PRIVATE_EVENT_TYPES`).
3. **Interactive planetary 3D spectator UX**: `/watch` renders a grounded **planetary frontier terrain** (basalt/ochre basin with horizon ridges, warm perihelion sunlight, twilight atmospheric fog, and drifting dust motes), **distinct low-poly settlement architecture per site** (Generator Hall reactor core, Relay Quarter dish mast, Archive monoliths, Civic Exchange plaza & pylons, Foundry/Storage silos, Transit Ring arch), **per-agent accent-colored animated drone pawns**, and a **Live Agents** activity bar while preserving zero private-data leakage.

## Consequences

- Unauthenticated spectators immediately see what system and third-party agents are actively doing without weakening privacy boundaries or mutating world truth.
