#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from bsn.common import file_import_tree
file_import_tree.file_begin(__name__)
import os
f_strFileName = os.path.split(__file__)[1]
f_strFileBaseName = os.path.splitext(f_strFileName)[0]
import logging
from ctypes import * 

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
 
def get_u16(iAddr):
    pvAddr = cast(iAddr, POINTER(c_uint16))
    return pvAddr.contents.value

def set_u16(iAddr, u16):
    pvAddr = cast(iAddr, POINTER(c_uint16))
    pvAddr.contents.value = u16

def get_i16(iAddr):
    pvAddr = cast(iAddr, POINTER(c_int16))
    return pvAddr.contents.value

def set_i16(iAddr, i16):
    pvAddr = cast(iAddr, POINTER(c_int16))
    pvAddr.contents.value = i16
 
def get_u32(iAddr):
    pvAddr = cast(iAddr, POINTER(c_uint32))
    return pvAddr.contents.value

def set_u32(iAddr, u32):
    pvAddr = cast(iAddr, POINTER(c_uint32))
    pvAddr.contents.value = u32

def get_i32(iAddr):
    pvAddr = cast(iAddr, POINTER(c_int32))
    return pvAddr.contents.value

def set_i32(iAddr, i32):
    pvAddr = cast(iAddr, POINTER(c_int32))
    pvAddr.contents.value = i32
 
 
def get_u64(iAddr):
    pvAddr = cast(iAddr, POINTER(c_uint64))
    return pvAddr.contents.value

def set_u64(iAddr, u64):
    pvAddr = cast(iAddr, POINTER(c_uint64))
    pvAddr.contents.value = u64

def get_i64(iAddr):
    pvAddr = cast(iAddr, POINTER(c_int64))
    return pvAddr.contents.value

def set_i64(iAddr, i64):
    pvAddr = cast(iAddr, POINTER(c_int64))
    pvAddr.contents.value = i64
 
file_import_tree.file_end(__name__)