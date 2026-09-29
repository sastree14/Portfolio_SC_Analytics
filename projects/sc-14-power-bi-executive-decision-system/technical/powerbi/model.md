# Semantic model

Star schema:

- FactSales → DimDate, DimProduct, DimCustomer, DimOwner
- FactPipeline → DimDate, DimCustomer, DimOwner
- FactTargets → DimDate, DimOwner

Measures live in a dedicated measure table. Filter direction should remain single-direction unless a documented business requirement needs otherwise.
