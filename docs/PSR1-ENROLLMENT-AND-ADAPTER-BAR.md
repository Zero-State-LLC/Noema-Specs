# PSR-1 Enrollment Route & Third-Party Adapter/Endurance Bar

Status: Operator-locked contract for `#383` and `#363` (2026-11-24). Does not promote any capability or authorize a live campaign.

## Third-Party (Tier-3) Enrollment Route (`#383`)

- **Standardized route**: Device-code `/connect` approval path (outside operator runs `noema connect`; human approves via watch-link / Connect UI).
- **Official client baseline**: `noema-client==0.1.24` (live on PyPI; replaces the stale `0.1.21` reference).
- **Closeout bar**: Record at least one live enrollment receipt from an outside (tier-3) operator on the live pin.

## Third-Party Adapter & Endurance Bar (`#363`)

To move `third_party_agent_compatibility_at_scale` out of `BLOCKED`, the cohort MUST satisfy the locked PSR-1/PSR-2 bar using Gate B/E receipt shapes:

- **Cohort size**: `>= 6` Controllers total.
- **Non-first-party coverage**: `>= 2` Controllers on non-first-party integration paths, spanning **2 distinct integration styles**:
  1. At least one framework-backed third-party agent adapter.
  2. At least one independent custom HTTP/WS client.
- **Operator independence**: `>= 1` tier-3 Controller built or operated outside Zero-State.
- **Endurance**: `Δcycle >= 24`, `>= 20` actions per Player, `>= 60` total actions, with zero protocol or crash regressions.
