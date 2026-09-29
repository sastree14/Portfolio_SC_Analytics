# SC-06 · AI Workflow Automation Hub

**An event-driven automation layer that combines deterministic workflows with AI steps only where interpretation is useful.**

**Designed for:** Operations · finance · sales · internal automation

## Why this project matters

- Automate repetitive cross-system work
- Keep deterministic steps deterministic
- Use AI selectively for extraction, classification or drafting
- Make retries and exceptions visible

A business reviewer can stay on this page. A technical reviewer can move directly to the [technical implementation](technical/README.md).

## Example operating flow

```text
Webhook / event
    ↓\n    Validation
        ↓\n        Rules
            ↓\n            AI step when required
                ↓\n                Approval
                    ↓\n                    External systems
                        ↓\n                        Outcome log
```

## Technology at a glance

**n8n · Python · FastAPI · PostgreSQL · Redis · Webhooks · Zapier Webhooks · Make Webhooks · Docker**

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

Representative workflow events, payload hashes, AI outputs, approval state and downstream responses.

The repository does not contain client credentials or confidential records.

## Local review

The public implementation is designed so that the core example can be inspected locally without production credentials. Tool-specific connectors are configured through environment variables and are documented separately.

[Open the technical implementation →](technical/README.md)
