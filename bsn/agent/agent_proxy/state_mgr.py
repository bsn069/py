#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from bsn.common import file_import_tree
file_import_tree.file_begin(__name__)

import asyncio
import enum
import logging
from bsn.agent.agent_proxy import state_enum

class CStateMgr(object):
    """ 
    """
    
    '''
    bsn.agent.agent_proxy.state_enum.EState
    '''
    StateCreateFun = {}
    
    @staticmethod
    def reg_state(eEState, funCreate):
        '''
        eEState bsn.agent.agent_proxy.state_enum.EState
        '''
        logging.info("{} {}".format(eEState, funCreate))
        CStateMgr.StateCreateFun[eEState.value] = funCreate

    def __init__(self, oCAgentProxy):
        """
        """
        logging.info("{}".format(self))

        self._oCState = {}
        for uIndex in CStateMgr.StateCreateFun:
            funcCreate = CStateMgr.StateCreateFun[uIndex]
            self._oCState[uIndex] = funcCreate(oCAgentProxy)
        self._oCStateCur = self._oCState[state_enum.EState.Init.value]

    def to_state(self, EState_To):
        '''
        '''
        logging.info("{} EState_To={}".format(self, EState_To))
        CAgentState_Old = self.state 
        CAgentState_New = self._oCState[EState_To.value]
        if CAgentState_Old is CAgentState_New:
            return
        CAgentState_Old.leave()
        self._oCStateCur = CAgentState_New
        CAgentState_New.enter()

    async def on_recv_msg(self, u16Cmd, byData):
        '''
        '''
        logging.info("{} u16Cmd={}".format(self, u16Cmd))
        await self.state.on_recv_msg(u16Cmd, byData)

    @property
    def state(self):
        return self._oCStateCur

file_import_tree.file_end(__name__)
