"""
Notebook 03: Demographics & Benchmark Analytics
Bluestock Mutual Fund Analytics Platform
"""

import os
import sqlite3
import pandas as pd

DB_PATH = "data/processed/mf_analytics.db"

def run_demographics_benchmark():
    conn = sqlite3.connect(DB_PATH)
    
    print("--- 1. Investor Age Demographics & SIP Breakdown ---")
    df_age = pd.read_sql("""
        SELECT investor_age_group, 
               COUNT(DISTINCT investor_id) as investor_count,
               SUM(amount) as total_invested,
               AVG(amount) as avg_ticket_size
        FROM fact_transactions
        GROUP BY investor_age_group
        ORDER BY investor_count DESC
    """, conn)
    print(df_age)
    
    print("\n--- 2. Top 5 Investor States ---")
    df_states = pd.read_sql("""
        SELECT investor_state, 
               COUNT(DISTINCT investor_id) as investor_count,
               SUM(amount) as total_amount
        FROM fact_transactions
        GROUP BY investor_state
        ORDER BY total_amount DESC
        LIMIT 5
    """, conn)
    print(df_states)
    
    print("\n--- 3. City Tier Inflow Dynamics ---")
    df_tier = pd.read_sql("""
        SELECT city_tier,
               COUNT(transaction_id) as txn_count,
               SUM(amount) as volume_amount
        FROM fact_transactions
        GROUP BY city_tier
    """, conn)
    print(df_tier)
    
    conn.close()

if __name__ == "__main__":
    run_demographics_benchmark()
