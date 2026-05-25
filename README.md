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

## Notes
2008 financial market crash visible on monumentum heatmap and 2014 - 2016 energy crisis visible on monumentum heatmap