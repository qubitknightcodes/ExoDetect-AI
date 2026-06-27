"""
Transit analysis utilities.

Author: ExoDetect-AI
"""

from __future__ import annotations

import numpy as np


class TransitAnalyzer:
    """
    Extract basic transit parameters from a phase-folded light curve.
    """

    def analyze(self, phase: np.ndarray, flux: np.ndarray):

        phase = np.asarray(phase)
        flux = np.asarray(flux)

        median_flux = np.median(flux)

        min_idx = np.argmin(flux)

        transit_center = phase[min_idx]

        transit_depth = median_flux - flux[min_idx]

        threshold = median_flux - transit_depth / 2

        in_transit = flux < threshold

        if np.any(in_transit):
            duration = phase[in_transit].max() - phase[in_transit].min()
        else:
            duration = 0.0

        return {
            "transit_depth": float(transit_depth),
            "transit_duration": float(duration),
            "transit_center": float(transit_center),
        }