# Run17: Expanded Universe (20 Assets, 10yr Train / 5yr Test)

## Configuration Summary

**Base**: Run10 champion config (TCN_FUSION + full TAPE reward stack)
**Changes**: Asset universe expanded 10 -> 20, data split shifted

### Asset Universe (20 + cash)

| # | Ticker | Sector | Regime Role |
|---|--------|--------|-------------|
| 1 | MSFT | Tech / Software | Growth, quality |
| 2 | AAPL | Tech / Hardware | Quality, mega-cap anchor |
| 3 | NVDA | Tech / Semis | High-beta growth, AI cycle |
| 4 | GOOGL | Tech / Advertising | Growth, different revenue model |
| 5 | AMZN | E-commerce / Cloud | Consumer + enterprise |
| 6 | JPM | Banking | Rate-cycle proxy |
| 7 | BRK-B | Conglomerate | Value investing proxy |
| 8 | V | Payments | Consumer spending proxy |
| 9 | UNH | Healthcare / MCO | Defensive growth |
| 10 | JNJ | Healthcare / Pharma | Ultra-defensive |
| 11 | PG | Consumer Staples | Low-vol defensive |
| 12 | KO | Beverages | Global defensive, dividend |
| 13 | HD | Home Improvement | Housing cycle exposure |
| 14 | CAT | Construction | Infrastructure / cyclical |
| 15 | HON | Diversified Industrial | Industrial + tech crossover |
| 16 | XOM | Oil & Gas (Major) | Energy / inflation hedge |
| 17 | COP | Oil & Gas (E&P) | Higher-beta energy |
| 18 | NEE | Utilities | Clean energy, low-beta |
| 19 | GLD | Gold ETF | Crisis / inflation hedge |
| 20 | AMT | REIT / Towers | Real estate, rate-sensitive |

Sectors: Tech(5), Financials(2), Healthcare(2), Staples(2), Industrials(2), Energy(2), Utilities(1), Gold(1), REIT(1), Payments(1)

### Data Split

| Period | Range |
|--------|-------|
| Analysis start | 2009-01-01 |
| Training | ~mid-2009 to 2019-12-31 (10 years after lookback NaN drop) |
| Testing | 2020-01-01 to present (~5 years) |

### Architecture (unchanged from Run10)

- TCN_FUSION: filters=[64,96,128,128,128], dilations=[1,2,4,8,16], kernel=5
- FiLM regime conditioning
- Distributional critic (17 quantiles)
- Per-asset alpha heads with exp_tanh activation
- Dirichlet policy (21-dim: 20 assets + cash)

### Reward Stack (unchanged from Run10)

- Base return (scaled x100)
- DSR + PBRS (dsr_scalar=2.0)
- Turnover ceiling (target=0.35, penalty=0.50)
- Terminal bonus (TAPE score, signed mode, scalar=10.0)
- Lagrangian CVaR (penalty_scale=3.0)
- Drawdown controller (target=0.15, penalty_coef=1.5)

### Key Differences from Run10

| Dimension | Run10 | Run17 |
|-----------|-------|-------|
| Assets | 10 | 20 |
| Action dims | 11 (10+cash) | 21 (20+cash) |
| Obs dims | ~554 | ~1104 |
| Train period | 2016-01 to 2021-12 | 2009-mid to 2019-12 |
| Test period | 2022-01 to 2025-08 | 2020-01 to present |
| Train years | ~6 | ~10 |
| Test includes | 2022 bear market | COVID + QE + inflation + rate hikes + AI rally |

## Training Log

*(To be filled during training)*
