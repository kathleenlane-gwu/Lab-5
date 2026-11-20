# Lab-5
Repository for Lab 5

```
Lab-5/
├── README.md
├── environment.yml
├── Snakefile
├── data/
    ├── messy_samples.csv
    ├── cohort.db
├── scripts/
    ├── features.py
    ├── samples.R
    ├── report.py
├── results/
    ├── clean_samples.csv
    ├── feature_table.tsv
    ├── summary_figure.png
    ├── summary_report.md
├── evidence/
    ├── 01_clean_run.txt
    ├── 03_partial_rerun.txt
├── .gitignore      
└── AI_USAGE.md
```

## Necessary Tools/Downloads for Repository
* Terminal
* Python -- https://www.python.org/downloads/
* Miniforge for Conda/Mamba -- https://github.com/conda-forge/miniforge/releases
* R -- https://www.r-project.org/

## Getting Started
Open the terminal on your computer and copy/paste the code below into the terminal. The cd ~/Desktop command tells the computer to work within your Desktop folder and will clone the repo there. The git clone command will clone the Lab-5 repository using the GitHub URL. Then cd Lab-5 enters the repository, and ls lets you view the files in the repo. You should see the same files from the project structure above.
```
cd ~/Desktop
git clone https://github.com/kathleenlane-gwu/Lab-5.git
cd Lab-5
ls 
```
## Analysis
To run the Snakemake file, you will need to have the correct environment.

In the terminal, copy/paste the following code. `mamba env create` recreates the necessary environment from the `environment.yml` file. We then need to access the Lab-5 environment, which has the necessary Python/R/Snakemake versions and associated packages needed to run our Snakemake file. `Snakemake --version` tells you what version of Snakemake you have. It should return 9.x (ex. 9.27.2).
```
mamba env create -f environment.yml
conda activate Lab-5
Snakemake --version
```


## Running Pipeline from Clean Slate
Run the following code to run the full pipeline from a clean slate. This code creates a folder called `evidence` with a .txt file `01_clean_run.txt` that shows the terminal output from running the Snakemake file from a clean slate.
```
mkdir evidence
snakemake --cores 1 -p 2>&1 | tee evidence/01_clean_run.txt
```
The screenshot below shows that all four Snakemake rules were run.
<img width="570" height="502" alt="Screenshot 2026-11-18 at 2 18 17 PM" src="https://github.com/user-attachments/assets/44eb8d8f-2c04-4d97-b592-bad8f59df526" />


## Changing Upstream Input
Run the following code to delete `clean_samples.csv` from the results folder. This will cause a partial re-run, as only three of the four Snakemake rules rely on this file. This code adds another .txt file called `03_partial_rerun.txt` to the `evidence` folder that shows the terminal output from running the Snakemake file after deleting `clean_samples.csv`.
```
rm results/clean_samples.csv && snakemake --cores 1 -p 2>&1 | tee evidence/03_partial_rerun.txt
```
The screenshot below shows that only three of the four Snakemake rules were run.
<img width="566" height="460" alt="Screenshot 2026-11-18 at 2 14 32 PM" src="https://github.com/user-attachments/assets/dff039c0-ef45-49a0-b0c0-96e2515c6954" />

