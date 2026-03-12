from abc import ABC, abstractmethod


class IBasicStats(ABC):
    """Interface for mean, median, mode, and spread (Interface Segregation)."""

    @abstractmethod
    def mean(self) -> float: pass

    @abstractmethod
    def median(self) -> float: pass

    @abstractmethod
    def mode(self) -> list: pass

    @abstractmethod
    def spread(self) -> float: pass
