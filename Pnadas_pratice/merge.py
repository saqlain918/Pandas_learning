import pandas as pd

# Load the main dataset
df1 = pd.read_csv("Students Social Media Addiction.csv")

# Let's make another small DataFrame to merge
df2 = pd.DataFrame({
    'Student_ID': [101, 102, 103],
    'Exam_Score': [88, 75, 93]
})

# Merge on 'Student_ID'
merged_df = pd.merge(df1, df2, on='Student_ID', how='left')

print(" Merged DataFrame:")
print(merged_df.head())



