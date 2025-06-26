import pandas as pd
# Load your dataset again
df = pd.read_csv("Students Social Media Addiction.csv")

# Unique values in one column
print("📊 Unique values in 'Country':", df['Country'].nunique())

# Unique values in all columns
print("\n📊 Unique values in all columns:")
print(df.nunique())
