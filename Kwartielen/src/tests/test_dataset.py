"""
TDD unit tests for BatteryDataset.

Red → Green → Refactor cycle:
  Each test was written BEFORE the implementation to drive the design.
"""

import pytest
from Kwartielen.src.interfaces.IDataset import IDataset
from Kwartielen.src.models.BatteryDataset import BatteryDataset


class TestBatteryDatasetInterface:
    """Verify BatteryDataset satisfies the IDataset contract (Liskov Substitution)."""

    def test_is_instance_of_idataset(self):
        dataset = BatteryDataset("Brand A", [100, 90])
        assert isinstance(dataset, IDataset)


class TestBatteryDatasetCreation:

    def test_stores_name(self):
        dataset = BatteryDataset("Brand A", [100, 90, 80])
        assert dataset.get_name() == "Brand A"

    def test_sorts_values_on_creation(self):
        dataset = BatteryDataset("Brand A", [100, 90, 80])
        assert dataset.get_values() == [80, 90, 100]

    def test_already_sorted_values_unchanged(self):
        dataset = BatteryDataset("Brand A", [80, 90, 100])
        assert dataset.get_values() == [80, 90, 100]

    def test_empty_values_raise_value_error(self):
        with pytest.raises(ValueError):
            BatteryDataset("Brand A", [])


class TestBatteryDatasetImmutability:

    def test_get_values_returns_copy(self):
        dataset = BatteryDataset("Brand A", [80, 90, 100])
        values = dataset.get_values()
        values.append(999)
        assert 999 not in dataset.get_values()
