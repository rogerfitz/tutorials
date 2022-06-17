# Using Prediction Markets to Budget and Hedge for Your Roadtrip

1. [Video](https://youtu.be/ZsUi_HAwJzg) Intro: Overview, Connecting to Kalshi and using Kalshi to Estimate Gas Prices
2. COMING SOON -- Hedging your Roadtrip using Kalshi

#### Outline

## Install
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
cd kalshi_prediction_market
conda env create -f environment.yml
```

## Running the Code
From the tutorials directory
```
cd kalshi_prediction_market
conda activate kalshi_prediction_market
jupyter notebook
```