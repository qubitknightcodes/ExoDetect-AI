"""
Download real TESS light curves.

Author: ExoDetect-AI
"""

from pathlib import Path

import lightkurve as lk

SAVE_DIR = Path("data/raw")
SAVE_DIR.mkdir(parents=True, exist_ok=True)

# Famous confirmed exoplanets
TARGETS = [
    "TOI-700",
    "Pi Mensae",
    "LHS 3844",
    "HD 219134",
    "WASP-18",
]

for target in TARGETS:

    print(f"\nSearching {target}...")

    search = lk.search_lightcurve(
        target,
        mission="TESS",
    )

    if len(search) == 0:
        print("No data found.")
        continue

    lc = search.download()

    filename = SAVE_DIR / f"{target.replace(' ','_')}.fits"

    lc.to_fits(filename, overwrite=True)

    print(f"Saved -> {filename}")