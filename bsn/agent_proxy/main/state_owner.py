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

from ..agent import state_owner as agent
from bsn.common import tcp_accept

class CStateOwner(base_state_owner.CStateOwner, tcp_accept.CTCPAccept):
    """ 
    """

    def __init__(self, oCOwner, oCApp, u64CreateIndex):
        """
        """
        logging.info("oCOwner={}".format(oCOwner, u64CreateIndex))
        base_state_owner.CStateOwner.__init__(self, oCOwner, oCApp, u64CreateIndex)
        tcp_accept.CTCPAccept.__init__(self, self.app.loop)
        self._oCStateMgr = state_mgr.CStateMgr(self)

        self._u64AgentCreateIndex = 0
        self._mapId2Agents = {}
        self._mapIndex2Agents = {}

    def _create_session(self):
        '''
        '''
        logging.info("{}".format(self))
        self._u64AgentCreateIndex = self._u64AgentCreateIndex + 1
        oAgent = agent.CStateOwner(self, self.app, self._u64AgentCreateIndex)
        self._mapIndex2Agents[self._u64AgentCreateIndex] = oAgent
        return  oAgent

    def get_agent_by_id(self, u32Id):
        return self._mapId2Agents.get(u32Id)

    def get_agent_by_index(self, u64Index):
        return self._mapIndex2Agents.get(u64Index)

    def remove_agent(self, oAgent):
        logging.info("oAgent={}".format(oAgent))
        self._mapIndex2Agents.pop(oAgent.create_index)
        if oAgent.id is not None:
            self._mapId2Agents.pop(oAgent.id)

    def set_agent_id(self, oAgent, u32Id):
        logging.info("oAgent={} u32Id={}".format(oAgent, u32Id))
        oAgent.set_id(u32Id)
        self._mapId2Agents[u32Id] = oAgent

file_import_tree.file_end(__name__)