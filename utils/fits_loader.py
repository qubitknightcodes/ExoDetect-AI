from pathlib import Path

import lightkurve as lk
import numpy as np


class FITSLoader:
    def load(self, fits_path):

        lc = lk.read(Path(fits_path))

        lc = lc.remove_nans()

        time = np.asarray(lc.time.value, dtype=np.float32)
        flux = np.asarray(lc.flux.value, dtype=np.float32)

        return time, flux