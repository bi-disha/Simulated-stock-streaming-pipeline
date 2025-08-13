#Checking data from data base
import sqlite3
import sys

db_path = r"data_warehouse/database/stocks.db"
table_names = ["AAPL","GOOGL","TSLA","INFY","RELIANCE"]

conn = None

try:
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    for table in table_names:
        print(f"Attempting to query data from table: {table}...")
        cursor.execute(f"SELECT * FROM {table};")

        column_names = [description[0] for description in cursor.description]
        rows = cursor.fetchmany(5)

        print("\nQuery successful. Displaying results:")
        print(" | ".join(column_names))
        print("-" * (len(" | ".join(column_names)) + 2))
        for row in rows:
            row_strings = [str(item) for item in row]
            print(" | ".join(row_strings))

except sqlite3.OperationalError as e:
    print(f"SQLite Operational Error: {e}")
    print(f"Please ensure the table '{table}' exists in the database.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    print("Unexpected error:", sys.exc_info()[0])
    
finally:
    if conn:
        print("\nClosing the database connection.")
        conn.close()

