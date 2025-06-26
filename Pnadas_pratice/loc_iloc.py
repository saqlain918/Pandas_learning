import pandas as pd

# Load your dataset
df = pd.read_csv("Students Social Media Addiction.csv")

# View the first few rows
print(df.head())
#loc

# 1. Get one specific row using loc by index label
print("\n Row with index label 0 using loc:")
print(df.loc[0])

# 2. Get specific rows and columns by labels
print("\n Select rows 0 and 1, and columns 'Student_ID', 'Gender':")
print(df.loc[[0, 1], ['Student_ID', 'Gender']])

# 3. Filter rows where Age > 22
print("\n Filter rows where Age > 22:")
print(df.loc[df['Age'] > 22])

# 4. Filter where 'Gender' is 'Female' and show 'Mental_Health_Score'
print("\n Female students and their Mental Health Score:")
print(df.loc[df['Gender'] == 'Female', ['Student_ID', 'Mental_Health_Score']])

# 5. Change value using loc
df.loc[0, 'Country'] = 'UpdatedCountry'
print("\n Changed Country in row 0 using loc:")
print(df.loc[0, 'Country'])



#iloc
# 1. Get the first row using iloc
print("\n First row using iloc:")
print(df.iloc[0])

# 2. Get the first 5 rows and first 3 columns
print("\n First 5 rows and first 3 columns using iloc:")
print(df.iloc[:5, :3])

# 3. Get specific rows and columns using position
print("\n Rows 1 and 2, Columns 2 and 3 (iloc):")
print(df.iloc[[1, 2], [2, 3]])

# 4. Access a single cell using iloc
print("\n Value at row 2, column 4 (iloc):")
print(df.iloc[2, 4])

# 5. Modify a value using iloc
df.iloc[1, 0] = 99999  # Change Student_ID in row 1
print("\n✏ Updated Student_ID at row 1 using iloc:")
print(df.iloc[1, 0])
