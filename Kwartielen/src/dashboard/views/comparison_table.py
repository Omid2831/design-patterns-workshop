import pandas as pd


def print_comparison_table(stats, brand_names):
    """Print a formatted comparison table using a pandas DataFrame."""

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

    rows = []
    for label, key in metrics:
        left_value = stats[brand_names[0]][key]
        right_value = stats[brand_names[1]][key]

        rows.append(
            {
                "Statistic": label,
                brand_names[0]: str(left_value) if isinstance(left_value, list) else f"{left_value:.2f}",
                brand_names[1]: str(right_value) if isinstance(right_value, list) else f"{right_value:.2f}",
            }
        )

    frame = pd.DataFrame(rows, columns=["Statistic", brand_names[0], brand_names[1]])
    print("\n" + frame.to_string(index=False))
