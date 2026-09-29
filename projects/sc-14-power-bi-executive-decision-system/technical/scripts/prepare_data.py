from pathlib import Path
import pandas as pd
root=Path(__file__).resolve().parents[1]
sales=pd.read_csv(root/"data"/"fact_sales.csv")
sales["GrossMargin"]=sales["Revenue"]-sales["Cost"]
print(sales.groupby("Owner")[["Revenue","GrossMargin"]].sum())
