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
from bsn.common import tcp_client
from bsn.pb.agent_agentproxy import cmd_pb2
from bsn.pb.agent_agentproxy import trans_pb2
# from ..sub_module import state_owner as sub_module

class CStateOwner(base_state_owner.CStateOwner, tcp_client.CTCPClient):
    """ 
    """

    def __init__(self, oCOwner, oCApp, u64CreateIndex):
        """
        """
        logging.info("oCOwner={} u64CreateIndex={} ".format(oCOwner, u64CreateIndex))
        base_state_owner.CStateOwner.__init__(self, oCOwner, oCApp, u64CreateIndex)
        self._oCStateMgr = state_mgr.CStateMgr(self)

        tcp_client.CTCPClient.__init__(self, self.app.loop)

    def set_host_port(self, oCHost, oCPort):
        logging.info("{}".format(self))
        self._CHost = oCHost
        self._CPort = oCPort

    def send_pkg_to_agent(self, u32ToAgentId, u32Cmd, byData):
        '''
        '''
        oM2AgentProxy_ToAgent = trans_pb2.M2AgentProxy_ToAgent()
        oM2AgentProxy_ToAgent.u32ToAgentId = u32ToAgentId
        oM2AgentProxy_ToAgent.u32Cmd = u32Cmd
        oM2AgentProxy_ToAgent.byData = byData
        self.send_pb(cmd_pb2.EMsgId2AgentProxy_ToAgent, oM2AgentProxy_ToAgent)

file_import_tree.file_end(__name__)