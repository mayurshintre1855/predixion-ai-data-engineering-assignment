"""
    Predixion AI Assignment
    Author: Mayur Netaji Shintre

    Task 1 - Data Generation
"""

import json
import random
from datetime import datetime, timedelta

# Fixed seed so output is always same
random.seed(42)

records = []

for i in range(500):

    # Generate random start time
    start_time = datetime(
        2026,
        random.randint(1, 5),
        random.randint(1, 28),
        random.randint(8, 20),
        random.randint(0, 59),
        random.randint(0, 59)
    )

    # Random call duration
    duration = random.randint(10, 900)

    end_time = start_time + timedelta(seconds=duration)

    call_record = {
        "call_id": f"CALL_{i+1}",
        "agent_id": f"AGENT_{random.randint(1,10)}",
        "customer_phone": str(random.randint(9000000000,9999999999)),
        "start_time": str(start_time),
        "end_time": str(end_time),
        "call_outcome": random.choice(
            ["connected","no_answer","dropped","callback_requested"]
        ),
        "language": random.choice(
            ["Hindi","English","Marathi"]
        ),
        "disposition_code": random.choice(
            ["PTP","FOLLOW_UP","CALL_BACK"]
        ),
        "amount_promised": random.choice(
            [None,500,1000,2000,5000]
        ),
        "retry_flag": random.choice([True,False])
    }

    records.append(call_record)

# Add Missing Fields (15%)
for i in range(int(len(records)*0.15)):
    record = random.choice(records)
    field = random.choice(list(record.keys()))

    if field in record:
        del record[field]

# Add Duplicates (5%)
for i in range(int(len(records)*0.05)):
    records.append(random.choice(records))

# Add Bad Timestamps (3%)
for i in range(int(len(records)*0.03)):
    record = random.choice(records)

    if "start_time" in record:
        record["start_time"] = "wrong_date"

# Save JSON File
with open("raw_calls.json","w") as file:
    json.dump(records,file,indent=4)

print("Dataset Generated Successfully")