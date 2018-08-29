#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from bsn.common import file_import_tree
file_import_tree.file_begin(__name__)

import enum


class EState(enum.Enum):
    Init = 0
    Init2 = 1


file_import_tree.file_end(__name__)