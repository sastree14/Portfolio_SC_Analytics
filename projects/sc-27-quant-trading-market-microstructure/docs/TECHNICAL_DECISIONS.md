# Technical decisions

The stack is not a list of logos. Each technology has to earn its place in the architecture.

## Key decisions

1. ClickHouse retains high-frequency event history while Redis keeps current live state.
2. Research and execution are deliberately separated; the public project does not route orders.
3. Transaction costs are part of backtest evaluation rather than an afterthought.

## Technology footprint

- **Python**
- **TypeScript**
- **WebSockets**
- **ClickHouse**
- **Redis**
- **Pandas**
- **NumPy**
- **Plotly**
- **Docker**

## Decision rule

If a simpler component can meet the same operational requirement with lower maintenance cost, it should be preferred. The public implementation keeps boundaries explicit so individual tools can be replaced without redesigning the whole project.
