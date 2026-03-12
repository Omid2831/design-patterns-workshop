from abc import ABC, abstractmethod

"""
This module defines:
- IDataset: Abstract base class (interface) for any dataset (Dependency Inversion, Interface Segregation).
"""
class IDataset(ABC):
    """Interface that any dataset must implement (Dependency Inversion Principle)."""

    @abstractmethod
    def get_values(self) -> list:
        pass

    @abstractmethod
    def get_name(self) -> str:
        pass

