# Overview
[IN PROGRESS NOT DONE YET!]  
Here are a few tutorials meant to get you started quickly with using the reddit API. It's meant to take no more than a weekend to go through and provide you with the building blocks you need to do your own projects using Reddit.
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
cd introduction_to_jupyter_notebooks
conda create -n intro_jupyter python=3.9 pandas=1.3.2 jupyter=1.0.0 matplotlib=3.4.2 -y
conda activate intro_jupyter
```

## Running the Code
With intro_jupyter "activated" and in the tutorials directory: `conda activate intro_jupyter`
```
jupyter notebook
```

## Modules

