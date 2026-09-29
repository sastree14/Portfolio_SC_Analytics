# SC-23 · Operations Simulation & What-If Engine

**A discrete-event and Monte Carlo simulation environment for testing operational changes before implementation.**

Designed for **Service operations · logistics · support teams · capacity planning · process redesign**.

## Business impact

- Test operational changes without disrupting live processes
- Quantify waiting time, utilization and bottleneck risk
- Compare staffing and demand scenarios under uncertainty
- Separate average outcomes from tail-risk behaviour

## Example use case

A service operation wants to know whether one additional specialist is enough for a projected 20% demand increase. The simulator compares waiting time and utilization distributions under both scenarios.

## Technology at a glance

**Python · SimPy · NumPy · Pandas · Monte Carlo · Plotly · FastAPI · Docker**

## Evidence

- [Business impact](docs/BUSINESS_IMPACT.md)
- [Architecture](docs/ARCHITECTURE.md)
- [Credentials and integrations](docs/CREDENTIALS_AND_INTEGRATIONS.md)
- [Environments](docs/ENVIRONMENTS.md)
- [Limitations](docs/LIMITATIONS.md)
- [Example output](examples/outputs/result.json)
- [Execution log](examples/logs/example.log)
- [Generated analytical visual](examples/visuals/result.svg)
- [Technical implementation](technical/README.md)

## Run locally

The technical README contains the exact environment and execution path.

The public example is deterministic and does not require production credentials.
