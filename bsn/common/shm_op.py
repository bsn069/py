#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from bsn.common import file_import_tree
file_import_tree.file_begin(__name__)
import os
f_strFileName = os.path.split(__file__)[1]
f_strFileBaseName = os.path.splitext(f_strFileName)[0]
import logging
from ctypes import * 
# from bsn.swig.shm.py import plug 

def get_u8(iAddr):
    pvAddr = cast(iAddr, POINTER(c_uint8))
    return pvAddr.contents.value

def set_u8(iAddr, u8):
    pvAddr = cast(iAddr, POINTER(c_uint8))
    pvAddr.contents.value = u8

def get_i8(iAddr):
    pvAddr = cast(iAddr, POINTER(c_int8))
    return pvAddr.contents.value

def set_i8(iAddr, i8):
    pvAddr = cast(iAddr, POINTER(c_int8))
    pvAddr.contents.value = i8
 
file_import_tree.file_end(__name__)