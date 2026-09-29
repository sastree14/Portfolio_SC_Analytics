# SC-01 · Long-Running AI Agent Platform

**Reliable AI agents for business processes that cannot be completed safely inside a single prompt.**

Designed for **operations, sales, internal tools, document workflows and approval-based automation**.

## What changes for the business

A normal AI interaction ends when the response is returned. Many real processes do not.

They wait for a person, call another system, fail temporarily, resume later and still need a clear record of what happened. SC-01 is designed around that operating reality.

| Business need | SC-01 response |
|---|---|
| Keep work alive after the initial request | Persistent run state |
| Pause before a sensitive action | Human approval gate |
| Continue work outside the API request | Background execution |
| Recover from temporary integration failures | Retry-capable worker architecture |
| Understand what happened later | Persisted audit events |
| Connect to existing systems | Authenticated API/webhook boundary |

[See the business impact in detail](docs/BUSINESS_IMPACT.md)

## Example use case

A qualified lead asks for a pricing call.

Instead of asking an LLM to "handle it" in one opaque step, the platform can:

1. receive the objective
2. prepare the intended CRM action
3. persist the plan
4. stop for approval
5. resume when a person approves it
6. call the configured business-system endpoint
7. store the result and execution history

The same pattern applies to document review, internal operations, customer support, research and other workflows where an AI system prepares or executes multi-step work.

## Impact

SC-01 is intended to improve **control, continuity and reliability** rather than simply generate better text.

The platform makes several operational KPIs measurable: completion rate, failure rate, approval time, retry count, end-to-end execution time and external-action success rate.

## Technology at a glance

**Python · FastAPI · PostgreSQL · Redis · Celery · Docker · REST APIs · Webhooks · OpenAI adapter · Anthropic adapter · SQL**

The technology is visible here for quick screening. The main project explanation does not require knowledge of these tools.

## How the system works

```text
Request
   ↓
Persistent run
   ↓
Background execution
   ↓
Model plan
   ↓
Approval when required
   ↓
External business-system action
   ↓
Persisted result + audit trail
```

For implementation detail, SQL, tests and infrastructure, go to the [technical implementation](technical/README.md).

## Evidence in the repository

You can inspect the project without running it:

- [generated API outputs](examples/outputs/)
- [execution log](examples/logs/approval-flow.log)
- [architecture](docs/ARCHITECTURE.md)
- [business impact](docs/BUSINESS_IMPACT.md)
- [credentials and integrations](docs/CREDENTIALS_AND_INTEGRATIONS.md)
- [environments](docs/ENVIRONMENTS.md)
- [limitations](docs/LIMITATIONS.md)
- [SQL](technical/sql/)
- [tests](technical/tests/)

## Run locally

For deterministic inspection without external AI credentials:

```bash
cd technical
PYTHONPATH=src pytest -q
python scripts/generate_examples.py
```

For the multi-service environment:

```bash
cp .env.example .env
docker compose -f technical/infra/docker-compose.yml up --build
```

The default example uses the mock provider. OpenAI and Anthropic adapters are available when their corresponding environment variables are configured.

## Credentials

No credentials are stored in the repository.

The project documents each credential boundary, which service uses it, what data crosses the integration and what changes in a production environment.

[Credentials and integrations →](docs/CREDENTIALS_AND_INTEGRATIONS.md)
