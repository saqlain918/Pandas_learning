
import pandas as pd

data = pd.read_csv("Students Social Media Addiction.csv")

# Convert DataFrame to dictionary
dict_output = data.to_dict()

print("🔹 to_dict() default output:\n")
print(dict_output)

# Each row becomes a dictionary in a list
print("\n▶ Records format:")
print(data.to_dict(orient='records'))

# Columns as keys (default)
print("\n▶ Columns format:")
print(data.to_dict(orient='dict'))

# Convert to dict with split orientation
split_dict = data.to_dict(orient='split')

# Print result
print("\n🔹 to_dict with orient='split':")
print(split_dict)


# Convert to dict with index orientation
index_dict = data.to_dict(orient='index')

# Print result
print("\n🔹 to_dict with orient='index':")
print(index_dict)

# Show just first 2 rows from split dict data
print("\n▶ First 2 'data' rows from split:")
print(split_dict['data'][:2])

# Show just first 2 rows from index dict
print("\n▶ First 2 rows from index dict:")
for key in list(index_dict)[:2]:
    print(f"{key} → {index_dict[key]}")


