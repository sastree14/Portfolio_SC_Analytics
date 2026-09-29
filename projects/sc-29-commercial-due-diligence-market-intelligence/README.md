# SC-29 · Commercial Due Diligence & Market Intelligence System

**A structured research system for market sizing, competitors, company signals and evidence-backed investment questions.**

**Designed for:** Private equity · corporate development · strategy · consulting

## Why this project matters

- Turn open-ended research into explicit questions
- Separate source evidence from interpretation
- Combine market and company signals
- Expose unsupported assumptions

A business reviewer can stay on this page. A technical reviewer can move directly to the [technical implementation](technical/README.md).

## Example operating flow

```text
Research questions
    ↓\n    Source collection
        ↓\n        Evidence store
            ↓\n            Structured extraction
                ↓\n                Analysis
                    ↓\n                    Synthesis
                        ↓\n                        Human review
```

## Technology at a glance

**Python · Pandas · DuckDB · FastAPI · Playwright · BeautifulSoup · OpenAI · PostgreSQL · Plotly**

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

Representative research questions, source metadata, extracted evidence, analytical tables and claim-support records.

The repository does not contain client credentials or confidential records.

## Local review

The public implementation is designed so that the core example can be inspected locally without production credentials. Tool-specific connectors are configured through environment variables and are documented separately.

[Open the technical implementation →](technical/README.md)
