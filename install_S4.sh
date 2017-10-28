#!/bin/bash

echo Welcome!

cd

git clone https://github.com/bro-acid/S4.git

apt-get install liblua5.2-dev libpython2.7-dev libfftw3-dev libsuitesparse-dev libopenblas-dev

cd S4
make
make all
make install
make S4_pyext
python setup.py install

clear
echo Installation finished!
