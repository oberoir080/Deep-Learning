import yfinance as yf
from datetime import datetime, timedelta
import pandas as pd

def dump_stock_data():
    try:
        # Get current date in IST (Indian Standard Time)
        ist_tz = pd.Timestamp.now(tz='Asia/Kolkata')
        end_date = ist_tz.strftime('%Y-%m-%d')
        start_date = (ist_tz - timedelta(days=25)).strftime('%Y-%m-%d')
        
        print(f"Requesting data from {start_date} to {end_date}")
        
        # Download historical data
        ticker = yf.Ticker("ASIANPAINT.NS")
        df = ticker.history(start=start_date, end=end_date, interval='15m')
        
        if df.empty:
            print("No data returned. Trying alternative ticker RELIANCE.NS...")
            ticker = yf.Ticker("RELIANCE.NS")
            df = ticker.history(start=start_date, end=end_date, interval='15m')
        
        if df.empty:
            print("Still no data. Please check your internet connection.")
            return
            
        # Convert index to IST timezone
        df.index = pd.to_datetime(df.index).tz_convert('Asia/Kolkata')
        
        # Filter for market hours (9:15 to 15:15) and weekdays
        market_start = ((df.index.hour == 9) & (df.index.minute >= 15)) | (df.index.hour > 9)
        market_end = (df.index.hour < 15) | ((df.index.hour == 15) & (df.index.minute <= 15))
        trading_hours = market_start & market_end
        weekdays = df.index.dayofweek < 5
        
        df = df[trading_hours & weekdays]
        
        # Save to CSV
        output_file = 'stock_data4.csv'
        df.to_csv(output_file)
        print(f"Data saved to {output_file}")
        print(f"Shape of data: {df.shape}")
        print(f"Date range: {df.index.min()} to {df.index.max()}")
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    dump_stock_data()