# Bluestock Mutual Fund Analytics Platform — BI Dashboard Specification

**Platform**: Power BI / Tableau  
**Theme**: Fintech Blue & Emerald (`#0A192F` / `#00D2FF` / `#10B981`)  
**Data Connection**: SQLite (`data/processed/mf_analytics.db`) / PostgreSQL

---

## 📊 Dashboard Structure (4 Pages)

### Page 1: Market Overview & AMC Benchmark Anchors
- **KPI Cards**:
  - Total Industry AUM: **₹12.5L Cr** (SBI Mutual Fund Anchor: 18.5% Market Share)
  - Dec '25 Monthly SIP Inflows: **₹31,002 Cr** milestone
  - Active Folios: **46,000+ Daily NAV records** across **40 Schemes**
- **Visuals**:
  - **AUM Bar Chart**: Market share breakdown across 10 AMCs (SBI, HDFC, ICICI, Nippon, Kotak, Axis, ABSL, UTI, Mirae, DSP).
  - **SIP Growth Trend Line**: Monthly SIP inflow trajectory from July 2025 to June 2026.
  - **Category Inflow Donut Chart**: Equity (Large, Mid, Small, Flexi) vs Debt vs Hybrid.

---

### Page 2: Fund Performance & Risk Analytics
- **KPI Cards**:
  - Average 3Y CAGR: **18.2%**
  - Average Sharpe Ratio: **1.28**
- **Visuals**:
  - **Sharpe vs. Sortino Scatter Plot**: X-axis (Sortino), Y-axis (Sharpe), Size (AUM), Tooltip (Fund Name, Alpha).
  - **Risk-Reward Bar Chart**: Value at Risk (VaR 95%) vs Maximum Drawdown per scheme.
  - **Alpha Ranking Table**: Interactive leaderboard ranking funds by 3Y CAGR and Alpha vs Nifty 50.

---

### Page 3: Investor Demographics & Regional Inflows
- **KPI Cards**:
  - Total Investor Pool: **5,000 Investors** across **12 States**
  - Youth Share (<30 Years): **31% Investors** (Highest SIP adoption)
  - Tier-2 City Growth: **+19% YoY** (Growing 2.5x faster than Tier-1)
- **Visuals**:
  - **State Choropleth Map**: Geographic density of investments (MH, KA, TN, DL, GJ top states).
  - **SIP vs Lumpsum Pie Chart**: 72% SIP vs 20% Lumpsum vs 8% Redemption volume.
  - **Age Group Demographics Bar Chart**: Volume and ticket size distribution across <30, 30-45, 45-60, 60+.

---

### Page 4: Portfolio Holdings & Sector Concentration
- **Visuals**:
  - **Sector Concentration Sunburst / Treemap**: Hierarchical view of fund portfolio weightings (Financial Services, IT, Oil & Gas, Capital Goods).
  - **Top Stock Holdings Table**: Top 10 underlying stock positions with market value in Crores.

---

## 🎨 Interactive Features
- **Slicers**: Filter by AMC, Category, Risk Grade, State, and Date Range.
- **Drill-Through**: Click on any scheme to drill through into daily NAV line charts vs Nifty 50 benchmark.
- **Tooltips**: Dynamic cards showing 1Y/3Y/5Y CAGR, Expense Ratio, and Alpha on hover.
