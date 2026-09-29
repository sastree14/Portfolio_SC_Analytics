# Business impact

A reproducible analytics-engineering pipeline with tests, lineage-friendly transformations and explicit data-quality gates.

## Operating impact

1. Catch broken data before it reaches reports or models
2. Make transformations reviewable in SQL
3. Separate raw, staging and business-ready layers
4. Create repeatable build and test steps for analytics

## Decisions supported

The implementation is designed to make the following questions easier to answer and act on:

- How is **test pass rate** changing?
- How is **freshness SLA** changing?
- How is **invalid rows** changing?
- How is **build duration** changing?
- How is **models rebuilt** changing?

## Example operating scenario

Daily commercial data lands as Parquet, passes schema and rule checks, builds staging models and then produces finance-ready revenue and margin marts.

## Measurement

The public example exposes measurable technical and operating indicators without claiming production impact that has not been measured in a live organization.

Relevant KPIs include:

- test pass rate
- freshness SLA
- invalid rows
- build duration
- models rebuilt
