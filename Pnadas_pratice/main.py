import pandas as pd

df = pd.read_csv("Students Social Media Addiction.csv")

print(df.columns)
# Total number of records (rows)
total_records = len(df)
print("Total records:", total_records)

df.rename(columns={
    'Mental_Health_Score': 'MentalScore',
    'Addicted_Score': 'AddictionLevel'
}, inplace=True)

print(df.columns)
df.to_csv("updated_dataset.csv", index=False)  # saves without row numbers
