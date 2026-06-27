"""
Download public exoplanet and false-positive catalogs.

Author: ExoDetect-AI
"""

from pathlib import Path

import pandas as pd

EXOPLANET_URL = (
    "https://exoplanetarchive.ipac.caltech.edu/TAP/sync?"
    "query=select+pl_name,hostname,tic_id+from+ps&format=csv"
)

SAVE_DIR = Path("data/labels")
SAVE_DIR.mkdir(parents=True, exist_ok=True)

print("Downloading confirmed exoplanet catalog...")

df = pd.read_csv(EXOPLANET_URL)

df.to_csv(
    SAVE_DIR / "confirmed_exoplanets.csv",
    index=False,
)

print(f"Downloaded {len(df)} confirmed planets.")