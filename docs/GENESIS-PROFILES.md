# Genesis Profiles

Small closed catalog of **three** admin-selectable starting history postures.

Catalog: [`specs/genesis-profiles.v06.json`](../specs/genesis-profiles.v06.json)  
Schema: [`specs/genesis-profile.schema.json`](../specs/genesis-profile.schema.json)

| profile_id | Intent |
|---|---|
| `YOUNG_FRONTIER` | Thin history, open opportunity |
| `FRACTURED_OLD_WORLD` | Scars, incomplete records, unresolved claims |
| `RECOVERING_NETWORK` | Damaged connectivity; repair/alliance paths |

Each profile bounds: resource abundance, infrastructure condition, inhabited/abandoned area counts, historical age band, institution presence, artifact density, conflict pressure, trade pressure.

Do **not** expand into a large profile catalog for v0.6.


## Extension Points

Non-normative guidance for future maintenance; this section changes no current behavior or promotion status.

- Profile documentation can add bounded examples within the existing YOUNG_FRONTIER, FRACTURED_OLD_WORLD, and RECOVERING_NETWORK postures. Keep profile selection admin-only and distinguish starting-history texture from a scripted future for Players.

- Catalog bounds and profile IDs remain pinned to the v0.6 schema/catalog. A future profile or changed bounds needs explicit catalog/schema compatibility review and release scope approval; it is not permission to enlarge the closed foundation catalog or reseed an active world.

- Validate examples against each profile's resource, infrastructure, history, and institution bounds. Reproduce identical Cycle 0 output from identical versioned inputs and seed, retain distinct valid outputs for different seeds, and check preview never performs activation.
