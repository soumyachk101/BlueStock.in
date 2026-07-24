import os
import re
import requests
import pandas as pd

SCHEME_MAP = {
    "HDFC Top 100 Direct": 125497,
    "SBI Bluechip": 119551,
    "ICICI Bluechip": 120503,
    "Nippon Large Cap": 118632,
    "Axis Bluechip": 119092,
    "Kotak Bluechip": 120841
}

def generate_slug(name: str) -> str:
    """Convert scheme name to a clean snake_case slug."""
    slug = re.sub(r'[^a-zA-Z0-9\s]', '', name).strip().lower()
    return re.sub(r'\s+', '_', slug)

def fetch_and_save_nav(scheme_name: str, scheme_code: int, output_dir: str = "data/raw") -> bool:
    """Fetch live NAV data from mfapi.in and save to CSV."""
    url = f"https://api.mfapi.in/mf/{scheme_code}"
    print(f"Fetching NAV data for '{scheme_name}' (Code: {scheme_code}) from {url}...")
    
    try:
        response = requests.get(url, timeout=15)
        if response.status_code != 200:
            print(f"[ERROR] Failed to fetch data for {scheme_name} (Code: {scheme_code}). Status code: {response.status_code}")
            return False
        
        json_data = response.json()
        nav_data = json_data.get("data", [])
        
        if not nav_data:
            print(f"[WARNING] No NAV data found in response for {scheme_name}.")
            return False
        
        df = pd.DataFrame(nav_data)
        # Ensure exact columns: date, nav
        if "date" in df.columns and "nav" in df.columns:
            df = df[["date", "nav"]]
        
        slug = generate_slug(scheme_name)
        file_path = os.path.join(output_dir, f"{slug}_nav_raw.csv")
        
        os.makedirs(output_dir, exist_ok=True)
        df.to_csv(file_path, index=False)
        print(f"[SUCCESS] Saved {len(df)} records for '{scheme_name}' to {file_path}")
        return True

    except Exception as e:
        print(f"[ERROR] Exception occurred while fetching NAV for '{scheme_name}': {e}")
        return False

def main():
    print("Starting Live NAV Fetching Process...")
    os.makedirs("data/raw", exist_ok=True)
    success_count = 0
    for name, code in SCHEME_MAP.items():
        if fetch_and_save_nav(name, code):
            success_count += 1
    print(f"\nFetch complete. Successfully saved {success_count}/{len(SCHEME_MAP)} schemes.")

if __name__ == "__main__":
    main()
