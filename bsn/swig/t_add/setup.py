#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
 
"""
setup.py file for SWIG 
"""
 
from distutils.core import setup, Extension
 
 
example_module = Extension('_t_add',
                           sources=['./build/t_wrap.cpp', './src/t.cpp'],
                           include_dirs=['src']
                           )
 
setup (name = 't_app',
       version = '0.1',
       author      = "SWIG Docs",
       description = """Simple swig example from docs""",
       ext_modules = [example_module],
       py_modules = ["t_add"],
       )