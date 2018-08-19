#!/bin/bash

cd ../pb
rm -rf *.py

cd ../proto
protoc -I./ --python_out=./../pb *.proto