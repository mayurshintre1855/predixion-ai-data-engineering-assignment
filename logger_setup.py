"""
    Predixion AI Assignment
    Author: Mayur Netaji Shintre

    Task 6 - logging per pipeline stage with timings
"""

import logging

logging.basicConfig(
    filename="pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)