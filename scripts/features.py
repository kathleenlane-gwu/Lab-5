import sqlite3, pandas as pd
con = sqlite3.connect('scripts/cohort.db')
def q(sql): return pd.read_sql(sql, con)

task_one = q('''SELECT p.patient_id, m.gene_symbol, COUNT(m.variant_classification) AS protein_altering_mutations
FROM patients p
LEFT JOIN samples s on s.patient_id=p.patient_id
LEFT JOIN mutations m on m.sample_id=s.sample_id
WHERE gene_symbol in ('TP53','KRAS','EGFR','STK11','KEAP1') AND (variant_classification != 'silent')
GROUP BY p.patient_id, m.gene_symbol''')

wide_task_one = task_one.pivot_table(index="patient_id", columns="gene_symbol" , values="protein_altering_mutations")

feature_table = q('''SELECT p.patient_id, p.sex, p.age_at_diagnosis, p.stage, s.tissue_source_site, s.tmb_nonsynonymous
FROM patients p
LEFT JOIN samples s on s.patient_id=p.patient_id''')

feature_table = feature_table.merge(wide_task_one.reset_index(), on="patient_id", how="left")

feature_table.to_csv("results/feature_table.tsv", sep="\t", index=False)