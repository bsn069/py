#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from bsn.common import file_import_tree
file_import_tree.file_begin(__name__)

import logging

from bsn.agent.agent_proxy import state_enum
from bsn.agent.agent_proxy import state_mgr
from bsn.common.state_mgr import base_state_owner

from bsn.common import tcp_client

class CStateOwner(base_state_owner.CStateOwner, tcp_client.CTCPClient):
    """ 
    """

    def __init__(self, oCOwner, u64CreateIndex = 0, u32Id = 0):
        """
        """
        logging.info("oCOwner={} u64CreateIndex={} u32Id={}".format(oCOwner, u64CreateIndex, u32Id))
        base_state_owner.CStateOwner.__init__(self, oCOwner, u64CreateIndex = u64CreateIndex, u32Id=u32Id)
        self._oCStateMgr = state_mgr.CStateMgr(self)

        tcp_client.CTCPClient.__init__(self, oCOwner.owner.loop)

    def set_host_port(self, oCHost, oCPort):
        logging.info("{}".format(self))
        self._CHost = oCHost
        self._CPort = oCPort

file_import_tree.file_end(__name__)