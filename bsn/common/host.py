#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from bsn.common import file_import_tree
file_import_tree.file_begin(__name__)

import re
from bsn.common import err
 

class CHost(object):
    def __init__(self, host):
        self._host = host

    def __str__(self):
        return self._host

file_import_tree.file_end(__name__)