import pandas as pd

# Load dataset
df = pd.read_csv("Students Social Media Addiction.csv")

# 1. View all column names
print(" Column Names:\n", df.columns)

# 2. Select one column
print("\n 'Age' Column:\n", df['Age'].head())

# 3. Select multiple columns
print("\n 'Gender' and 'Country' Columns:\n", df[['Gender', 'Country']].head())

# 4. Rename a column
df.rename(columns={'Gender': 'Sex'}, inplace=True)
print("\n Renamed 'Gender' to 'Sex':\n", df[['Sex', 'Country']].head())

# 5. Add a new column
df['Social_Hours_Per_Week'] = df['Avg_Daily_Usage_Hours'] * 7
print("\n New Column 'Social_Hours_Per_Week':\n", df[['Avg_Daily_Usage_Hours', 'Social_Hours_Per_Week']].head())

# 6. Drop a column
df.drop('Relationship_Status', axis=1, inplace=True)
print("\n Dropped 'Relationship_Status':\n", df.columns)

# 7. Check column data types
print("\n Column Data Types:\n", df.dtypes)

print('\n Numbr of row and columns')
print(df.shape)

print('Summary of data frame')
df.info()

df['Age'] = df['Age'].astype(float)
print(df.dtypes['Age'])  # should now show float64


