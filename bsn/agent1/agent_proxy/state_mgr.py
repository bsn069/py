#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from bsn.common import file_import_tree
file_import_tree.file_begin(__name__)

import logging
from bsn.agent.agent_proxy import state_enum
from bsn.common.state_mgr import base_state_mgr

class CStateMgr(base_state_mgr.CStateMgr):
    '''
    bsn.agent.agent_proxy.state_enum.EState
    '''
    C_mapStateCreateFun = {}


    def __init__(self, oCOwner):
        """
        """
        logging.info("{}".format(oCOwner))
        super().__init__(oCOwner)


file_import_tree.file_end(__name__)