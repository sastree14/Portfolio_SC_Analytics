-- Representative operational grain for the public Power BI control-tower example
select
    order_id,
    customer_id,
    destination_id,
    incoterm,
    order_date,
    promised_date,
    delivery_date,
    exception_status
from analytics.fact_order_fulfilment;
