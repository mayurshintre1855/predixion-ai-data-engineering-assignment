import sqlite3
import pandas as pd

conn = sqlite3.connect("calls.db")

df = pd.read_sql(
    "SELECT * FROM calls LIMIT 5",
    conn
)

print(df)

conn.close()