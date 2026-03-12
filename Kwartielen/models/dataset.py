"""
This module defines the BatteryDataset class, which represents a dataset of battery values.
The BatteryDataset class has the following attributes:
- name: The name of the dataset.
- values: A sorted list of battery values.
"""

class BatteryDataset:

    def __init__(self, name, values):
        self.name = name
        self.values = sorted(values)

    def get_values(self):
        return self.values