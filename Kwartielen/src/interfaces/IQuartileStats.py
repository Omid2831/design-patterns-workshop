from abc import ABC, abstractmethod


class IQuartileStats(ABC):
    """Interface for quartile and interquartile range calculations."""

    @abstractmethod
    def quartile(self, q: int) -> float:
        pass

    @abstractmethod
    def interquartile_range(self) -> float:
        pass
