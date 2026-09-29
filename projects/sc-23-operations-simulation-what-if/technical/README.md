# Technical implementation

This is the code-level entry point for **SC-23 · Operations Simulation & What-If Engine**.

## Main responsibilities

- SimPy models event timing directly instead of approximating queues with static averages.
- Monte Carlo replications quantify outcome distributions.
- P95 and utilization metrics are retained alongside mean values to expose operational risk.

## Technical map

- `README.md/` — project implementation asset
- `data/` — project implementation asset
- `requirements.txt/` — project implementation asset
- `sql/` — project implementation asset
- `src/` — project implementation asset
- `tests/` — project implementation asset

## Technology

- Python
- SimPy
- NumPy
- Pandas
- Monte Carlo
- Plotly
- FastAPI
- Docker

## Validation

See [VALIDATION.md](VALIDATION.md) for the checks included with this project.

## Local execution

Use the project-specific dependency file, environment example and scripts in this directory. External credentials are not required for the deterministic public path unless the project documentation explicitly says otherwise.

## Read next

- [Architecture](../docs/ARCHITECTURE.md)
- [Technical decisions](../docs/TECHNICAL_DECISIONS.md)
- [Credentials and integrations](../docs/CREDENTIALS_AND_INTEGRATIONS.md)
- [Security and permissions](../docs/SECURITY_AND_PERMISSIONS.md)
