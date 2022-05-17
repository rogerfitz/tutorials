# Menu Scraping at Scale
First video done.
1. How to Scrape a PDF Menu - [Youtube](https://youtu.be/VP7mrps2u_8) 

Will cover PDF, web scraping, and how to orchestrate a spider to scrape unseen websites
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
cd menu_spider_scraping
conda env create -f environment.yml
```

## Running the Code
From the tutorials directory
```
cd menu_spider_scraping
conda activate menu_spider_scraping
jupyter notebook
```