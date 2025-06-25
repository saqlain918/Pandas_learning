import pandas as pd
import numpy as np

df = pd.read_csv("Students Social Media Addiction.csv")

print("\n Check if any values are missing:")
print(df.isnull())

print("\n Count of missing values per column:")
print(df.isnull().sum())

df_any_dropped = df.dropna(axis=1)
print("\n Drop columns with ANY missing value:")
print(df_any_dropped.head())

df_all_dropped = df.dropna(axis=1, how='all')
print("\n Drop columns only if ALL values are missing:")
print(df_all_dropped.head())

df_filled_default = df.fillna("Not Available")
print("\n Fill missing values with 'Not Available':")
print(df_filled_default.head())

df_fill_specific = df.copy()
df_fill_specific['country'] = df['country'].fillna("Unknown country")

print("\n Fill missing 'country' values with 'Unknown country':")
print(df_fill_specific[['Name', 'country']].head())

df_num_fill = df.copy()
df_num_fill['age'] = df['age'].fillna(df['age'].mean())

print("\n💰 Fill missing 'age' with mean:")
print(df_num_fill[['Name', 'age']].head())

df_ffill = df.fillna(method='ffill')
df_bfill = df.fillna(method='bfill')

print("\n⏩ Forward Fill Example:")
print(df_ffill.head())

print("\n⏪ Backward Fill Example:")
print(df_bfill.head())

