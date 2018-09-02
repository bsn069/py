#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from bsn.common import file_import_tree
file_import_tree.file_begin(__name__)
import os
f_strFileName = os.path.split(__file__)[1]
f_strFileBaseName = os.path.splitext(f_strFileName)[0]

import logging
from bsn.agent.agent_proxy import state_enum
from bsn.agent.agent_proxy import state_mgr
from bsn.agent.agent_proxy.state import _base

class CState(_base.CState):
    """ 
    """
    C_strState = f_strFileBaseName

    def __init__(self, oCStateMgr):
        """
        """
        super().__init__(oCStateMgr)

    def _enter(self, oCStatePre):
        logging.info("{} oCStatePre={}".format(self, oCStatePre))
        self.to_state('wait_connect')

def create_func(oCStateMgr):
    logging.info("oCStateMgr={}".format(oCStateMgr))
    return CState(oCStateMgr)
state_mgr.CStateMgr.reg_state(CState.C_strState, create_func)
file_import_tree.file_end(__name__)