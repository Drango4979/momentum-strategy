import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load portfolio weights to recalculate ranks
monthly_returns = pd.read_csv("data/monthly_returns.csv", index_col=0, parse_dates=True)

# Recalculate momentum and ranks
def momentum_12_1(returns):
    raw_mom = returns.rolling(12).apply(lambda x: (1 + x).prod() - 1)
    return raw_mom.shift(1)

momentum = momentum_12_1(monthly_returns)
ranks = momentum.rank(axis=1, ascending=False)

# Plot heatmap
plt.figure(figsize=(16, 6))
sns.heatmap(
    ranks.T,
    cmap="RdYlGn_r",
    linewidths=0.1,
    cbar_kws={"label": "Rank (1=highest momentum)"}
)
plt.title("Monthly Momentum Rankings — SPDR Sector ETFs (2006–2024)")
plt.xlabel("Date")
plt.ylabel("ETF")
plt.tight_layout()
plt.savefig("results/momentum_rank_heatmap.png", dpi=150)
plt.close()
print("Saved: results/momentum_rank_heatmap.png")