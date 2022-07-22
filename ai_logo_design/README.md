# Using AI to Create Logos
[Explainer Youtube Video](https://youtu.be/KhmOJzCmu1o) - Learn how to make a logo using AI, postprocess in Python or GIMP, and make your own T-Shirt!
-  0_Generating_and_Postprocessing_the_Logo
-  [Using guiding icons to control the AI](https://youtu.be/sZJ8m4zP8FM)


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
cd ai_logo_design
conda env create -f environment.yml
```

## Running the Code
From the tutorials directory
```
cd ai_logo_design
conda activate ai_logo_design
jupyter notebook
```