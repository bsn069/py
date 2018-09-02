#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from bsn.common import file_import_tree
file_import_tree.file_begin(__name__)
import os
f_strFileName = os.path.split(__file__)[1]
f_strFileBaseName = os.path.splitext(f_strFileName)[0]

import logging
from bsn.common.state_mgr import base_state

class CState(base_state.CState):
    """ 
    """
    C_strState = None

    def __init__(self, oCStateMgr):
        """
        """
        super().__init__(oCStateMgr)


file_import_tree.file_end(__name__)