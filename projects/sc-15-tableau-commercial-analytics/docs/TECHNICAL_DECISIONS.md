# Technical decisions

- The semantic/datasource layer owns KPI definitions so calculations are not duplicated across visuals.
- SQL prepares stable analytical grain before the BI tool applies interactive calculations.
- Native Tableau visuals are treated as the presentation layer, not as a substitute for data modelling.
