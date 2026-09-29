# Architecture

## Objective

The system must preserve execution state independently from the lifetime of an HTTP request.

It must also support a controlled boundary between model reasoning and external action.

## Components

### FastAPI

Receives run creation, inspection and approval requests.

FastAPI does not execute long-running work directly. It persists the run and sends execution to the task queue.

### PostgreSQL

Acts as the durable source of truth.

Stored information includes:

- run identifier
- requested goal
- selected provider
- execution status
- generated plan
- external-action result
- failure message
- creation and update timestamps

The database is deliberately separate from Redis. Losing the queue should not remove the business state of a run.

### Redis

Provides the Celery broker and result backend.

Redis carries execution messages. It is not treated as the authoritative record for a business run.

### Celery worker

Executes agent work outside the API request lifecycle.

The worker:

1. reads the durable run
2. calls the configured model provider
3. persists the proposed plan
4. pauses if approval is required
5. calls the external tool boundary
6. persists the outcome

Transient HTTP failures are retried with exponential backoff.

### Provider layer

The provider interface currently supports:

- Mock
- OpenAI
- Anthropic

Provider-specific SDKs are kept behind one interface.

This prevents orchestration code from depending directly on one model vendor.

### Human approval gate

A run configured with `requires_approval=true` stops after the plan is generated.

The run remains durable in PostgreSQL until an explicit approval request resumes execution.

### Outbound webhook

The webhook represents the boundary to an external business system.

Examples include:

- CRM
- workflow platform
- internal operations API
- document service
- notification service

The public repository keeps this boundary generic because private production endpoints and credentials should not be published.

## Data flow

```text
POST /runs
   |
   v
PostgreSQL: QUEUED
   |
   v
Redis / Celery
   |
   v
Worker: RUNNING
   |
   v
LLM provider
   |
   v
Persist plan
   |
   +------ approval required ------> WAITING_APPROVAL
   |                                      |
   |                                 POST /approve
   |                                      |
   +--------------------------------------+
   |
   v
Outbound webhook
   |
   v
Persist result
   |
   v
COMPLETED
```

## Failure handling

Current controls:

- durable run state
- explicit failure state
- stored error message
- Celery retry for transient HTTP failures
- separation of queue state from business state

Production extensions should include:

- idempotency keys
- dead-letter handling
- structured event log
- distributed tracing
- webhook signature verification
- alerting
- retry policies by error class
