#! /usr/bin/env bash

# http://pythonfun.wordpress.com/
# 2011/08/08/installing-pygame-with-python-3-2-on-ubuntu-11-04/
#pygame install dependencies
sudo apt-get install -y python3-dev libsdl-image1.2-dev libsdl-mixer1.2-dev \
 libsdl-ttf2.0-dev libsdl1.2-dev libsmpeg-dev python-numpy subversion \
 libportmidi-dev libavformat-dev libswscale-dev python3

#pygame installation
mkdir -p ${HOME}/opt/pygame/src/
cd ${HOME}/opt/pygame/src/
svn co svn://seul.org/svn/pygame/trunk pygame
cd pygame
python3 setup.py build
sudo python3 setup.py install
