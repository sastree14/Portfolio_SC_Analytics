# SC-05 · Document Intelligence & Due Diligence Agent

**A document-analysis system that extracts evidence, retrieves supporting passages and produces reviewable findings.**

Designed for **Due diligence · legal and commercial review · investment analysis · procurement · compliance**.

## What changes for the business

- Reduce time spent searching long document sets
- Keep findings linked to the source evidence used to produce them
- Separate extracted facts from model interpretation
- Create repeatable review workflows across many documents

[Business impact →](docs/BUSINESS_IMPACT.md)

## Example use case

A data room contains supplier contracts, commercial agreements and financial notes. The system extracts clauses, retrieves evidence for predefined questions and produces a finding register with source references.

## Technology at a glance

**Python · FastAPI · Qdrant · PostgreSQL · PyMuPDF · OpenAI · S3 / MinIO · Docker · Pydantic**

The technology is visible here for fast technical screening. The business explanation does not depend on understanding the stack.

## How the system works

```text
Business event / request
        ↓
Validation + context
        ↓
Core decision / orchestration layer
        ↓
Controlled integration boundary
        ↓
Result, action or analytical output
        ↓
Audit / monitoring
```

For implementation details, tests, SQL and infrastructure, use the [technical entry point](technical/README.md).

## Evidence

- [Business impact](docs/BUSINESS_IMPACT.md)
- [Architecture](docs/ARCHITECTURE.md)
- [Credentials and integrations](docs/CREDENTIALS_AND_INTEGRATIONS.md)
- [Environments](docs/ENVIRONMENTS.md)
- [Limitations](docs/LIMITATIONS.md)
- [Example input](examples/inputs/example.json)
- [Example output](examples/outputs/result.json)
- [Example execution log](examples/logs/example.log)
- [Generated analytical visual](examples/visuals/result.svg)
- [Technical implementation](technical/README.md)

## Run locally

```bash
cd technical
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python src/main.py
pytest -q
```

The included example is deterministic and does not require external credentials. Real integrations are activated through environment configuration.

## Credentials

No credentials are committed. Integration boundaries and expected environment variables are documented explicitly.

[Credentials and integrations →](docs/CREDENTIALS_AND_INTEGRATIONS.md)
