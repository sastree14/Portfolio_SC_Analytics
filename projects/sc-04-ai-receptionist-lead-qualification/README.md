# SC-04 · AI Receptionist & Lead Qualification

**A conversational intake layer that qualifies enquiries, captures structured requirements and routes the next action.**

Designed for **Service businesses · consultancies · clinics · real estate · appointment-led sales**.

## What changes for the business

- Respond consistently to inbound enquiries
- Capture structured qualification data instead of free-form notes
- Route high-value requests to the right person or scheduling path
- Reduce repetitive intake work while preserving human escalation

[Business impact →](docs/BUSINESS_IMPACT.md)

## Example use case

A prospect asks whether a service fits their needs. The receptionist captures company size, objective, urgency and budget range, then offers a scheduling path or human escalation.

## Technology at a glance

**TypeScript · Node.js · Fastify · Twilio · Calendly · OpenAI · PostgreSQL · Docker · Webhooks**

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
