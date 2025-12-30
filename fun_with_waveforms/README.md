# Fun With Waveforms
Loosely inspired by https://github.com/torvalds/GuitarPedal/. My goal is to write Python that converts to mermaid, circuit blocks, and waveforms I can listen to in Jupyter. I should probably just figure out how to use KiCad or something though.
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
cd fun_with_waveforms
conda env create -f environment.yml
conda activate fun_with_waveforms
jupyter notebook
```