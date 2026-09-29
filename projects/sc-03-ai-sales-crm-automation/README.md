# SC-03 · AI Sales & CRM Automation System

**A sales-operations system that scores inbound activity, prepares follow-ups and keeps CRM actions controlled.**

Designed for **B2B sales · agencies · SaaS · professional services · RevOps**.

## What changes for the business

- Prioritize leads using consistent scoring rules and model signals
- Reduce manual CRM updates and follow-up preparation
- Keep the salesperson in control before high-impact customer communication
- Create a measurable path from inbound signal to next action

[Business impact →](docs/BUSINESS_IMPACT.md)

## Example use case

An inbound lead requests pricing. The system enriches CRM context, calculates priority, drafts the next action and waits for salesperson approval before updating the deal.

## Technology at a glance

**Python · FastAPI · PostgreSQL · n8n · HubSpot API · Webhooks · OpenAI · Docker · SQL**

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
