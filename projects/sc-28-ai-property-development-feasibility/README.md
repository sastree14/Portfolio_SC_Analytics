# SC-28 · AI Property Development Feasibility & Operations System

**A property-development decision system combining feasibility modelling, documents, scenarios and workflow automation.**

**Designed for:** Property development · investment · development finance

## Why this project matters

- Unify acquisition and development assumptions
- Reduce document-review effort
- Compare downside and upside cases
- Move projects through explicit review gates

A business reviewer can stay on this page. A technical reviewer can move directly to the [technical implementation](technical/README.md).

## Example operating flow

```text
Site + deal inputs
    ↓
    Document extraction
        ↓
        Cost / revenue model
            ↓
            Finance
                ↓
                Scenario analysis
                    ↓
                    Investment gate
                        ↓
                        Workflow
```

## Technology at a glance

**Python · FastAPI · PostgreSQL · Pandas · GeoPandas · OpenAI · n8n · Docker · Plotly**

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

Representative site coordinates, acquisition terms, build costs, financing assumptions, document-extracted terms and scenario outputs.

The repository does not contain client credentials or confidential records.

## Visual evidence

![SC-28 project visual](examples/visuals/result.svg)

## Main technical execution

**Start with [`technical/run_project.py`](technical/run_project.py).** This is the principal end-to-end code path for the public implementation.

## Local review

The public implementation is designed so that the core example can be inspected locally without production credentials. Tool-specific connectors are configured through environment variables and are documented separately.

[Open the technical implementation →](technical/README.md)
