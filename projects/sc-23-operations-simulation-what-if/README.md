# SC-23 · Operations Simulation & What-If Engine

**A discrete-event and Monte Carlo environment for testing operational changes before implementation.**

**Designed for:** Service operations · logistics · support · process redesign

## Why this project matters

- Test changes without disrupting operations
- Quantify waiting-time and utilization risk
- Compare staffing scenarios under uncertainty
- Expose tail outcomes, not only averages

A business reviewer can stay on this page. A technical reviewer can move directly to the [technical implementation](technical/README.md).

## Example operating flow

```text
Arrival process
    ↓\n    Queue
        ↓\n        Resource pool
            ↓\n            Service events
                ↓\n                Simulation replications
                    ↓\n                    Distribution metrics
                        ↓\n                        Scenario comparison
```

## Technology at a glance

**Python · SimPy · NumPy · Pandas · Monte Carlo · Plotly · FastAPI · Docker**

The stack is shown early because technical fit matters. The project is still explained in business terms first.

## What is included

- [Business impact and KPIs](docs/BUSINESS_IMPACT.md)
- [Example results and how to read them](docs/RESULTS.md)
- [Architecture](docs/ARCHITECTURE.md)
- [Technical decisions](docs/TECHNICAL_DECISIONS.md)
- [Data and public sample structure](docs/DATA.md)
- [Security and permissions](docs/SECURITY_AND_PERMISSIONS.md)
- [Credentials and integrations](docs/CREDENTIALS_AND_INTEGRATIONS.md)
- [Environments](docs/ENVIRONMENTS.md)
- [Limitations](docs/LIMITATIONS.md)
- [Example inputs, outputs and logs](examples/README.md)
- [Technical implementation, SQL and tests](technical/README.md)

## What the example data represents

Representative arrival rates, service-time distributions, resource capacity and simulation replications.

The repository does not contain client credentials or confidential records.

## Local review

The public implementation is designed so that the core example can be inspected locally without production credentials. Tool-specific connectors are configured through environment variables and are documented separately.

[Open the technical implementation →](technical/README.md)
