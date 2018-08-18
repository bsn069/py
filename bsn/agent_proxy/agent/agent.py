#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from bsn.common import file_import_tree
file_import_tree.file_begin(__name__)

import asyncio
import enum
import logging
from bsn.common import tcp_session
from bsn.common import err

from bsn.agent_proxy.agent import state_enum
from bsn.agent_proxy.agent import state_mgr

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
        self._CStateMgr = state_mgr.CStateMgr(self)

    def connection_made(self, transport):
        logging.info("{} {}".format(self, transport))
        super().connection_made(transport)
        self.state_mgr.to_state(state_enum.EState.Connected)
       
    def connection_lost(self, exc):
        logging.info("{} {}".format(self, exc))
        self.state_mgr.to_state(state_enum.EState.DisConnect)
        super().connection_lost(exc)

    def _on_recv_pkg(self, byData):
        logging.info("{} byData:{}".format(self, byData))
        self.state_mgr.proc_pkg(byData)

    def _update(self):
        # logging.info("{}".format(self))
        pass
        
    @property
    def state_mgr(self):
        return self._CStateMgr


file_import_tree.file_end(__name__)