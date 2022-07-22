# Overview
I show you how I made https://github.com/rogerfitz/icon-image a pip package to help with AI logo generation.  

[Youtube Video](https://youtu.be/sZJ8m4zP8FM)
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
cd make_your_own_pip_package
conda env create -f environment.yml
git clone <PACKAGE YOU ARE FORKING OR TRYING TO PUT ON PYPI>
#Then see steps below 
```

## Steps to Make your Own Package on Pip
1. Forked https://github.com/minimaxir/icon-image
1. Installed test python env of python 3.9 with latest pillow, numpy using conda. Rest with pip
1. Added setup.cfg
1. Added setup.py
1. Moved packages to icon_image and edited setup.py vars
1. installed twine==4.0.1 (`pip install twine==4.0.1`) (a dev dependency not actual dependency)
1. Create pypi.org account and verified email
1. Ran the steps under MAKE (on windows just delete dist directory manually if it already exists)
