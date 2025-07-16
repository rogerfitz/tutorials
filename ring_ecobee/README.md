# Rincobee - Connecting your Ring with Ecobee
Integration between Ring and Ecobee to set to away when you leave
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
cd ring_ecobee
conda env create -f environment.yml
conda activate ring_ecobee
python -m playwright install chromium
```
Run with python run.py. Setup with Cron to run every 5 minutes.
```
*/5 * * * * cd /home/ubuntu/ && /home/ubuntu/miniconda3/envs/ring_ecobee/bin/python /home/ubuntu/tutorials/ring_ecobee/run.py > /home/ubuntu/ring_ecobee.log
```