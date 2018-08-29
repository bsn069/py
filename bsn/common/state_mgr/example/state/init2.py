#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from bsn.common import file_import_tree
file_import_tree.file_begin(__name__)


import logging
from bsn.common.state_mgr.example import state_enum
from bsn.common.state_mgr.example import state_mgr
from bsn.common.state_mgr import base_state

class CState(base_state.CState):
    """ 
    """
    C_eEState = state_enum.EState.Init2

    def __init__(self, oOwner):
        """
        """
        super().__init__(oOwner)


def create_func(oCOwner):
    logging.info("{}".format(oCOwner))
    return CState(oCOwner)
state_mgr.CStateMgr.reg_state(CState.C_eEState, create_func)
file_import_tree.file_end(__name__)