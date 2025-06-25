import pandas as pd

df = pd.read_csv("Students Social Media Addiction.csv")

print(df.columns)
# Total number of records (rows)
total_records = len(df)
print("Total records:", total_records)

