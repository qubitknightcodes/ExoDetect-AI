"""
Common interface for period search algorithms.
"""

from abc import ABC, abstractmethod


class PeriodSearcher(ABC):
    @abstractmethod
    def find_period(self, time, flux):
        """
        Returns:
            best_period, power
        """
        pass