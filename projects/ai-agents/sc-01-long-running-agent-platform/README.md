# SC-01 · Long-Running AI Agent Platform

A durable agent execution platform for business processes that cannot be completed safely inside a single LLM request.

## Business problem

Many agent prototypes work while the interaction is short and everything succeeds on the first attempt. Real operating processes are different. They may wait for a human decision, call external systems, fail temporarily, resume later and still need a complete audit trail.

This implementation separates the agent's reasoning from execution state so that a run can be paused, inspected, approved and resumed without losing context.

Typical use cases include:

- sales and CRM operations
- document review workflows
- internal operations assistants
- approval-based automations
- research tasks that call external services
- multi-step processes that may take minutes or hours

## What the system does

A user submits a goal through the API.

The platform:

1. creates a persistent run in PostgreSQL
2. sends execution to a background worker
3. asks the selected LLM provider for an action plan
4. stores the plan and current state
5. pauses before external action when approval is required
6. resumes after approval
7. calls an external webhook when configured
8. stores the final result or failure state

A run therefore remains inspectable even when the API process restarts.

## Architecture

```text
Client
  |
  v
FastAPI
  |
  +--------------------> PostgreSQL
  |                       run state
  |                       plan
  |                       result
  |
  v
Redis
  |
  v
Celery worker
  |
  +----> OpenAI / Anthropic / Mock provider
  |
  +----> Human approval gate
  |
  +----> External webhook / business system
```

See [Architecture](docs/ARCHITECTURE.md).

## Why these technologies are here

| Technology | Responsibility |
|---|---|
| FastAPI | API boundary for creating, inspecting and approving runs |
| PostgreSQL | Durable source of truth for execution state and audit fields |
| Redis | Message broker between the API and background workers |
| Celery | Background execution, retries and separation from request lifetime |
| OpenAI / Anthropic | Optional model providers behind the same provider interface |
| HTTPX | Controlled outbound HTTP calls to external systems |
| Docker Compose | Reproducible local environment containing API, worker, database and broker |

The design intentionally keeps provider logic separate from orchestration. Changing the model provider should not require rewriting the execution state machine.

## Human approval

External action can be placed behind an approval gate.

When `requires_approval=true`, the worker stores the proposed plan and changes the run to:

```text
WAITING_APPROVAL
```

No outbound webhook is executed until the approval endpoint is called.

This pattern is useful when an agent can prepare a decision but should not execute a material business action autonomously.

## Credentials and integrations

The repository contains no credentials.

Configuration is supplied through environment variables. A safe template is available in [`.env.example`](.env.example).

The public implementation supports:

- OpenAI API credentials
- Anthropic API credentials
- PostgreSQL connection
- Redis connection
- optional API access key
- optional bearer token for outbound webhooks

See [Credentials and integrations](docs/CREDENTIALS_AND_INTEGRATIONS.md).

## Environments

The repository includes a Docker Compose environment for local development.

The same services can be separated across managed infrastructure in staging or production. Environment-specific decisions are documented in [Environments](docs/ENVIRONMENTS.md).

## Run locally

Copy the configuration template:

```bash
cp .env.example .env
```

Start the platform:

```bash
docker compose up --build
```

The API will be available at:

```text
http://localhost:8000
```

Health check:

```bash
curl http://localhost:8000/health
```

Create a run:

```bash
curl -X POST http://localhost:8000/runs \
  -H "Content-Type: application/json" \
  -d @examples/create_run.json
```

Inspect a run:

```bash
curl http://localhost:8000/runs/<run_id>
```

Approve a paused run:

```bash
curl -X POST http://localhost:8000/runs/<run_id>/approve
```

## Public implementation

The default provider is `mock`, which allows the orchestration, persistence and approval flow to be inspected without an external model account.

OpenAI and Anthropic adapters are included and can be enabled through environment configuration.

External business systems are represented through a generic authenticated webhook boundary so the execution layer can be connected to a CRM, internal API, workflow platform or other service without exposing private production connections.

## Validation

The implementation includes a basic API health test and isolates orchestration from provider-specific code.

Before production use, additional validation should cover:

- idempotency for external actions
- provider timeout behaviour
- worker crash recovery
- duplicate task delivery
- webhook retries and dead-letter handling
- authorization by user or organization
- structured audit events
- rate limits and cost controls
- model output validation

## Limitations

This version demonstrates the execution pattern rather than a complete enterprise agent platform.

It does not currently include multi-tenant authorization, distributed tracing, model evaluation dashboards or a dedicated workflow engine for workflows lasting several days.

Those concerns are intentionally documented rather than hidden behind a demo.
