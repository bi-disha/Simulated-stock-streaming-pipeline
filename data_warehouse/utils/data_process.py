def process_stock_data(raw_data):
    processed_data = {}
    for data in raw_data:
        flag = data["ticker"]
        processed_data[flag] = data
    
    return processed_data