# ETL Pipeline Script for Bluestock Mutual Fund Analytics Platform
# Author: Soumya Chakraborty

import os
import glob
import sqlite3
import pandas as pd
from sqlalchemy import create_engine

RAW_DIR = "data/raw"
PROCESSED_DIR = "data/processed"
DB_PATH = os.path.join(PROCESSED_DIR, "mf_analytics.db")

def run_etl():
    print("Starting ETL Process...")
    os.makedirs(PROCESSED_DIR, exist_ok=True)
    engine = create_engine(f"sqlite:///{DB_PATH}")
    
    # 1. Load Fund Master
    print("Loading dim_fund table...")
    df_fund = pd.read_csv(os.path.join(RAW_DIR, "01_fund_master.csv"))
    df_fund['launch_date'] = pd.to_datetime(df_fund['launch_date']).dt.strftime('%Y-%m-%d')
    df_fund.to_sql("dim_fund", engine, if_exists="replace", index=False)
    print(f"Loaded {len(df_fund)} records into dim_fund.")
    
    # 2. Load NAV History
    print("Loading fact_nav table...")
    df_nav = pd.read_csv(os.path.join(RAW_DIR, "02_nav_history.csv"))
    
    # Check for live API downloads
    api_nav_files = glob.glob(os.path.join(RAW_DIR, "*_nav_raw.csv"))
    if api_nav_files:
        for f in api_nav_files:
            try:
                df_api = pd.read_csv(f)
                df_api['date'] = pd.to_datetime(df_api['date'], format='%d-%m-%Y', errors='coerce').dt.strftime('%Y-%m-%d')
                df_api['nav'] = pd.to_numeric(df_api['nav'], errors='coerce')
                
                code = 125497 if "hdfc" in f else (119551 if "sbi" in f else 120503)
                df_api['scheme_code'] = code
                df_api['repurchase_price'] = df_api['nav']
                df_api['sale_price'] = df_api['nav']
                df_nav = pd.concat([df_nav, df_api], ignore_index=True)
            except Exception as e:
                print(f"Skipping {f}: {e}")
                
    df_nav['date'] = pd.to_datetime(df_nav['date']).dt.strftime('%Y-%m-%d')
    df_nav = df_nav.drop_duplicates(subset=['scheme_code', 'date']).sort_values(['scheme_code', 'date'])
    
    # Calculate daily percentage returns
    df_nav['daily_return_pct'] = df_nav.groupby('scheme_code')['nav'].pct_change() * 100
    df_nav['daily_return_pct'] = df_nav['daily_return_pct'].fillna(0.0)
    
    df_nav.to_sql("fact_nav", engine, if_exists="replace", index=False)
    print(f"Loaded {len(df_nav)} records into fact_nav.")
    
    # 3. Load AUM
    print("Loading fact_aum table...")
    df_aum = pd.read_csv(os.path.join(RAW_DIR, "03_aum_by_fund_house.csv"))
    df_aum['as_of_date'] = pd.to_datetime(df_aum['as_of_date']).dt.strftime('%Y-%m-%d')
    df_aum.to_sql("fact_aum", engine, if_exists="replace", index=False)
    
    # 4. Load Monthly SIP
    print("Loading fact_sip table...")
    df_sip = pd.read_csv(os.path.join(RAW_DIR, "04_monthly_sip.csv"))
    df_sip.to_sql("fact_sip", engine, if_exists="replace", index=False)
    
    # 5. Load Transactions
    print("Loading fact_transactions table...")
    df_txns = pd.read_csv(os.path.join(RAW_DIR, "08_transactions.csv"))
    df_txns['transaction_date'] = pd.to_datetime(df_txns['transaction_date']).dt.strftime('%Y-%m-%d')
    df_txns.to_sql("fact_transactions", engine, if_exists="replace", index=False)
    
    print(f"ETL completed successfully! SQLite DB saved to {DB_PATH}")

if __name__ == "__main__":
    run_etl()
