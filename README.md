# Lab-5
Repository for lab 5

```
Lab-5/
├── README.md
├── environment.yml
├── renv.lock
├── Snakefile
├── data/
    ├── messy_samples.csv
    ├── cohort.db
├── scripts/
    ├── features.py
    ├── samples.R
├── results/
    ├── clean_samples.csv
    ├── feature_table.tsv
├── .gitignore      
└── AI_USAGE.md
```

## Necessary Tools/Downloads for Repository
* Terminal
* Python -- https://www.python.org/downloads/
* VS Code (optional) -- https://code.visualstudio.com/
* Miniforge for Conda/Mamba -- https://github.com/conda-forge/miniforge/releases

## Getting Started
Open the terminal on your computer and copy/paste the code below into the terminal. The cd ~/Desktop command tells the computer to work within your Desktop folder and will clone the repo there. The git clone command will clone the Lab-5 repository using the GitHub URL. Then cd Lab-5 enters the repository, and ls lets you view the files in the repo. You should see the same files from the project structure above.
```
cd ~/Desktop
git clone https://github.com/kathleenlane-gwu/Lab-5.git
cd Lab-5
ls 
```
## Analysis
To run features.py and samples.R, you must first recreate the necessary environments. We will begin with the python file. 

In the terminal, copy/paste the following code. `mamba env create` recreates the necessary environment from the `environment.yml` file. We then need to access the hds-practical environment, which has the necessary Python and packages needed to run our analyses. Once these steps are complete, we can open and run the `analyze.py` file.
```
mamba env create -f environment.yml
conda activate Lab-5
python scripts/features.py
```
For our R file, open RStudio and copy/paste the following code into the R console. We are setting `Lab-5` as our working directory and initializing renv.  
```
setwd("~Desktop/Lab-5")
renv::init()
```
`renv::init()` will create four options to choose from. Choose the first option, "Restore the project from the lockfile" by entering '1' into the console. Then run the following in the R console.
```
source("scripts/samples.R")
```
