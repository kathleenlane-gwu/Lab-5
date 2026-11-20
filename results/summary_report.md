# Summary Report

## Cleaned samples

`clean_samples.csv` has 46 rows and 8 columns.

| Column | Type | Missing values |
|---|---|---|
| sample_id | object | 0 |
| glucose_value | float64 | 0 |
| glucose_unit | object | 0 |
| patient_name | object | 0 |
| dob | object | 0 |
| sex | object | 0 |
| enrollment_site | object | 0 |
| notes | object | 42 |

## Patient feature table

`feature_table.tsv` has 566 rows and 11 columns.

| Column | Type | Missing values |
|---|---|---|
| patient_id | object | 0 |
| sex | object | 52 |
| age_at_diagnosis | float64 | 71 |
| stage | object | 54 |
| tissue_source_site | object | 0 |
| tmb_nonsynonymous | float64 | 0 |
| EGFR | float64 | 494 |
| KEAP1 | float64 | 462 |
| KRAS | float64 | 398 |
| STK11 | float64 | 490 |
| TP53 | float64 | 279 |

