import pandas as pd
import matplotlib.pyplot as plt
import os

src_dir = "./reports"
out_dir = "./tables"
os.makedirs(out_dir, exist_ok=True)

ALGO_LABELS = {
    "brute_force": "Brute Force",
    "greedy": "Greedy",
    "modified_greedy": "Modified Greedy",
    "local_search": "Local Search",
    "vns": "VNS",
    "simulated_annealing": "Simulated Annealing",
    "genetic_algorithm": "Genetic Algorithm",
    "memetic_algorithm": "Memetic Algorithm",
}


def load(name):
    df = pd.read_csv(os.path.join(src_dir, f"{name}.csv"))
    df = df.set_index("dimension")
    return df


def build_comparison_table(algo_keys, title, out_name, footnote=None):
    """
    algo_keys: list of csv basenames (without .csv) to compare, in the
    order they should appear as columns.
    """
    dfs = {k: load(k) for k in algo_keys}

    # union of all dimensions present across the compared algorithms
    all_dims = sorted(set().union(*[df.index for df in dfs.values()]))

    rows = []
    for dim in all_dims:
        row = [dim]
        for k in algo_keys:
            if dim in dfs[k].index:
                obj = dfs[k].loc[dim, "average_objective"]
                t = dfs[k].loc[dim, "time"]
                row.append(f"{obj:.2f}" if pd.notna(obj) else "—")
                row.append(f"{t:.4f}" if pd.notna(t) else "—")
            else:
                row.append("—")
                row.append("—")
        rows.append(row)

    columns = ["Dim"]
    for k in algo_keys:
        label = ALGO_LABELS.get(k, k)
        columns.append(f"{label}\nObjective")
        columns.append(f"{label}\nTime (s)")

    df_display = pd.DataFrame(rows, columns=columns)

    n_rows = len(df_display)
    n_cols = len(columns)
    fig_width = 1.6 * n_cols
    fig_height = 0.4 * n_rows + 1.4
    fig, ax = plt.subplots(figsize=(fig_width, fig_height))
    ax.axis("off")
    ax.set_title(title, fontsize=15, fontweight="bold", pad=16)

    table = ax.table(
        cellText=df_display.values,
        colLabels=df_display.columns,
        cellLoc="center",
        loc="center",
    )
    table.auto_set_font_size(False)
    table.set_fontsize(9)
    table.scale(1, 1.5)

    # header styling
    for j in range(n_cols):
        cell = table[0, j]
        cell.set_facecolor("#2c3e50")
        cell.set_text_props(color="white", fontweight="bold")

    # zebra stripes
    for i in range(1, n_rows + 1):
        color = "#f2f2f2" if i % 2 == 0 else "white"
        for j in range(n_cols):
            table[i, j].set_facecolor(color)

    # widen the "Dim" column, keep the rest even
    table.auto_set_column_width(col=list(range(n_cols)))

    if footnote:
        fig.text(0.5, 0.01, footnote, ha="center", fontsize=8, style="italic", color="#555555")

    plt.tight_layout()
    out_path = os.path.join(out_dir, out_name)
    plt.savefig(out_path, dpi=200, bbox_inches="tight")
    plt.close(fig)
    print("Saved", out_path)


BF_NOTE = "— : brute force not computed beyond dimension 11 (exponential runtime, 15,743s at n=11)"

# Table 1: exact method vs. constructive heuristics
build_comparison_table(
    ["brute_force", "greedy", "modified_greedy"],
    "Brute Force vs. Greedy vs. Modified Greedy",
    "table1_brute_greedy_modgreedy.png",
    footnote=BF_NOTE,
)

# Table 2: exact method vs. local-search-based metaheuristics
build_comparison_table(
    ["brute_force", "local_search", "vns", "simulated_annealing"],
    "Brute Force vs. Local Search vs. VNS vs. Simulated Annealing",
    "table2_brute_ls_vns_sa.png",
    footnote=BF_NOTE,
)

# Table 3: exact method vs. population-based metaheuristics (+ VNS for reference)
build_comparison_table(
    ["brute_force", "genetic_algorithm", "memetic_algorithm", "vns"],
    "Brute Force vs. Genetic Algorithm vs. Memetic Algorithm vs. VNS",
    "table3_brute_ga_ma_vns.png",
    footnote=BF_NOTE,
)
