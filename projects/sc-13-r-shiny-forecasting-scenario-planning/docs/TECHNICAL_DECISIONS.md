# Technical decisions

The stack is not a list of logos. Each technology has to earn its place in the architecture.

## Key decisions

1. Shiny is used because the intended user needs interactive scenario control without code.
2. ggplot2 provides analytical plots directly from the R model objects.
3. Database access is isolated through DBI rather than embedded in reactive expressions.

## Technology footprint

- **R**
- **Shiny**
- **forecast**
- **fable**
- **ggplot2**
- **dplyr**
- **DBI**
- **PostgreSQL**

## Decision rule

If a simpler component can meet the same operational requirement with lower maintenance cost, it should be preferred. The public implementation keeps boundaries explicit so individual tools can be replaced without redesigning the whole project.
