import pandas as pd
import numpy as np

# Load saved price data
prices = pd.read_csv("data/sector_etf_prices.csv", index_col=0, parse_dates=True)

# Step 1 — Resample daily prices to month-end
monthly_prices = prices.resample("ME").last()
print(f"Monthly prices shape: {monthly_prices.shape}")

# Step 2 — Calculate monthly returns
monthly_returns = monthly_prices.pct_change()
print("Monthly returns calculated")

# Step 3 — Calculate 12-1 momentum signal
def momentum_12_1(returns):
    # Rolling 12-month compounded return, skip most recent month
    raw_mom = returns.rolling(12).apply(lambda x: (1 + x).prod() - 1)
    return raw_mom.shift(1)

momentum = momentum_12_1(monthly_returns)
print("Momentum signal calculated")

# Step 4 — Rank ETFs each month (1 = highest momentum)
ranks = momentum.rank(axis=1, ascending=False)

# Step 5 — Pick top 3 ETFs and assign equal weights
top3_mask = ranks <= 3
portfolio_weights = top3_mask.div(top3_mask.sum(axis=1), axis=0)

# Save for use in backtest
monthly_returns.to_csv("data/monthly_returns.csv")
portfolio_weights.to_csv("data/portfolio_weights.csv")
print("Saved monthly returns and portfolio weights")

# Sanity check — print last 6 months of weights
print("\nLast 6 months of portfolio weights:")
print(portfolio_weights.tail(6).to_string())