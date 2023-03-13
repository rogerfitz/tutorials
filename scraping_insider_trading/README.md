# Overview
[VERY MUCH IN PROGRESS NOT DONE YET!]  
## Install Steps
If this is your first tutorial you've used please start with installing miniconda and cloning the repo.  
Install miniconda https://docs.conda.io/en/latest/miniconda.html (choose latest python version under your OS. Likely 64 bit)
```
git clone https://github.com/rogerfitz/tutorials
cd tutorials
```
The exact python version doesn't matter because with each project I'll have you create a different environment with the proper version of python.

From the tutorials directory
```
git pull origin master
cd scraping_insider_trading
conda env create -f environment.yaml
conda activate scraping_insider_trading
pip install -r requirements.txt
```

## Running the Code
From the tutorials directory
```
cd scraping_insider_trading
conda activate scraping_insider_trading
jupyter notebook
```