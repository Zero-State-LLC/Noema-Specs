# Deployment

## Environments

Required environment names are local, test, staging, production, and research-isolated.

## Deployment concerns

Document configuration loading, migrations, secrets management, database, queue, object storage, world processes, workers, replay workers, research workers, backups, disaster recovery, and world snapshot retention.

## Vendor neutrality

No production vendor lock-in is required. Implementations may use managed services if interfaces and data export remain compatible with this spec.

## Research-isolated environment

Research-isolated deployments separate private data, public dataset candidates, experimental agents, replay workers, and Atlas export from production worlds unless an RFC approves a narrower partition.
