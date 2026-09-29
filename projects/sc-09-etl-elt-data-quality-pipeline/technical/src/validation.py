import pandera as pa
from pandera import Column, DataFrameSchema, Check

schema=DataFrameSchema({
    "record_id": Column(str, nullable=False),
    "signal_a": Column(int, Check.ge(0)),
    "signal_b": Column(float, Check.in_range(0,1)),
    "priority": Column(str, Check.isin(["low","medium","high"]))
})
