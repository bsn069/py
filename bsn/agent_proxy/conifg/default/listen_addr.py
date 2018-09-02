#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from bsn.common import file_import_tree
file_import_tree.file_begin(__name__)
import os
f_strFileName = os.path.split(__file__)[1]
f_strFileBaseName = os.path.splitext(f_strFileName)[0]
from bsn.common.port import CPort
from bsn.common.ip import CIP
from .config import f_mapConfig

f_mapConfig['ip'] =  CIP('0.0.0.0')
f_mapConfig['port'] =  CPort(10001)

file_import_tree.file_end(__name__)