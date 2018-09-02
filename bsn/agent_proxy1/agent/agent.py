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
        logging.info("0{}".format(self))
        logging.info("1{}".format(self))
        super().__init__()
        logging.info("2{}".format(self))

        self._CAgentProxy = oCAgentProxy
        self._uCreateIndex = uCreateIndex
        logging.info("{}".format(self))
        self._CStateMgr = state_mgr.CStateMgr(self)
        logging.info("{}".format(self))

    def connection_made(self, transport):
        logging.info("{} {}".format(self, transport))
        super().connection_made(transport)
        self.state_mgr.to_state(state_enum.EState.Connected)
       
    def connection_lost(self, exc):
        logging.info("{} {}".format(self, exc))
        self.state_mgr.to_state(state_enum.EState.DisConnect)
        super().connection_lost(exc)

    def on_recv_msg(self, oCMsg):
        self.state_mgr.on_recv_msg(oCMsg)

    def _update(self):
        # logging.info("{}".format(self))
        pass
        
    @property
    def state_mgr(self):
        return self._CStateMgr


file_import_tree.file_end(__name__)