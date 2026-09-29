# SC-07 · Full-Stack LLM Business Copilot

**A full-stack web application that combines conversational analysis, structured tools and persistent business context.**

Designed for **Internal analytics · operations · customer portals · SaaS products · decision support**.

## What changes for the business

- Give users one interface for asking questions and taking structured actions
- Keep business tools separate from free-form model output
- Persist conversations and tool results for later review
- Support a product experience rather than a standalone prompt

[Business impact →](docs/BUSINESS_IMPACT.md)

## Example use case

A manager asks why pipeline conversion changed, requests the supporting records and then creates a follow-up task from the same interface.

## Technology at a glance

**Next.js · TypeScript · React · PostgreSQL · Supabase · OpenAI · Vercel · Zod · Tailwind CSS**

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
