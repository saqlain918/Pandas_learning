import pandas as pd
df = pd.read_csv("Students Social Media Addiction.csv")

# 1. Drop one column
df1 = df.drop('Age', axis=1)
print("\n Drop one column ('Age'):")
print(df1)

# 2. Drop multiple columns
df2 = df.drop(['Age', 'Gender'], axis=1)
print("\n Drop multiple columns ('Age' and 'Score'):")
print(df2)

# 3. Drop column in-place
# df_copy = df.copy()
# df_copy.drop('Gender', axis=1, inplace=True)
# print("\n Drop 'Gender' in-place:")
# print(df_copy)

# 4. Drop non-existent column with and without error handling
try:
    df.drop('Height', axis=1)
except KeyError as e:
    print("\n⚠ Error dropping non-existent column:")
    print(e)

df3 = df.drop('Height', axis=1, errors='ignore')
print("\n Drop non-existent column safely (with errors='ignore'):")
print(df3)

# 5. Drop column by index position
col_to_drop = df.columns[1]  # 'Age'
df4 = df.drop(columns=[col_to_drop])
print("\n🔹 Drop column by index position (2nd column):")
print(df4)

# 6. Keep only specific column (not drop)
df5 = df[['Gender']]
print("\n🔹 Keep only 'Gender' column:")
print(df5)

