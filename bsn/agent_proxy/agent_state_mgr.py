#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import asyncio
import enum
import logging
from bsn.common import tcp_session
from bsn.common import err
# from bsn.agent_proxy import agent_state_connected
# from bsn.agent_proxy import agent_state_wait_login
# from bsn.agent_proxy import agent_state_init
# from bsn.agent_proxy import agent_state_disconnect
 
class EState(enum.Enum):
    Init = 0
    Connected = 1
    DisConnect = 2
    WaitLogin = 3

class CAgentStateMgr(object):
    """ 
    """
    
    @staticmethod
    def reg_state(strState, funCreate):
        logging.info("{} {}".format(strState, funCreate))
        pass

    def __init__(self, oCAgent):
        """
        """
        logging.info("{}".format(self))
        self._CAgentState = [
            # agent_state_init.CAgentState(oCAgent),
            # agent_state_connected.CAgentState(oCAgent),
            # agent_state_disconnect.CAgentState(oCAgent),
            # agent_state_wait_login.CAgentState(oCAgent)
        ]
        self._CAgentStateCur = self._CAgentState[EState.Init.value]

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


    
 
