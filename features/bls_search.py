"""
Box Least Squares period search.

Author: ExoDetect-AI
"""

import numpy as np

from astropy.timeseries import BoxLeastSquares

from features.period_search import PeriodSearcher


class BLSSearch(PeriodSearcher):

    def __init__(
        self,
        min_period=0.5,
        max_period=30,
        duration=0.2,
    ):
        self.min_period = min_period
        self.max_period = max_period
        self.duration = duration

    def find_period(self, time, flux):

        model = BoxLeastSquares(time, flux)

        periods = np.linspace(
            self.min_period,
            self.max_period,
            1000,
        )

        results = model.power(
            periods,
            self.duration,
        )

        idx = np.argmax(results.power)

        return (
            float(results.period[idx]),
            float(results.power[idx]),
        )