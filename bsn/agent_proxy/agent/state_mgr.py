#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from bsn.common import file_import_tree
file_import_tree.file_begin(__name__)

import asyncio
import enum
import logging
from bsn.agent_proxy.agent import state_enum

class CStateMgr(object):
    """ 
    """
    
    '''
    bsn.agent_proxy.agent.state_enum.EState
    '''
    StateCreateFun = {}
    
    @staticmethod
    def reg_state(eEState, funCreate):
        '''
        eEState bsn.agent_proxy.agent.state_enum.EState
        '''
        # logging.info("{} {}".format(eEState, funCreate))
        CStateMgr.StateCreateFun[eEState.value] = funCreate

    def __init__(self, oCAgent):
        """
        """
        logging.info("{}".format(self))

        self._CAgentState = {}
        for uIndex in CStateMgr.StateCreateFun:
            funcCreate = CStateMgr.StateCreateFun[uIndex]
            self._CAgentState[uIndex] = funcCreate(oCAgent)
        self._CAgentStateCur = self._CAgentState[state_enum.EState.Init.value]

    def to_state(self, EState_To):
        '''
        '''
        logging.info("{} {}".format(self, EState_To))
        CAgentState_Old = self._CAgentStateCur 
        CAgentState_New = self._CAgentState[EState_To.value]
        if CAgentState_Old is CAgentState_New:
            return
        CAgentState_Old.leave()
        self._CAgentStateCur = CAgentState_New
        CAgentState_New.enter()

    def proc_pkg(self, byPkg):
        logging.info("{} {}".format(self, byPkg))
        self._CAgentStateCur.proc_pkg(byPkg)

file_import_tree.file_end(__name__)
