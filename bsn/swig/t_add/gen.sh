#!/bin/bash

V_ModuleNam=t_add

mkdir build
swig -c++ -python -o ./build/t_wrap.cpp src/t.i 

mkdir py
mv ./build/*.py ./py/

python3 setup.py build_ext --inplace
mv *.so ./py/_t_add.so