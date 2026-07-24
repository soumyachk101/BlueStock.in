# Notebook 03: Demographics & Regional Inflows Analysis
# Author: Soumya Chakraborty

import sqlite3
import pandas as pd

DB_PATH = "data/processed/mf_analytics.db"

def main():
    conn = sqlite3.connect(DB_PATH)
    
    print("--- Investor Age Breakdown ---")
    df_age = pd.read_sql("""
        SELECT investor_age_group, 
               COUNT(DISTINCT investor_id) as total_investors,
               SUM(amount) as total_invested_inr
        FROM fact_transactions
        GROUP BY investor_age_group
        ORDER BY total_investors DESC
    """, conn)
    print(df_age)
    
    print("\n--- Top States by Investment Volume ---")
    df_states = pd.read_sql("""
        SELECT investor_state, 
               COUNT(DISTINCT investor_id) as investors,
               SUM(amount) as total_amount
        FROM fact_transactions
        GROUP BY investor_state
        ORDER BY total_amount DESC
        LIMIT 5
    """, conn)
    print(df_states)
    
    conn.close()

if __name__ == "__main__":
    main()
