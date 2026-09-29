from pathlib import Path
import pandas as pd

def test_sales_grain_and_margin():
    p=Path(__file__).resolve().parents[1]/"data"/"fact_sales.csv"
    df=pd.read_csv(p)
    assert {"Date","Revenue","Cost"}.issubset(df.columns)
    assert (df["Revenue"]>=df["Cost"]).all()
