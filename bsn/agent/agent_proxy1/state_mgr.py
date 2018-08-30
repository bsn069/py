#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from bsn.common import file_import_tree
file_import_tree.file_begin(__name__)

import asyncio
import enum
import logging
from bsn.agent.agent_proxy import state_enum
from bsn.common.state_mgr import state_mgr

class CStateMgr(state_mgr.CStateMgr):
    """ 
    """
    
    '''
    bsn.agent.agent_proxy.state_enum.EState
    '''
    # StateCreateFun = {}
    
    # @staticmethod
    # def reg_state(eEState, funCreate):
    #     '''
    #     eEState bsn.agent.agent_proxy.state_enum.EState
    #     '''
    #     logging.info("{} {}".format(eEState, funCreate))
    #     CStateMgr.StateCreateFun[eEState.value] = funCreate

    def __init__(self, oCAgentProxy):
        """
        """
        logging.info("{}".format(oCAgentProxy))
        super().__init__(oCAgentProxy)
        self.to_state(state_enum.EState.Init)


file_import_tree.file_end(__name__)
