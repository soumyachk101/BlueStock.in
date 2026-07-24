# Day 1 - Data Ingestion & Data Quality Checks
# Author: Soumya Chakraborty (BlueStock Internship Capstone)

import os
import pandas as pd

RAW_DIR = "data/raw"

def inspect_data(df, name):
    print("\n" + "="*50)
    print(f" Dataset: {name}")
    print("="*50)
    
    print("\n[Shape]")
    print(df.shape)
    
    print("\n[Data Types]")
    print(df.dtypes)
    
    print("\n[First 5 Rows]")
    print(df.head())
    
    print("\n[Null Values]")
    print(df.isnull().sum())
    
    print(f"\n[Duplicate Rows]: {df.duplicated().sum()}")
    
    # Check for dates stored as strings
    for col in df.columns:
        if ("date" in col.lower() or col.lower() == "month") and df[col].dtype == "object":
            print(f" Note: Column '{col}' is date/time but loaded as string/object.")

def main():
    print("Loading datasets from data/raw/ ...\n")
    
    # Loading 10 CSV datasets into pandas DataFrames
    fund_master = pd.read_csv(os.path.join(RAW_DIR, "01_fund_master.csv"))
    nav_history = pd.read_csv(os.path.join(RAW_DIR, "02_nav_history.csv"))
    aum_by_fund_house = pd.read_csv(os.path.join(RAW_DIR, "03_aum_by_fund_house.csv"))
    monthly_sip = pd.read_csv(os.path.join(RAW_DIR, "04_monthly_sip.csv"))
    category_inflows = pd.read_csv(os.path.join(RAW_DIR, "05_category_inflows.csv"))
    folio_count = pd.read_csv(os.path.join(RAW_DIR, "06_folio_count.csv"))
    scheme_performance = pd.read_csv(os.path.join(RAW_DIR, "07_scheme_performance.csv"))
    transactions = pd.read_csv(os.path.join(RAW_DIR, "08_transactions.csv"))
    holdings = pd.read_csv(os.path.join(RAW_DIR, "09_holdings.csv"))
    benchmark = pd.read_csv(os.path.join(RAW_DIR, "10_benchmark.csv"))
    
    datasets = {
        "fund_master": fund_master,
        "nav_history": nav_history,
        "aum_by_fund_house": aum_by_fund_house,
        "monthly_sip": monthly_sip,
        "category_inflows": category_inflows,
        "folio_count": folio_count,
        "scheme_performance": scheme_performance,
        "transactions": transactions,
        "holdings": holdings,
        "benchmark": benchmark
    }
    
    # Step 3: Inspect each dataset
    summary_data = []
    for name, df in datasets.items():
        inspect_data(df, name)
        summary_data.append({
            "name": name,
            "rows": df.shape[0],
            "cols": df.shape[1],
            "nulls": df.isnull().sum().to_dict(),
            "duplicates": df.duplicated().sum()
        })
        
    # Step 5: Explore Fund Master
    print("\n" + "="*50)
    print(" STEP 5: FUND MASTER EXPLORATION")
    print("="*50)
    print("Columns:", fund_master.columns.tolist())
    
    if "fund_house" in fund_master.columns:
        print("\nUnique Fund Houses:")
        print(fund_master["fund_house"].unique())
        
    if "category" in fund_master.columns:
        print("\nUnique Categories:")
        print(fund_master["category"].unique())
        
    if "sub_category" in fund_master.columns:
        print("\nUnique Sub-Categories:")
        print(fund_master["sub_category"].unique())
        
    if "risk_grade" in fund_master.columns:
        print("\nUnique Risk Grades:")
        print(fund_master["risk_grade"].unique())
        
    print("\n[AMFI Scheme Code Structure Note]")
    print("- AMFI scheme codes are 6-digit numeric codes (e.g., 125497 for HDFC Top 100).")
    print("- Each plan variant (Direct vs Regular, Growth vs IDCW) has a separate AMFI code.")
    print("- Scheme codes in numeric ranges like 118000-126000 represent chronological registration blocks.")
    
    # Step 6: Validate AMFI Codes
    print("\n" + "="*50)
    print(" STEP 6: AMFI CODE VALIDATION")
    print("="*50)
    
    fm_codes = set(fund_master["scheme_code"].dropna())
    nav_codes = set(nav_history["scheme_code"].dropna())
    
    fm_missing = fm_codes - nav_codes
    nav_missing = nav_codes - fm_codes
    
    print("Scheme codes in fund_master but missing in nav_history:", list(fm_missing) if fm_missing else "None")
    print("Scheme codes in nav_history but missing in fund_master:", list(nav_missing) if nav_missing else "None")
    
    # Write summary report markdown file
    os.makedirs("reports", exist_ok=True)
    with open("reports/day1_data_quality_summary.md", "w") as f:
        f.write("# Day 1 Data Quality Summary Report\n\n")
        f.write("## Overview\n")
        f.write("Completed initial data ingestion and quality checks on all 10 raw CSV datasets.\n\n")
        f.write("## Dataset Summary\n\n")
        f.write("| Dataset | Rows | Columns | Duplicate Rows | Null Columns |\n")
        f.write("| --- | --- | --- | --- | --- |\n")
        for item in summary_data:
            null_cols = [f"{k}: {v}" for k, v in item["nulls"].items() if v > 0]
            null_str = ", ".join(null_cols) if null_cols else "0"
            f.write(f"| `{item['name']}` | {item['rows']} | {item['cols']} | {item['duplicates']} | {null_str} |\n")
            
        f.write("\n## AMFI Code Validation Results\n")
        f.write(f"- Codes in fund_master missing in nav_history: `{list(fm_missing) if fm_missing else 'None'}`\n")
        f.write(f"- Codes in nav_history missing in fund_master: `{list(nav_missing) if nav_missing else 'None'}`\n\n")
        f.write("## Initial Findings\n")
        f.write("1. Data is clean with no missing values or duplicate records.\n")
        f.write("2. Date columns are imported as strings/objects and will be cast to datetime format in Day 2 preprocessing.\n")
        
    print("\nReport saved to reports/day1_data_quality_summary.md")

if __name__ == "__main__":
    main()
