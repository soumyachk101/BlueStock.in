-- ====================================================================
-- Bluestock Mutual Fund Analytics Platform - Star Schema Relational DDL
-- Database Target: SQLite / PostgreSQL
-- ====================================================================

-- 1. Dimension Table: Fund Master
CREATE TABLE IF NOT EXISTS dim_fund (
    scheme_code INTEGER PRIMARY KEY,
    scheme_name TEXT NOT NULL,
    fund_house TEXT NOT NULL,
    category TEXT NOT NULL,
    sub_category TEXT NOT NULL,
    risk_grade TEXT,
    launch_date DATE
);

-- 2. Fact Table: Daily NAV History
CREATE TABLE IF NOT EXISTS fact_nav (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    scheme_code INTEGER NOT NULL,
    date DATE NOT NULL,
    nav REAL NOT NULL,
    daily_return_pct REAL,
    FOREIGN KEY (scheme_code) REFERENCES dim_fund(scheme_code)
);

-- 3. Fact Table: AUM by Fund House
CREATE TABLE IF NOT EXISTS fact_aum (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fund_house TEXT NOT NULL,
    total_aum_in_crores REAL NOT NULL,
    market_share_percent REAL,
    as_of_date DATE NOT NULL
);

-- 4. Fact Table: Monthly SIP Inflows
CREATE TABLE IF NOT EXISTS fact_sip (
    month TEXT PRIMARY KEY,
    total_sip_inflow_crores REAL NOT NULL,
    active_sip_accounts INTEGER,
    avg_sip_amount_inr REAL
);

-- 5. Fact Table: Investor Transactions
CREATE TABLE IF NOT EXISTS fact_transactions (
    transaction_id TEXT PRIMARY KEY,
    investor_id TEXT NOT NULL,
    scheme_code INTEGER NOT NULL,
    transaction_date DATE NOT NULL,
    transaction_type TEXT NOT NULL,
    amount REAL NOT NULL,
    units REAL NOT NULL,
    nav REAL NOT NULL,
    investor_state TEXT,
    investor_age_group TEXT,
    city_tier TEXT,
    FOREIGN KEY (scheme_code) REFERENCES dim_fund(scheme_code)
);

-- Indices for Query Performance Optimization
CREATE INDEX IF NOT EXISTS idx_nav_scheme_date ON fact_nav(scheme_code, date);
CREATE INDEX IF NOT EXISTS idx_txn_investor ON fact_transactions(investor_id);
CREATE INDEX IF NOT EXISTS idx_txn_date ON fact_transactions(transaction_date);
