from collections import Counter

"""
This module contains the `StatisticsCalculator` class,
which provides methods to calculate various statistics such as
- mean,
- median,
- mode,
- variance, and
- standard deviation for a given dataset.
"""

class StatisticsCalculator:

    def __init__(self, dataset):
        self.dataset = dataset
        self.data = dataset.get_values()

    # define methods for mean
    def mean(self):
        return sum(self.data) / len(self.data)
    
    # define methods for median
    def median(self):
        sorted_data = sorted(self.data)
        n = len(sorted_data)
        if n % 2 == 0:
            return (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2
        else:
            return sorted_data[n // 2]
        
    # define methods for mode
    def mode(self):
        counter = Counter(self.data)
        mode_data = counter.most_common()
        # Get the maximum count of occurrences
        max_count = mode_data[0][1]
        # get all the values that have the maximum count
        modes = [value for value, count in mode_data if count == max_count]

        return modes

    # define methods for range
    def data_range(self):
        return max(self.data) - min(self.data)
    