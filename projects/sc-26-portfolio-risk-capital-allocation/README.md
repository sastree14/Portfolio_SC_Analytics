# SC-26 · Portfolio Risk & Capital Allocation Engine

**A portfolio analytics engine for expected return, covariance, stress testing and constrained capital allocation.**

Designed for **Investment teams · treasury · wealth analytics · quantitative research · risk management**.

## Business impact

- Measure portfolio risk using more than standalone asset volatility
- Compare allocation choices under explicit constraints
- Stress the portfolio under adverse return scenarios
- Translate risk appetite into a reproducible allocation problem

## Example use case

A portfolio must satisfy asset-class limits and a maximum risk budget. The engine estimates covariance, runs stress scenarios and produces feasible allocations for different risk targets.

## Technology at a glance

**Python · NumPy · Pandas · SciPy · CVXPY · Plotly · Monte Carlo · FastAPI**

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
