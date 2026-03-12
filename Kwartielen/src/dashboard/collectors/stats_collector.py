import numpy as np


def collect_stats(calculators, brand_names):
    """Collect all statistics needed by the dashboard for each brand."""
    stats = {}
    for calculator, name in zip(calculators, brand_names):
        stats[name] = {
            "mean": calculator.mean(),
            "median": calculator.median(),
            "mode": calculator.mode(),
            "spread": calculator.spread(),
            "q1": calculator.quartile(1),
            "q2": calculator.quartile(2),
            "q3": calculator.quartile(3),
            "iqr": calculator.interquartile_range(),
            "data": np.array(calculator.get_data()),
        }
    return stats
