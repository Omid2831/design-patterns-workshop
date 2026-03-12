"""
Dashboard module for battery statistics visualization.
Uses numpy for calculations and matplotlib for plotting.
"""

import numpy as np
import matplotlib.pyplot as plt
from typing import List


class StatisticsDashboard:
    """Visualizes battery statistics using box plots and summary tables."""

    def __init__(self, calculators: List, brand_names: List[str]):
        """
        Initialize dashboard with calculators and brand names.
        
        Args:
            calculators: List of StatisticsCalculator instances
            brand_names: List of brand names corresponding to calculators
        """
        self.calculators = calculators
        self.brand_names = brand_names
        self.stats = self._collect_stats()

    def _collect_stats(self) -> dict:
        """Collect all statistics for each calculator."""
        stats = {}
        for calc, name in zip(self.calculators, self.brand_names):
            stats[name] = {
                "mean": calc.mean(),
                "median": calc.median(),
                "mode": calc.mode(),
                "spread": calc.spread(),
                "q1": calc.quartile(1),
                "q2": calc.quartile(2),
                "q3": calc.quartile(3),
                "iqr": calc.interquartile_range(),
                "data": np.array(calc._data),
            }
        return stats

    def print_comparison_table(self) -> None:
        """Print a formatted comparison table of statistics."""
        print("\n" + "=" * 100)
        print(f"{'Statistic':<25} {'Brand A':<35} {'Brand B':<35}")
        print("=" * 100)

        metrics = [
            ("Mean (Ge)", "mean"),
            ("Median (Me)", "median"),
            ("Mode (Mo)", "mode"),
            ("Spread (VB)", "spread"),
            ("Q1", "q1"),
            ("Q2", "q2"),
            ("Q3", "q3"),
            ("IQR (IKA)", "iqr"),
        ]

        for label, key in metrics:
            brand_a_val = self.stats["Brand A"][key]
            brand_b_val = self.stats["Brand B"][key]

            if isinstance(brand_a_val, list):
                brand_a_str = str(brand_a_val)
                brand_b_str = str(brand_b_val)
            else:
                brand_a_str = f"{brand_a_val:.2f}"
                brand_b_str = f"{brand_b_val:.2f}"

            print(f"{label:<25} {brand_a_str:<35} {brand_b_str:<35}")

        print("=" * 100)

    def plot_boxplots(self) -> None:
        """Create side-by-side box plots for both brands."""
        fig, ax = plt.subplots(1, 1, figsize=(10, 6))

        data_list = [self.stats["Brand A"]["data"], self.stats["Brand B"]["data"]]
        bp = ax.boxplot(
            data_list,
            labels=self.brand_names,
            patch_artist=True,
            widths=0.6,
            showmeans=True,
        )

        # Color the boxes
        colors = ["#FF6B6B", "#4ECDC4"]
        for patch, color in zip(bp["boxes"], colors):
            patch.set_facecolor(color)
            patch.set_alpha(0.7)

        ax.set_ylabel("Lifespan (hours)", fontsize=12, fontweight="bold")
        ax.set_xlabel("Battery Brands", fontsize=12, fontweight="bold")
        ax.set_title("Battery Lifespan Comparison - Box Plot", fontsize=14, fontweight="bold")
        ax.grid(axis="y", alpha=0.3)

        plt.tight_layout()
        return fig

    def plot_distribution(self) -> None:
        """Create overlaid histograms showing distribution of both brands."""
        fig, ax = plt.subplots(1, 1, figsize=(10, 6))

        brand_a_data = self.stats["Brand A"]["data"]
        brand_b_data = self.stats["Brand B"]["data"]

        ax.hist(brand_a_data, bins=8, alpha=0.6, label="Brand A", color="#FF6B6B", edgecolor="black")
        ax.hist(brand_b_data, bins=8, alpha=0.6, label="Brand B", color="#4ECDC4", edgecolor="black")

        ax.axvline(self.stats["Brand A"]["mean"], color="#FF6B6B", linestyle="--", linewidth=2, label="Brand A Mean")
        ax.axvline(self.stats["Brand B"]["mean"], color="#4ECDC4", linestyle="--", linewidth=2, label="Brand B Mean")

        ax.set_xlabel("Lifespan (hours)", fontsize=12, fontweight="bold")
        ax.set_ylabel("Frequency", fontsize=12, fontweight="bold")
        ax.set_title("Battery Lifespan Distribution", fontsize=14, fontweight="bold")
        ax.legend()
        ax.grid(axis="y", alpha=0.3)

        plt.tight_layout()
        return fig

    def plot_statistics_comparison(self) -> None:
        """Create a bar chart comparing key statistics."""
        fig, axes = plt.subplots(2, 2, figsize=(12, 10))
        fig.suptitle("Battery Statistics Comparison", fontsize=14, fontweight="bold")

        metrics = [
            ("Mean", "mean", axes[0, 0]),
            ("Median", "median", axes[0, 1]),
            ("Spread", "spread", axes[1, 0]),
            ("IQR", "iqr", axes[1, 1]),
        ]

        x_pos = np.arange(len(self.brand_names))
        colors = ["#FF6B6B", "#4ECDC4"]

        for label, key, ax in metrics:
            values = [self.stats[name][key] for name in self.brand_names]
            bars = ax.bar(x_pos, values, color=colors, alpha=0.7, edgecolor="black")
            ax.set_xticks(x_pos)
            ax.set_xticklabels(self.brand_names)
            ax.set_ylabel(label, fontweight="bold")
            ax.set_title(f"{label} Comparison")
            ax.grid(axis="y", alpha=0.3)

            # Add value labels on bars
            for i, (bar, val) in enumerate(zip(bars, values)):
                ax.text(bar.get_x() + bar.get_width() / 2, val, f"{val:.2f}", ha="center", va="bottom")

        plt.tight_layout()
        return fig

    def show_all(self) -> None:
        """Display all visualizations."""
        self.print_comparison_table()
        self.plot_boxplots()
        self.plot_distribution()
        self.plot_statistics_comparison()
        plt.show()
