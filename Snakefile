rule all:
    input:
        "results/clean_samples.csv",
        "results/feature_table.tsv",
        "results/summary_report.md",
        "results/summary_figure.png"

rule clean_samples:
    input:
        "data/messy_samples.csv",
        "scripts/samples.R"
    output:
        "results/clean_samples.csv"
    shell:
        "Rscript scripts/samples.R"

rule make_features:
    input:
        "data/cohort.db",
        "scripts/features.py"
    output:
        "results/feature_table.tsv"
    shell:
        "python scripts/features.py"

rule summary_report:
    input:
        "results/clean_samples.csv",
        "results/feature_table.tsv",
        "scripts/report.py"
    output:
        "results/summary_report.md",
        "results/summary_figure.png"
    shell:
        "python scripts/report.py"