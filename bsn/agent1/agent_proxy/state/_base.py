#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from bsn.common import file_import_tree
file_import_tree.file_begin(__name__)
import os
f_strFileName = os.path.split(__file__)[1]

import logging
from bsn.agent.agent_proxy import state_enum
from bsn.agent.agent_proxy import state_mgr
from bsn.common.state_mgr import base_state

class CState(base_state.CState):
    """ 
    """
    C_eEState = None

    def __init__(self, oCStateMgr):
        """
        """
        super().__init__(oCStateMgr)


file_import_tree.file_end(__name__)