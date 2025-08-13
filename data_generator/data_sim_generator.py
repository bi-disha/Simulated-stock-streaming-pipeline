import random
import numpy as np
import time
from datetime import datetime
# Get the timestamp
timestamp = datetime.now().isoformat()

# Configuration for multiple stocks
stock_configs = {
    "AAPL": {"price": 180.0, "avg_volume": 1200, "volatility": 2.0},
    "GOOGL": {"price": 2800.0, "avg_volume": 900, "volatility": 3.5},
    "TSLA": {"price": 700.0, "avg_volume": 1500, "volatility": 5.0},
    "INFY": {"price": 1500.0, "avg_volume": 1000, "volatility": 1.2},
    "RELIANCE": {"price": 2500.0, "avg_volume": 1300, "volatility": 2.2}
}

def simulate_stock(stock_data):
    price = stock_data["price"]
    avg_volume = stock_data["avg_volume"]
    volatility = stock_data["volatility"]

    # Simulate inputs
    volume = random.randint(int(avg_volume * 0.5), int(avg_volume * 1.5))
    buy_pressure = random.uniform(0.49, 0.75)
    delta_volume = volume - avg_volume
    sensitivity = 0.0005
    drift = 0.02  # upward bias to simulate general market growth

    # Price update
    price_change = drift + buy_pressure * delta_volume * sensitivity
    new_price = price + np.tanh(price_change) * volatility
    new_price = max(new_price, 1.0)  # prevent negative or zero prices

    stock_data["price"] = new_price  # update for next tick


    return {
        "ticker": stock_data.get("ticker", ""),
        "price": round(new_price, 2),
        "volume": volume,
        "buy_pressure": round(buy_pressure, 2)
    }

# Attach tickers to each config
for ticker in stock_configs:
    stock_configs[ticker]["ticker"] = ticker

def generate_all_stocks():
    all_data = []
    for ticker, config in stock_configs.items():
        stock_data = simulate_stock(config)
        stock_data["timestamp"] = timestamp
        all_data.append(stock_data)
    return all_data

# Example run (single tick)
if __name__ == "__main__":
    for _ in range(1):
    #while True:
        print(generate_all_stocks())
