"""
Entry point for the Battery Brand Statistics comparison.

Run from the project root:
    cd Kwartielen && python main.py
"""

from src.models.BatteryDataset import BatteryDataset
from src.statistics.statistics_calculator import StatisticsCalculator
from src.data.brands import brand_a, brand_b
from src.dashboard.dashboard import StatisticsDashboard


def main() -> None:
    # Create datasets
    dataset_a = BatteryDataset("Brand A", brand_a)
    dataset_b = BatteryDataset("Brand B", brand_b)

    # Create calculators
    calc_a = StatisticsCalculator(dataset_a)
    calc_b = StatisticsCalculator(dataset_b)

    # Display dashboard
    dashboard = StatisticsDashboard(
        calculators=[calc_a, calc_b],
        brand_names=["Brand A", "Brand B"]
    )
    dashboard.show_all()


if __name__ == "__main__":
    main()
