import pandas as pd

data = pd.read_csv("Students Social Media Addiction.csv")

# Convert DataFrame to string
string_output = data.to_string()

# Print it
print("🔹 to_string() output:\n")
print(string_output)
