# Overview

Install steps for [FuseDream](https://github.com/gnobitab/FuseDream) as of 12/8/2021. My GPU too small, I think you need 16GB of GPU memory, so shelving this for now but I hope this helps someone. 

## Install
```
conda create -n image_generation_with_fuse_dream python=3.7
conda activate image_generation_with_fuse_dream
git clone https://github.com/gnobitab/FuseDream.git
conda install pytorch=1.10.0 torchvision=0.11.1 torchaudio=0.10.0 cudatoolkit=11.3 -c pytorch
pip install ftfy regex tqdm numpy scipy h5py lpips==0.1.4
pip install git+https://github.com/openai/CLIP.git
```
Download weights from https://drive.google.com/drive/folders/1nJ3HmgYgeA9NZr-oU-enqbYeO7zBaANs?usp=sharing and store under FuseDream/BigGan_utils/weights
## Run
With your shell in the FuseDream folder and the image_generation_with_fuse_dream directory activated run:  
```
python fusedream_generator.py --text 'A photo of a blue dog.' --seed 1234
```