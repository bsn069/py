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
from bsn.pb.agent_agentproxy import define_pb2


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

        if u16Cmd == cmd_pb2.EMsgId2AgentProxy_LoginReq:
            oM2AgentProxy_LoginReq = self.get_pb(login_pb2.M2AgentProxy_LoginReq, byData)
            logging.info("{} oM2AgentProxy_LoginReq={}".format(self, oM2AgentProxy_LoginReq))

            oM2Agent_LoginRes = login_pb2.M2Agent_LoginRes()
            oM2Agent_LoginRes.u32AgentProxyId = self.main.id

            u32AentId = oM2AgentProxy_LoginReq.id
            if u32AentId == 0:
                u32AentId = self.main.gen_auto_agent_id()
                if u32AentId is None:
                    oM2Agent_LoginRes.err = 'id had full'
            else:
                if u32AentId is None:
                    oM2Agent_LoginRes.err = 'not agent id'

            oM2Agent_LoginRes.u32AgentId = u32AentId
            if oM2Agent_LoginRes.err is None:
                oAgent = self.main.get_agent_by_id(u32AentId)
                if oAgent is None:
                    self.main.set_agent_id(self.owner, u32AentId)
                else:
                    oM2Agent_LoginRes.err = 'had exist'

            logging.info("{} oM2Agent_LoginRes={}".format(self, oM2Agent_LoginRes))
            self.send_pb(cmd_pb2.EMsgId2Agent_LoginRes, oM2Agent_LoginRes)


def create_func(oCStateMgr):
    logging.info("oCStateMgr={}".format(oCStateMgr))
    return CState(oCStateMgr)


state_mgr.CStateMgr.reg_state(CState.C_strState, create_func)

file_import_tree.file_end(__name__)
