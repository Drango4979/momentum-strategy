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

2024-07 XLC, XLF, XLK
2024-08 XLC, XLF, XLK
2024-09 XLC, XLF, XLK
2024-10 XLC, XLF, XLU
2024-11 XLC, XLF, XLU
2024-12 XLC, XLF, XLI

How many months each ETF was selected (out of total):
  XLK: 99 months
  XLY: 88 months
  XLF: 69 months
  XLV: 68 months
  XLU: 68 months
  XLE: 64 months
  XLP: 64 months
  XLI: 57 months
  XLB: 56 months
  XLC: 32 months
  XLRE: 16 months

## Notes
2008 financial market crash visible on monumentum heatmap and 2014 - 2016 energy crisis visible on monumentum heatmap