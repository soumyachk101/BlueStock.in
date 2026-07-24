import os
import glob
import sqlite3
import pandas as pd
from sqlalchemy import create_engine

# Directories
RAW_DIR = "data/raw"
PROCESSED_DIR = "data/processed"
DB_PATH = os.path.join(PROCESSED_DIR, "mf_analytics.db")

def run_etl():
    print("==================================================================")
    print("      MUTUAL FUND ANALYTICS PLATFORM - AUTOMATED ETL PIPELINE     ")
    print("==================================================================")
    
    os.makedirs(PROCESSED_DIR, exist_ok=True)
    engine = create_engine(f"sqlite:///{DB_PATH}")
    
    # 1. Extract & Load dim_fund
    print("\n[1/5] Processing Dimension: dim_fund...")
    fund_master_path = os.path.join(RAW_DIR, "01_fund_master.csv")
    df_fund = pd.read_csv(fund_master_path)
    df_fund['launch_date'] = pd.to_datetime(df_fund['launch_date']).dt.strftime('%Y-%m-%d')
    df_fund.to_sql("dim_fund", engine, if_exists="replace", index=False)
    print(f" Loaded {len(df_fund)} records into 'dim_fund'.")
    
    # 2. Extract & Clean fact_nav
    print("\n[2/5] Processing Fact Table: fact_nav...")
    nav_path = os.path.join(RAW_DIR, "02_nav_history.csv")
    df_nav = pd.read_csv(nav_path)
    
    # Also integrate live NAV CSVs fetched from API if present
    live_nav_files = glob.glob(os.path.join(RAW_DIR, "*_nav_raw.csv"))
    if live_nav_files:
        print(f" Found {len(live_nav_files)} live API NAV CSV extractions. Merging...")
        for file in live_nav_files:
            try:
                # Extract scheme code from filename or mapping
                df_live = pd.read_csv(file)
                df_live['date'] = pd.to_datetime(df_live['date'], format='%d-%m-%Y', errors='coerce').dt.strftime('%Y-%m-%d')
                df_live['nav'] = pd.to_numeric(df_live['nav'], errors='coerce')
                # Default scheme code matching
                scheme_code = 125497 if "hdfc" in file else (119551 if "sbi" in file else 120503)
                df_live['scheme_code'] = scheme_code
                df_live['repurchase_price'] = df_live['nav']
                df_live['sale_price'] = df_live['nav']
                df_nav = pd.concat([df_nav, df_live], ignore_index=True)
            except Exception as e:
                print(f"  Warning loading {file}: {e}")
                
    df_nav['date'] = pd.to_datetime(df_nav['date']).dt.strftime('%Y-%m-%d')
    df_nav = df_nav.drop_duplicates(subset=['scheme_code', 'date']).sort_values(['scheme_code', 'date'])
    
    # Calculate derived daily returns
    df_nav['daily_return_pct'] = df_nav.groupby('scheme_code')['nav'].pct_change() * 100
    df_nav['daily_return_pct'] = df_nav['daily_return_pct'].fillna(0.0)
    
    df_nav.to_sql("fact_nav", engine, if_exists="replace", index=False)
    print(f" Loaded {len(df_nav)} clean records into 'fact_nav'.")
    
    # 3. Extract & Load fact_aum
    print("\n[3/5] Processing Fact Table: fact_aum...")
    df_aum = pd.read_csv(os.path.join(RAW_DIR, "03_aum_by_fund_house.csv"))
    df_aum['as_of_date'] = pd.to_datetime(df_aum['as_of_date']).dt.strftime('%Y-%m-%d')
    df_aum.to_sql("fact_aum", engine, if_exists="replace", index=False)
    print(f" Loaded {len(df_aum)} records into 'fact_aum'.")
    
    # 4. Extract & Load fact_sip
    print("\n[4/5] Processing Fact Table: fact_sip...")
    df_sip = pd.read_csv(os.path.join(RAW_DIR, "04_monthly_sip.csv"))
    df_sip.to_sql("fact_sip", engine, if_exists="replace", index=False)
    print(f" Loaded {len(df_sip)} records into 'fact_sip'.")
    
    # 5. Extract & Load fact_transactions
    print("\n[5/5] Processing Fact Table: fact_transactions...")
    df_txns = pd.read_csv(os.path.join(RAW_DIR, "08_transactions.csv"))
    df_txns['transaction_date'] = pd.to_datetime(df_txns['transaction_date']).dt.strftime('%Y-%m-%d')
    df_txns.to_sql("fact_transactions", engine, if_exists="replace", index=False)
    print(f" Loaded {len(df_txns)} records into 'fact_transactions'.")
    
    print("\n==================================================================")
    print(f" ETL Pipeline Finished Successfully! Star Schema DB: {DB_PATH}")
    print("==================================================================")

if __name__ == "__main__":
    run_etl()
