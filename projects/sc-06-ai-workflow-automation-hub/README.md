# SC-06 · AI Workflow Automation Hub

**An event-driven automation layer that combines deterministic workflows with AI steps where interpretation is actually useful.**

Designed for **Operations · finance · sales · reporting · internal automation**.

## What changes for the business

- Automate repetitive cross-system workflows without turning every step into an AI decision
- Use model calls only where classification, extraction or drafting adds value
- Keep retries, approvals and failure handling visible
- Reduce manual movement of data between SaaS tools

[Business impact →](docs/BUSINESS_IMPACT.md)

## Example use case

A signed commercial form triggers validation, CRM update, document generation, internal notification and an AI-written summary for review.

## Technology at a glance

**n8n · Python · FastAPI · PostgreSQL · Redis · Webhooks · Zapier Webhooks · Make Webhooks · Docker**

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
