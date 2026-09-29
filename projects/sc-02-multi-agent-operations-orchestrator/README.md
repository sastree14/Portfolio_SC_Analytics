# SC-02 · Multi-Agent Operations Orchestrator

**A controlled multi-agent system that separates planning, specialist work, review and execution.**

Designed for **Operations · internal tooling · complex multi-step workflows · cross-functional automation**.

## What changes for the business

- Break large workflows into accountable specialist steps
- Keep agent responsibilities explicit instead of relying on one opaque prompt
- Insert review and approval before material actions
- Create a traceable record of delegation, hand-offs and final decisions

[Business impact →](docs/BUSINESS_IMPACT.md)

## Example use case

Coordinate a customer escalation that requires account context, policy review, a proposed resolution and manager approval.

## Technology at a glance

**Python · FastAPI · LangGraph · PostgreSQL · Redis · Docker · OpenAI · Anthropic · Pydantic**

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
