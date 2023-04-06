# My coding setups

* Things I often do and throw in readme's but which were across my projects.
* Also I find helpful information and then forget it, so this is quick reference for myself.
* These have some helpful hints and are the precursor to this readme.
* <https://gist.github.com/garland3>

## Python setup

Everything related to setting up python

### Isolation

* Always use a seperate python enviroment.
* I liked using `conda`  for a long time, but in general seems like `pip` is easier to use. However, you can't specify a python version with `pip`, so now I make a `conda` enviroment and then install everything with `pip`.

```bash
# https://docs.conda.io/en/latest/miniconda.html
wget https://repo.anaconda.com/miniconda/Miniconda3-py39_4.12.0-Linux-x86_64.sh
chmod 711 Miniconda3-py39_4.12.0-Linux-x86_64.sh
sh Miniconda3-py39_4.12.0-Linux-x86_64.sh
```


* In this example, you would want to give something other than `MYNAME` and also specify which version of `python` that you actually want to use.

```bash
conda create --name MYNAME python=3.10
conda activate MYNAME
pip install mycoolpackagees
pip list --format=freeze > requirements.txt
# conda env export --no-builds > my_env.yml
# make the enviroment
pip install -r requirements.txt
# conda env create -n MYNAME -f my_env.yml
# conda env update --file my_env.yml --prune
# OR to update an env that you are not in (probably better)
# conda env update --name myenv --file my_env.yml --prune
```

### Jupyter

Sometimes kernels are not added automatically. Assuming you have a `conda` setup, then try this.  

```bash
conda activate mytestenv
pip install ipykernel
python -m ipykernel install --user --name=mytestenv
```

### Specific python package index
```bash
pip install XXX -i  https://pypi.org/simple
# install a git repo
pip install git+blahblah
```



### Python try-except

The default debug messages in python are OK. But using traceback can help a lot for finding problems.

```python
import traceback
try:
  raise Exception("my error")
except Exception as e:
  print(e)
  print(traceback.format_exc())
```

## Working Dir setup

### Config
Dynaconfig seems to work well. https://www.dynaconf.com/
### Folder setup
Pyscaffold works well. https://pyscaffold.org/en/stable/

## Cuda version

```bash
nvidia-smi
```

* I have several of these items in `gists` already and reference them often, but I feel like a more structured approach would be better.

## VScode

I like to use VScode.

### Extensions

Here are my extensions that I think are helpful

* `Copilot`  for using a LLM to complete my code. :)
* `Docker`  for docker syntax highlighting
* `Python` from microsoft
* `Pylance` language server for python. If it is having a hard time finding a package, you might need to add the path explicitly.
  * Go to settings
  * Search for `add item`
  * find the `python -> analysis:Extra paths`
  * add the `../site-packages` or where ever the path you want to add is actually located.
  * You do this by clicking `add Item`
* `Remote - Containers` Lets you develop INSIDE a container which is super helpful.
* `Remote SSH` Same
* `Remote Development` Same.
* `markddownlint` helpful for making better looking markdown. Sometimes it can be  pain, but most of the time it is good.
* CSV color highlighter??
* `google-search` maybe. still experimenting with this one.
* `diff` a simple tool for diffing 2 files.

### VScode short cuts

I can never remember them all, but here are some that are helpful.

* `ctrl` + `B`, close the side panel
* `ctrl` + `shift` + `E`, open the explore panel
* `ctrl` + `g`, then type a line number to jump to that line.
* `ctrl` + `p` then type the name of a file, to go that file.
* `ctrl` +  `shift`  + `p` to open the command center
* `ctrl` + `backtick` to go the terminal
* `ctrl` + `1` or (`2` , ...) to go to the split window text editor (or open it)

This video has a lot of great hits. <https://www.youtube.com/watch?v=ifTF3ags0XI>
Also here are some great tips. <https://code.visualstudio.com/docs/getstarted/tips-and-tricks>

## Docker
ON windows sometimes docker causes problems. If I stop docker and memory usage is super high still, then stop the wsl
```ps
wsl --shutdown
```

## Git
Fix untracked files
 
 ```bash
git rm -r --cached .    
git add .    
git commit -m "fixed untracked files"    

 ```

* I always forget how to undo the last commit. Here is the command.

 ```
 git reset HEAD~    
 ```
 
 
 
 * I alwyas forget how to make a local repo, and sync for the 1st time to a remote repo. 
 ```
 git pull origin main  -f --allow-unrelated-histories
 ```
 
 When merging and you want to keep `theirs` or `ours`
 ```bash
 git merge -X theirs otherbranch
 ```

## Enviroments

### Linux

* See the enviroment (Ubuntu)

```bash
printenv
printenv | grep txtImLookingfor
```

* set var

```
set MYVAR=MYVALUE
```
 
 
 ## Linux Screen
 You can use the screen tool to keep your process running after you close your ssh session (at least that is my most common use case). Here are the short cuts you need. 
 * `screen` to start a new screen terminal
 * `screen -ls` to list screens
 * `screen -r XXXX` to attach (go into) a particular screen session
 * `exit` in the terminal to stop/end a screen session
<!--  * `ctrl` + `a` then `"` to list all existing screens -->

## Linux `top`
`top` command can be super helpful for understanding if you are actually using your computer to the max or why things are running slow. This link walks you through using it. 
https://www.howtogeek.com/668986/how-to-use-the-linux-top-command-and-understand-its-output/


### cuda on ubuntu 22.04
1. activate the additional drivers and install nvidia-XXX-515 (the newest 520 didnt' work for me)
2. download the cuda-11.7 runfile (don't try the network version). Install only cuda (skip the driver)
3. add cuda to the path
```bash
export PATH="/usr/local/cuda-11.7/bin:$PATH"
export LD_LIBRARY_PATH="usr/local/cuda-11.7/lib64:$LD_LIBRARY_PATH"
```
4. download and install Miniconda (see download at the top)
5. make new `env` and then install torch into the `env`. `conda install pytorch torchvision torchaudio pytorch-cuda=11.7 -c pytorch -c nvidia`
6. install other things `sudo apt-get install openssh-server`
7. remote into the machine and try some training https://github.com/pytorch/examples/blob/main/mnist/main.py
8. be happy


## Windows copy some text from a file. 
```cmd
type mytext.txt | clip
```
