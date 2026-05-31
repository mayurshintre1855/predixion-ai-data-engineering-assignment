"""
Predixion AI Assignment
Author: Mayur Netaji Shintre

Task 2 - Data Validation
Task 3 - Data Transformation
"""

import json
import pandas as pd
import json
import pandas as pd
import logging

# Configure logging
logging.basicConfig(
    filename="pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Pipeline Started")

# Read JSON file
with open("raw_calls.json","r") as file:
    records = json.load(file)

valid_records = []
rejected_records = []

seen_call_ids = []

required_fields = [
    "call_id",
    "agent_id",
    "customer_phone",
    "start_time",
    "end_time",
    "call_outcome",
    "language",
    "disposition_code",
    "retry_flag",
    "amount_promised"
]

# Validation
for record in records:

    # Check missing fields
    missing_field_found = False

    for field in required_fields:

        if field not in record:

            rejected_records.append({
                "call_id": record.get("call_id"),
                "reason": "missing_field"
            })

            missing_field_found = True
            break

    if missing_field_found:
        continue

    # Check duplicate call_id
    if record["call_id"] in seen_call_ids:

        rejected_records.append({
            "call_id": record["call_id"],
            "reason": "duplicate"
        })

        continue

    seen_call_ids.append(record["call_id"])

    # Check timestamp
    try:
        pd.to_datetime(record["start_time"])
        pd.to_datetime(record["end_time"])

    except:

        rejected_records.append({
            "call_id": record["call_id"],
            "reason": "bad_timestamp"
        })

        continue

    valid_records.append(record)

# Summary
print("Total Records :", len(records))
print("Valid Records :", len(valid_records))
print("Rejected Records :", len(rejected_records))
logging.info(
    f"Valid Records: {len(valid_records)}"
)

logging.info(
    f"Rejected Records: {len(rejected_records)}"
)

# Save rejected records
pd.DataFrame(rejected_records).to_csv(
    "rejected_log.csv",
    index=False
)

# ---------------------------------
# Transformations
# ---------------------------------

df = pd.DataFrame(valid_records)

# Convert datetime columns
df["start_time"] = pd.to_datetime(df["start_time"])
df["end_time"] = pd.to_datetime(df["end_time"])

# Calculate call duration
df["call_duration_seconds"] = (
    df["end_time"] - df["start_time"]
).dt.total_seconds()

# Extract hour
df["call_hour"] = df["start_time"].dt.hour

# Extract date
df["call_date"] = df["start_time"].dt.date

# Weekend flag
df["is_weekend"] = (
    df["start_time"].dt.dayofweek >= 5
)

# Duration category
def duration_bucket(seconds):

    if seconds < 60:
        return "short"

    elif seconds <= 300:
        return "medium"

    else:
        return "long"

df["duration_bucket"] = (
    df["call_duration_seconds"]
    .apply(duration_bucket)
)

# Handle null amounts
df["is_amount_imputed"] = (
    df["amount_promised"].isnull()
)

df["amount_promised"] = (
    df["amount_promised"].fillna(0)
)

# Save clean data
df.to_csv(
    "clean_calls.csv",
    index=False
)
logging.info(
    "Transformation Completed"
)

logging.info(
    f"Clean Records Saved: {len(df)}"
)

logging.info(
    "Pipeline Finished Successfully"
)

print("\nTransformation Complete")
print(df.head())
