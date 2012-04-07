#! /usr/bin/env bash

# http://ubuntuforums.org/showthread.php?t=1818188
# numpy install dependencies
sudo apt-get install -y gcc gfortran \
 python3.2 python3.2-dev libatlas-base-dev

#numpy installation
mkdir -p ${HOME}/opt/numpy/
cd ${HOME}/opt/numpy
wget http://sourceforge.net/projects/numpy/files/NumPy/1.6.1/numpy-1.6.1.tar.gz
tar xzf numpy-1.6.1.tar.gz
unset PYTHONPATH
cd numpy-1.6.1
python3.2 setup.py build --fcompiler=gnu95
sudo python3.2 setup.py install
