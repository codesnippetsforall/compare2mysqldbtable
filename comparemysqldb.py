import pandas as pd
import mysql.connector

# Connect to the MySQL databases
source_db = mysql.connector.connect(
    host="HOST", user="USERNAME", password="PASSWORD", database="payroll_dev"
)

target_db = mysql.connector.connect(
    host="HOST", user="USERNAME", password="PASSWORD", database="payroll_qa"
)

# Define the tables to compare
source_table = "employee"
target_table = "employee"

# Fetch data from the tables
source_cursor = source_db.cursor()
source_cursor.execute(f"SELECT * FROM {source_table}")
source_data = pd.DataFrame(source_cursor.fetchall(), columns=[desc[0] for desc in source_cursor.description])

target_cursor = target_db.cursor()
target_cursor.execute(f"SELECT * FROM {target_table}")
target_data = pd.DataFrame(target_cursor.fetchall(), columns=[desc[0] for desc in target_cursor.description])

# Compare the dataframes
if source_data.equals(target_data):
    print("Tables have the same data.")
else:
    print("Tables have different data.")
