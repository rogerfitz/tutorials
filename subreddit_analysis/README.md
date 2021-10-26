# Overview
[TUTORIAL 3 still in progress!]
Here are a few tutorials meant to get you started quickly with using the reddit API. It's meant to take no more than a weekend to go through and provide you with the building blocks you need to do your own projects using Reddit.  
NOTE: Reddit has a limit of 1000 values per requests. These tutorials use the Reddit API. If you want to access more data use pushshift, they store a copy of reddit and give you much more history https://www.reddit.com/r/pushshift/comments/bcxguf/new_to_pushshift_read_this_faq/
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
conda create -n subreddit_analysis python=3.9 pandas=1.3.2 jupyter=1.0.0 matplotlib=3.4.2 -y
conda activate subreddit_analysis
pip install -r requirements.txt
```

## Running the Code
```
jupyter notebook
```

## Modules
1. [Project setup and API Basics](https://github.com/rogerfitz/tutorials/blob/master/subreddit_analysis/0_Setup.ipynb)
1. Top Links over period [part 1](https://github.com/rogerfitz/tutorials/blob/master/subreddit_analysis/1_Top_Links.ipynb) [part 2](https://github.com/rogerfitz/tutorials/blob/master/subreddit_analysis/2_Top_Links_with_Basic_Cleaning.ipynb)
   - Say you're interested in knowing what sites are biggest in the /r/learnpython community
1. Analyze the interests of people who comment on a post [pedalboard /r/python]
1. Further work [website, Reddit bot, argument detection, proper NSFW categorizer that lets you filter out porn but keep the rest]

## Other
Feedback welcome!  
I've considered adding a .py example with usage like `python analyze_subreddit --name learnpython`. If you'd like me to make that let me know
