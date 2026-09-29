# Technical implementation

## Structure

- `src/` — core analytical logic
- `tests/` — deterministic smoke tests
- `sql/` — persistence and reporting queries
- `data/` — compact representative data
- `scripts/` — output-generation utilities
- `shiny/` — R Shiny application

## Technology

- R
- Shiny
- forecast
- fable
- ggplot2
- dplyr
- DBI
- PostgreSQL

## Run

```bash
R -e "shiny::runApp('shiny')"
```
