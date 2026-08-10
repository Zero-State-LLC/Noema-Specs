# Infrastructure

## v0.1 closed set (preserved)

| Type | Primary function |
|------|------------------|
| `relay` | Communication quality and power stability signals |
| `generator` | Multiplies resource node regeneration |
| `storage_bay` | Increases effective storage capacity in room |
| `production_node` | Enables or improves HARVEST |

Condition range remains 0–100. Condition drives modifiers and bottlenecks exactly as specified in [RESOURCE-ECONOMY.md](RESOURCE-ECONOMY.md).

## Progression dimensions (keep deliberately small)

| Dimension | Meaning | Strategic choice |
|-----------|---------|------------------|
| Capacity | How much the infrastructure can process or hold | Expand vs specialize |
| Condition | Current operational health | Repair vs replace vs abandon |
| Efficiency | Modifier strength | Invest in quality vs quantity |
| Connectivity | Links to other infrastructure or routes | Network effects vs isolation risk |
| Defensibility | Resistance to disruption and contest | Soft target vs hardened asset |
| Specialization | Focused on one resource or function | Versatility vs peak performance |

## Investment choices (opportunity cost)

At any moment an actor faces real tradeoffs:

- Repair existing generator  
  vs increase storage capacity  
  vs improve relay condition  
  vs expand or create a new production node  
  vs build redundancy in another location

There is no large tech tree in early versions. Depth comes from placement, condition management, network effects, and exposure.

## Control and ownership

Infrastructure has `controller_id` / `owner_id`. Control contributes to Territory and Realm projections ([TERRITORY-CONTROL.md](TERRITORY-CONTROL.md), [REALMS.md](REALMS.md)). Sabotage and contestation (v0.2) target condition and control directly ([STRATEGIC-CONFLICT.md](STRATEGIC-CONFLICT.md)).

## Degradation and maintenance

World Event Director degradation continues. Neglect is a strategic choice with visible consequences. Repair is always available but costly in energy, compute, and storage ([ACTION-CONTRACTS.md](ACTION-CONTRACTS.md)).
