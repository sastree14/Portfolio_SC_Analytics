# Technical implementation

## Main execution path

**Start here → [`run_project.R`](run_project.R)**

This is the principal public execution file for **SC-13 · R Shiny Forecasting & Scenario Planning Application**. It shows the end-to-end path in one place: **input → validation/context → core logic → business output**.

The files below are supporting implementation details used by that main path.

## Supporting implementation

- `shiny/app.R`
- `tests/`
- `sql/`
- `data/`

## Stack

- R
- Shiny
- forecast
- fable
- ggplot2

## Validation

See [VALIDATION.md](VALIDATION.md).

## Review order

1. Project README
2. Principal execution file
3. Supporting modules
4. SQL / integrations / tests / outputs

The principal execution file is intentionally the fastest technical route through the project.
