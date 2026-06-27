"""
Phase folding utilities for exoplanet transit analysis.

Author: ExoDetect-AI
"""

from __future__ import annotations

import numpy as np


class PhaseFolder:
    """
    Fold a light curve using a known orbital period.
    """

    def __init__(self, period: float, t0: float = 0.0):
        if period <= 0:
            raise ValueError("Period must be greater than zero.")

        self.period = period
        self.t0 = t0

    def fold(self, time: np.ndarray, flux: np.ndarray):
        """
        Fold a light curve into phase space.

        Returns
        -------
        phase : np.ndarray
            Phase values in the range [-0.5, 0.5).

        folded_flux : np.ndarray
            Flux sorted by phase.
        """

        time = np.asarray(time)
        flux = np.asarray(flux)

        phase = ((time - self.t0) / self.period) % 1.0
        phase[phase >= 0.5] -= 1.0

        order = np.argsort(phase)

        return phase[order], flux[order]