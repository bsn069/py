#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from bsn.common import file_import_tree
file_import_tree.file_begin(__name__)

import asyncio
import enum
import logging
from bsn.common import tcp_client
from bsn.common import err

from bsn.agent_proxy.agent import state_enum
from bsn.agent_proxy.agent import state_mgr

class CAgentProxy(tcp_client.CTCPClient):
    """ 
    """

    def __init__(self, oCAgent, _u64CreateIndex):
        """
        """
        logging.info("{}".format(self))
        super().__init__()
        self._oCAgent = oCAgent
        self._u64CreateIndex = _u64CreateIndex
        self._oCStateMgr = state_mgr.CStateMgr(self)

    async def on_recv_msg(self, u16Cmd, byData):
        '''
        '''
        await self.state_mgr.on_recv_msg(u16Cmd, byData)

    @property
    def state_mgr(self):
        return self._oCStateMgr


file_import_tree.file_end(__name__)