import pandas as pd

df = pd.read_csv("Students Social Media Addiction.csv")

print("\n Average stats by Gender:")
print(df.groupby("Gender").mean(numeric_only=True))

print("\n Number of students per Country:")
print(df.groupby("Country")['Student_ID'].count())

print("\n Avg Daily Social Media Usage by Academic Level:")
print(df.groupby("Academic_Level")['Avg_Daily_Usage_Hours'].mean())

print("\n Mental Health Score by Relationship Status:")
print(df.groupby("Relationship_Status")['Mental_Health_Score'].describe())

print("\n Avg Usage by Country and Gender:")
print(df.groupby(['Country', 'Gender'])['Avg_Daily_Usage_Hours'].mean())

# Count how many students per platform
print(df.groupby('Most_Used_Platform')['Student_ID'].count())

# Total Addicted Score per Country
print(df.groupby('Country')['Addicted_Score'].sum())

# Min/Max usage per Academic Level
print(df.groupby('Academic_Level')['Avg_Daily_Usage_Hours'].agg(['min', 'max', 'mean']))
