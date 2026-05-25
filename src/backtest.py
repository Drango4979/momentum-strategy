import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load data
monthly_returns = pd.read_csv("data/monthly_returns.csv", index_col=0, parse_dates=True)
portfolio_weights = pd.read_csv("data/portfolio_weights.csv", index_col=0, parse_dates=True)

# --- Run the Backtest ---
# Weights at month t earn returns at month t+1
weights_applied = portfolio_weights.shift(1)

# Multiply each ETF weight by its return, sum across ETFs
strategy_returns = (weights_applied * monthly_returns).sum(axis=1)

# Benchmark: equal weight across all 11 ETFs
bench_returns = monthly_returns.mean(axis=1)

# Remove NaN rows at the start
strategy_returns = strategy_returns.dropna()
bench_returns = bench_returns.loc[strategy_returns.index]

# --- Performance Metrics ---
# Cumulative wealth index
cum_strategy = (1 + strategy_returns).cumprod()
cum_bench = (1 + bench_returns).cumprod()

# Annualised return
ann_return_strat = strategy_returns.mean() * 12
ann_return_bench = bench_returns.mean() * 12

# Annualised volatility
ann_vol_strat = strategy_returns.std() * np.sqrt(12)
ann_vol_bench = bench_returns.std() * np.sqrt(12)

# Sharpe ratio (4% annual risk-free rate)
rf_monthly = 0.04 / 12
sharpe_strat = (strategy_returns.mean() - rf_monthly) / strategy_returns.std() * np.sqrt(12)
sharpe_bench = (bench_returns.mean() - rf_monthly) / bench_returns.std() * np.sqrt(12)

# Maximum drawdown
rolling_max = cum_strategy.cummax()
drawdown = (cum_strategy - rolling_max) / rolling_max
max_drawdown_strat = drawdown.min()

rolling_max_bench = cum_bench.cummax()
drawdown_bench = (cum_bench - rolling_max_bench) / rolling_max_bench
max_drawdown_bench = drawdown_bench.min()

# Hit rate
hit_rate_strat = (strategy_returns > 0).mean()
hit_rate_bench = (bench_returns > 0).mean()

# Print results table
print("=" * 55)
print(f"{'Metric':<25} {'Strategy':>12} {'Benchmark':>12}")
print("=" * 55)
print(f"{'Ann. Return':<25} {ann_return_strat:>11.1%} {ann_return_bench:>11.1%}")
print(f"{'Ann. Volatility':<25} {ann_vol_strat:>11.1%} {ann_vol_bench:>11.1%}")
print(f"{'Sharpe Ratio':<25} {sharpe_strat:>12.2f} {sharpe_bench:>12.2f}")
print(f"{'Max Drawdown':<25} {max_drawdown_strat:>11.1%} {max_drawdown_bench:>11.1%}")
print(f"{'Hit Rate':<25} {hit_rate_strat:>11.1%} {hit_rate_bench:>11.1%}")
print("=" * 55)

# --- Chart 1: Cumulative Wealth Index ---
plt.figure(figsize=(14, 6))
plt.plot(cum_strategy.index, cum_strategy, label="Momentum Strategy", color="blue")
plt.plot(cum_bench.index, cum_bench, label="Benchmark (Equal Weight)", color="orange", linestyle="--")
plt.title("Cumulative Wealth Index — Momentum Strategy vs Benchmark")
plt.xlabel("Date")
plt.ylabel("Growth of $1")
plt.legend()
plt.tight_layout()
plt.savefig("results/cumulative_wealth.png", dpi=150)
plt.close()
print("Saved: results/cumulative_wealth.png")

# --- Chart 2: Monthly Drawdown ---
plt.figure(figsize=(14, 5))
plt.fill_between(drawdown.index, drawdown, 0, color="red", alpha=0.4, label="Strategy Drawdown")
plt.fill_between(drawdown_bench.index, drawdown_bench, 0, color="orange", alpha=0.3, label="Benchmark Drawdown")
plt.title("Monthly Drawdown — Momentum Strategy vs Benchmark")
plt.xlabel("Date")
plt.ylabel("Drawdown")
plt.legend()
plt.tight_layout()
plt.savefig("results/drawdown.png", dpi=150)
plt.close()
print("Saved: results/drawdown.png")

# --- Chart 3: Rolling 12-Month Sharpe Ratio ---
rolling_sharpe = (
    strategy_returns.rolling(12).mean() - rf_monthly
) / strategy_returns.rolling(12).std() * np.sqrt(12)

rolling_sharpe_bench = (
    bench_returns.rolling(12).mean() - rf_monthly
) / bench_returns.rolling(12).std() * np.sqrt(12)

plt.figure(figsize=(14, 5))
plt.plot(rolling_sharpe.index, rolling_sharpe, label="Momentum Strategy", color="blue")
plt.plot(rolling_sharpe_bench.index, rolling_sharpe_bench, label="Benchmark", color="orange", linestyle="--")
plt.axhline(y=0, color="red", linestyle="--", linewidth=0.8, label="Sharpe = 0")
plt.title("Rolling 12-Month Sharpe Ratio — Momentum Strategy vs Benchmark")
plt.xlabel("Date")
plt.ylabel("Sharpe Ratio")
plt.legend()
plt.tight_layout()
plt.savefig("results/rolling_sharpe.png", dpi=150)
plt.close()
print("Saved: results/rolling_sharpe.png")