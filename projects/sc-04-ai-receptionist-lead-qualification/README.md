# SC-04 · AI Receptionist & Lead Qualification

**A conversational intake layer that qualifies enquiries, captures structured requirements and routes the next action.**

**Designed for:** Service businesses · consultancies · clinics · real estate

## Why this project matters

- Respond consistently to new enquiries
- Capture structured qualification data
- Route high-value requests quickly
- Reduce repetitive intake work while preserving escalation

A business reviewer can stay on this page. A technical reviewer can move directly to the [technical implementation](technical/README.md).

## Example operating flow

```text
Inbound message
    ↓\n    Conversation context
        ↓\n        Structured extraction
            ↓\n            Qualification
                ↓\n                Routing
                    ↓\n                    Scheduling / human hand-off
```

## Technology at a glance

**TypeScript · Node.js · Fastify · Twilio · Calendly · OpenAI · PostgreSQL · Docker · Webhooks**

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

Representative enquiry messages, qualification fields, routing decisions and scheduling hand-off state.

The repository does not contain client credentials or confidential records.

## Local review

The public implementation is designed so that the core example can be inspected locally without production credentials. Tool-specific connectors are configured through environment variables and are documented separately.

[Open the technical implementation →](technical/README.md)
