# Momentum-Strategy
A mini quant trading research project for my TY work experience at Fineco Asset Management.

## What is Momentum?
Momentum is the tendency for assets that have performed well in the recent 
past to continue outperforming in the near future, and for poor performers 
to continue underperforming.

In this project, I test a cross-sectional momentum strategy across 11 S&P 500 
sector ETFs -- each month buying the top 3 ETFs by 12-month return and holding 
them equally weighted for the following month.

## Key Observation
XLK (Technology) is the highest growing ETF in the dataset, which is unsurprising 
given the tech boom of the last decade. This is visible in the normalised price chart.

## Data & Universe
- **Source:** Yahoo Finance via yfinance
- **Universe:** 11 SPDR Sector ETFs (XLK, XLF, XLV, XLY, XLP, XLE, XLI, XLB, XLRE, XLU, XLC)
- **Period:** January 2005 -- December 2024
- **Price series:** Adjusted Close (accounts for dividends and splits)

## Data Universe

| Ticker | ETF Name | Sector |
|---|---|---|
| XLK | Technology Select Sector | Information Technology |
| XLF | Financial Select Sector | Financials |
| XLV | Health Care Select Sector | Health Care |
| XLY | Consumer Discret. Select | Consumer Discretionary |
| XLP | Consumer Staples Select | Consumer Staples |
| XLE | Energy Select Sector | Energy |
| XLI | Industrial Select Sector | Industrials |
| XLB | Materials Select Sector | Materials |
| XLRE | Real Estate Select Sector | Real Estate |
| XLU | Utilities Select Sector | Utilities |
| XLC | Comm. Services Select | Communication Services |

## best performing EFT's in the last 6 months 

| Date | Selected ETFs |
|---|---|
| 2024-07 | XLC, XLF, XLK |
| 2024-08 | XLC, XLF, XLK |
| 2024-09 | XLC, XLF, XLK |
| 2024-10 | XLC, XLF, XLU |
| 2024-11 | XLC, XLF, XLU |
| 2024-12 | XLC, XLF, XLI |

## ETF Selection Frequency (2006-2024)

| Ticker | Months Selected | Sector |
|---|---|---|
| XLK | 99 | Technology |
| XLY | 88 | Consumer Discretionary |
| XLF | 69 | Financials |
| XLV | 68 | Health Care |
| XLU | 68 | Utilities |
| XLE | 64 | Energy |
| XLP | 64 | Consumer Staples |
| XLI | 57 | Industrials |
| XLB | 56 | Materials |
| XLC | 32 | Communications |
| XLRE | 16 | Real Estate |


## Chart Explanations

### Normalised Price Chart
![Normalised Prices](https://raw.githubusercontent.com/KBucur/momentum-strategy/main/results/normalised_prices.png)

All 11 ETFs are normalised to start at a value of 100 so they can be fairly 
compared regardless of their actual price. XLK (Technology) grows the most 
over the period, reflecting the tech boom of the last two decades. The 2008 
financial crisis is clearly visible as a sharp drop across all ETFs. XLC and 
XLRE show gaps at the start as they launched after 2005.

---

### Correlation Heatmap
![Correlation Heatmap](https://raw.githubusercontent.com/KBucur/momentum-strategy/main/results/correlation_heatmap.png)

Shows how closely each pair of ETFs moves together, on a scale of 0 to 1. 
XLK and XLC are highly correlated (0.85) as both are technology-heavy. 
XLU (Utilities) and XLE (Energy) are least correlated with the rest of the 
universe as they are driven by different factors -- interest rates and oil 
prices respectively -- rather than the broader market.

---

### Momentum Rank Heatmap
![Momentum Rank Heatmap](https://raw.githubusercontent.com/KBucur/momentum-strategy/main/results/momentum_rank_heatmap.png)

Shows the momentum rank of each ETF every month from 2006 to 2024. 
Green = high momentum (rank 1-3), Red = low momentum (rank 9-11). 
XLK (Technology) appears green for long stretches, reflecting persistent 
momentum in the tech sector. XLC and XLRE show grey areas at the start 
as they launched after 2005 and require 12 months of data before a valid 
signal can be calculated.

---

### Cumulative Wealth Index
![Cumulative Wealth](https://raw.githubusercontent.com/KBucur/momentum-strategy/main/results/cumulative_wealth.png)

Shows how $1 invested in 2006 would have grown over time. The blue line 
is the momentum strategy and the orange dashed line is the equal-weight 
benchmark. Both lines track each other closely, consistent with the results 
table showing similar annualised returns of 10.4% vs 10.5%. The 2008 
financial crisis is the most significant drawdown period for both.

---

### Drawdown Chart
![Drawdown](https://raw.githubusercontent.com/KBucur/momentum-strategy/main/results/drawdown.png)

Shows how far each portfolio fell from its previous peak at any given point. 
0% means the portfolio is at an all-time high. The momentum strategy reached 
a maximum drawdown of -43.0% versus -49.1% for the benchmark, meaning it 
offered better downside protection during the worst periods -- most notably 
the 2008 financial crisis.

---

### Rolling 12-Month Sharpe Ratio
![Rolling Sharpe](https://raw.githubusercontent.com/KBucur/momentum-strategy/main/results/rolling_sharpe.png)

Shows the risk-adjusted return over every rolling 12-month window. Above 0 
means the strategy generated positive risk-adjusted returns. Both lines go 
deeply negative around 2008 as the financial crisis destroyed returns across 
all sectors. Overall the strategy and benchmark track each other closely, 
consistent with a Sharpe ratio of 0.43 vs 0.44.

---

### Monthly Rebalance Log
The full rebalance log is saved in results/rebalance_log.csv. XLK (Technology) 
was selec



## Notes
2008 financial market crash visible on monumentum heatmap and 2014 - 2016 energy crisis visible on monumentum heatmap