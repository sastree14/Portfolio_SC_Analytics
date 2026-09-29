# SC-01 · Long-Running AI Agent Platform

**Durable execution for AI workflows that must pause, resume, call external systems and preserve an audit trail.**

**Designed for:** Operations · sales · internal tools · approval-based automation

## Why this project matters

- Keep workflow state independent from a single LLM request
- Require explicit approval before sensitive external actions
- Recover from transient failures without losing the business process
- Preserve an inspectable execution history

A business reviewer can stay on this page. A technical reviewer can move directly to the [technical implementation](technical/README.md).

## Example operating flow

```text
Request
    ↓\n    Persist run
        ↓\n        Background worker
            ↓\n            Model plan
                ↓\n                Approval gate
                    ↓\n                    External action
                        ↓\n                        Audit + result
```

## Technology at a glance

**Python · FastAPI · PostgreSQL · Redis · Celery · Docker · OpenAI · Anthropic · SQL**

The stack is shown early because technical fit matters. The project is still explained in business terms first.

## What is included

- [Business impact and KPIs](docs/BUSINESS_IMPACT.md)
- [Example results and how to read them](docs/RESULTS.md)
- [Architecture](docs/ARCHITECTURE.md)
- [Technical decisions](docs/TECHNICAL_DECISIONS.md)
- [Data and public sample structure](docs/DATA.md)
- [Security and permissions](docs/SECURITY_AND_PERMISSIONS.md)
- [Credentials and integrations](docs/CREDENTIALS_AND_INTEGRATIONS.md)
- [Environments](docs/ENVIRONMENTS.md)
- [Limitations](docs/LIMITATIONS.md)
- [Example inputs, outputs and logs](examples/README.md)
- [Technical implementation, SQL and tests](technical/README.md)

## What the example data represents

Run state, model plan, approval events and external-action results. Public examples use deterministic mock execution.

The repository does not contain client credentials or confidential records.

## Local review

The public implementation is designed so that the core example can be inspected locally without production credentials. Tool-specific connectors are configured through environment variables and are documented separately.

[Open the technical implementation →](technical/README.md)
