# Technical decisions

- Forecast metrics are evaluated by planning horizon instead of one blended accuracy number.
- The semantic model separates demand facts, forecast facts, inventory facts and shared dimensions.
- DAX owns interactive KPI logic while SQL owns repeatable source-grain preparation.
- Public visual evidence uses sanitized illustrative data and does not publish the supplied PBIX files.
