# Adjusted Strength of Schedule for the NFL
[IN PROGRESS!!]
Strength of schedule is a fundamentally flawed metric. Losing to a team shouldn't give you an easier strength of schedule. 
Let's remove those from the calculation and see if this produces better results
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
cd adjusted_strength_of_schedule
conda env create -f environment.yml
```

## Running the Code
From the tutorials directory
```
cd adjusted_strength_of_schedule
conda activate adjusted_strength_of_schedule
jupyter notebook
```