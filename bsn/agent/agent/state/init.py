#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from bsn.common import file_import_tree
file_import_tree.file_begin(__name__)


import logging
from bsn.agent.agent import state_enum
from bsn.agent.agent import state_mgr
from bsn.agent.agent.state import _base

class CState(_base.CState):
    """ 
    """
    C_eEState = state_enum.EState.Init

    def __init__(self, oCStateMgr):
        """
        """
        super().__init__(oCStateMgr)

    def _enter(self, oCStatePre):
        logging.info("{} oCStatePre={}".format(self, oCStatePre))
        self.to_state(state_enum.EState.Run)

def create_func(oCStateMgr):
    logging.info("oCStateMgr={}".format(oCStateMgr))
    return CState(oCStateMgr)
state_mgr.CStateMgr.reg_state(CState.C_eEState, create_func)
file_import_tree.file_end(__name__)