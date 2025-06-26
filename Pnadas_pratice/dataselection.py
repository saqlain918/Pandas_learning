import pandas as pd

# Load your dataset
df = pd.read_csv("Students Social Media Addiction.csv")

# ===============================
# 1. View Basic Info
# ===============================
print("🔍 Basic Dataset Info:")
df.info()

# ===============================
# 2. Check original data types
# ===============================
print("\n🧪 Original Data Types:")
print(df.dtypes)

# ===============================
# 3. Convert Age column to float
# ===============================
df['Age'] = df['Age'].astype(float)
print("\n✅ After Converting 'Age' to float:")
print(df.dtypes['Age'])

# ===============================
# 4. Select one column
# ===============================
print("\n📌 Gender Column (Series):")
print(df['Gender'])

# ===============================
# 5. Select multiple columns
# ===============================
print("\n📌 Selected Columns (Age, Country):")
print(df[['Age', 'Country']])

# ===============================
# 6. Select rows using iloc (by index number)
# ===============================
print("\n🧾 First 5 rows using iloc:")
print(df.iloc[0:5])

# ===============================
# 7. Select rows using loc (by label)
# ===============================
print("\n🧾 First 3 rows, select Gender & Country columns using loc:")
print(df.loc[0:2, ['Gender', 'Country']])

# ===============================
# 8. Conditional selection
# ===============================
print("\n🔍 Students with Age > 20:")
print(df[df['Age'] > 20])

print("\n🔍 Students from Pakistan:")
print(df[df['Country'] == 'Pakistan'])
