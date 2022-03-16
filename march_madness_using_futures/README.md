# [IN PROGRESS]HOPING TO KNOCK OUT BY end of day 3/16/2022
# March Madness Predictions Using the Crowd

In this tutorial I'll go through how to scrape sports betting futures 
to create a pretty decent march madness bracket. You can use this sort of approach with
lots of other sports too!
#### Outline
1. Intro
2. Scraping Futures Using Beautiful Soup
3. Implied Odds and Power Rankings
4. Generating a bracket
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
cd march_madness_using_futures
conda env create -f environment.yaml
```

## Running the Code
From the tutorials directory
```
cd march_madness_using_futures
conda activate march_madness_using_futures
jupyter notebook
```