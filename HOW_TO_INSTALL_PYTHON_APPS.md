Installation
============

Operating systems and Python version
------------------------------------

The library/tool is designed to work with Python 3 (3.9 and greater), from the official Python 
implementation [CPython](https://www.python.org/), and is systematically tested on Windows. 
It should also support any other operating systems which has a decent Python 3 support.

Dependencies
------------

All Required packages are listed in requirements.txt, which is further bifurcated in 4 categories:
1. ```requirements_build.txt```Needed Build Tools / Libraries 
2. ```requirements_external.txt```Needed External Tools / Libraries
3. ```requirements_internal_lib.txt```Needed Internal Libraries
4. ```requirements_internal_tool.txt```Needed Internal Tools

Few Basic Scripts are also present under <i>scripts</i> folder.
   - Currently, Scripts are targeting virtual environment with folder name as <i>venv</i> (Present in parallel of <i>scripts</i> folder)
   - However, same can be modified as per user choice.
    
   **Note:** installing library/tool in virtual environment is optional but preferred.

Automatic installation
----------------------

An installation script is available.
As soon as you have cloned or downloaded the repository, you can use it to install
the tool/library within your Python package directory:

```
python setup.py install
```