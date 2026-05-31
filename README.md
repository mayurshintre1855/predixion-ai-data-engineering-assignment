# Predixion AI Data Engineering Assignment

## Author

Mayur Netaji Shintre

## Project Overview

This project is my solution for the Predixion AI Data Engineering Take-Home Assignment.

The goal of this project was to create a simple ETL pipeline that:

* Generates call log data
* Validates the data
* Cleans and transforms the data
* Stores the data in SQLite
* Uses SQL queries to answer business questions

This project helped me understand how ETL pipelines work in real-world data engineering projects.

---

## Tools Used

* Python
* Pandas
* SQLite
* SQL

---

## Files in the Project

* generate.py → Generates raw call data
* pipeline.py → Validates and transforms the data
* load_to_sqlite.py → Loads data into SQLite database
* analytics.py → Runs SQL queries and generates reports
* logger_setup.py → Setup file for logging
* raw_calls.json → Raw generated data
* clean_calls.csv → Cleaned data
* rejected_log.csv → Invalid records
* calls.db → SQLite database
* pipeline.log → Log file
* README.md → Project documentation

---

## Task 1 - Data Generation

I generated 500 call records with the following fields:

* call_id
* agent_id
* customer_phone
* start_time
* end_time
* call_outcome
* language
* disposition_code
* amount_promised
* retry_flag

To simulate real-world data quality issues, I intentionally added:

* Missing fields
* Duplicate records
* Invalid timestamps

---

## Task 2 - Data Validation

The pipeline checks for:

* Missing fields
* Duplicate call IDs
* Invalid timestamps

Rejected records are stored in:

rejected_log.csv

---

## Task 3 - Data Transformation

The following transformations were performed:

* Converted date and time values
* Calculated call duration
* Extracted call hour
* Extracted call date
* Identified weekends
* Created duration categories (Short, Medium, Long)
* Replaced missing amount values with 0

The cleaned data is stored in:

clean_calls.csv

---

## Task 4 - SQLite Loading

The cleaned data is loaded into a SQLite database called:

calls.db

Tables created:

* calls
* ingestion_log

---

## Task 5 - Analytics

Using SQL queries, the following business questions were answered:

1. Connect rate by language
2. Callback requested count by hour
3. Percentage of long calls
4. Average promised amount for long calls
5. Top 3 agents by total calls handled
6. Outcome distribution for top agents
7. Call volume trend across dates

Output CSV files are generated for each analysis.

---

## Task 6 - Bonus

I implemented logging to track pipeline execution.

The log file generated is:

pipeline.log

---

## How to Run the Project

### Install Packages

pip install -r requirements.txt

### Generate Data

python generate.py

### Validate and Transform Data

python pipeline.py

### Load Data into Database

python load_to_sqlite.py

### Run Analytics

python analytics.py

---

## What I Learned

Through this project I learned:

* Basic ETL concepts
* Data validation techniques
* Data cleaning using Pandas
* Working with SQLite databases
* Writing SQL queries in Python
* Generating reports from data

---

## Future Improvements

If I continue working on this project, I would like to:

* Use PostgreSQL instead of SQLite
* Add more automated tests
* Create visual dashboards
* Schedule the pipeline automatically

---

## Conclusion

This project demonstrates a complete ETL workflow using Python, SQL, Pandas, and SQLite. It helped me gain hands-on experience with data engineering concepts and data processing pipelines.
