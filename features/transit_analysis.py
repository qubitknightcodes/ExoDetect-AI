import numpy as np


class TransitAnalyzer:

    def analyze(self, phase, flux):

        phase = np.asarray(phase)
        flux = np.asarray(flux)

        baseline = np.median(flux)

        sorted_flux = np.sort(flux)

        n = max(5, len(sorted_flux) // 100)

        depth = baseline - np.mean(sorted_flux[:n])

        idx = np.argmin(flux)

        center = phase[idx]

        threshold = baseline - depth / 2

        mask = flux < threshold

        if np.sum(mask) > 1:
            duration = np.ptp(phase[mask])
        else:
            duration = 0.0

        return {
            "transit_depth": float(depth),
            "transit_duration": float(duration),
            "transit_center": float(center),
        }