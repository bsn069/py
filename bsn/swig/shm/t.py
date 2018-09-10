#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
 
"""
setup.py file for SWIG 
"""
 
from bsn.swig.shm.py import plug as t_add
 
# import importlib
# t_add = importlib.import_module('bsn.swig.{}.py.plug'.format("t_add"))

print(t_add)
print(t_add.add(1, 2))

import os
f_strDirName = __file__.split(os.path.sep)[-2]
print(f_strDirName )