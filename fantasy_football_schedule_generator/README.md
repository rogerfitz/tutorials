# Generating Fantasy Football Schedules for your Divisional League

[Video that uses this](https://www.youtube.com/watch?v=KBxQa6dycto)

# IMPORTANT NOTE
You must have an even number of teams in your divisions and conferences for this approach to work

#### Outline

I'm a co-commissioner in a fantasy football league. Yahoo doesn't do a good job creating a simple divisional schedule
like play your division twice then random for every one else. I didn't see any schedule generators up yet and decided to make my own in python
real quick. Take a gander, feel free to update the code as you wish.

## Install
If this is your first tutorial you've used please start with installing miniconda and cloning the repo.  
Install miniconda https://docs.conda.io/en/latest/miniconda.html (choose latest python version under your OS. Likely 64 bit)
```
git clone https://github.com/rogerfitz/tutorials
cd fantasy_football_schedule_generator
```
The exact python version doesn't matter because with each project I'll have you create a different environment with the proper version of python.

From the tutorials directory
```
git pull origin master
cd fantasy_football_schedule_generator
conda env create -f environment.yml
```

## Running the Code
From the tutorials directory
```
cd fantasy_football_schedule_generator
conda activate fantasy_football_schedule_generator
jupyter notebook
```