import pandas as pd
import sqlite3

# Step 1: Load CSV data
df = pd.read_csv("Students Social Media Addiction.csv")

# Step 2: Connect to SQLite database (creates file if not exists)
conn = sqlite3.connect("nba_db.sqlite")

# Step 3: Save DataFrame to SQL table named 'students'
df.to_sql(name='students', con=conn, if_exists='replace', index=False)

# Step 4: Read data back from SQL to confirm
df_from_sql = pd.read_sql("SELECT * FROM students", conn)
print(df_from_sql.head())
