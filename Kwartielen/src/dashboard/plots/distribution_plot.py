def plot_distribution(stats, brand_names, ax):
    """Draw overlaid histograms showing brand lifespan distributions."""
    ax.clear()

    colors = ["#FF6B6B", "#4ECDC4"]
    for index, name in enumerate(brand_names):
        ax.hist(
            stats[name]["data"],
            bins=8,
            alpha=0.6,
            label=name,
            color=colors[index],
            edgecolor="black",
        )
        ax.axvline(
            stats[name]["mean"],
            color=colors[index],
            linestyle="--",
            linewidth=2,
            label=f"{name} Mean",
        )

    ax.set_xlabel("Lifespan (hours)", fontsize=12, fontweight="bold")
    ax.set_ylabel("Frequency", fontsize=12, fontweight="bold")
    ax.set_title("Battery Lifespan Distribution", fontsize=14, fontweight="bold")
    ax.legend()
    ax.grid(axis="y", alpha=0.3)
    return ax
