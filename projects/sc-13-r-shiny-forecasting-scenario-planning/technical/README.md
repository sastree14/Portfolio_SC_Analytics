# Technical implementation

This is the code-level entry point for **SC-13 · R Shiny Forecasting & Scenario Planning Application**.

## Main responsibilities

- Shiny is used because the intended user needs interactive scenario control without code.
- ggplot2 provides analytical plots directly from the R model objects.
- Database access is isolated through DBI rather than embedded in reactive expressions.

## Technical map

- `README.md/` — project implementation asset
- `data/` — project implementation asset
- `renv.lock/` — project implementation asset
- `shiny/` — project implementation asset
- `sql/` — project implementation asset
- `tests/` — project implementation asset

## Technology

- R
- Shiny
- forecast
- fable
- ggplot2
- dplyr
- DBI
- PostgreSQL

## Validation

See [VALIDATION.md](VALIDATION.md) for the checks included with this project.

## Local execution

Use the project-specific dependency file, environment example and scripts in this directory. External credentials are not required for the deterministic public path unless the project documentation explicitly says otherwise.

## Read next

- [Architecture](../docs/ARCHITECTURE.md)
- [Technical decisions](../docs/TECHNICAL_DECISIONS.md)
- [Credentials and integrations](../docs/CREDENTIALS_AND_INTEGRATIONS.md)
- [Security and permissions](../docs/SECURITY_AND_PERMISSIONS.md)
