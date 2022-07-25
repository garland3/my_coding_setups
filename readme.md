# My coding setups

* Things I often do and throw in readme's but which were across my projects.
* Also I find helpful information and then forget it, so this is quick reference for myself.
* I have several of these items in `gists` already and reference them often, but I feel like a more structured approach would be better.

## VScode

I like to use VScode.

### Extensions

Here are my extensions that I think are helpful

* `Git Project Manager`. lets you click on a few things rather than remembering all the `git commands`.
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

### VScode short cuts

I can never remember them all, but here are some that are helpful.

* `ctrl` + `g`, then type a line number to jump to that line.
* `ctrl` + `p` then type the name of a file, to go that file.
* `ctrl` +  `shift`  + `p` to open the command center
* `ctrl` + `backtick` to go the terminal
* `ctrl` + `1` or (`2` , ...) to go to the split window text editor (or open it)

This video has a lot of great hits. <https://www.youtube.com/watch?v=ifTF3ags0XI>

## python setup

Everything related to setting up python

### Isolation

* Always use a seperate python enviroment. 
* I liked using `conda`  for a long time, but in general seems like `pip` is easier to use. However, you can't specify a python version with `pip`, so now I make a `conda` enviroment and then install everything with `pip`.
* In this example, you would want to give something other than `MYNAME` and also specify which version of `python` that you actually want to use.

```bash
conda create --name MYNAME python=3.10
conda activate MYNAME
pip install mycoolpackagees
pip list --format=freeze > requirements.txt
# make the enviroment
pip install -r requirements.txt
```

### Jupyter

Sometimes kernels are not added automatically. Assuming you have a `conda` setup, then try this.  

```bash
conda activate mytestenv
pip install ipykernel
python -m ipykernel install --user --name=mytestenv
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

## My Gists
* These have some helpful hints and are the precursor to this readme.
* https://gist.github.com/garland3
