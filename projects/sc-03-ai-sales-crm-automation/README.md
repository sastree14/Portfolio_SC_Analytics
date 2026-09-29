# SC-03 · AI Sales & CRM Automation System

**A sales-operations system that scores inbound activity, prepares follow-ups and controls CRM actions.**

**Designed for:** B2B sales · agencies · SaaS · RevOps

## Why this project matters

- Prioritize leads consistently
- Reduce manual CRM administration
- Prepare context-aware follow-ups
- Keep salespeople in control of material customer actions

A business reviewer can stay on this page. A technical reviewer can move directly to the [technical implementation](technical/README.md).

## Example operating flow

```text
Inbound signal
    ↓
    CRM context
        ↓
        Lead score
            ↓
            Next-action draft
                ↓
                Approval
                    ↓
                    CRM update
                        ↓
                        Audit
```

## Technology at a glance

**Python · FastAPI · PostgreSQL · n8n · HubSpot API · Webhooks · OpenAI · Docker · SQL**

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

Representative contacts, deal state, engagement signals, scores, proposed actions and CRM update events.

The repository does not contain client credentials or confidential records.

## Visual evidence

![SC-03 project visual](examples/visuals/result.svg)

## Main technical execution

**Start with [`technical/run_project.py`](technical/run_project.py).** This is the principal end-to-end code path for the public implementation.

## Local review

The public implementation is designed so that the core example can be inspected locally without production credentials. Tool-specific connectors are configured through environment variables and are documented separately.

[Open the technical implementation →](technical/README.md)
