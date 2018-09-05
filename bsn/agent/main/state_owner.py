#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from bsn.common import file_import_tree
file_import_tree.file_begin(__name__)
import os
f_strFileName = os.path.split(__file__)[1]
f_strFileBaseName = os.path.splitext(f_strFileName)[0]

import logging

from . import state_mgr
from bsn.common.state_mgr import base_state_owner

from ..agent_proxy import state_owner as agent_proxy

class CStateOwner(base_state_owner.CStateOwner):
    """ 
    """

    def __init__(self, oCOwner, oCApp, u64CreateIndex):
        """
        """
        logging.info("oCOwner={} u64CreateIndex={}".format(oCOwner, u64CreateIndex))
        base_state_owner.CStateOwner.__init__(self, oCOwner, oCApp, u64CreateIndex)
        self._oCStateMgr = state_mgr.CStateMgr(self)

        self._u64SubModuleCreateIndex = 0
        self._listAgentProxy = []

    def create_module_agent_proxy(self):
        '''
        '''
        logging.info("{}".format(self))
        self._u64SubModuleCreateIndex = self._u64SubModuleCreateIndex + 1
        oModule = agent_proxy.CStateOwner(self, self.app, self._u64SubModuleCreateIndex)
        self._listAgentProxy.append(oModule)
        return  oModule

    def get_agent_proxy_by_id(self, u32AgentProxyId):
        for i in self._listAgentProxy:
            oAgentProxy = self._listAgentProxy[i]
            if oAgentProxy.id == u32AgentProxyId:
                return oAgentProxy

    def get_agent_proxy_by_dest_agent_id(self, u32AgentId):
        '''
        '''
        return self._listAgentProxy[0]

    def get_send_use_agent_proxy(self, u32ToAgentId, u32Cmd, u32AgentProxyId):
        '''
        '''
        oAgentProxy = None
        if u32AgentProxyId is not None:
            oAgentProxy = self.get_agent_proxy_by_id(u32AgentProxyId)
        else:
            oAgentProxy = self.get_agent_proxy_by_dest_agent_id(u32ToAgentId)
        return oAgentProxy

    def send_pkg_to_agent(self, u32ToAgentId, u32Cmd, byData, u32AgentProxyId = None):
        '''
        '''
        oAgentProxy = self.get_send_use_agent_proxy(u32ToAgentId, u32Cmd, u32AgentProxyId)
        if oAgentProxy is None:
            return -1
        return oAgentProxy.send_pkg_to_agent(u32ToAgentId, u32Cmd, byData)

    def send_pb_to_agent(self, u32ToAgentId, u32Cmd, oPbMsg, u32AgentProxyId = None):
        '''
        '''
        oAgentProxy = self.get_send_use_agent_proxy(u32ToAgentId, u32Cmd, u32AgentProxyId)
        if oAgentProxy is None:
            return -1
        return self.send_pb_to_agent(u32ToAgentId, u32Cmd, oPbMsg, u32AgentProxyId)

file_import_tree.file_end(__name__)