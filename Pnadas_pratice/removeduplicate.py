import pandas as pd

# Load your dataset
df = pd.read_csv("Students Social Media Addiction.csv")

# Check for duplicate rows
print(" Total duplicate rows:", df.duplicated().sum())

# Remove duplicate rows
df_no_duplicates = df.drop_duplicates()

# Show the cleaned data
print(" Data after removing duplicates:")
print(df_no_duplicates)

# Remove duplicates based only on 'Student_ID'
df_unique_ids = df.drop_duplicates(subset='Student_ID')

