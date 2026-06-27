"""
Detrending utilities for astronomical light curves.

This module removes long-term stellar and instrumental trends while
preserving short-duration transit events.

Supported methods:
- Savitzky-Golay filter

Author: ExoDetect-AI
"""

from __future__ import annotations

import numpy as np
from scipy.signal import savgol_filter


class Detrender:
    """
    Detrend astronomical light curves.
    """

    def __init__(
        self,
        window_length: int = 101,
        polyorder: int = 3,
    ):
        self.window_length = window_length
        self.polyorder = polyorder

    def _fill_nan(self, flux: np.ndarray) -> np.ndarray:
        """
        Replace NaN values using linear interpolation.
        """
        flux = np.asarray(flux, dtype=float)

        mask = np.isnan(flux)

        if np.any(mask):
            x = np.arange(len(flux))
            flux[mask] = np.interp(
                x[mask],
                x[~mask],
                flux[~mask],
            )

        return flux

    def _sgolay(self, flux: np.ndarray) -> np.ndarray:
        """
        Estimate the long-term trend using a Savitzky-Golay filter.
        """

        window = self.window_length

        if window % 2 == 0:
            window += 1

        return savgol_filter(
            flux,
            window_length=window,
            polyorder=self.polyorder,
        )

    def detrend(
        self,
        time: np.ndarray,
        flux: np.ndarray,
    ):
        """
        Detrend a light curve.

        Parameters
        ----------
        time : np.ndarray
            Observation times.

        flux : np.ndarray
            Relative stellar flux.

        Returns
        -------
        trend : np.ndarray
            Estimated trend.

        flattened_flux : np.ndarray
            Detrended and normalized flux.
        """

        flux = self._fill_nan(flux)

        trend = self._sgolay(flux)

        trend = np.where(
            np.abs(trend) < 1e-12,
            1e-12,
            trend,
        )

        flattened = flux / trend
        flattened /= np.median(flattened)

        return trend, flattened