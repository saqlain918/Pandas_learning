import pandas as pd

# Load the dataset
df = pd.read_csv("Students Social Media Addiction.csv")

print(df.isnull())

print(df.isnull().sum())

print(df.isnull().any())

print(df.isnull().sum().sum())

print(df['Age'].isnull().sum())
