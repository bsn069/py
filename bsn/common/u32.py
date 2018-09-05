#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from bsn.common import file_import_tree
file_import_tree.file_begin(__name__)

from bsn.common import err

class u32(object):
    MIN = 0
    MAX = (1 << 32) - 1


file_import_tree.file_end(__name__)        