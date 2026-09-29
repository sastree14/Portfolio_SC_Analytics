# Calculated fields

## Gross Margin
```text
SUM([Revenue]) - SUM([Cost])
```

## Gross Margin %
```text
(SUM([Revenue]) - SUM([Cost])) / SUM([Revenue])
```

## Account Revenue LOD
```text
{ FIXED [Account ID] : SUM([Revenue]) }
```

## Cohort Retention
Defined from first purchase month and active-month logic in the prepared datasource.
