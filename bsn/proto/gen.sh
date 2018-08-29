#!/bin/bash

cd ..
rm -rf pb

cd proto
protoc -I./  --python_out=./../../  bsn/pb/*.proto bsn/pb/*/*.proto