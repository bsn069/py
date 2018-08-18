#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

 
from bsn.common import tree

_import_tree = tree.CTree()

def file_begin(strName):
    global _import_tree
    _import_tree.enter(strName)

def file_end(strName):
    global _import_tree
    _import_tree.leave()

def file_print():
    global _import_tree
    _import_tree.print()


