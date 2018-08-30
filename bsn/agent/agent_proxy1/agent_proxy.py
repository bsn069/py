#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from bsn.common import file_import_tree
file_import_tree.file_begin(__name__)

import asyncio
import enum
import logging
from bsn.common import tcp_client
from bsn.common import err

from bsn.agent.agent_proxy import state_enum
from bsn.agent.agent_proxy import state_mgr

class CAgentProxy(tcp_client.CTCPClient):
    """ 
    """

    def __init__(self, oOwner, u64CreateIndex):
        """
        oOwner CAgent
        """
        logging.info("{}".format(self))
        super().__init__(oOwner.loop)
        self._oOwner = oOwner
        self._u64CreateIndex = u64CreateIndex
        self._oCStateMgr = state_mgr.CStateMgr(self)
        self.to_state(state_enum.EState.WaitConnect)

    async def on_recv_msg(self, u16Cmd, byData):
        '''
        '''
        await self.state_mgr.on_recv_msg(u16Cmd, byData)


    @property
    def state_mgr(self):
        return self._oCStateMgr

    @property
    def owner(self):
        return self._oOwner

    def to_state(self, EState_To):
        '''
        EState_To state_enum.EState.
        '''
        self.state_mgr.to_state(EState_To)

    def set_host_port(self, oCHost, oCPort):
        logging.info("{}".format(self))
        self._CHost = oCHost
        self._CPort = oCPort

file_import_tree.file_end(__name__)