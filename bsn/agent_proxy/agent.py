#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import asyncio
import enum
import logging
from bsn.common import tcp_session
from bsn.common import err
from bsn.agent_proxy import agent_state
from bsn.agent_proxy import agent_state_mgr

class EState(enum.Enum):
    Null = 0
    WaitConnect = 1
    Runing = 2
    WaitClose = 3

class CAgent(tcp_session.CTCPSession):
    """ 
    """

    def __init__(self, oCAgentProxy, uCreateIndex):
        """
        """
        logging.info("{}".format(self))
        super().__init__()

        self._CAgentProxy = oCAgentProxy
        self._uCreateIndex = uCreateIndex
        self._CAgentStateMgr = agent_state_mgr.CAgentStateMgr(self)

    def connection_made(self, transport):
        logging.info("{} {}".format(self, transport))
        super().connection_made(transport)
        self.state_mgr.to_state(agent_state_mgr.EState.Connected)
       
    def connection_lost(self, exc):
        logging.info("{} {}".format(self, exc))
        self.state_mgr.to_state(agent_state_mgr.EState.DisConnect)
        super().connection_lost(exc)

    def _on_recv_pkg(self, byData):
        logging.info("{} byData:{}".format(self, byData))
        self.state_mgr.proc_pkg(byData)

    def _update(self):
        # logging.info("{}".format(self))
        pass
        
    @property
    def state_mgr(self):
        return self._CAgentStateMgr
    
 
