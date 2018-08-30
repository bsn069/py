#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from bsn.common import file_import_tree
file_import_tree.file_begin(__name__)

import asyncio
import enum
import logging
from bsn.agent.agent_proxy import state_enum
from bsn.agent.agent_proxy import state_mgr
from bsn.common.port import CPort
from bsn.common.host import CHost
from bsn.pb import comm_pb2
from bsn.pb.agent2agentproxy import login_pb2
from bsn.pb.agent2agentproxy import cmd_pb2
from bsn.common.state_mgr import state

class CState(state.CState):
    """ 
    """
    C_EState = state_enum.EState.Login

    def __init__(self, oOwner):
        """
        """
        super().__init__(oOwner)

    def _enter(self, oCStatePre):
        logging.info("{} oCStatePre={}".format(self, oCStatePre))

        oMReq = login_pb2.MReq()
        oMReq.id = self.owner.owner.id
        self.send_pb(cmd_pb2.EMsgId_Login, oMReq) 

    def on_recv_msg(self, u16Cmd, byData):
        logging.info("{} u16Cmd={}".format(self, u16Cmd))

def create_func(oOwner):
    logging.info("{}".format(oOwner))
    return CState(oOwner)

state_mgr.CStateMgr.reg_state(CState.C_EState, create_func)

file_import_tree.file_end(__name__)