from ..interfaces.IDataset import IDataset



"""
This module defines:
- BatteryDataset: Concrete dataset holding battery lifespan values (Single Responsibility).
"""

class BatteryDataset(IDataset):
    """
    Represents a named, immutable, sorted dataset of battery lifespan values.
    Single Responsibility: stores and exposes data only.
    """

    def __init__(self, name: str, values: list):
        if not values:
            raise ValueError("Dataset cannot be empty")
        self._name = name
        self._values = sorted(values)

    def get_values(self) -> list:
        return list(self._values)  # return copy to prevent external mutation

    def get_name(self) -> str:
        return self._name