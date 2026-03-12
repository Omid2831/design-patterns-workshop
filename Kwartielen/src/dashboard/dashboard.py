"""Dashboard orchestrator for battery statistics visualization."""

import matplotlib.pyplot as plt
from typing import List

from .collectors.stats_collector import collect_stats
from .navigator import DashboardNavigator
from .plots.boxplot import plot_boxplots
from .plots.distribution_plot import plot_distribution
from .plots.statistics_comparison import plot_statistics_comparison
from .views.comparison_table import print_comparison_table


class StatisticsDashboard:
    """Coordinates dashboard data collection, text output, and charts."""

    def __init__(self, calculators: List, brand_names: List[str]):
        """Initialize the dashboard with calculators and brand names."""
        self.calculators = calculators
        self.brand_names = brand_names
        self.stats = collect_stats(self.calculators, self.brand_names)
        pages = [
            ("Box Plot", plot_boxplots),
            ("Distribution", plot_distribution),
            ("Statistics", plot_statistics_comparison),
        ]
        self.navigator = DashboardNavigator(self.stats, self.brand_names, pages)

    def print_comparison_table(self) -> None:
        """Print the statistics comparison table."""
        print_comparison_table(self.stats, self.brand_names)

    def plot_boxplots(self) -> None:
        """Create side-by-side box plots for the configured brands."""
        figure, axis = plt.subplots(1, 1, figsize=(11, 7))
        plot_boxplots(self.stats, self.brand_names, axis)
        figure.tight_layout()
        return figure

    def plot_distribution(self) -> None:
        """Create overlaid histograms for the configured brands."""
        figure, axis = plt.subplots(1, 1, figsize=(11, 7))
        plot_distribution(self.stats, self.brand_names, axis)
        figure.tight_layout()
        return figure

    def plot_statistics_comparison(self) -> None:
        """Create a bar-chart comparison of key statistics."""
        figure, axis = plt.subplots(1, 1, figsize=(11, 7))
        plot_statistics_comparison(self.stats, self.brand_names, axis)
        figure.tight_layout()
        return figure

    def show_all(self) -> None:
        """Display all visualizations in one figure with left/right navigation."""
        self.print_comparison_table()
        figure, axis = plt.subplots(1, 1, figsize=(11, 7))
        self.navigator.render_current_page(figure, axis)
        figure.canvas.mpl_connect(
            "key_press_event",
            lambda event: self.navigator.handle_key_press(event, figure, axis),
        )
        plt.show()
