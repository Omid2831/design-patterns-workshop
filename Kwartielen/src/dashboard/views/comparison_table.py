def print_comparison_table(stats, brand_names):
    """Print a formatted comparison table of all core statistics."""
    print("\n" + "=" * 100)
    print(f"{'Statistic':<25} {brand_names[0]:<35} {brand_names[1]:<35}")
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
        left_value = stats[brand_names[0]][key]
        right_value = stats[brand_names[1]][key]

        if isinstance(left_value, list):
            left_text = str(left_value)
            right_text = str(right_value)
        else:
            left_text = f"{left_value:.2f}"
            right_text = f"{right_value:.2f}"

        print(f"{label:<25} {left_text:<35} {right_text:<35}")

    print("=" * 100)
