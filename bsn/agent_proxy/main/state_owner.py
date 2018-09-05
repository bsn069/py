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
from bsn.pb.agent_agentproxy import trans_pb2
from bsn.pb.agent_agentproxy import cmd_pb2
from bsn.common.u32 import u32
from bsn.pb.agent_agentproxy import define_pb2

class CStateOwner(base_state_owner.CStateOwner, tcp_accept.CTCPAccept):
    """ 
    """
    C_u32AutoAgentIdMax = (1 << (32 - define_pb2.EGlobal_AgentProxyIdBitMax)) - 1

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

        self._u32AutoAgentIdIndex = 0

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

    def send_pkg_from_agent_to_agent(self, u32FromAgentId, u32ToAgentId, u32Cmd, byData):
        logging.info("form {} to {} trans cmd {}".format(u32FromAgentId, u32ToAgentId, u32Cmd))
        oToAgent = self.get_agent_by_id(u32ToAgentId)
        if oToAgent is None:
            return

        oM2Agent_FromAgent = trans_pb2.M2Agent_FromAgent()
        oM2Agent_FromAgent.u32FromAgentId = u32FromAgentId
        oM2Agent_FromAgent.u32Cmd = u32Cmd
        oM2Agent_FromAgent.byData = byData
        oToAgent.send_pb(cmd_pb2.EMsgId2Agent_FromAgent, oM2Agent_FromAgent)

    def gen_auto_agent_id(self):
        if self._u32AutoAgentIdIndex >= CStateOwner.C_u32AutoAgentIdMax:
            return None

        self._u32AutoAgentIdIndex = self._u32AutoAgentIdIndex + 1
        u32AgentId = (self._u32AutoAgentIdIndex << define_pb2.EGlobal_AgentProxyIdBitMax) + self.id
        return u32AgentId

file_import_tree.file_end(__name__)