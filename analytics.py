"""
Predixion AI Assignment
Author: Mayur Netaji Shintre

Task 5 - analytics

Question 1:
What is the connect rate by language?

"""
# Import SQLite library
import sqlite3

# Import Pandas library
import pandas as pd

# ----------------------------------------------------
# Connect to SQLite Database
# ----------------------------------------------------

conn = sqlite3.connect("calls.db")

print("Database Connected Successfully")

# ====================================================
# QUESTION 1
# What is the connect rate by language?
# ====================================================

print("\nQUESTION 1")
print("What is the connect rate by language?\n")

query1 = """

SELECT

    language,

    ROUND(

        100.0 *

        SUM(

            CASE

                WHEN call_outcome = 'connected'

                THEN 1

                ELSE 0

            END

        )

        /

        COUNT(*),

        2

    ) AS connect_rate

FROM calls

GROUP BY language

"""

# Execute SQL query
result1 = pd.read_sql(query1, conn)

# Display output
print(result1)

# Save result as CSV
result1.to_csv(
    "connect_rate.csv",
    index=False
)

# ====================================================
# QUESTION 2
# Which hour has highest callback requested count?
# ====================================================

print("\nQUESTION 2")
print("Which hour has highest callback_requested rate?\n")

query2 = """

SELECT

    call_hour,

    COUNT(*) AS callback_count

FROM calls

WHERE call_outcome = 'callback_requested'

GROUP BY call_hour

ORDER BY callback_count DESC

"""

result2 = pd.read_sql(query2, conn)

print(result2)

result2.to_csv(
    "callback_rate.csv",
    index=False
)

# ====================================================
# QUESTION 3
# Long Calls Percentage + Average Amount
# ====================================================

print("\nQUESTION 3")
print("Percentage of long calls and average amount promised\n")

query3 = """

SELECT

    ROUND(

        COUNT(*) * 100.0 /

        (SELECT COUNT(*) FROM calls),

        2

    ) AS long_call_percentage,

    ROUND(

        AVG(amount_promised),

        2

    ) AS average_amount_promised

FROM calls

WHERE duration_bucket = 'long'

"""

result3 = pd.read_sql(query3, conn)

print(result3)

result3.to_csv(
    "long_calls_analysis.csv",
    index=False
)

# ====================================================
# QUESTION 4
# Top 3 Agents by Total Calls
# ====================================================

print("\nQUESTION 4")
print("Top 3 agents by total calls handled\n")

query4 = """

SELECT

    agent_id,

    COUNT(*) AS total_calls

FROM calls

GROUP BY agent_id

ORDER BY total_calls DESC

LIMIT 3

"""

result4 = pd.read_sql(query4, conn)

print(result4)

result4.to_csv(
    "top_agents.csv",
    index=False
)

# ====================================================
# QUESTION 4A
# Outcome Distribution For Top Agents
# (Extra - Helps Impress Interviewer)
# ====================================================

print("\nQUESTION 4A")
print("Outcome distribution for top agents\n")

query4a = """

SELECT

    agent_id,

    call_outcome,

    COUNT(*) AS total

FROM calls

WHERE agent_id IN (

    SELECT agent_id

    FROM calls

    GROUP BY agent_id

    ORDER BY COUNT(*) DESC

    LIMIT 3

)

GROUP BY

    agent_id,
    call_outcome

ORDER BY

    agent_id,
    total DESC

"""

result4a = pd.read_sql(query4a, conn)

print(result4a)

result4a.to_csv(
    "top_agents_outcome_distribution.csv",
    index=False
)

# ====================================================
# QUESTION 5
# Call Volume Trend Across Dates
# ====================================================

print("\nQUESTION 5")
print("Call volume trend across dates\n")

query5 = """

SELECT

    call_date,

    COUNT(*) AS total_calls

FROM calls

GROUP BY call_date

ORDER BY call_date

"""

result5 = pd.read_sql(query5, conn)

print(result5)

result5.to_csv(
    "call_volume_trend.csv",
    index=False
)

# ----------------------------------------------------
# Close Database Connection
# ----------------------------------------------------

conn.close()

print("\nDatabase Connection Closed")

print("\nAll Analytics Completed Successfully")

print("\nGenerated Files:")

print("1. connect_rate.csv")
print("2. callback_rate.csv")
print("3. long_calls_analysis.csv")
print("4. top_agents.csv")
print("5. top_agents_outcome_distribution.csv")
print("6. call_volume_trend.csv")