# PyMTL Installation Process

Refer to the following page for more details:
[GitHub cornell-brg/pymtl]
(https://github.com/cornell-brg/pymtl)

## Install Verilator

```
sudo apt-get install git make autoconf g++ flex bison
sudo -i
mkdir -p ${HOME}/src
cd ${HOME}/src
wget http://www.veripool.org/ftp/verilator-3.876.tgz
tar -xzvf verilator-3.876.tgz
cd verilator-3.876
./configure
make
sudo make install
export PYMTL_VERILATOR_INCLUDE_DIR="/usr/local/share/verilator/include"
```

## Install git, Python headers, and libffi

```sudo apt-get install git python-dev libffi-dev```

## Install virtualenv

```
sudo apt-get install python-virtualenv
mkdir ${HOME}/venvs
virtualenv --python=python2.7 ${HOME}/venvs/pymtl
source ${HOME}/venvs/pymtl/bin/activate
```

## Install PyMTL

```
mkdir -p ${HOME}/vc/git-hub/cornell-brg
cd ${HOME}/vc/git-hub/cornell-brg
```

Their suggestion is to use `git+https`, I was able to clone using `https`.

```
git clone https://github.com/cornell-brg/pymtl.git
pip install --editable ./pymtl
```


## Initial testing to make sure PyMTL is working

`cd /home/vc/git-hub/cornell-brg`

Running Python

```
python
>>> from pymtl import *
>>> a = Bits(8, 255)
>>> a
Bits( 8, 0xff )
```

## PyMTL Test Preparation

```
mkdir -p ${HOME}/vc/git-hub/cornell-brg/pymtl/build
cd ${HOME}/vc/git-hub/cornell-brg/pymtl/build
```

Install the following packages to reduce the number of test errors.

```
sudo apt-get install python-setuptools
sudo apt-get install pylint // Test pylint by running pylint-gui
easy_install -U pytest
easy_install greenlet
easy_install cffi
```

To run the tests, make sure you're in the following directory as super user.
`/home/vc/git-hub/cornell-brg/pymtl/build`

## Running Tests
Warning since there are a lot of tests.

```
py.test ..
py.test .. --verbose
```

The Verilog simulation tests are only executed if the `--test-verilog` flag is 
provided. For Verilog testing to work, PyMTL requires that Verilator is on your 
`PATH` and that the `PYMTL_VERILATOR_INCLUDE_DIR` environment:
`py.test .. --test-verilog`

When you're done testing/developing, you can deactivate the virtualenv.
`deactivate`

## Add Python import path for `import pymtl`

[Stack Overflow - Permanently add a directory to PYTHONPATH]
(http://stackoverflow.com/questions/3402168/permanently-add-a-directory-to-pythonpath)

`export PYTHONPATH="${PYTHONPATH}:/home/vc/git-hub/cornell-brg/pymtl"`

However, still I'm forced to run Python files with PyMTL objects in the 
terminal. Also, I cannot use the Sublime's build to quickly check if a script
has errors or not.

`sudo apt-get install gtkwave`
