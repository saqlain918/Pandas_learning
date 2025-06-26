import pandas as pd

data = pd.read_csv("Students Social Media Addiction.csv")

#Full data frame
df = pd.DataFrame(data)
print("Full DataFrame:")
print(df)

print("\n🔹 df.head()")
print(df.head())

print("\n🔹 df.head()")
print(df.head(10))

print("\n🔹 df.head()")
print(df.head(0))

print("\n🔹 df.head()")
print(df.head(800))

print("\n🔹 df.head()")
print(df.head(-1))

print("\n🔹 df.tail()")
print(df.tail())

print("\n🔹 df.tail()")
print(df.tail(0))

print("\n🔹 df.tail()")
print(df.tail(3))

print("\n🔹 df.tail()")
print(df.tail(-2))

print("\n🔹 df.tail()")
print(df.tail(820))

