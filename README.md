# tutorials

### Setup
### NEW CHANGES
Going forward all new tutorial projects will follow the pattern of subreddit_analysis/ 
with a readme and specific install steps.  
  
For older projects feel free to create
an issue if you need help installing and I will fix it sooner. In general I would recommend using [Miniconda](https://docs.conda.io/en/latest/miniconda.html) 
Latest 64 bit for your operating system.

### Install Steps
Windows:  
1. Download [Minconda](https://docs.conda.io/en/latest/miniconda.html) -- Select Latest Windows 64 bit
1. Install and select the option to add Minconda to your system path (it isn't default)
1. Install [Windows Terminal](https://www.microsoft.com/en-us/p/windows-terminal/9n0dx20hk701?activetab=pivot:overviewtab)
1. [Optional but recommended] Install [git-bash](https://git-scm.com/downloads)
1. Open windows terminal and select a shell of your choice, on Windows I use Command Prompt or Git Bash
1. Test that conda was installed```  conda info  ```
  should give something like 
  ```
  active environment : None
         user config file : C:\Users\minim\.condarc
   populated config files :
            conda version : 4.10.1
      conda-build version : not installed
           python version : 3.9.1.final.0
         virtual packages : __cuda=11.3=0
                            __win=0=0
                            __archspec=1=x86_64
         base environment : C:\Users\minim\miniconda3  (writable)
        conda av data dir : C:\Users\minim\miniconda3\etc\conda
    conda av metadata url : https://repo.anaconda.com/pkgs/main
             channel URLs : https://repo.anaconda.com/pkgs/main/win-64
                            https://repo.anaconda.com/pkgs/main/noarch
                            https://repo.anaconda.com/pkgs/r/win-64
                            https://repo.anaconda.com/pkgs/r/noarch
                            https://repo.anaconda.com/pkgs/msys2/win-64
                            https://repo.anaconda.com/pkgs/msys2/noarch
            package cache : C:\Users\minim\miniconda3\pkgs
                            C:\Users\minim\.conda\pkgs
                            C:\Users\minim\AppData\Local\conda\conda\pkgs
         envs directories : C:\Users\minim\miniconda3\envs
                            C:\Users\minim\.conda\envs
                            C:\Users\minim\AppData\Local\conda\conda\envs
                 platform : win-64
               user-agent : conda/4.10.1 requests/2.25.0 CPython/3.9.1 Windows/10 Windows/10.0.19041
            administrator : False
               netrc file : None
             offline mode : False
  ```
7. Now choose where you want to run the projects. Use `cd` commands and you can download the repository by doing `git clone https://github.com/rogerfitz/tutorials` 
7. Nearly done now, `cd` into the directory and test that a tutorial works. I'd recommend starting with [subreddit_analysis/README.md](https://github.com/rogerfitz/tutorials/blob/master/subreddit_analysis/README.md)

### Mac
Windows:  
1. Download [Minconda](https://docs.conda.io/en/latest/miniconda.html) -- Select Latest Mac 64 bit
1. Install and select the option to add Minconda to your system path (it isn't default)
1. Open the Mac Terminal and test that conda was installed```  conda info  ```
  should give something like 
  ```
  active environment : None
         user config file : C:\Users\minim\.condarc
   populated config files :
            conda version : 4.10.1
      conda-build version : not installed
           python version : 3.9.1.final.0
         virtual packages : __cuda=11.3=0
                            __win=0=0
                            __archspec=1=x86_64
         base environment : C:\Users\minim\miniconda3  (writable)
        conda av data dir : C:\Users\minim\miniconda3\etc\conda
    conda av metadata url : https://repo.anaconda.com/pkgs/main
             channel URLs : https://repo.anaconda.com/pkgs/main/win-64
                            https://repo.anaconda.com/pkgs/main/noarch
                            https://repo.anaconda.com/pkgs/r/win-64
                            https://repo.anaconda.com/pkgs/r/noarch
                            https://repo.anaconda.com/pkgs/msys2/win-64
                            https://repo.anaconda.com/pkgs/msys2/noarch
            package cache : C:\Users\minim\miniconda3\pkgs
                            C:\Users\minim\.conda\pkgs
                            C:\Users\minim\AppData\Local\conda\conda\pkgs
         envs directories : C:\Users\minim\miniconda3\envs
                            C:\Users\minim\.conda\envs
                            C:\Users\minim\AppData\Local\conda\conda\envs
                 platform : win-64
               user-agent : conda/4.10.1 requests/2.25.0 CPython/3.9.1 Windows/10 Windows/10.0.19041
            administrator : False
               netrc file : None
             offline mode : False
  ```
7. Install github command line if you don't have it already, in Mac terminal `brew install git`
7. Now choose where you want to run the projects. Use `cd` commands and you can download the repository by doing `git clone https://github.com/rogerfitz/tutorials` 
7. Nearly done now, `cd` into the directory and test that a tutorial works. I'd recommend starting with [subreddit_analysis/README.md](https://github.com/rogerfitz/tutorials/blob/master/subreddit_analysis/README.md)
