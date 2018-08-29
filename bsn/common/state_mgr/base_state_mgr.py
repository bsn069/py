#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from bsn.common import file_import_tree
file_import_tree.file_begin(__name__)

import logging

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
        eEState enum
        '''
        logging.info("{} {}".format(eEState, funCreate))
        CStateMgr.StateCreateFun[eEState.value] = funCreate

    def __init__(self, oCOwner):
        """
        """
        logging.info("{}".format(self))

        self._oCState = {}
        for uIndex in CStateMgr.StateCreateFun:
            funcCreate = CStateMgr.StateCreateFun[uIndex]
            self._oCState[uIndex] = funcCreate(oCOwner)

        self._oCStateCur = None

    @property
    def state(self):
        return self._oCStateCur

    def to_state(self, eEStateTo):
        '''
        '''
        logging.info("{} eEStateTo={}".format(self, eEStateTo))
        oCAgentStateOld = self.state 
        oCAgentStateNew = self._oCState[eEStateTo.value]
        if oCAgentStateOld is oCAgentStateNew:
            return
        if oCAgentStateOld is not None:
            oCAgentStateOld._leave(oCAgentStateNew)
        self._oCStateCur = oCAgentStateNew
        oCAgentStateNew._enter(oCAgentStateOld)

    async def on_recv_msg(self, u16Cmd, byData):
        '''
        '''
        logging.info("{} u16Cmd={} byData={}".format(self, u16Cmd, byData))
        await self.state.on_recv_msg(u16Cmd, byData)



file_import_tree.file_end(__name__)
