import pandas as pd

def process_stock_data(raw_data):
    if not raw_data:
        return pd.DataFrame()
    
    if isinstance(raw_data, dict):
        raw_data = list(raw_data.values())

    df = pd.DataFrame(raw_data)

    required_cols = ["price", "volume", "buy_pressure", "timestamp", "ticker"]
    missing = [col for col in required_cols if col not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    numeric_cols = ["price", "volume", "buy_pressure"]
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")

    df["value_traded"] = df["price"] * df["volume"]
    df["price_change_pct"] = df.groupby("ticker")["price"].pct_change().fillna(0) * 100

    df = df.sort_values(by=["timestamp", "ticker"]).reset_index(drop=True)

    return df

if __name__ == "__main__":
    from I_O import get_data
    raw_data = get_data()
    print(process_stock_data(raw_data))
