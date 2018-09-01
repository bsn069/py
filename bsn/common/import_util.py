#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


from bsn.common import file_import_tree
file_import_tree.file_begin(__name__)

import importlib
import os  

def import_init_dir(strPackageName, strDir): 
    '''
    import dir file, without __init__.py and __pycache__
    from bsn.common import import_util
    import_util.import_init_dir(__package__, __file__)
    '''
    print(strPackageName, strDir)
    if strPackageName is None:
        return  
    strDir = os.path.dirname(strDir) 
    listPath = os.listdir(strDir)
    for strPathName in listPath:
        if strPathName == '__init__.py' or strPathName == '__pycache__':
            continue
        # print(strPathName)
        strModule = os.path.splitext(strPathName)[0]
        # print(strModule)
        strModuleFull = '{}.{}'.format(strPackageName, strModule)
        # print( strModuleFull )
        importlib.import_module(strModuleFull)


file_import_tree.file_end(__name__)
