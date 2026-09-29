# Business impact

## What changes

1. Measure forecast quality separately by planning horizon
2. Expose bias as well as absolute forecast error
3. Translate forecasts into inventory and purchasing decisions
4. Compare complex models against simple operational baselines

## Example operating scenario

Daily SKU demand is forecast at H1, H3, H6 and H9. The system backtests each horizon, compares baseline and ML approaches, then exposes the selected forecast with prediction intervals.

## KPIs

- WAPE
- MAE
- forecast bias
- service level
- inventory coverage

These are measurable project KPIs. The repository does not claim organization-wide production impact where it has not been measured.
