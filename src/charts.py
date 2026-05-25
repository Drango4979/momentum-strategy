import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the saved price data
prices = pd.read_csv("data/sector_etf_prices.csv", index_col=0, parse_dates=True)

# --- Chart 1: Normalised Price Series ---
# Normalise each ETF to start at 100 so we can compare them fairly
normalised = prices.div(prices.iloc[0]) * 100

plt.figure(figsize=(14, 7))
for ticker in normalised.columns:
    plt.plot(normalised.index, normalised[ticker], label=ticker)

plt.title("SPDR Sector ETFs — Normalised Price Series (Base = 100)")
plt.xlabel("Date")
plt.ylabel("Normalised Price")
plt.legend(loc="upper left", fontsize=8)
plt.tight_layout()
plt.savefig("results/normalised_prices.png", dpi=150)
plt.close()
print("Saved: results/normalised_prices.png")

# --- Chart 2: Correlation Heatmap of Monthly Returns ---
# Resample to month-end and calculate returns
monthly_prices = prices.resample("ME").last()
monthly_returns = monthly_prices.pct_change().dropna()

plt.figure(figsize=(10, 8))
sns.heatmap(
    monthly_returns.corr(),
    annot=True,
    fmt=".2f",
    cmap="coolwarm",
    center=0,
    square=True
)
plt.title("Correlation Heatmap — Monthly Returns (2005–2024)")
plt.tight_layout()
plt.savefig("results/correlation_heatmap.png", dpi=150)
plt.close()
print("Saved: results/correlation_heatmap.png")