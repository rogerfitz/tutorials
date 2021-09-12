# Overview
[IN PROGRESS NOT DONE YET! TUTORIAL 0 is FINISHED]  
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
cd subreddit_analyzer
conda create -n subreddit_analysis python=3.9 pandas=1.3.2 jupyter=1.0.0 -y
conda activate subreddit_analysis
pip install -r requirements.txt
```

## Running the Code
```
jupyter notebook
```

## Modules
1. [Project setup and API Basics](https://github.com/rogerfitz/tutorials/blob/master/subreddit_analysis/0_Setup.ipynb)
1. Top Links over period [store links with depth and upvotes], say you're interested in knowing what sites are biggest in the learn python community
1. Finding the Top Keywords [basics of gensim or nltk]
1. Analyze the interests of people who comment on a post [pedalboard /r/python]
1. Further work [website, Reddit bot, argument detection, proper NSFW categorizer that lets you filter out porn but keep the rest]

## Other
Feedback welcome!  
I've considered adding a .py example with usage like `python analyze_subreddit --name learnpython`. If you'd like me to make that let me know
