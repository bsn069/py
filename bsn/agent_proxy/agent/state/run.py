#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from bsn.common import file_import_tree
file_import_tree.file_begin(__name__)
import os
f_strFileName = os.path.split(__file__)[1]
f_strFileBaseName = os.path.splitext(f_strFileName)[0]

import logging
import importlib
state_mgr = importlib.import_module('{}_mgr'.format(__package__))
from . import _base
from bsn.pb.agent_agentproxy import login_pb2
from bsn.pb.agent_agentproxy import trans_pb2
from bsn.pb.agent_agentproxy import cmd_pb2

class CState(_base.CState):
    """ 
    """
    C_strState = f_strFileBaseName

    def __init__(self, oCStateMgr):
        """
        """
        super().__init__(oCStateMgr)

    def on_recv_msg(self, u16Cmd, byData):
        logging.info("{} u16Cmd={}".format(self, u16Cmd))

        if u16Cmd == cmd_pb2.EMsgId2AgentProxy_ToAgent:
            oM2AgentProxy_ToAgent = self.get_pb(trans_pb2.M2AgentProxy_ToAgent, byData)
            self.main.send_pkg_from_agent_to_agent(self.owner.id, oM2AgentProxy_ToAgent.u32ToAgentId, oM2AgentProxy_ToAgent.u32Cmd, oM2AgentProxy_ToAgent.byData)


def create_func(oCStateMgr):
    logging.info("oCStateMgr={}".format(oCStateMgr))
    return CState(oCStateMgr)
state_mgr.CStateMgr.reg_state(CState.C_strState, create_func)

file_import_tree.file_end(__name__)