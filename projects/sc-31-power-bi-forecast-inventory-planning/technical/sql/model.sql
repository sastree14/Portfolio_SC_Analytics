-- Representative analytical grain for the public Power BI planning example
select
    forecast_date,
    product_id,
    market_id,
    horizon_months,
    actual_demand,
    forecast_demand,
    stock_units
from analytics.fact_forecast_inventory;
