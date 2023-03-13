# Overview
[Watch on Youtube](https://youtu.be/fmJ4h_WAIXI) or [read the blogpost](https://www.ergosum.co/learn-how-to-use-jupyter-while-scraping-dogecoin-prices/)
## Install Steps
If this is your first tutorial you've used please start with the base [README.md](https://github.com/rogerfitz/tutorials/blob/master/README.md) file. Then proceed with the install steps below

```
git clone https://github.com/rogerfitz/tutorials
cd tutorials
```
The exact python version doesn't matter because with each project I'll have you create a different environment with the proper version of python.

From the tutorials directory
```
git pull origin master
cd _introduction_to_jupyter_notebooks
conda create -n jupyter_notebooks python=3.9 pandas=1.3.2 jupyter=1.0.0 matplotlib=3.4.2 -y
conda activate jupyter_notebooks
pip install -r requirements.txt
```

## Running the Code
With jupyter_notebooks "activated" and in this directory: `conda activate jupyter_notebooks`
```
jupyter notebook
```
