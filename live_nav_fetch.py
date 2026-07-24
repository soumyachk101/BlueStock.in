import os
import requests
import pandas as pd

# 6 key scheme codes for benchmark fetching
SCHEMES = {
    "HDFC Top 100 Direct": 125497,
    "SBI Bluechip": 119551,
    "ICICI Bluechip": 120503,
    "Nippon Large Cap": 118632,
    "Axis Bluechip": 119092,
    "Kotak Bluechip": 120841
}

def fetch_nav(name, code):
    url = f"https://api.mfapi.in/mf/{code}"
    print(f"Fetching NAV data for {name} ({code})...")
    
    try:
        res = requests.get(url, timeout=15)
        if res.status_code != 200:
            print(f"Error: API returned status {res.status_code} for {name}")
            return
        
        data = res.json().get("data", [])
        if not data:
            print(f"No NAV records returned for {name}")
            return
        
        # Save to DataFrame and select date, nav
        df = pd.DataFrame(data)
        df = df[['date', 'nav']]
        
        # Format filename slug
        slug = name.lower().replace(" ", "_").replace("-", "_")
        filename = f"data/raw/{slug}_nav_raw.csv"
        
        df.to_csv(filename, index=False)
        print(f"Done! Saved {len(df)} rows to {filename}")

    except Exception as err:
        print(f"Failed to fetch NAV for {name}: {err}")

def main():
    os.makedirs("data/raw", exist_ok=True)
    print("--- Starting Live NAV Data Download ---")
    for name, code in SCHEMES.items():
        fetch_nav(name, code)
    print("Live NAV fetch script completed.")

if __name__ == "__main__":
    main()
