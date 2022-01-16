###[Notebooks Done]! Feel free to get started using this. It "should" work. I'm working on creating some videos now.
# Overview
Takes a video of page turning, identifies pages, does OCR, and generates an audio file.    
It should be realitvely easy to create your own page turning video. Just notice how in my video I keep the camera still and avoided having too many shadows in the video
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
cd book_scanner_to_audiobook
conda env create -f environment.yaml
```

## Running the Code
From the tutorials directory
```
cd book_scanner_to_audiobook
conda activate book_scanner_to_audiobook
jupyter notebook
```