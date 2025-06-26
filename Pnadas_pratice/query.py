import pandas as pd

# Load your dataset
df = pd.read_csv("Students Social Media Addiction.csv")
# Students who use social media more than 5 hours
filtered = df.query('Avg_Daily_Usage_Hours > 5')
print(filtered.head())


# Students from Pakistan or India
df_country = df[df['Country'].isin(['Pakistan', 'India'])]
print(df_country.head())
