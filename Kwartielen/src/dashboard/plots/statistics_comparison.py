import numpy as np


def plot_statistics_comparison(stats, brand_names, ax):
    """Draw a grouped bar chart for key statistics on the given axis."""
    ax.clear()

    metrics = ["mean", "median", "spread", "iqr"]
    labels = ["Mean", "Median", "Spread", "IQR"]

    x_positions = np.arange(len(metrics))
    width = 0.35
    colors = ["#FF6B6B", "#4ECDC4"]

    for index, name in enumerate(brand_names):
        values = [stats[name][metric] for metric in metrics]
        offset = (-width / 2) if index == 0 else (width / 2)
        bars = ax.bar(
            x_positions + offset,
            values,
            width=width,
            color=colors[index],
            alpha=0.7,
            edgecolor="black",
            label=name,
        )

        for bar, value in zip(bars, values):
            ax.text(
                bar.get_x() + bar.get_width() / 2,
                value,
                f"{value:.2f}",
                ha="center",
                va="bottom",
            )

    ax.set_xticks(x_positions)
    ax.set_xticklabels(labels)
    ax.set_ylabel("Value", fontweight="bold")
    ax.set_title("Battery Statistics Comparison", fontsize=14, fontweight="bold")
    ax.legend()
    ax.grid(axis="y", alpha=0.3)
    return ax
