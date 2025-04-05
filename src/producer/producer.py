import yfinance as yf
import json
import time
from azure.eventhub import EventHubProducerClient, EventData
import os

EVENT_HUB_CONNECTION_STRING = os.getenv("EVENT_HUB_CONNECTION_STRING")
event_hub_name = "stock-data"
tickers = ["AAPL", "TSLA", "NVDA", "MSFT", "GOOGL", "AMZN", "META", "AMD", "INTC", "PYPL", "DIS", "NFLX"]

producer = EventHubProducerClient.from_connection_string(EVENT_HUB_CONNECTION_STRING, eventhub_name=event_hub_name)

def fetch_and_send_stock_data(ticker):
    stock = yf.Ticker(ticker)
    data = stock.history(period="1d", interval="1m").tail(1)
    
    if data.empty:
        print(f"No data for {ticker}")
        return

    for index, row in data.iterrows():
        msg = {
            "ticker": ticker,
            "price": float(row["Close"]),
            "timestamp": index.isoformat()
        }
        event_data = EventData(json.dumps(msg))
        producer.send_batch([event_data])
        print(f"Sent: {msg}")

try:
    while True:
        for ticker in tickers:
            fetch_and_send_stock_data(ticker)
        time.sleep(60)  # 1-minute pause to match data interval
except KeyboardInterrupt:
    print("Stopped by user.")
finally:
    producer.close()
    print("Producer closed.")