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
conda create -n scraping_insider_trading python=3.9 pandas=1.3.2 jupyter=1.0.0 matplotlib=3.4.2 -y
pip install -r requirements.txt
conda activate scraping_insider_trading
```

## Running the Code
From the tutorials directory
```
cd scraping_insider_trading
conda activate scraping_insider_trading
jupyter notebook
```