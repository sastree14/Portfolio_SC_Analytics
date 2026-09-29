# SC-16 · Recommendation, Search & Ranking Engine

**A hybrid recommendation and ranking system combining behavioural signals, content similarity and business rules.**

Designed for **Marketplaces · e-commerce · media · SaaS · internal knowledge discovery**.

## Business impact

- Increase relevance beyond simple popularity sorting
- Combine customer behaviour with item content
- Keep business constraints visible in final ranking
- Measure ranking quality using offline evaluation

[Business impact in detail →](docs/BUSINESS_IMPACT.md)

## Example use case

A user opens a marketplace category. The engine retrieves content-similar items, combines behavioural features, ranks candidates and applies inventory and eligibility rules before returning results.

## Technology at a glance

**Python · Scikit-learn · LightGBM · Sentence Transformers · FAISS · FastAPI · PostgreSQL · Redis**

## What a reviewer can inspect

- [Architecture](docs/ARCHITECTURE.md)
- [Credentials and integrations](docs/CREDENTIALS_AND_INTEGRATIONS.md)
- [Environments](docs/ENVIRONMENTS.md)
- [Limitations](docs/LIMITATIONS.md)
- [Example output](examples/outputs/result.json)
- [Execution log](examples/logs/example.log)
- [Generated analytical visual](examples/visuals/result.svg)
- [Technical implementation](technical/README.md)

## Run locally

See [technical/README.md](technical/README.md) for the project-specific execution path.

## Technology and business are separated deliberately

A non-technical reviewer can understand the decision and impact from this page. A technical reviewer can enter the implementation, SQL, model logic, tests and environment configuration directly.
