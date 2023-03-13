# Analyzing Sports Betting
In this folder I analyze casino win percents from publically available data and attempt to interpret why. 
[Youtube video](https://www.youtube.com/watch?v=ABdukCadhs4) 
#### Outline
1. Intro
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
cd analyzing_sports_betting
conda env create -f environment.yml
```

## Running the Code
From the tutorials directory
```
cd march_madness
conda activate analyzing_sports_betting
jupyter notebook
```