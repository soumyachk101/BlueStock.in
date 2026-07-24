import os
import random
import numpy as np
import pandas as pd
from datetime import datetime, timedelta

# Seed for reproducibility
random.seed(42)
np.random.seed(42)

RAW_DIR = "data/raw"
os.makedirs(RAW_DIR, exist_ok=True)

# 1. 10 AMCs
AMCS = [
    "SBI Mutual Fund", "HDFC Mutual Fund", "ICICI Prudential Mutual Fund",
    "Nippon India Mutual Fund", "Kotak Mahindra Mutual Fund", "Axis Mutual Fund",
    "Aditya Birla Sun Life Mutual Fund", "UTI Mutual Fund",
    "Mirae Asset Mutual Fund", "DSP Mutual Fund"
]

# 2. 40 Schemes Across Categories
CATEGORIES = {
    "Equity Scheme": ["Large Cap Fund", "Mid Cap Fund", "Small Cap Fund", "Flexi Cap Fund"],
    "Debt Scheme": ["Liquid Fund", "Corporate Bond Fund", "Short Duration Fund"],
    "Hybrid Scheme": ["Aggressive Hybrid Fund", "Arbitrage Fund"]
}

RISK_GRADES = ["Low", "Moderate", "High", "Very High"]

# Generate 40 Schemes
schemes = []
start_code = 118001

for i, amc in enumerate(AMCS):
    # 4 schemes per AMC
    amc_short = amc.split()[0]
    subcats = [
        ("Equity Scheme", "Large Cap Fund", "Very High"),
        ("Equity Scheme", "Mid Cap Fund", "Very High"),
        ("Equity Scheme", "Flexi Cap Fund", "High"),
        ("Debt Scheme" if i % 2 == 0 else "Hybrid Scheme", "Liquid Fund" if i % 2 == 0 else "Aggressive Hybrid Fund", "Moderate" if i % 2 == 0 else "High")
    ]
    
    for cat, subcat, risk in subcats:
        code = start_code
        start_code += 150
        name = f"{amc_short} {subcat.replace(' Fund', '')} - Direct Plan - Growth"
        launch_yr = random.randint(2005, 2018)
        launch_date = f"{launch_yr}-01-01"
        schemes.append({
            "scheme_code": code,
            "scheme_name": name,
            "fund_house": amc,
            "category": cat,
            "sub_category": subcat,
            "risk_grade": risk,
            "launch_date": launch_date
        })

df_fund_master = pd.DataFrame(schemes)
df_fund_master.to_csv(os.path.join(RAW_DIR, "01_fund_master.csv"), index=False)
print(f"Generated 01_fund_master.csv with {len(df_fund_master)} schemes across 10 AMCs.")

# 3. 02_nav_history.csv (46k+ daily NAV records)
# Generate ~1200 days per scheme for 40 schemes = 48,000 NAV records
end_date = datetime(2026, 7, 24)
start_date = end_date - timedelta(days=1200)
date_range = pd.date_range(start=start_date, end=end_date, freq='B') # Business days

nav_records = []
for scheme in schemes:
    code = scheme["scheme_code"]
    base_nav = random.uniform(20.0, 150.0)
    current_nav = base_nav
    
    # Generate random walk with drift
    returns = np.random.normal(0.0004, 0.012, size=len(date_range))
    for d, r in zip(date_range, returns):
        current_nav = max(5.0, current_nav * (1 + r))
        nav_records.append({
            "scheme_code": code,
            "date": d.strftime("%Y-%m-%d"),
            "nav": round(current_nav, 4),
            "repurchase_price": round(current_nav, 4),
            "sale_price": round(current_nav, 4)
        })

df_nav_history = pd.DataFrame(nav_records)
df_nav_history.to_csv(os.path.join(RAW_DIR, "02_nav_history.csv"), index=False)
print(f"Generated 02_nav_history.csv with {len(df_nav_history)} NAV rows.")

# 4. 03_aum_by_fund_house.csv (Anchored by SBI ₹12.5L Cr AUM)
aum_data = [
    {"fund_house": "SBI Mutual Fund", "total_aum_in_crores": 1250000.0, "market_share_percent": 18.5, "as_of_date": "2026-06-30"},
    {"fund_house": "ICICI Prudential Mutual Fund", "total_aum_in_crores": 890000.0, "market_share_percent": 13.2, "as_of_date": "2026-06-30"},
    {"fund_house": "HDFC Mutual Fund", "total_aum_in_crores": 820000.0, "market_share_percent": 12.1, "as_of_date": "2026-06-30"},
    {"fund_house": "Nippon India Mutual Fund", "total_aum_in_crores": 540000.0, "market_share_percent": 8.0, "as_of_date": "2026-06-30"},
    {"fund_house": "Kotak Mahindra Mutual Fund", "total_aum_in_crores": 460000.0, "market_share_percent": 6.8, "as_of_date": "2026-06-30"},
    {"fund_house": "Axis Mutual Fund", "total_aum_in_crores": 340000.0, "market_share_percent": 5.0, "as_of_date": "2026-06-30"},
    {"fund_house": "Aditya Birla Sun Life Mutual Fund", "total_aum_in_crores": 320000.0, "market_share_percent": 4.7, "as_of_date": "2026-06-30"},
    {"fund_house": "UTI Mutual Fund", "total_aum_in_crores": 290000.0, "market_share_percent": 4.3, "as_of_date": "2026-06-30"},
    {"fund_house": "Mirae Asset Mutual Fund", "total_aum_in_crores": 250000.0, "market_share_percent": 3.7, "as_of_date": "2026-06-30"},
    {"fund_house": "DSP Mutual Fund", "total_aum_in_crores": 180000.0, "market_share_percent": 2.7, "as_of_date": "2026-06-30"}
]
df_aum = pd.DataFrame(aum_data)
df_aum.to_csv(os.path.join(RAW_DIR, "03_aum_by_fund_house.csv"), index=False)
print("Generated 03_aum_by_fund_house.csv.")

# 5. 04_monthly_sip.csv (Anchored by Dec '25 ₹31,002 Cr)
sip_data = [
    {"month": "2025-07", "total_sip_inflow_crores": 23500.0, "active_sip_accounts": 81200000, "avg_sip_amount_inr": 2350},
    {"month": "2025-08", "total_sip_inflow_crores": 24800.0, "active_sip_accounts": 83400000, "avg_sip_amount_inr": 2380},
    {"month": "2025-09", "total_sip_inflow_crores": 26100.0, "active_sip_accounts": 85900000, "avg_sip_amount_inr": 2410},
    {"month": "2025-10", "total_sip_inflow_crores": 27900.0, "active_sip_accounts": 88100000, "avg_sip_amount_inr": 2440},
    {"month": "2025-11", "total_sip_inflow_crores": 29400.0, "active_sip_accounts": 90500000, "avg_sip_amount_inr": 2470},
    {"month": "2025-12", "total_sip_inflow_crores": 31002.0, "active_sip_accounts": 93200000, "avg_sip_amount_inr": 2500},
    {"month": "2026-01", "total_sip_inflow_crores": 31800.0, "active_sip_accounts": 94800000, "avg_sip_amount_inr": 2520},
    {"month": "2026-02", "total_sip_inflow_crores": 32500.0, "active_sip_accounts": 96100000, "avg_sip_amount_inr": 2540},
    {"month": "2026-03", "total_sip_inflow_crores": 33200.0, "active_sip_accounts": 97800000, "avg_sip_amount_inr": 2560},
    {"month": "2026-04", "total_sip_inflow_crores": 34100.0, "active_sip_accounts": 99200000, "avg_sip_amount_inr": 2580},
    {"month": "2026-05", "total_sip_inflow_crores": 34900.0, "active_sip_accounts": 100800000, "avg_sip_amount_inr": 2600},
    {"month": "2026-06", "total_sip_inflow_crores": 35800.0, "active_sip_accounts": 102400000, "avg_sip_amount_inr": 2620}
]
df_sip = pd.DataFrame(sip_data)
df_sip.to_csv(os.path.join(RAW_DIR, "04_monthly_sip.csv"), index=False)
print("Generated 04_monthly_sip.csv.")

# 6. 05_category_inflows.csv
cat_inflows = []
months = ["2026-04", "2026-05", "2026-06"]
for m in months:
    cat_inflows.append({"month": m, "category": "Equity Scheme", "sub_category": "Large Cap Fund", "net_inflow_crores": 3450.5})
    cat_inflows.append({"month": m, "category": "Equity Scheme", "sub_category": "Mid Cap Fund", "net_inflow_crores": 4890.2})
    cat_inflows.append({"month": m, "category": "Equity Scheme", "sub_category": "Small Cap Fund", "net_inflow_crores": 5120.0})
    cat_inflows.append({"month": m, "category": "Equity Scheme", "sub_category": "Flexi Cap Fund", "net_inflow_crores": 6210.8})
    cat_inflows.append({"month": m, "category": "Debt Scheme", "sub_category": "Liquid Fund", "net_inflow_crores": -1850.4})
    cat_inflows.append({"month": m, "category": "Hybrid Scheme", "sub_category": "Arbitrage Fund", "net_inflow_crores": 2340.1})

df_cat_inflows = pd.DataFrame(cat_inflows)
df_cat_inflows.to_csv(os.path.join(RAW_DIR, "05_category_inflows.csv"), index=False)
print("Generated 05_category_inflows.csv.")

# 7. 06_folio_count.csv
folios = []
for s in schemes:
    ret = random.randint(100000, 2500000)
    hni = random.randint(10000, 150000)
    inst = random.randint(500, 5000)
    folios.append({
        "scheme_code": s["scheme_code"],
        "scheme_name": s["scheme_name"],
        "retail_folios": ret,
        "hni_folios": hni,
        "institutional_folios": inst,
        "total_folios": ret + hni + inst
    })
df_folios = pd.DataFrame(folios)
df_folios.to_csv(os.path.join(RAW_DIR, "06_folio_count.csv"), index=False)
print("Generated 06_folio_count.csv.")

# 8. 07_scheme_performance.csv
perf = []
for s in schemes:
    c1 = round(random.uniform(12.0, 32.0), 2)
    c3 = round(random.uniform(14.0, 24.0), 2)
    c5 = round(random.uniform(13.0, 20.0), 2)
    sharpe = round(random.uniform(0.85, 1.65), 2)
    exp = round(random.uniform(0.45, 1.45), 2)
    perf.append({
        "scheme_code": s["scheme_code"],
        "scheme_name": s["scheme_name"],
        "cagr_1yr_pct": c1,
        "cagr_3yr_pct": c3,
        "cagr_5yr_pct": c5,
        "sharpe_ratio": sharpe,
        "expense_ratio_pct": exp
    })
df_perf = pd.DataFrame(perf)
df_perf.to_csv(os.path.join(RAW_DIR, "07_scheme_performance.csv"), index=False)
print("Generated 07_scheme_performance.csv.")

# 9. 08_transactions.csv (32,000 realistic transactions, 5k investors across 12 states)
STATES = ["MH", "KA", "TN", "DL", "GJ", "UP", "WB", "RJ", "TS", "HR", "MP", "PB"]
AGE_GROUPS = ["<30", "30-45", "45-60", "60+"]
CITY_TIERS = ["Tier-1", "Tier-2", "Tier-3"]
TXN_TYPES = ["SIP", "LUMPSUM", "REDEMPTION"]

investors = [f"INV{1000 + i}" for i in range(5000)]
investor_state_map = {inv: random.choice(STATES) for inv in investors}
investor_age_map = {inv: random.choices(AGE_GROUPS, weights=[0.31, 0.42, 0.20, 0.07])[0] for inv in investors}
investor_tier_map = {inv: random.choices(CITY_TIERS, weights=[0.45, 0.38, 0.17])[0] for inv in investors}

txns = []
txn_start = datetime(2025, 1, 1)
scheme_codes = [s["scheme_code"] for s in schemes]

for i in range(32000):
    txn_id = f"TXN{100000 + i}"
    inv_id = random.choice(investors)
    code = random.choice(scheme_codes)
    t_days = random.randint(0, 560)
    t_date = (txn_start + timedelta(days=t_days)).strftime("%Y-%m-%d")
    t_type = random.choices(TXN_TYPES, weights=[0.72, 0.20, 0.08])[0]
    
    amount = round(random.choice([1000, 2500, 5000, 10000, 25000, 50000, 100000]), 2)
    nav_val = round(random.uniform(25.0, 180.0), 4)
    units = round(amount / nav_val, 4)
    
    txns.append({
        "transaction_id": txn_id,
        "investor_id": inv_id,
        "scheme_code": code,
        "transaction_date": t_date,
        "transaction_type": t_type,
        "amount": amount,
        "units": units,
        "nav": nav_val,
        "investor_state": investor_state_map[inv_id],
        "investor_age_group": investor_age_map[inv_id],
        "city_tier": investor_tier_map[inv_id]
    })

df_txns = pd.DataFrame(txns)
df_txns.to_csv(os.path.join(RAW_DIR, "08_transactions.csv"), index=False)
print(f"Generated 08_transactions.csv with {len(df_txns)} transactions.")

# 10. 09_holdings.csv
COMPANIES = [
    ("HDFC Bank Ltd", "Financial Services"), ("ICICI Bank Ltd", "Financial Services"),
    ("Reliance Industries Ltd", "Oil & Gas"), ("Infosys Ltd", "Information Technology"),
    ("TCS Ltd", "Information Technology"), ("Larsen & Toubro Ltd", "Capital Goods"),
    ("Axis Bank Ltd", "Financial Services"), ("Bharti Airtel Ltd", "Telecommunication"),
    ("ITC Ltd", "Consumer Goods"), ("State Bank of India", "Financial Services")
]

holdings_data = []
for s in schemes:
    code = s["scheme_code"]
    selected = random.sample(COMPANIES, 5)
    weights = [25.0, 20.0, 18.0, 15.0, 12.0]
    for (comp, sec), w in zip(selected, weights):
        mkt_val = round(random.uniform(500.0, 8000.0), 2)
        holdings_data.append({
            "scheme_code": code,
            "company_name": comp,
            "sector": sec,
            "weight_pct": w,
            "market_value_crores": mkt_val
        })

df_holdings = pd.DataFrame(holdings_data)
df_holdings.to_csv(os.path.join(RAW_DIR, "09_holdings.csv"), index=False)
print("Generated 09_holdings.csv.")

# 11. 10_benchmark.csv
bm_dates = pd.date_range(start=start_date, end=end_date, freq='B')
bm_records = []
indices = ["Nifty 50 TRI", "Nifty 100 TRI", "BSE SmallCap"]

for idx_name in indices:
    base_val = 22000.0 if "50" in idx_name else (28000.0 if "100" in idx_name else 45000.0)
    c_val = base_val
    for d in bm_dates:
        r = np.random.normal(0.0004, 0.011)
        c_val = max(1000.0, c_val * (1 + r))
        o_val = c_val * (1 + np.random.normal(0, 0.003))
        h_val = max(c_val, o_val) * (1 + abs(np.random.normal(0, 0.004)))
        l_val = min(c_val, o_val) * (1 - abs(np.random.normal(0, 0.004)))
        
        bm_records.append({
            "date": d.strftime("%Y-%m-%d"),
            "benchmark_index": idx_name,
            "open_price": round(o_val, 2),
            "high_price": round(h_val, 2),
            "low_price": round(l_val, 2),
            "close_price": round(c_val, 2)
        })

df_bm = pd.DataFrame(bm_records)
df_bm.to_csv(os.path.join(RAW_DIR, "10_benchmark.csv"), index=False)
print(f"Generated 10_benchmark.csv with {len(df_bm)} rows.")

print("\nAll 10 CSV datasets successfully updated according to Bluestock Capstone specs!")
