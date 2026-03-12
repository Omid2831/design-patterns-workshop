"""
StatisticsCalculator: Concrete calculator that depends on IDataset abstraction
(Dependency Inversion, Single Responsibility, Open/Closed).
Interfaces live in src/interfaces/.
"""

from collections import Counter

from ..interfaces.IDataset import IDataset
from ..interfaces.IBasicStats import IBasicStats
from ..interfaces.IQuartileStats import IQuartileStats


class StatisticsCalculator(IBasicStats, IQuartileStats):
    """
    Calculates statistical measures from any IDataset.

    SOLID principles applied:
    - S: Single Responsibility — only calculates statistics.
    - O: Open/Closed — extend by subclassing; no modification needed.
    - L: Liskov Substitution — any IDataset implementation can be injected.
    - I: Interface Segregation — IBasicStats and IQuartileStats are separate interfaces.
    - D: Dependency Inversion — depends on IDataset abstraction, not BatteryDataset directly.
    """

    def __init__(self, dataset: IDataset):
        self._dataset = dataset
        self._data = dataset.get_values()  # already sorted by BatteryDataset

    # ------------------------------------------------------------------ median_definer ---
    def _median_of(self, data: list) -> float:
        n = len(data)
        if n % 2 == 0:
            return (data[n // 2 - 1] + data[n // 2]) / 2
        return float(data[n // 2])

    # ----------------------------------------------------------- mean ---
    def mean(self) -> float:
        return sum(self._data) / len(self._data)
    # ----------------------------------------------------------- median ---
    def median(self) -> float:
        return self._median_of(self._data)
    # ----------------------------------------------------------- mode ---
    def mode(self) -> list:
        counter = Counter(self._data)
        max_count = counter.most_common(1)[0][1]
        return [value for value, count in counter.items() if count == max_count]
    # ----------------------------------------------------------- spread "range" ---
    def spread(self) -> float:
        """Range (VB): difference between maximum and minimum value."""
        return max(self._data) - min(self._data)
    # ----------------------------------------------------------- Interquartiles ---
    def interquartile_range(self) -> float:
        """IQR (IKA) = Q3 - Q1."""
        return self.quartile(3) - self.quartile(1)