# Architecture

## Objective

Preserve execution state independently from the lifetime of an HTTP request, while maintaining a controlled boundary between model reasoning and external action.

```text
Client
  |
  v
FastAPI
  |
  +-----------------------> PostgreSQL
  |                          runs + audit events
  |
  v
Task dispatcher
  |
  +--> inline backend (tests / deterministic examples)
  |
  +--> Redis + Celery (asynchronous environment)
             |
             v
          Worker
             |
             +--> Model provider
             |      Mock / OpenAI / Anthropic
             |
             +--> Approval gate
             |
             +--> Authenticated webhook
                       |
                       v
                External system
```

## Component responsibilities

### FastAPI

Owns the HTTP boundary: create runs, inspect state and approve paused runs.

### PostgreSQL

Authoritative persistence for both run state and audit events. Queue state is intentionally not treated as business state.

### Redis / Celery

Provides asynchronous task delivery in the multi-service environment. Tasks are separate from API request lifetime.

### Provider layer

Keeps model-vendor SDKs behind one interface so orchestration does not depend directly on one provider.

### Approval gate

Prevents configured external actions from being executed until an explicit approval is received.

### Outbound webhook

Represents the integration boundary to CRM, workflow tooling, internal APIs or other business systems.

## State flow

```text
QUEUED
  -> RUNNING
      -> WAITING_APPROVAL
          -> RUNNING
              -> COMPLETED

Any execution stage can move to FAILED when an exception is persisted.
```

## Audit events

The implementation records events such as:

- `run_created`
- `worker_started`
- `plan_generated`
- `approval_required`
- `approval_received`
- `webhook_executed`
- `external_action_skipped`
- `run_completed`
- `run_failed`

This makes the execution path inspectable without relying only on application logs.
