# Technical decisions

The stack is not a list of logos. Each technology has to earn its place in the architecture.

## Key decisions

1. dbt owns transformation lineage and SQL model tests.
2. Pandera validates dataframe contracts before SQL transformations.
3. DuckDB keeps the public example runnable locally without weakening the warehouse pattern.

## Technology footprint

- **dbt**
- **DuckDB**
- **Python**
- **Pandera**
- **Parquet**
- **Apache Airflow**
- **SQL**
- **Docker**
- **GitHub Actions**

## Decision rule

If a simpler component can meet the same operational requirement with lower maintenance cost, it should be preferred. The public implementation keeps boundaries explicit so individual tools can be replaced without redesigning the whole project.
