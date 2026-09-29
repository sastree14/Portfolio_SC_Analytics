# SC-05 · Document Intelligence & Due Diligence Agent

**A document-analysis system that extracts evidence, retrieves supporting passages and produces reviewable findings.**

**Designed for:** Due diligence · legal review · investment analysis · compliance

## Why this project matters

- Reduce time spent searching large document sets
- Keep every finding tied to source evidence
- Separate extracted fact from interpretation
- Make document review repeatable

A business reviewer can stay on this page. A technical reviewer can move directly to the [technical implementation](technical/README.md).

## Example operating flow

```text
Document ingest
    ↓
    Text extraction
        ↓
        Chunking + embeddings
            ↓
            Vector retrieval
                ↓
                Structured analysis
                    ↓
                    Finding register
                        ↓
                        Review
```

## Technology at a glance

**Python · FastAPI · Qdrant · PostgreSQL · PyMuPDF · OpenAI · S3 / MinIO · Docker · Pydantic**

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

Representative documents, extracted chunks, metadata, retrieval hits and evidence-linked findings.

The repository does not contain client credentials or confidential records.

## Visual evidence

![SC-05 project visual](examples/visuals/result.svg)

## Main technical execution

**Start with [`technical/run_project.py`](technical/run_project.py).** This is the principal end-to-end code path for the public implementation.

## Local review

The public implementation is designed so that the core example can be inspected locally without production credentials. Tool-specific connectors are configured through environment variables and are documented separately.

[Open the technical implementation →](technical/README.md)
