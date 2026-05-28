# Momentum-Strategy
A mini quant trading research project for my TY work experience at Fineco Asset Management.

### What is Momentum?
Momentum is the tendency for assets that have performed well in the recent 
past to continue outperforming in the near future, and for poor performers 
to continue underperforming.

In this project, I test a cross-sectional momentum strategy across 11 S&P 500 
sector ETFs -- each month buying the top 3 ETFs by 12-month return and holding 
them equally weighted for the following month.

### Key Observation
XLK (Technology) is the highest growing ETF in the dataset, which is unsurprising 
given the tech boom of the last decade. This is visible in the normalised price chart.

### Data & Universe
- **Source:** Yahoo Finance via yfinance
- **Universe:** 11 SPDR Sector ETFs (XLK, XLF, XLV, XLY, XLP, XLE, XLI, XLB, XLRE, XLU, XLC)
- **Period:** January 2005 -- December 2024
- **Price series:** Adjusted Close (accounts for dividends and splits)

### Data Universe

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

The universe consists of 11 SPDR Sector ETFs, each tracking a different 
sector of the S&P 500 index. All 11 ETFs trade in US dollars
meaning there is no currency conversion needed. Note that XLC launched in 
2018 and XLRE in 2015, so results before those dates only include 9-10 ETFs. 
This is a known and is reflected in the momentum 
rank heatmap.

### Best Performing ETFs in the Last 6 Months

| Date | Selected ETFs |
|---|---|
| 2024-07 | COMM, FIN, TECH |
| 2024-06 | COMM, FIN, TECH |
| 2024-09 | COMM, FIN, TECH |
| 2024-10 | COMM, FIN, UTIL |
| 2024-11 | COMM, FIN, UTIL |
| 2024-12 | COMM, FIN, IND |

The table above shows the top 3 ETFs selected by the momentum strategy 
for each of the last 6 months of the dataset. XLC (Communications) and 
XLF (Financials) appeared consistently throughout the second half of 2024, 
reflecting strong momentum in those sectors. XLK (Technology) dominated 
the earlier months before being replaced by XLU (Utilities) in October 
and XLI (Industrials) in December, suggesting a rotation out of technology 
and into more defensive and industrial sectors towards the end of 2024.

### ETF Selection Frequency (2006-2024)

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

### Monthly Rebalance Log

The full rebalance log is saved in results/rebalance_log.csv. XLK (Technology) 
dominates the selection frequency, appearing in 99 out of 228 months -- nearly 
half of all rebalances. This reflects the persistent momentum of the technology 
sector over the past 20 years, driven by the rise of mega-cap tech companies 
like Apple, Microsoft and Nvidia. XLY (Consumer Discretionary) is the second 
most selected at 88 months, benefiting from strong consumer spending trends. 
At the other end, XLRE (Real Estate) and XLC (Communications) have low counts 
partly due to their later launch dates -- XLRE in 2015 and XLC in 2018 -- 
rather than poor momentum performance.


## Chart Explanations

### Normalised Price Chart
![Normalised Prices](https://raw.githubusercontent.com/Drango4979/momentum-strategy/main/results/normalised_prices.png)

All 11 ETFs are normalised to start at a value of 100 so they can be fairly 
compared regardless of their actual price. XLK (Technology) grows the most 
over the period, reflecting the tech boom of the last two decades. The 2008 
financial crisis is clearly visible as a sharp drop across all ETFs. XLC and 
XLRE show gaps at the start as they launched after 2005.

---

### Correlation Heatmap
![Correlation Heatmap](https://raw.githubusercontent.com/Drango4979/momentum-strategy/main/results/correlation_heatmap.png)

Shows how closely each pair of ETFs moves together, on a scale of 0 to 1. 
XLK and XLC are highly correlated (0.85) as both are technology-heavy. 
XLU (Utilities) and XLE (Energy) are least correlated with the rest of the 
universe as they are driven by different factors -- interest rates and oil 
prices respectively -- rather than the broader market.

---

### Momentum Rank Heatmap
![Momentum Rank Heatmap](https://raw.githubusercontent.com/Drango4979/momentum-strategy/main/results/momentum_rank_heatmap.png)

Shows the momentum rank of each ETF every month from 2006 to 2024. 
Green = high momentum (rank 1-3), Red = low momentum (rank 9-11). 
XLK (Technology) appears green for long stretches, reflecting persistent 
momentum in the tech sector. XLC and XLRE show grey areas at the start 
as they launched after 2005 and require 12 months of data before a valid 
signal can be calculated.

---

### Cumulative Wealth Index
![Cumulative Wealth](https://raw.githubusercontent.com/Drango4979/momentum-strategy/main/results/cumulative_wealth.png)

Shows how $1 invested in 2006 would have grown over time. The blue line 
is the momentum strategy and the orange dashed line is the equal-weight 
benchmark. Both lines track each other closely, consistent with the results 
table showing similar annualised returns of 10.4% vs 10.5%. The 2008 
financial crisis is the most significant drawdown period for both.

---

### Drawdown Chart
![Drawdown](https://raw.githubusercontent.com/Drango4979/momentum-strategy/main/results/drawdown.png)

The drawdown chart shows how far each portfolio fell from its previous peak 
at any given point in time. A value of 0% means the portfolio is at an 
all-time high. A value of -43% means the portfolio is 43% below its 
previous peak.

### Key Drawdown Events
- **2008-2009 Financial Crisis** -- the largest drawdown for both portfolios.
  The momentum strategy fell -43.0% while the benchmark fell -49.1%, meaning
  the momentum strategy protected capital better during the worst crash in 
  modern financial history.
- **2020 COVID Crash** -- a sharp but short drawdown visible for both 
  portfolios. Markets recovered quickly as governments and central banks 
  intervened.
- **2022 Rate Hike Selloff** -- as the US Federal Reserve aggressively raised 
  interest rates to fight inflation, both portfolios experienced a notable 
  drawdown.

---

### Rolling 12-Month Sharpe Ratio
![Rolling Sharpe](https://raw.githubusercontent.com/Drango4979/momentum-strategy/main/results/rolling_sharpe.png)

Shows the risk-adjusted return over every rolling 12-month window. Above 0 
means the strategy generated positive risk-adjusted returns. Both lines go 
deeply negative around 2008 as the financial crisis destroyed returns across 
all sectors. Overall the strategy and benchmark track each other closely, 
consistent with a Sharpe ratio of 0.43 vs 0.44.

---

## Profit Analysis

### Performance Metrics

The momentum strategy was tested against an equal-weight benchmark across 
all 11 sector ETFs from 2005 to 2024. The strategy rebalances monthly into 
the top 3 ETFs by 12-month momentum score, with each position equally weighted 
at one third of the portfolio. The results below compare the strategy against 
simply holding all 11 ETFs in equal weights and rebalancing monthly.

| Metric | Strategy | Benchmark |
|---|---|---|
| Ann. Return | 10.4% | 10.5% |
| Ann. Volatility | 15.0% | 14.8% |
| Sharpe Ratio | 0.43 | 0.44 |
| Max Drawdown | -43.0% | -49.1% |
| Hit Rate | 62.1% | 65.4% |

If you had invested $1,000 in January 2005:

| | Momentum Strategy |
|---|---|
| Starting Investment | $1,000 |
| Final Value (December 2024) | $6,354 |
| Total Profit | $5,354 |
| Annualised Return | 10.4% |
| Worst Loss from Peak | -43.0% |

Over approximately 20 years, the momentum strategy turned $1,000 into $6,354 --
a total profit of $5,354. This represents a 535% return on the original 
investment, driven by consistent monthly rebalancing into the top performing 
sectors. The strategy achieved this while limiting the worst drawdown to -43.0%, 
outperforming the equal-weight benchmark which fell -49.1% at its worst point 
during the 2008 financial crisis.

### AI Tools Used

This project was built using AI assistance.

**GitHub Copilot**
Used throughout the project for boilerplate code, docstrings, and README 
drafting. All generated code was looked at before pushing

**Claude (Anthropic)**
Used to assist with code structure, explanations
