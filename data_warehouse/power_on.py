import time
#from utils import get_data,process_data,load_data
import sqlite3

db_path="data_warehouse/database/stocks.db"
stocks_list = ["AAPL","GOOGL","TSLA","INFY","RELIANCE"]

#{'ticker': 'AAPL', 'price': np.float64(179.77), 'volume': 694, 'buy_pressure': 0.53, 'timestamp': '2025-08-13T14:54:51.607020'}

def warehouse_power_on():
    """
    Function to power on the data warehouse system.
    This function initializes the necessary components and services
    required for the data warehouse to operate.
    """
    print("Powering on the data warehouse...")
    
    # Initialize database connections
    initialize_database_connections()
    
    # Start data ingestion services
    #start_data_ingestion_services()



#def start_data_ingestion_services(power):
#    while power:
#        data = get_data()
#        load_data(process_data(data))
#        time.sleep(5)

def initialize_database_connections():
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    for stock in stocks_list:
        query = f"""
            CREATE TABLE IF NOT EXISTS {stock} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                ticker TEXT,
                price REAL,
                volume INT,
                buy_pressure REAL,
                timestamp TEXT
                )"""
        cur.execute(query)
        conn.commit()
        print(f"{stock} table created successfully")
    print("All tables created successfully")

warehouse_power_on()