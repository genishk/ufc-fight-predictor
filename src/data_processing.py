import os
import json
import pandas as pd

df = pd.read_csv('../data/ufc-master.csv')
print(df.head())

# Print basic information about the DataFrame
print("\nDataFrame Summary:")
print("-" * 50)
print(f"Number of rows: {len(df)}")
print(f"Number of columns: {df.columns.size}")


