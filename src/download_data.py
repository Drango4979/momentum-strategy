import yfinance as yf
import pandas as pd

# The 11 SPDR Sector ETFs we are tracking
tickers = ["XLK", "XLF", "XLV", "XLY", "XLP", "XLE", "XLI", "XLB", "XLRE", "XLU", "XLC"]

print("Downloading ETF price data from Yahoo Finance...")

# Download historical data from 2005 to end of 2024
# auto_adjust=False so we can manually select Adj Close
raw = yf.download(tickers, start="2005-01-01", end="2024-12-31", auto_adjust=False)

# Always use Adj Close — it accounts for dividends and splits
prices = raw["Adj Close"]

print(f"Downloaded {len(prices)} rows and {len(prices.columns)} ETFs")
print(prices.head())

# Save to CSV so i don't have to re-download every time
prices.to_csv("data/sector_etf_prices.csv")
print("Saved to data/sector_etf_prices.csv")