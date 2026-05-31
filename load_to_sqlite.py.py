"""
Predixion AI Assignment
Author: Mayur Netaji Shintre

Task 4 - Load Data into SQLite

"""

# Import pandas
import pandas as pd

# Import SQLite
import sqlite3

# Import datetime
from datetime import datetime

# --------------------------
# Read Clean Data
# --------------------------

df = pd.read_csv("clean_calls.csv")

# --------------------------
# Connect to Database
# --------------------------

conn = sqlite3.connect("calls.db")

print("Connected to SQLite Database")

# --------------------------
# Create Calls Table
# --------------------------

df.to_sql(
    name="calls",
    con=conn,
    if_exists="replace",   # replace old table
    index=False
)

print("Calls Table Created")

# --------------------------
# Read Rejected Log
# --------------------------

rejected_df = pd.read_csv(
    "rejected_log.csv"
)

# --------------------------
# Create Ingestion Log
# --------------------------

log_data = pd.DataFrame({

    "run_timestamp":
    [datetime.now()],

    "records_processed":
    [len(df)],

    "rejected_count":
    [len(rejected_df)]

})

# Save log table

log_data.to_sql(
    name="ingestion_log",
    con=conn,
    if_exists="replace",
    index=False
)

print("Ingestion Log Created")

# --------------------------
# Close Connection
# --------------------------

conn.close()

print("Database Loaded Successfully")