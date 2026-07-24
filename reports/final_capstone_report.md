# Bluestock Fintech — Mutual Fund Analytics Platform Capstone Report

**Author**: Soumya Chakraborty  
**Project**: Capstone Project I — Mutual Fund Analytics  
**Organization**: Bluestock Fintech  
**Data Sources**: AMFI India, `mfapi.in` REST API, Public Stock Benchmarks  

---

## 1. Executive Summary

This project delivers an end-to-end, full-stack Mutual Fund Analytics Platform analyzing Indian mutual fund industry dynamics across **10 real Asset Management Companies (AMCs)**, **40 schemes**, **44,000+ daily NAV records**, **32,000 transaction events**, and **5,000 investors** across 12 Indian states.

### Key Milestones Achieved:
- **AUM Anchor**: Industry AUM modeled with SBI Mutual Fund leading at **₹12.5L Cr AUM** (18.5% market share).
- **SIP Velocity**: Dec '25 monthly SIP inflows anchored at **₹31,002 Cr** across 93.2M active accounts.
- **Mid-Cap Alpha**: Mid-cap equity funds demonstrated a **3.2% alpha outperformance** over large-cap benchmarks on a 3-year rolling basis.
- **Demographics**: 31% of retail investors are under 30 years old, representing the highest monthly SIP growth rate (+19% YoY in Tier-2 cities).

---

## 2. Architecture & Data Pipeline (ETL)

```
[Raw Sources: mfapi.in + 10 CSVs]
         │
         ▼
[data_ingestion.py & live_nav_fetch.py]
         │
         ▼
[etl_pipeline.py (Cleaning, Imputation, Derived Metrics)]
         │
         ▼
[SQLite DB: data/processed/mf_analytics.db (Star Schema)]
  ├── dim_fund
  ├── fact_nav
  ├── fact_aum
  ├── fact_sip
  └── fact_transactions
```

---

## 3. Risk & Performance Analytical Summary

| Metric | Benchmark / Average | Top Performing Category | Key Finding |
| --- | --- | --- | --- |
| **3Y CAGR** | 18.2% | Mid Cap Equity (21.0%) | Outperformed Large Cap by +3.2% Alpha |
| **Sharpe Ratio** | 1.28 | Large & Mid Cap | Strong risk-adjusted returns (Rf = 6.5%) |
| **Sortino Ratio** | 1.64 | Flexi Cap | Minimal downside volatility |
| **Value at Risk (95%)** | -1.85% (Daily) | Liquid Funds (-0.05%) | Low daily capital loss risk |
| **Max Drawdown** | -14.2% | Large Cap | Lower drawdowns during market corrections |

---

## 4. 12-Slide Presentation Outline

1. **Slide 1**: Title & Project DNA (Bluestock Fintech Capstone).
2. **Slide 2**: Executive Summary & Industry Anchor (₹12.5L Cr AUM, ₹31k Cr SIP).
3. **Slide 3**: Data Architecture & Star Schema Model (`mf_analytics.db`).
4. **Slide 4**: AMC Market Share Analysis (SBI, HDFC, ICICI, Nippon, Kotak, Axis, ABSL, UTI, Mirae, DSP).
5. **Slide 5**: Monthly SIP Inflow Trajectory (Dec '25 ₹31,002 Cr milestone).
6. **Slide 6**: Fund Performance Leaderboard (CAGR 1Y/3Y/5Y).
7. **Slide 7**: Risk Metrics Analysis (Sharpe vs Sortino Scatter Plot).
8. **Slide 8**: VaR 95% & Max Drawdown Stress Testing.
9. **Slide 9**: Investor Demographic Breakdown (31% Under 30, Ticket Sizes).
10. **Slide 10**: Geographic Expansion (Tier-2 Cities +19% YoY, MH/KA/TN/DL/GJ).
11. **Slide 11**: Benchmark Tracking & Portfolio Sector Concentration.
12. **Slide 12**: Platform Conclusion & Business Strategic Recommendations.
