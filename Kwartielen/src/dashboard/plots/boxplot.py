def plot_boxplots(stats, brand_names, ax):
    """Draw side-by-side box plots for all brands on the given axis."""
    ax.clear()

    data_list = [stats[name]["data"] for name in brand_names]
    boxplot = ax.boxplot(
        data_list,
        labels=brand_names,
        patch_artist=True,
        widths=0.6,
        showmeans=True,
    )

    colors = ["#FF6B6B", "#4ECDC4"]
    for patch, color in zip(boxplot["boxes"], colors):
        patch.set_facecolor(color)
        patch.set_alpha(0.7)

    ax.set_ylabel("Lifespan (hours)", fontsize=12, fontweight="bold")
    ax.set_xlabel("Battery Brands", fontsize=12, fontweight="bold")
    ax.set_title("Battery Lifespan Comparison - Box Plot", fontsize=14, fontweight="bold")
    ax.grid(axis="y", alpha=0.3)
    return ax
