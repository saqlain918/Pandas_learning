import pandas as pd

data = pd.read_csv("Students Social Media Addiction.csv")

#Full data frame
df = pd.DataFrame(data)
print("Full DataFrame:")
print(df)

# Describe numeric data
print("\n Numerical Columns Summary:")
print(df.describe())

# Describe including all types (e.g., strings too)
print("\n Summary of All Columns:")
print(df.describe(include='all'))

# Describe one column only
print("\n Describe Age column:")
print(df['Age'].describe())

# Describe Age and Score columns together
print("\n Describe Age and Addicted_Score:")
print(df[['Age', 'Addicted_Score']].describe())

# Describe a string column (e.g., Gender)
print("\n Describe Gender column:")
print(df['Gender'].describe())

# Describe only text (object) columns
print("🔍 Summary of text columns only:")
print(df.describe(include='object'))

