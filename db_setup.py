import pandas as pd
import sqlite3

# 1. Load the raw CSV data
df = pd.read_csv("raw_jobs.csv")

# 2. Connect to SQLite Database (It will automatically create the file)
conn = sqlite3.connect("jobs_market.db")

# 3. Convert the DataFrame into an SQL Table named 'job_postings'
df.to_sql("job_postings", conn, if_exists="replace", index=False)

print("✅ Success! Your SQL Database (jobs_market.db) has been created.")
conn.close()