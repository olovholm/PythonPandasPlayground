import pandas as pd

df = pd.read_csv("../../data/raw/us-border-crossings/border-crossings.csv")

for col in df.columns:
    print(f"Distinct values in {col}:")
    print(df[col].unique())
    print()
