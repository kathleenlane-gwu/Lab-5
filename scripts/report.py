import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

samples = pd.read_csv("results/clean_samples.csv")
features = pd.read_csv("results/feature_table.tsv", sep="\t")

def describe(df, title, filename, f):
    f.write(f"## {title}\n\n")
    f.write(f"`{filename}` has {len(df)} rows and {df.shape[1]} columns.\n\n")
    f.write("| Column | Type | Missing values |\n|---|---|---|\n")
    for col in df.columns:
        f.write(f"| {col} | {df[col].dtype} | {int(df[col].isna().sum())} |\n")
    f.write("\n")

with open("results/summary_report.md", "w") as f:
    f.write("# Summary Report\n\n")
    describe(samples, "Cleaned samples", "clean_samples.csv", f)
    describe(features, "Patient feature table", "feature_table.tsv", f)

# Figure: left = size of each table, right = % missing values per column
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Panel 1: rows and columns per table (grouped bars)
tables = ["Samples", "Features"]
rows = [len(samples), len(features)]
cols = [samples.shape[1], features.shape[1]]
x = range(len(tables))
bars_rows = ax1.bar([i - 0.2 for i in x], rows, width=0.4, label="Rows")
bars_cols = ax1.bar([i + 0.2 for i in x], cols, width=0.4, label="Columns")
ax1.bar_label(bars_rows, padding=3)
ax1.bar_label(bars_cols, padding=3)
ax1.set_xticks(list(x))
ax1.set_xticklabels(tables)
ax1.set_ylabel("Count")
ax1.set_title("Table dimensions")
ax1.margins(y=0.1)
ax1.legend()

# Panel 2: percent missing per column, both tables together
missing = pd.concat([
    (samples.isna().mean() * 100).rename(lambda c: f"samples: {c}"),
    (features.isna().mean() * 100).rename(lambda c: f"features: {c}"),
])
colors = ["tab:blue"] * samples.shape[1] + ["tab:orange"] * features.shape[1]
bars_missing = ax2.barh(missing.index, missing.values, color=colors)
ax2.bar_label(bars_missing, fmt="%.1f%%", padding=3)
ax2.set_xlabel("% missing")
ax2.set_title("Missing values by column")
ax2.margins(x=0.15)
ax2.invert_yaxis()

fig.tight_layout()
fig.savefig("results/summary_figure.png", dpi=150)