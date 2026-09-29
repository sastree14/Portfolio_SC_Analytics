# SC-22 · Resource, Capacity & Scheduling Optimization

**A scheduling engine that assigns work to limited resources while respecting skills, capacity and service targets.**

**Designed for:** Professional services · operations · field teams · manufacturing

## Why this project matters

- Allocate constrained resources consistently
- Expose bottlenecks early
- Balance utilization with service commitments
- Generate feasible schedules automatically

A business reviewer can stay on this page. A technical reviewer can move directly to the [technical implementation](technical/README.md).

## Example operating flow

```text
Jobs
    ↓
    Resources + skills
        ↓
        Availability
            ↓
            Constraints
                ↓
                Solver
                    ↓
                    Schedule
                        ↓
                        Operational hand-off
```

## Technology at a glance

**Python · OR-Tools · Pyomo · Pandas · FastAPI · PostgreSQL · Docker · Plotly**

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

Representative jobs, durations, deadlines, resource calendars, skill matrices and optimized assignments.

The repository does not contain client credentials or confidential records.

## Visual evidence

![SC-22 project visual](examples/visuals/result.svg)

## Main technical execution

**Start with [`technical/run_project.py`](technical/run_project.py).** This is the principal end-to-end code path for the public implementation.

## Local review

The public implementation is designed so that the core example can be inspected locally without production credentials. Tool-specific connectors are configured through environment variables and are documented separately.

[Open the technical implementation →](technical/README.md)
