# Overview
Tutorial 0 done, should add a few more by end of April or so  
[Youtube Video](https://youtu.be/iEaU__JdI7c)
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
cd python_chess
conda create -n python_chess python=3.9 pandas=1.3.4 jupyter=1.0.0 matplotlib=3.4 -y
conda activate python_chess
pip install -r requirements.txt
```
Then you need to download the Stockfish executable and place it on your PATH.  
- https://stockfishchess.org/download/ #choose the AVX2
- Check it's loaded on your PATH or edit your environment variables it include it. I have a folder on my computer called misc_apps that is always added to PATH
- (Watch the video](https://youtu.be/iEaU__JdI7c) if you aren't sure how to do this, it is a little bit trickier for newer developers

## Running the Code
From the tutorials directory
```
cd python_chess
conda activate python_chess
jupyter notebook
```