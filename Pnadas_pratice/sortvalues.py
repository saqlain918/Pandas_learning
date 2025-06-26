import pandas as pd

df = pd.read_csv("Students Social Media Addiction.csv")

# Sort by Age (youngest to oldest)
sorted_df = df.sort_values(by='Age')
print(" Sorted by Age (ascending):")
print(sorted_df[['Student_ID', 'Age']].head())

# Sort by Addicted Score (highest to lowest)
sorted_df = df.sort_values(by='Addicted_Score', ascending=False)
print("\n Top Addicted Scores:")
print(sorted_df[['Student_ID', 'Addicted_Score']].head())


# Sort first by Country, then by Mental Health Score (descending)
sorted_df = df.sort_values(by=['Country', 'Mental_Health_Score'], ascending=[True, False])
print("\n Sorted by Country and Mental Health Score:")
print(sorted_df[['Country', 'Student_ID', 'Mental_Health_Score']].head(10))


# Sort by Most Used Platform (A-Z)
sorted_df = df.sort_values(by='Most_Used_Platform')
print("\n Sorted by Most Used Platform:")
print(sorted_df[['Most_Used_Platform', 'Student_ID']].head())
