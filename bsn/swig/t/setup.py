#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
 
"""
setup.py file for SWIG 
"""
 
from distutils.core import setup, Extension
import os
f_strCurDir = os.getcwd()
f_strDirName = f_strCurDir.split(os.path.sep)[-1]
f_strPlugName = f_strDirName

def add_source_file(strDir, listCppFiles):
    listPath = os.listdir(strDir)
    for strPathName in listPath:
        strExt = os.path.splitext(strPathName)[-1]
        if strExt in ['.cpp']:
            listCppFiles.append('.{}{}{}{}'.format(os.path.sep, strDir, os.path.sep, strPathName))


f_listCppFiles = []
add_source_file('build', f_listCppFiles)
add_source_file('src', f_listCppFiles)
print(f_listCppFiles)

example_module = Extension('_{}'.format(f_strPlugName),
                           sources=f_listCppFiles,
                           include_dirs=['src']
                           )

setup (name = f_strPlugName,
       version = '0.1',
       author      = "SWIG Docs",
       description = """Simple swig example from docs""",
       ext_modules = [example_module],
       py_modules = [f_strPlugName],
       extra_compile_args = ['-std=c++17'],
       )
