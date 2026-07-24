"""
Notebook 01: Exploratory Data Analysis (EDA) & Market Overview
Bluestock Mutual Fund Analytics Platform
"""

import os
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set style
sns.set_theme(style="whitegrid")
plt.rcParams["figure.figsize"] = (10, 6)

DB_PATH = "data/processed/mf_analytics.db"

def run_eda():
    conn = sqlite3.connect(DB_PATH)
    
    print("--- 1. Market AUM Share by Fund House ---")
    df_aum = pd.read_sql("SELECT * FROM fact_aum ORDER BY total_aum_in_crores DESC", conn)
    print(df_aum[['fund_house', 'total_aum_in_crores', 'market_share_percent']])
    
    print("\n--- 2. Monthly SIP Inflow Trends (Dec '25 Milestone) ---")
    df_sip = pd.read_sql("SELECT * FROM fact_sip ORDER BY month", conn)
    print(df_sip)
    
    print("\n--- 3. Category & Scheme Distribution ---")
    df_fund = pd.read_sql("SELECT category, sub_category, COUNT(*) as scheme_count FROM dim_fund GROUP BY category, sub_category", conn)
    print(df_fund)
    
    conn.close()

if __name__ == "__main__":
    run_eda()
