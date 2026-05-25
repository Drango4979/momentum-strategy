import pandas as pd

# Load portfolio weights
portfolio_weights = pd.read_csv("data/portfolio_weights.csv", index_col=0, parse_dates=True)

# Build a readable rebalance log
rebalance_log = []

for date, row in portfolio_weights.iterrows():
    # Get the ETFs selected that month (weight > 0)
    selected = [etf for etf, weight in row.items() if weight > 0]
    if selected:
        rebalance_log.append({
            "Date": date.strftime("%Y-%m"),
            "Top 3 ETFs": ", ".join(selected)
        })

# Convert to DataFrame
log_df = pd.DataFrame(rebalance_log)

# Save to CSV
log_df.to_csv("results/rebalance_log.csv", index=False)
print("Saved: results/rebalance_log.csv")

# Print last 12 months
print("\nLast 12 months of rebalances:")
print(log_df.tail(12).to_string(index=False))

# Count how many times each ETF was selected overall
all_selected = portfolio_weights[portfolio_weights > 0].count()
all_selected = all_selected.sort_values(ascending=False)

print("\nHow many months each ETF was selected (out of total):")
for etf, count in all_selected.items():
    print(f"  {etf}: {count} months")