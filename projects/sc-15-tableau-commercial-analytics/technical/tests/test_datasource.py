from pathlib import Path
import pandas as pd

def test_commercial_datasource():
    p=Path(__file__).resolve().parents[1]/"data"/"commercial.csv"
    df=pd.read_csv(p)
    assert {"account_id","segment","revenue","cost","stage"}.issubset(df.columns)
    assert df["account_id"].notna().all()
