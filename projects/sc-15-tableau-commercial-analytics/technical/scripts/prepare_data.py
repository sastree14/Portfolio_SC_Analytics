from pathlib import Path
import pandas as pd
root=Path(__file__).resolve().parents[1]
df=pd.read_csv(root/"data"/"commercial.csv")
df["gross_margin"]=df["revenue"]-df["cost"]
print(df.groupby("segment")[["revenue","gross_margin"]].sum())
