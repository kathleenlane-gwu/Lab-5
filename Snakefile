rule all:
    input:
        "results/cleaned_samples.csv",
        "results/feature_table.tsv"

rule clean_samples:
    input:
        "data/messy_samples.csv"
    output:
        "results/cleaned_samples.csv"
    shell:
        "Rscript scripts/samples.R"

rule make_features:
    input:
        "data/cohort.db"
    output:
        "results/feature_table.tsv"
    shell:
        "python scripts/features.py"