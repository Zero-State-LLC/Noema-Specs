# GC8-S7 — WAIT burns cargo for energy

Authority: [RFC-0119](../rfcs/RFC-0119-wait-cargo-fuel.md). Catalog: [`economy-catalog.gc8-s7.json`](../specs/economy-catalog.gc8-s7.json).

WAIT already rests attention/compute and RFC-0117 lockout (energy 0 and storage 0 → energy 2, storage 1). This slice burns **one cargo for +2 energy** when the Player is carrying and below the energy grant.

| Before WAIT | After WAIT |
|-------------|------------|
| occupied ≥ 1 and energy < 80, and not lockout rest | energy +2 (clamp 80), free storage +1 |
| energy 0 and storage 0 | RFC-0117 only (energy 2, storage 1). No extra burn. |
| energy ≥ 80 | no burn |

No new verbs. No currency. WATCH silent. PLAY MAY say `Waiting can burn cargo for energy.`
