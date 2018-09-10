#!/bin/bash

rm -rf build
mkdir build
swig -c++ -python -o ./build/plug_wrap.cpp src/plug.i 

rm -rf py
mkdir py
mv ./build/*.py ./py/

python3 setup.py build_ext --inplace
mv *.so ./py/_plug.so

