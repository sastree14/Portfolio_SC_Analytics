# Technical decisions

The stack is not a list of logos. Each technology has to earn its place in the architecture.

## Key decisions

1. SimPy models event timing directly instead of approximating queues with static averages.
2. Monte Carlo replications quantify outcome distributions.
3. P95 and utilization metrics are retained alongside mean values to expose operational risk.

## Technology footprint

- **Python**
- **SimPy**
- **NumPy**
- **Pandas**
- **Monte Carlo**
- **Plotly**
- **FastAPI**
- **Docker**

## Decision rule

If a simpler component can meet the same operational requirement with lower maintenance cost, it should be preferred. The public implementation keeps boundaries explicit so individual tools can be replaced without redesigning the whole project.
