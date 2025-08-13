import sqlite3

conn = sqlite3.connect(r"data_warehouse/database/stocks.db")
cursor = conn.cursor()

def load_data(data):
    for stock in data.keys():
        stock_data =data[stock]
        
        query =f"INSERT INTO {stock} (ticker, price, volume, buy_pressure, timestamp) VALUES (?, ?, ?, ?, ?)"
        data_to_insert = (
        stock_data['ticker'],
        stock_data['price'],
        stock_data['volume'],
        stock_data['buy_pressure'],
        stock_data['timestamp']
    )
        cursor.execute(query,data_to_insert)
    conn.commit()