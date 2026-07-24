# Notebook 01: Exploratory Data Analysis
# Author: Soumya Chakraborty

import sqlite3
import pandas as pd

DB_PATH = "data/processed/mf_analytics.db"

def eda_summary():
    conn = sqlite3.connect(DB_PATH)
    
    print("--- AMC Market Share (AUM) ---")
    df_aum = pd.read_sql("SELECT fund_house, total_aum_in_crores, market_share_percent FROM fact_aum ORDER BY total_aum_in_crores DESC", conn)
    print(df_aum)
    
    print("\n--- Monthly SIP Inflows ---")
    df_sip = pd.read_sql("SELECT month, total_sip_inflow_crores, active_sip_accounts FROM fact_sip ORDER BY month", conn)
    print(df_sip)
    
    print("\n--- Scheme Counts by Category ---")
    df_fund = pd.read_sql("SELECT category, sub_category, COUNT(*) as count FROM dim_fund GROUP BY category, sub_category", conn)
    print(df_fund)
    
    conn.close()

if __name__ == "__main__":
    eda_summary()
