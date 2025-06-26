import pandas as pd
df = pd.read_csv("Students Social Media Addiction.csv")



print("👥 Gender Distribution:")
print(df['Gender'].value_counts())

print("📱 Platform Usage:")
print(df['Most_Used_Platform'].value_counts())
